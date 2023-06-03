from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class AdminUserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=150)
  password = serializers.CharField(max_length=128, write_only=True)

  def create(self, validated_data):
    username = validated_data['username']
    password = validated_data['password']
    # location = models.CharField(max_length=255)
    # phone = models.CharField(max_length=255, help_text='Use (,) comma for separate phone numbers')
    # sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    # dob = models.DateField()

    if User.objects.filter(username=username).exists():
      raise ValidationError("User with this username already exists.")

    user = User.objects.create_user(
      username=username,
      password=password,
      is_staff=True,
      is_superuser=True
    )
    return user
