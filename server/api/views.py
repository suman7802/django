import json
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from .models import Student
from .serializers import Student_serializer

@api_view(["GET"])
def api_home (request):
    return Response({'message': 'Hello, World!'})


@api_view(["POST"])
def api_body(request):
    data = json.loads(request.body)
    name = data.get('name', 'no name provided') #'no name provided' if not provided
    return Response({"response":f"your name is {name}"})


@api_view(["GET"])
def api_params(request):
    id_num = request.GET.get('id_num', 'no id_num provided')
    return Response({"response":f"your id is {id_num}"})


@csrf_exempt
@api_view(["POST"])
def api_form(request):   
    serialize_data = Student_serializer(data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return  Response({"response":f"{serialize_data.data}"})
    else:
        return Response({"response":"error detected"})


@api_view(['GET'])
def api_data_id(request, id):
    students = Student.objects.get(id=id)
    serializer_student = Student_serializer(students)
    return Response(serializer_student.data)


@api_view(['GET'])
def api_data(request):
    students = Student.objects.all()
    serializer_student = Student_serializer(students, many="true")
    return Response(serializer_student.data)