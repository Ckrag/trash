from django.urls import path, include

from . import views
from .views import SignUpView

app_name = 'public'
urlpatterns = [
    path('', views.index, name='index'),
    path('contribute/', views.contribute, name='contribute'),
    path('contribution/<int:route_id>/', views.contribution, name='contribution'),
    path('nodes/', views.get_map_relevant_nodes, name='nodes'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]
