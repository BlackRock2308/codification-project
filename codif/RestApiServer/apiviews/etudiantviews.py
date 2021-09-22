from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404 
from RestApiServer.models import Etudiant
from RestApiServer.serializers import EtudiantSerializer



class EtudiantList(APIView):
    
    def get(self, request, format=None):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantSerializer(etudiants, many=True)
        return Response(serializer.data)

    def post(self, request, format=True):
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EtudiantDetail(APIView):
    
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Etudiant.objects.get(pk=pk)
        except Etudiant.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        etudiant = self.get_object(pk)
        serializer = EtudiantSerializer(etudiant, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        etudiant = self.get_object(pk)
        serializer = EtudiantSerializer(etudiant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        etudiant = self.get_object(pk)
        etudiant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
