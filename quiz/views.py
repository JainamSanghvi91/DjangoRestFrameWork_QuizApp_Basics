# This file contains views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET','POST'])
def index(request):
    # message = 'This Url is at index'
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        return Response(data={"message" :" GET Method - jainam"}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        print(request.data)
        return Response(data=request.data, status=status.HTTP_200_OK)
    else :
        return Response(data="Response method is not valid")


class Message(APIView):
    def get(self, request):
        print("Hit by get request")
        return Response(data="This is class based View hit by get request", status=status.HTTP_200_OK)

    def post(self, request):
        print("Hit by post request")
        print(request.data)
        return Response(data="This is class based View hit by the post request", status=status.HTTP_200_OK)
