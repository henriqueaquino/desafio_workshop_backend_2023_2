from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Empregado, Departamento
from .serializers import EmpregadoSerializer, DepartamentoSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics

class EmpregadoList(APIView):
    def get(self, request, format=None):
        empregados = Empregado.objects.all()
        serializer = EmpregadoSerializer(empregados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpregadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentoList(APIView):
    def get(self, request, format=None):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpregadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empregado.objects.get(pk=pk)
        except Empregado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empregado = self.get_object(pk)
        serializer = EmpregadoSerializer(empregado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empregado = self.get_object(pk)
        serializer = EmpregadoSerializer(empregado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        empregado = self.get_object(pk)
        empregado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        departamento = self.get_object(pk)
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
