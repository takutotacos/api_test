from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from project.models import User, LargeGenre, MiddleGenre, Topic, Prefecture, City, Subscription
from project.serializers import UserSerializer, LargeGenreSerializer, MiddleGenreSerializer, TopicSerializer, PrefectureSerializer, CitySerializer, SubscriptionSerializer
from collections import OrderedDict
import pdb

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        # pdb.set_trace()
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST.get('email', ''), password=request.POST.get('password',''))
        except User.DoesNotExist:
            return HttpResponse(status=404)
        serializer = UserSerializer(user)
        data = OrderedDict([('user', serializer.data)])
        return JsonResponse(data, safe=False)

@csrf_exempt
def user_subscription(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        subscriptions = Subscription.objects.filter(user_id=user.id)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        data = OrderedDict([('subscriptions', serializer.data)])
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        # パラメータ: user_id, middle_genre_id
        subscription = user.subscription_set.create(middle_genre_id=request.POST.get('middle_genre_id', ''))
        serializer = SubscriptionSerializer(data=subscription)
        # serializer = SubscriptionSerializer(data=(request.POST.get('user_id'))
        if serializer.is_valid():
            serializer.save()
            data = OrderedDict([('subscription', serializer.data)])
            return JsonResponse(data, status=201)
        data = OrderedDict([('subscription', serializer.data)])
        return JsonResponse(data, status=400)

@csrf_exempt
def user_subscription_delete(request, user_id):
    if request.method == 'POST':
        Subscription.objects.get(user_id=user_id, middle_genre_id=request.POST.get('middle_genre_id', '')).delete()
        return JsonResponse(data='', safe=False, status=200)

@csrf_exempt
def prefecture_list(request):
    if request.method == 'GET':
        try:
            prefectures = Prefecture.objects.all()
        except Prefecture.DoesNotExist:
            return HttpResponse(status=404)
        serializer = PrefectureSerializer(prefectures, many=True)
        data = OrderedDict([('prefecture_list', serializer.data)])
        return JsonResponse(data, safe=False)

@csrf_exempt
def city_list(request):
    if request.method == 'GET':
        try:
            cities = City.objects.all()
            print(cities)
        except City.DoesNotExist:
            return HttpResponse(status=404)
        serializer = CitySerializer(cities, many=True)
        data = OrderedDict([('city_list', serializer.data)])
        return JsonResponse(data, safe=False)

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
def topic_list_for_middle_genre(request, middle_genre_id):
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

@csrf_exempt
def updated_topic_list_for_area(request, area_id, user_id):
    return