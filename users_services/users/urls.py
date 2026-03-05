from django.urls import path
from .views import UserList, UserDetail
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
