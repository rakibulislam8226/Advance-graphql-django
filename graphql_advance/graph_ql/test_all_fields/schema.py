import graphene
from . import types
from . import resolvers
from . import mutations


class TestAllFieldsQueries(graphene.ObjectType):
    test_all_fields = graphene.List(types.TestAllFieldsType)

    # all the resolvers
    def resolve_test_all_fields(self, info):
        return resolvers.resolve_test_all_fields(self, info)


class TestAllFieldsMutations(graphene.ObjectType):
    create_test_all_fields = mutations.CreateTestAllFields.Field()
    update_test_all_fields = mutations.UpdateTestAllFields.Field()
    delete_test_all_fields = mutations.DeleteTestAllField.Field()
