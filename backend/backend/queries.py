import graphene
from .types import TopicsType
from api.models import Topics

class Query(graphene.ObjectType):
    topics = graphene.List(TopicsType)
    topic = graphene.Field(TopicsType, topicId=graphene.String())

    # Resolver for topics field
    def resolve_topics(parent, info):
        return Topics.objects.all().order_by('created_at')

    # Resolver for topic field
    def resolve_topic(parent, info):
        return Topics.objects.get(id=topicId)