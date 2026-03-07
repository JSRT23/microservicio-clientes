import graphene
from graphene_django.types import DjangoObjectType
from .models import User, Empleado

# --- 1. TIPOS (El traductor de datos para GraphQL) ---
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"

class EmpleadoType(DjangoObjectType):
    class Meta:
        model = Empleado
        fields = "__all__"

# --- 2. CONSULTAS (Para buscar y leer datos) ---
class Query(graphene.ObjectType):
    # Consultas de Usuarios
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    # Consultas de Empleados (Las tuyas)
    all_empleados = graphene.List(EmpleadoType)
    empleado = graphene.Field(EmpleadoType, id=graphene.Int())

    # Resolvers (Las funciones que van a la base de datos)
    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(pk=id)

    def resolve_all_empleados(root, info):
        return Empleado.objects.all()

    def resolve_empleado(root, info, id):
        return Empleado.objects.get(pk=id)

# --- 3. MUTACIONES (Para crear, editar o borrar datos) ---
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()

    def mutate(self, info, name, email, phone):
        user = User(name=name, email=email, phone=phone)
        user.save()
        return CreateUser(user=user)

class CreateEmpleado(graphene.Mutation):
    empleado = graphene.Field(EmpleadoType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        role = graphene.String()

    def mutate(self, info, name, email, phone, role):
        # create_at no se incluye porque se genera automáticamente
        empleado = Empleado(name=name, email=email, phone=phone, role=role)
        empleado.save()
        return CreateEmpleado(empleado=empleado)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_empleado = CreateEmpleado.Field()

# --- 4. CONSTRUCCIÓN DEL ESQUEMA FINAL ---
schema = graphene.Schema(query=Query, mutation=Mutation)