## API de Receitas com GraphQL
Repositório criado para estudar GraphQL. Foi feita uma API para representar um "caderno de receitas". 
É possível cadastrar receitas, ingredientes e unidades de medida.

### Rodando o projeto
```
docker-compose build
docker-compose up
```
### Utilizando a API
Acesse a url: http://127.0.0.1:8000/graphql

**Cadastrando itens**

Unidade de medida:
```
mutation {
  createUnidadeMedida(nome: "colher de chá") {
    unidadeMedida {
      nome
    }
  }
}
```

Receita:
```
mutation {
  createReceita(nome: "Bolo de iogurte") {
    receita {
      nome
    }
  }
}
```

Ingrediente:
```
mutation {
  createIngrediente(nome: "iogurte", quantidade: "1.5", unidadeMedidaId: 4, receitaId: 3) {
    ingrediente {
      nome,
      quantidade,
      unidadeMedida {
        nome
      },
      receita {
        nome
      }
    }
  }
}
```

**Consultando itens**

Todas as receitas:
```
query {
  listaReceitas {
    edges {
      node {
        id
        nome
        ingredientes {
          nome
          quantidade
          unidadeMedida{
            nome
          }
        }
      }
    }
  }
}
```

Receitas filtradas por nome:
```
query {
  listaReceitas(nome_Icontains: "cenoura") {
    edges {
      node {
        id
        nome
        ingredientes {
          nome
          quantidade
          unidadeMedida{
            nome
          }
        }
      }
    }
  }
}
```

Receita filtrada por id:
```
query {
  receita(id: "UmVjZWl0YU5vZGU6MQ==") {
    id
    nome
    ingredientes {
      nome
      quantidade
      unidadeMedida{
        nome
      }
    }
  }
}
```