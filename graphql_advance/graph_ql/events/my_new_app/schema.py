import graphene
from . import types
from . import resolvers
from . import mutations
from django.contrib.auth.models import User


class MyNewAppQueries(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    total_user = graphene.String(default_value=len(User.objects.all()))
    active_user = graphene.String(default_value=len(User.objects.filter(is_active=True)))
    all_category = graphene.List(types.CategoryType)
    ingredients = graphene.List(types.IngredientsType)

    # all the resolvers
    def resolve_all_category(self, info):
        return resolvers.resolve_all_category(self, info)

    def resolve_ingredients(self, info):
        return resolvers.resolve_ingredients(self, info)


class MyNewAppMutations(graphene.ObjectType):
    create_ingredients = mutations.CreateIngredients.Field()
    update_ingredients = mutations.UpdateIngredients.Field()
    delete_ingredients = mutations.DeleteIngredients.Field()
