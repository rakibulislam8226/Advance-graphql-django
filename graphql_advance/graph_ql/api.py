import graphene
from .events.my_new_app.schema import MyNewAppQuries, MyNewAppMutations
from .test_all_fields.schema import TestAllFieldsQuries, TestAllFieldsMutations


class Query(MyNewAppQuries,TestAllFieldsQuries):
    pass



class Mutation(MyNewAppMutations,TestAllFieldsMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)