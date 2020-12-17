from .models import Post
from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Radio, Post

from rest_framework.permissions import IsAuthenticated


class RadioViewSet(APIView):
    def get(self, request, *args, **kwargs):
        radios = Radio.objects.all()
        serializer = serializers.RadioSerializer(radios, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        radios = Radio.objects.all()
        # This is how we serialize one instance
        #serializer = serializers.RadioSerializer(radios.first())
        # this is how we serialize multiple instances
        serializer = serializers.RadioSerializer(radios, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TestView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.PostSerializer(data=request.data)
        # check if the serialized data is valid
        if serializer.is_valid():
            # This will automatically match to the fields of the model and create an new post
            post = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# def testView(request):
#     # we passe date in the json response
#     # an api only cares about the data in form of a dictionnary
#     # we do not passe html or anything only the data
#     # if we want to passe a list of dictionnaries we use safe=False
#     data = {
#         'user': 'test@user.com',
#         'age': 23,
#         'rank': 2345,
#     }
#     return JsonResponse(data)


# def testListView(request):
#     # we passe date in the json response
#     # an api only cares about the data in form of a dictionnary
#     # we do not passe html or anything only the data
#     # if we want to passe a list of dictionnaries we use safe=False
#     data = []
#     for i in range(0, 10):
#         data.append({
#             'user': 'test@user.com',
#             'age': 23,
#             'rank': 2345,
#         })
#     return JsonResponse(data, safe=False)
