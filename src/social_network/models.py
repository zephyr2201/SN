from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    objects = UserManager()
    username = models.CharField(max_length=100, unique=True, db_index=True, null=False, blank=False)
    last_request = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='posts')
    body = models.TextField(default=" ", blank=True)
    likes = models.ManyToManyField(User, blank=True, through='Like', related_name='likes')


class Like(models.Model):
    time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
