from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import AdminUserSerializer

class AdminUserView(APIView):
  def post(self, request):
    serializer = AdminUserSerializer(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
    except ValidationError as e:
      return Response({'message': str(e)}, status=400)

    user = serializer.save()
    return Response({'message': 'Admin user created successfully.'})
