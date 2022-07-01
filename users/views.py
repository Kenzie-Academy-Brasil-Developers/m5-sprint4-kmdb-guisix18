from multiprocessing import set_forkserver_preload
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from movie.permission import CustomPermission

from .models import User


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED
        )


class ListUserView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request):
        try:
            users = User.objects.all()

            result_page = self.paginate_queryset(users, request, view=self)

            serializer = UserSerializer(result_page, many=True)

            return self.get_paginated_response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ListUserByIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
