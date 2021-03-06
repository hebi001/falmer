import graphene
from graphene_django import DjangoObjectType
from . import models


class ClientUser(DjangoObjectType):
    name = graphene.String()
    has_cms_access = graphene.Boolean()
    user_id = graphene.Int()

    class Meta:
        model = models.FalmerUser

    def resolve_name(self, info):
        return self.get_full_name()

    def resolve_user_id(self, info):
        return self.pk

    # this is a quick hack until we work on permissions etc
    def resolve_has_cms_access(self, info):
        return self.has_perm('wagtailadmin.access_admin')

