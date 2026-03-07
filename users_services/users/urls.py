from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from . import views

urlpatterns = [
    # --- RUTAS PARA USUARIOS ---
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # --- RUTAS PARA EMPLEADOS (Las tuyas) ---
    path('empleado/', views.EmpleadoList.as_view(), name='empleado-list'),
    path('empleado/<int:pk>/', views.EmpleadoDetail.as_view(), name='empleado-detail'),

    # --- RUTA GRAPHQL (La que ya tenías) ---
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]