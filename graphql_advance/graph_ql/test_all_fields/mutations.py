import graphene
from ...test_all_fields import models
from ...test_all_fields import serializers
from . import types
from graphene_django.rest_framework.mutation import SerializerMutation


# Ingredients Start #
class CreateTestAllFields(SerializerMutation):
    class Meta:
        serializer_class = serializers.TestAllFieldsSerializer
        model_operations = ['create']
        convert_choices_to_enum = False
    
    @classmethod
    def mutate(cls, root, info, **kwargs):
        kwargs['input']['integradient'] = kwargs['input']['integradient'].split(',')
        return super().mutate(root, info, **kwargs)
    
    
class UpdateTestAllFields(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        integradient = graphene.ID()
        category = graphene.ID()
        status_selection = graphene.String()
        max_number_events = graphene.String()
        internal_note = graphene.String()
        is_active = graphene.ID()
        publish_status = graphene.ID()

    testallfield = graphene.Field(types.TestAllFieldsType)

    @classmethod
    def mutate(cls, root, info, id, **update_data):
        testallfield = models.TestAllFields.objects.filter(id=id)
        if testallfield:
            params = update_data
            testallfield.update(**{k: v for k, v in params.items() if params[k]})
            return UpdateTestAllFields()
        else:
            raise ValueError("Data not found")


class DeleteTestAllField(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    testallfield = graphene.Field(types.TestAllFieldsType)

    @classmethod
    def mutate(cls, root, info, id):
        testallfield = models.TestAllFields.objects.get(id=id)
        testallfield.delete()

# End Ingredients #











