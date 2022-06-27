from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError("Email already exists")
        except User.DoesNotExist as error:
            return email
        except serializers.ValidationError:
            raise serializers.ValidationError("Email already exists")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
