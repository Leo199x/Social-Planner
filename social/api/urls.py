from django.urls import path
from .views import Profilelist, ProfileDetail, EventList, EventDetail

urlpatterns = [
    path('profile/', Profilelist.as_view()),
    path('profile/', ProfileDetail.as_view()),
    path('event/', EventList.as_view()),
    path('event/', EventDetail.as_view()),


]
