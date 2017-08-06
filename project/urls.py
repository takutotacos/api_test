from django.conf.urls import url
from project import views

urlpatterns = [
    # url(r'^project/users$', views.user_list),
    url(r'^project/user/create/$', views.user_create),
    url(r'^project/user/login/$', views.user_login),
    # 登録した中ジャンル一覧
    url(r'^project/user/(?P<user_id>[0-9]+)/subscriptions/$', views.user_subscription),
    url(r'^project/user/(?P<user_id>[0-9]+)/subscriptions/delete/$', views.user_subscription_delete),

    # url('r^project/user/(?P<user_id>[0-9]+)/subscriptions/(?P<middle_genre_id>[0-9]+)/$', views.user_subscriptions),
    # 登録した中ジャンル一覧（地域ごと作る？？）

    url(r'^project/prefectures/$', views.prefecture_list),
    url(r'^project/cities/$', views.city_list),
    url(r'^project/large_genres/(?P<area_id>[0-9]+)/$', views.large_genre_list),
    url(r'^project/large_genres/(?P<area_id>[0-9]+/)/(?P<user_id>[0-9]+)/$', views.updated_topic_list_for_area),
    url(r'^project/middle_genres/(?P<large_genre_id>[0-9]+)/$', views.middle_genre_list),
    url(r'^project/topic_list/(?P<middle_genre_id>[0-9]+)/$', views.topic_list_for_middle_genre),
    url(r'^project/topic_detail/(?P<topic_id>[0-9]+)/$', views.topic_detail)
]
