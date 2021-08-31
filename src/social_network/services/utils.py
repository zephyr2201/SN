import pytz
from datetime import datetime


def update_user_request(user):
    user.last_request = datetime.now().replace(tzinfo=pytz.UTC)


def post_like(post, user):
    post.likes.add(user)
    post.save()


def post_unlike(post, user):
    post.likes.remove(user)
    post.save()
