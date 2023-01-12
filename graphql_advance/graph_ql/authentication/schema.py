import graphene
import graphql_jwt
from . import resolvers
from . import mutations
from . import types
from django.contrib.auth.models import User
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


# create user start #
class CreateUser(graphene.Mutation):
    user = graphene.Field(types.AuthUserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)
# End create user #


class AuthQueries(graphene.ObjectType):
    me = graphene.Field(types.AuthUserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user


class AuthMutations(graphene.ObjectType):
    create_user = CreateUser.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()



