from django.conf.urls import include, url
from . import views # importando las views del blog

urlpatterns = [
	url(r'^$', views.post_list),
]