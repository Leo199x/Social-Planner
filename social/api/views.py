from rest_framework import generics

from .models import Profile, Event
from .serializers import ProfileSerializer, Eventserializer

# Create your views here.

class Profilelist(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class EventList(generics.ListCreateAPIView):
    serializer_class = Eventserializer
    queryset = Event.objects.all()

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Eventserializer
    queryset = Event.objects.all()


