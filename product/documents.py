from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'product'
    
    class Django:
        model = Product
        fields = ['name']
