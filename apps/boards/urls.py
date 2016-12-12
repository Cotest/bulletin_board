from django.conf.urls import url

from .views import BoardListView
from .views import BoardCreateView
from .views import BoardUpdateView

urlpatterns = [
    url(r'^$', BoardListView.as_view(), name='index'),
    url(r'^add/$', BoardCreateView.as_view(), name='post_create'),
    url(r'^update/(?P<pk>\d+)$', BoardUpdateView.as_view(), name='post_update'),
]