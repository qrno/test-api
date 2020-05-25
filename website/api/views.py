from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_except
from rest_framework.parsers import JSONParser
from api.Models import Student
from api.serializers import StudentSerializer

@csrf_except
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
