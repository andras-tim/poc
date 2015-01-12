from flask import g, redirect, url_for, abort
from flask.ext import restful

from .server import config, app, api, db, bcrypt, auth
from .models import User, Task
from .forms import UserCreateForm, TaskCreateForm
from .serializers import UserSerializer, TaskSerializer


@app.route('/test', methods=['GET'])
@app.route('/test/', methods=['GET'])
def index():
    return redirect(url_for('static', filename='index.html'))


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    abort(500)


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.user = user
    return bcrypt.check_password_hash(user.password, password)


class UserListView(restful.Resource):
    def post(self):  # create_user
        form = UserCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422

        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return UserSerializer(user).data


class UserView(restful.Resource):
    @auth.login_required
    def delete(self, id):  # delete_user
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404)
        if g.user.id != id:
            abort(403)
        db.session.delete(user)
        db.session.commit()
        return


class TaskListView(restful.Resource):
    @auth.login_required
    def get(self):
        posts = Task.query.all()
        return TaskSerializer(posts, many=True).data

    @auth.login_required
    def post(self):
        form = TaskCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
        task = Task(form.title.data, form.description.data)
        db.session.add(task)
        db.session.commit()
        return TaskSerializer(task).data, 201


class TaskView(restful.Resource):
    @auth.login_required
    def get(self, id):  # get_task
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        return TaskSerializer(task).data

    @auth.login_required
    def put(self, id):  # update_task
        form = TaskCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
        task = Task(form.title.data, form.description.data)
        db.session.add(task)
        db.session.commit()
        return TaskSerializer(task).data, 201

    @auth.login_required
    def delete(self, id):  # delete_task
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        db.session.delete(task)
        db.session.commit()
        return


api.add_resource(UserListView, '/%s/api/users' % config.App.NAME, endpoint='users')
api.add_resource(UserView, '/%s/api/users/<int:id>' % config.App.NAME, endpoint='user')
api.add_resource(TaskListView, '/%s/api/tasks' % config.App.NAME, endpoint='tasks')
api.add_resource(TaskView, '/%s/api/tasks/<int:id>' % config.App.NAME, endpoint='task')
