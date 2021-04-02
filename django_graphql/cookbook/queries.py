import graphene
from graphene_django import DjangoObjectType

from django_graphql.cookbook.models import UnidadeMedida, Ingrediente, Receita


class UnidadeMedidaNode(DjangoObjectType):
    class Meta:
        model = UnidadeMedida
        fields = '__all__'
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'nome': ['exact'],
        }


class IngredienteNode(DjangoObjectType):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'nome': ['exact'],
        }


class ReceitaNode(DjangoObjectType):
    class Meta:
        model = Receita
        fields = '__all__'
        filter_fields = {
            'nome': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node,)

    ingredientes = graphene.List(IngredienteNode)

    def resolve_ingredientes(self, info):
        return Ingrediente.objects.filter(receita=self)