from carros.serializers import MTCarsSerializer
from rest_framework.views import APIView
from carros.models import MTCars
from rest_framework.response import Response

class CarsView(APIView):
    def get(self, request):
        queryset = MTCars.objects.all().order_by('name')
        # importante informar que o queryset terá mais de 1 resultado usando many=True
        serializer = MTCarsSerializer(queryset, many=True )
        return Response(serializer.data)