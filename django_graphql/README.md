### Exemplos de consulta

url: http://127.0.0.1:8000/graphql

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

Filtra receitas por nome:
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

Pega receita pelo id:
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