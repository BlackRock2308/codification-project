from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404 
from RestApiServer.models import Codification
from RestApiServer.serializers import CodificationSerializer



class CodificationList(APIView):
    
    def get(self, request, format=None):
        codifications = Codification.objects.all()
        serializer = CodificationSerializer(codifications, many=True)
        return Response(serializer.data)

    def post(self, request, format=True):
        serializer = CodificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodificationDetail(APIView):

    def get_object(self, pk):
        try:
            return Codification.objects.get(pk=pk)
        except Codification.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        codification = self.get_object(pk)
        serializer = CodificationSerializer(codification, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        codification = self.get_object(pk)
        serializer = CodificationSerializer(codification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        codification = self.get_object(pk)
        codification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)