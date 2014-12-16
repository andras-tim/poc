from flask import render_template, current_app
from flask.ext.mail import Message
from app import mail
from .decorators import async
from config import ADMINS


@async
def __send_async_email(context, msg):
    with context:
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    __send_async_email(current_app.app_context(), msg)


def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed, follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))
