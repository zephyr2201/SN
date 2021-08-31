from django.core.exceptions import ValidationError
from django.db.models.aggregates import Count
from .models import Like, Post
from django.http import Http404


def get_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return post


def like_analitics(date_from, date_to):
    try:
        if date_from and date_to:
            return Like.objects.filter(
                time__range=(date_from, date_to)).values('time').annotate(count=Count('post'))
        elif date_to is None:
            return Like.objects.filter(
                time__gte=date_from).values('time').annotate(count=Count('post'))
        elif date_from is None:
            return Like.objects.filter(
                time__lte=date_to).values('time').annotate(count=Count('post'))
    except ValidationError:
        raise ValidationError('Invalid date')
