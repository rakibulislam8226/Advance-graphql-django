import graphene
from .events.my_new_app.schema import MyNewAppQueries, MyNewAppMutations
from .test_all_fields.schema import TestAllFieldsQueries, TestAllFieldsMutations


class Query(MyNewAppQueries, TestAllFieldsQueries):
    pass


class Mutation(MyNewAppMutations, TestAllFieldsMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
