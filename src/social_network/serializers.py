import pytz
from datetime import datetime

from .models import Post, User

from django.db.utils import IntegrityError

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


VALIDATION_ERROR = ValidationError('Username is taken')


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=25)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        try:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
        except IntegrityError:
            raise VALIDATION_ERROR

        return user


class ActivitySerializer(serializers.Serializer):
    last_login = serializers.SerializerMethodField()
    last_request = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        date = obj.last_login.replace(tzinfo=pytz.UTC)
        date_str = datetime.strftime(date, '%Y.%m.%d %H:%m:%S')
        return date_str

    def get_last_request(self, obj):
        date = obj.last_request.replace(tzinfo=pytz.UTC)
        date_str = datetime.strftime(date, '%Y.%m.%d %H:%m:%S')
        return date_str


class LikeAnaliticsSerializer(serializers.Serializer):
    date = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_date(self, obj):
        return obj['time']


class PostCreateSerializer(serializers.Serializer):
    body = serializers.CharField()

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        obj = Post.objects.create(user=user, body=validated_data['body'])
        return obj
