import graphene
from graphene_django.types import DjangoObjectType
from . import models


class ImageType(DjangoObjectType):

    class Meta:
        model = models.Image


class LikeType(DjangoObjectType):

    class Meta:
        model = models.Like


class CommentType(DjangoObjectType):

    class Meta:
        model = models.Comment
