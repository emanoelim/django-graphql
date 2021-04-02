import graphene
from graphene_django.filter import DjangoFilterConnectionField

from django_graphql.cookbook.mutations import CreateUnidadeMedida, CreateReceita, CreateIngrediente
from django_graphql.cookbook.queries import UnidadeMedidaNode, IngredienteNode, ReceitaNode


class Query(graphene.ObjectType):
    unidade_medida = graphene.relay.Node.Field(UnidadeMedidaNode)
    lista_unidades_medida = DjangoFilterConnectionField(UnidadeMedidaNode)

    ingrediente = graphene.relay.Node.Field(IngredienteNode)
    lista_ingredientes = DjangoFilterConnectionField(IngredienteNode)

    receita = graphene.relay.Node.Field(ReceitaNode)
    lista_receitas = DjangoFilterConnectionField(ReceitaNode)


class Mutation(graphene.ObjectType):
    create_unidade_medida = CreateUnidadeMedida.Field()
    create_receita = CreateReceita.Field()
    create_ingrediente = CreateIngrediente.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
