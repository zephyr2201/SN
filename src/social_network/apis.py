from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.params import date_from, date_to

from .serializers import (
    SignUpSerializer, ActivitySerializer,
    LikeAnaliticsSerializer, PostCreateSerializer,
)

from social_network.selectors import get_post, like_analitics
from social_network.services.utils import post_like, post_unlike, update_user_request


class SignUpApi(APIView):
    permission_classes = (AllowAny, )

    @swagger_auto_schema(
        operation_description='Registration',
        request_body=SignUpSerializer
    )
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'result': 1, 'success': True},
            status=status.HTTP_201_CREATED
        )


class ActivityApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serializer = ActivitySerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PostCreateApi(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        update_user_request(request.user)
        serializer = PostCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'result': 1, 'success': True},
            status=status.HTTP_201_CREATED
        )


class LikeApi(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, post_id):
        update_user_request(request.user)
        post = get_post(post_id)
        post_like(post, request.user)
        return Response(
            {'result': 1, 'success': True},
            status=status.HTTP_200_OK
        )


class UnLikeApi(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, post_id):
        update_user_request(request.user)
        post = get_post(post_id)
        post_unlike(post, request.user)
        return Response(
            {'result': 1, 'success': True},
            status=status.HTTP_200_OK
        )


class LikeAnaliticsApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='User registration',
        manual_parameters=[
            date_from, date_to
        ]
    )
    def get(self, request):
        update_user_request(request.user)
        params = request.query_params
        date_from = params.get('date_from')
        date_to = params.get('date_to')
        likes = like_analitics(date_from, date_to)
        print(likes)
        serializer = LikeAnaliticsSerializer(likes, many=True)
        data = serializer.data
        # print(data)
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
