import graphene
from .types import TopicsType,TopicsInput
from api.models import Topics

class AddTopic(graphene.Mutation):
    class Arguments:
        input = TopicsInput(required=True)

    topic = graphene.Field(TopicsType)

    def mutate(parents, info, input=None):
        if input is None:
            return AddTopic(topic=None)
        _topic = Topics.objects.create(**input)
        return AddTopic(topic=_topic)

class Mutation(graphene.ObjectType):
    add_topic = AddTopic.Field()