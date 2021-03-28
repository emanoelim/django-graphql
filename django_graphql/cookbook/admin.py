from django.contrib import admin

from django_graphql.cookbook.models import UnidadeMedida, Receita, Ingrediente

admin.site.register(UnidadeMedida)
admin.site.register(Receita)
admin.site.register(Ingrediente)

