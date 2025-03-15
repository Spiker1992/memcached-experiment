from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

class CachedDataView(APIView):
    def get(self, request):
        data = cache.get('my_key')
        if not data:
            data = 'This is some cached data'
            cache.set('my_key', data, timeout=60*15)
        return Response({'data': data})
