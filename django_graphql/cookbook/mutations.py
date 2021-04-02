import graphene

from django_graphql.cookbook.models import UnidadeMedida, Receita, Ingrediente
from django_graphql.cookbook.queries import UnidadeMedidaNode, ReceitaNode, IngredienteNode


class CreateUnidadeMedida(graphene.Mutation):
    class Arguments:
        nome = graphene.String()

    unidade_medida = graphene.Field(UnidadeMedidaNode)

    def mutate(self, info, nome):
        unidade_medida = UnidadeMedida.objects.create(
            nome=nome,
        )
        return CreateUnidadeMedida(
            unidade_medida=unidade_medida
        )


class CreateReceita(graphene.Mutation):
    class Arguments:
        nome = graphene.String()

    receita = graphene.Field(ReceitaNode)

    def mutate(self, info, nome):
        receita = Receita.objects.create(
            nome=nome,
        )
        return CreateReceita(
            receita=receita
        )


class CreateIngrediente(graphene.Mutation):
    class Arguments:
        nome = graphene.String()
        quantidade = graphene.Decimal()
        unidade_medida_id = graphene.Int()
        receita_id = graphene.Int()

    ingrediente = graphene.Field(IngredienteNode)

    def mutate(self, info, nome, quantidade, unidade_medida_id, receita_id):
        unidade_medida = UnidadeMedida.objects.get(id=unidade_medida_id)
        receita = Receita.objects.get(id=receita_id)
        ingrediente = Ingrediente.objects.create(
            nome=nome,
            quantidade=quantidade,
            unidade_medida=unidade_medida,
            receita=receita
        )
        return CreateIngrediente(
            ingrediente=ingrediente
        )
