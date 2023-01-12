import graphene
from .events.my_new_app.schema import MyNewAppQueries, MyNewAppMutations
from .test_all_fields.schema import TestAllFieldsQueries, TestAllFieldsMutations
from .authentication.schema import AuthQueries, AuthMutations


class Query(MyNewAppQueries, TestAllFieldsQueries, AuthQueries):
    pass


class Mutation(MyNewAppMutations, TestAllFieldsMutations, AuthMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
