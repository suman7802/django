import json
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

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


# --------------------------------------------------------------------


@api_view(['POST'])
def register(request):
    data = json.loads(request.body)
    email = data.get('email', 'no email provided')
    password = data.get('password', 'no password provided')

    if User.objects.filter(email=email).exists():
        return Response({"response":"email already exists"})
    else:
        user = User(email=email)
        user.set_password(password)
        user.save()
        return Response({"response":"user created successfully"})


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data.get('email', 'no email provided')
    password = data.get('password', 'no password provided')

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if user.check_password(password):
            return Response({"response":"login successful"})
        else:
            return Response({"response":"wrong password"})
    else:
        return Response({"response":"user does not exist"})