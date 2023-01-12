from ...test_all_fields import models
from graphene_django import DjangoObjectType



class TestAllFieldsType(DjangoObjectType):
    class Meta:
        model = models.TestAllFields
        fields = "__all__"
        


