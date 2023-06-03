from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
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

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=15)
    # Add your extra fields here
		

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirm_password', 'email', 'phone', 'first_name', 'last_name']  # Include extra fields

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        # Add any additional validation for extra fields here
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from validated data

        # Extract and remove extra fields from validated_data
        phone = validated_data.pop('phone')

        user = CustomUser.objects.create_user(**validated_data)

        # Save the extra fields to the user model
        user.phone = phone
        user.save()

        return user