from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username', 'password')


class AuthUserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
