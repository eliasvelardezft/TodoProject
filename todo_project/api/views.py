from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, FolderSerializer

from .models import Task, Folder

# Create your views here.


## This are the views for handling the tasks

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'task-List': '/task-list/',
        'task-Detail View': '/task-detail/<str:pk>',
        'task-Create': '/task-create/',
        'task-Update': '/task-update/<str:pk>',
        'task-Delete': '/task-delete/<str:pk>',
        'folder-List': '/folder-list/',
        'folder-Detail View': '/folder-detail/<str:pk>',
        'folder-Create': '/folder-create/',
        'folder-Update': '/folder-update/<str:pk>',
        'folder-Delete': '/folder-delete/<str:pk>',

    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('Item succesfully deleted!')




## This is the views for handling the folders



@api_view(['GET'])
def folderList(request):
    folders = Folder.objects.all().order_by('-id')
    serializer = FolderSerializer(folders, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def folderDetail(request, pk):
    folders = Folder.objects.get(id=pk)
    serializer = FolderSerializer(folders, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def folderCreate(request):
    serializer = FolderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    
    return Response(serializer.data)


@api_view(['POST'])
def folderUpdate(request, pk):
    folder = Folder.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    
    return Response(serializer.data)

@api_view(['DELETE'])
def folderDelete(request, pk):
    folder = Folder.objects.get(id=pk)
    folder.delete()
    
    return Response('Folder succesfully deleted!')


