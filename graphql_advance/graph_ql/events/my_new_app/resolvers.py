from ....events.my_new_app import models


def resolve_all_category(self, info):
    return models.Category.objects.all()


def resolve_ingredients(self, info):
    return models.Ingredient.objects.all()