from django.shortcuts import render
from rest_framework.views import APIView
from qv1.models import Question,Quiz
from qv1.serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Create your views here.

# class QuizView(viewsets.ModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

class QuizView(APIView):
    def get_object(self):
        try:
            return Quiz.objects.all()
        except:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, format=None):
        queryset = self.get_object()
        serializer = QuizSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        queryset = Quiz.objects.get(id = request.data['id'])
        queryset.delete()
        return Response(data="Deleted Successfully", status=status.HTTP_410_GONE)

    def put(self, request):
        quiz = Quiz.objects.get(id = request.data['id'])
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class QuizView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

@api_view(['GET'])
def quiz_view(request, slug):
    # message = 'This Url is at index'
    print(request.user)
    print(request.auth)
    try:
        quiz_data = Question.objects.get(id = slug)
        if request.method == 'GET':
            serializer = QuestionSerializer(quiz_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        # if request.method == 'POST':
        #     print(request.data)
        #     return Response(data=request.data, status=status.HTTP_200_OK)
    except Quiz.DoesNotExist :
        return Response(data="Response method is not valid")

@api_view(['PUT'])
def quiz_put_view(request, slug):
    try:
        quiz_data = Question.objects.get(id = slug)
    except Quiz.DoesNotExist :
        return Response(data="Response method is not valid")
    if request.method == 'PUT':
        serializer = QuestionSerializer(quiz_data, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def quiz_delete_view(request, slug):
    try:
        quiz_data = Question.objects.get(id = slug)
    except Quiz.DoesNotExist :
        return Response(data="Response method is not valid")
    if request.method == 'DELETE':
        operation = quiz_data.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

# @api_view(['POST'])
# def quiz_post_view(request, slug):
    