import graphene
from ....events.my_new_app import models
from ....events.my_new_app import serializers
from . import types
from graphene_django.rest_framework.mutation import SerializerMutation


# Ingredients Start #
class CreateIngredients(SerializerMutation):
    class Meta:
        serializer_class = serializers.IngredientSerializer
        model_operations = ['create']
        
        
class UpdateIngredients(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        notes = graphene.String()
        category = graphene.ID()
    
    ingredients = graphene.Field(types.IngredientsType)
    
    @classmethod
    def mutate(cls, root, info,id, name=None,notes=None, category=None):
        ingredients = models.Ingredient.objects.get(id=id)
        ingredients.id = id
        if name is not None:
            ingredients.name = name
        if notes is not None:
            ingredients.notes = notes
        if category is not None:
            ingredients.category = category
        ingredients.save()
        return UpdateIngredients(ingredients=ingredients)


class DeleteIngredients(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ingredients = graphene.Field(types.IngredientsType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredients = models.Ingredient.objects.get(id=id)
        ingredients.delete()

# End Ingredients #















