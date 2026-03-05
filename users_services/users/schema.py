import graphene
from graphene_django.types import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(pk=id)

# Mutations


class CreateUser(graphene.Mutation):

    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()

    def mutate(self, info, name, email, phone):

        user = User(
            name=name,
            email=email,
            phone=phone
        )

        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
