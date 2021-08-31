import json
import faker
import random
import logging
from typing import List
from django.db.utils import IntegrityError

from social_network.models import (
    User,
    Post,
)

logger = logging.getLogger(__name__)

fake = faker.Faker()


def create_user():
    username = fake.simple_profile()['username']
    password=fake.password()
    try:
        user = User.objects.create(username=username)
        logger.warning('User created')
    except IntegrityError:
        username = fake.simple_profile()['username']
        user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return user


def create_posts(user: User, post_count: int):
    posts = []
    body = fake.paragraph(nb_sentences=5)
    for i in range(0, random.randint(1, post_count)):
        post = Post.objects.create(user=user, body=body)
        posts.append(post)

    logger.warning(f'{len(posts)} posts created')
    return posts


def create_likes(posts: List):
    users = User.objects.all()
    for post in posts:
        for i in range(0, random.randint(1, users.count())):
            user = users[i]
            post.likes.add(user)
            logger.warning(f'User:{user.username} like post-{post.id}')


def main():
    with open('/code/bot.json', 'r') as f:
        data = f.read()

    data = json.loads(data)
    users_count = data.get('number_of_users')
    posts_count = data.get('max_posts_user')

    for i in range(0,users_count):
        user = create_user()
        posts = create_posts(user, posts_count)
        create_likes(posts)


main()