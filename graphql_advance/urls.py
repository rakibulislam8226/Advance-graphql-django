from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

GraphQLView.graphiql_template = "graphene_graphiql_explorer/graphiql.html"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('graphql_advance.events.my_new_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r"^graphql/$", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
