from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from .models import Snippet
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .serializers import SnippetSerializer
from rest_framework.views import APIView


def testView(request):
    return HttpResponse('<h1> Snippets app</h1>')


class SnippetList(APIView):

    """
    List all code snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
        Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, format=None, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, format=None, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if(request.method == 'GET'):
        snippets = Snippet.objects.all()
        ser = SnippetSerializer(snippets, many=True)
        return Response(ser.data)
    if(request.method == 'POST'):
        # data = JSONParser().parse(request.data)
        ser = SnippetSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            print(ser.validated_data)
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    snippet = get_object_or_404(Snippet, pk=pk)
    print(snippet)
    if(request.method == 'GET'):
        ser = SnippetSerializer(snippet, many=False)
        return Response(ser.data)
    if(request.method == 'PUT'):
        data = JSONParser().parse(request.data)
        ser = SnippetSerializer(snippet, data=data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if(request.method == 'DELETE'):
        snippet.delete()
        HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if(request.method == 'GET'):
#         snippets = Snippet.objects.all()
#         ser = SnippetSerializer(snippets, many=True)
#         return JsonResponse(ser.data, safe=False)
#     if(request.method == 'POST'):
#         data = JSONParser().parse(request.data)
#         ser = SnippetSerializer(data=data)
#         if (ser.is_valid()):
#             ser.save()
#             return JsonResponse(ser.validated_data, status=201)
#         else:
#             return JsonResponse(ser.errors, status=404)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     snippet = get_object_or_404(Snippet, pk=pk)
#     print(snippet)
#     if(request.method == 'GET'):
#         ser = SnippetSerializer(snippet, many=False)
#         return JsonResponse(ser.data, safe=True)
#     if(request.method == 'PUT'):
#         data = JSONParser().parse(request.data)
#         ser = SnippetSerializer(snippet, data=data)
#         if (ser.is_valid()):
#             ser.save()
#             return JsonResponse(ser.validated_data, status=201)
#         return JsonResponse(ser.errors, status=404)
#     if(request.method == 'DELETE'):
#         snippet.delete()
#         HttpResponse(status=204)
