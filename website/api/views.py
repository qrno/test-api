from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from api.models import Student, Dict, Word
from api.serializers import StudentSerializer, DictSerializer, WordSerializer

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def dict_list(request):
    if request.method == 'GET':
        dicts = Dict.objects.all()
        serializer = DictSerializer(dicts, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def dict_detail(request, pk):
    try:
        dict = Dict.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DictSerializer(dict)
        return JsonResponse(serializer.data)

@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
