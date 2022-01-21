from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSearchSerializer, ProductSerializer
from .documents import ProductDocument
from django.http import HttpResponse
from elasticsearch_dsl import Q
import json
class ProductSearch(APIView):
    productsearchserializer = ProductSearchSerializer
    search_document = ProductDocument

    def get(self, request, query):
        q = Q(
            'multi_match',
            query=query,
            fields=[
                'name',
            ]
        )
        search = self.search_document.search().query(q)
        response = search.execute()

        serializer = ProductSerializer(response, many=True)
        return HttpResponse(json.dumps(serializer.data))