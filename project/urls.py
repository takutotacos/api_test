from django.conf.urls import url
from project import views

urlpatterns = [
    # url(r'^project/users$', views.user_list),
    # url(r'^project/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^project/large_genres/(?P<area_id>[0-9]+)/$', views.large_genre_list),
    url(r'^project/middle_genres/(?P<large_genre_id>[0-9]+)/(?P<area_id>[0-9]+)/$', views.middle_genre_list),
    url(r'^project/topic_list/(?P<area_id>[0-9]+)/(?P<middle_genre_id>[0-9]+)/$', views.topic_list),
    url(r'^project/topic_detail/(?P<topic_id>[0-9]+)/$', views.topic_detail)
]
