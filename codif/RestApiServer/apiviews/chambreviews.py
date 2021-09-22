from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404 
from RestApiServer.models import Chambre
from RestApiServer.serializers import ChambreSerializer


class ChambreList(APIView):
    
    def get(self, request, format=None):
        chambres = Chambre.objects.all()
        serializer = ChambreSerializer(chambres, many=True)
        return Response(serializer.data)

    def post(self, request, format=True):
        serializer = ChambreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChambreDetail(APIView):
    
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Chambre.objects.get(pk=pk)
        except Chambre.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        chambre = self.get_object(pk)
        serializer = ChambreSerializer(chambre, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chambre = self.get_object(pk)
        serializer = ChambreSerializer(chambre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chambre = self.get_object(pk)
        chambre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
