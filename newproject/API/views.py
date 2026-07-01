from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerializer


# GET API
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# POST API
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT' , 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method =='GET':
        Serializer = UserSerializer(user)
        return Response(Serializer.data)

    elif request.method =='PUT':
        Serializer = UserSerializer(user, data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        return Response(Serializer.errors, status=status.HTTP_404_BAD_REQUSET)

    elif request.method =='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)