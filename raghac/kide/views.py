from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import permission_classes
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission

# ravi dzmao

class TaskPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method in ['PUT', 'PATCH', 'UPDATE']:
            return  request.user == obj.assignee
        if request.method == 'DELETE':
            return request.user.is_superuser




class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [TaskPermissions]




