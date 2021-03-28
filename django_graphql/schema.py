import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

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


class Query(graphene.ObjectType):
    unidade_medida = graphene.relay.Node.Field(UnidadeMedidaNode)
    lista_unidades_medida = DjangoFilterConnectionField(UnidadeMedidaNode)

    ingrediente = graphene.relay.Node.Field(IngredienteNode)
    lista_ingredientes = DjangoFilterConnectionField(IngredienteNode)

    receita = graphene.relay.Node.Field(ReceitaNode)
    lista_receitas = DjangoFilterConnectionField(ReceitaNode)


schema = graphene.Schema(query=Query)

