from flask import g, redirect, url_for
from flask.ext import restful
from flask.ext.restful import abort
from flask.ext.login import login_user, logout_user, current_user, login_required

from .server import config, app, lm, api, db, bcrypt
from .models import User, Task
from .forms import UserCreateForm, SessionCreateForm, TaskCreateForm
from .serializers import UserSerializer, TaskSerializer


@app.route('/test', methods=['GET'])
@app.route('/test/', methods=['GET'])
def index():
    return redirect(url_for('static', filename='index.html'))


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    abort(500)


@lm.user_loader
def load_user(unique_id):
    app.logger.debug("load_user: %s" % unique_id)
    return User.query.get(int(unique_id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        app.logger.debug("before_request: user: %s\nauthenticated" % str(g.user))
        # g.user.last_seen = datetime.utcnow()
        # db.session.add(g.user)
        # db.session.commit()
    else:
        app.logger.debug("before_request: user: %s\nnot authenticated" % str(g.user))


class UserListView(restful.Resource):
    def post(self):  # create_user
        form = UserCreateForm()
        if not form.validate_on_submit():
            abort(422, message=form.errors)

        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return UserSerializer(user).data


class UserView(restful.Resource):
    @login_required
    def delete(self, id):  # delete_user
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404)
        if g.user.id != id:
            abort(401)
        db.session.delete(user)
        db.session.commit()
        return


class SessionView(restful.Resource):
    def get(self):  # check is logged in
        if not g.user.is_authenticated():
            abort(401)
        user = User.get_user(g.user.email)
        return UserSerializer(user).data

    def post(self):  # login
        form = SessionCreateForm()
        if not form.validate_on_submit():
            abort(422, message=form.errors)

        user = User.get_user(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return UserSerializer(user).data, 201
        abort(401)

    @login_required
    def delete(self):  # logout
        logout_user()
        return


class TaskListView(restful.Resource):
    @login_required
    def get(self):
        posts = Task.query.all()
        return TaskSerializer(posts, many=True).data

    @login_required
    def post(self):
        form = TaskCreateForm()
        if not form.validate_on_submit():
            abort(422, message=form.errors)
        task = Task(form.title.data, form.description.data)
        db.session.add(task)
        db.session.commit()
        return TaskSerializer(task).data, 201


class TaskView(restful.Resource):
    @login_required
    def get(self, id):  # get_task
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        return TaskSerializer(task).data

    @login_required
    def put(self, id):  # update_task
        form = TaskCreateForm()
        if not form.validate_on_submit():
            abort(422, message=form.errors)
        task = Task(form.title.data, form.description.data)
        db.session.add(task)
        db.session.commit()
        return TaskSerializer(task).data, 201

    @login_required
    def delete(self, id):  # delete_task
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        db.session.delete(task)
        db.session.commit()
        return


api.add_resource(UserListView, '/%s/api/users' % config.App.NAME, endpoint='users')
api.add_resource(UserView, '/%s/api/users/<int:id>' % config.App.NAME, endpoint='user')
api.add_resource(SessionView, '/%s/api/sessions' % config.App.NAME, endpoint='sessions')
api.add_resource(TaskListView, '/%s/api/tasks' % config.App.NAME, endpoint='tasks')
api.add_resource(TaskView, '/%s/api/tasks/<int:id>' % config.App.NAME, endpoint='task')
