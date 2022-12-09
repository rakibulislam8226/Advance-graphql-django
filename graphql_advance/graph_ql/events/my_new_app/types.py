from ....events.my_new_app.models import Category, Ingredient
from graphene_django import DjangoObjectType



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = "__all__"