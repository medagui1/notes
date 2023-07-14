from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics

# Create your views here.
class NoteList(generics.ListCreateAPIView) :
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetails(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
