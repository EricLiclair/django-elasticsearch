from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSearchSerializer
from .documents import ProductDocument
from django.http import HttpResponse
from elasticsearch_dsl import Q

class ProductSearch(APIView):
    productserializer = ProductSearchSerializer
    search_document = ProductDocument

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'name',
                ]
            )
            search = self.search_document.search().query(q)
            response = search.execute()

            serializer = self.productserializer(response, many=True)
            return HttpResponse(serializer.data)
        except expression as e:
            return HttpResponse(e, status=500)
