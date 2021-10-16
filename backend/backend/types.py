import graphene
from graphene_django import DjangoObjectType, DjangoListField
from api.models import *

class TopicsType(DjangoObjectType):
    class Meta:
        model = Topics
        fields = ("id", "title", "subtitle", "content", "created_at")

class TopicsInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    subtitle = graphene.String()
    content = graphene.String()
    created_at = graphene.Date()