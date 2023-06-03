from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import AdminUserSerializer, UserCreateSerializer

class AdminUserView(APIView):
  def post(self, request):
    serializer = AdminUserSerializer(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
    except ValidationError as e:
      return Response({'message': str(e)}, status=400)

    user = serializer.save()
    return Response({'message': 'Admin user created successfully.'})


class UserCreateView(APIView):
  def post(self, request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({'message': 'User created successfully.'})
    return Response(serializer.errors, status=400)