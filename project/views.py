from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from project.models import User, LargeGenre, MiddleGenre, Topic
from project.serializers import UserSerializer, LargeGenreSerializer, MiddleGenreSerializer, TopicSerializer
from collections import OrderedDict
import pdb

# @csrf_exempt
# def user_list(request):
#     """
#     List all users, or create a new users
#
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         pdb.set_trace()
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.data, status=400)
#
# @csrf_exempt
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a user.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=404)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)
#
@csrf_exempt
def large_genre_list(request, area_id):
    if request.method == 'GET':
        try:
            lgenres = LargeGenre.objects.filter(city_id=area_id)
        except LargeGenre.DoesNotExist:
            return HttpResponse(status=404)
        serializer = LargeGenreSerializer(lgenres, many=True)
        data = OrderedDict([('large_genre_list', serializer.data)])
        return JsonResponse(data, safe=False)

@csrf_exempt
def middle_genre_list(request, large_genre_id):
    if request.method == 'GET':
        try:
            mgenres = MiddleGenre.objects.filter(large_genre_id=large_genre_id)
        except MiddleGenre.DoesNotExist:
            return HttpResponse(status=404)
        serializer = MiddleGenreSerializer(mgenres, many=True)
        data = OrderedDict([('middle_genre_list', serializer.data)])
        return JsonResponse(data, safe=False)

@csrf_exempt
def topic_list(request, middle_genre_id):
    if request.method == 'GET':
        try:
            topics = Topic.objects.filter(middle_genre_id=middle_genre_id)
        except Topic.DoesNotExist:
            return HttpResponse(status=404)
        serializer = TopicSerializer(topics, many=True)
        data = OrderedDict([('topic_list', serializer.data)])
        return JsonResponse(data, safe=False)

@csrf_exempt
def topic_detail(request, topic_id):
    if request.method == 'GET':
        try:
            topic = Topic.objects.get(pk=topic_id)
        except Topic.DoesNotExist:
            return HttpResponse(status=404)
        serializer = MiddleGenreSerializer(topic)
        data = OrderedDict([('topic', serializer.data)])
        return JsonResponse(data, safe=False)
