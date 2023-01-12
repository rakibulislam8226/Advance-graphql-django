from ...test_all_fields import models


def resolve_test_all_fields(self, info):
    return models.TestAllFields.objects.all()

