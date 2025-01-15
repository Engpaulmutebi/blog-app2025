from django.urls import path # type: ignore
from . import views


urlpatterns = [
  path("",views.Starting_page,name = 'starting-page'),
  path("posts",views.Posts,name = 'posts-page'),
  path("posts/<slug:slug>",views.Posts_detail, name = 'post-detail-page'),
  
]