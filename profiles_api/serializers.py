from rest_framework import serializers

<<<<<<< HEAD
from profiles_api import models

=======
>>>>>>> b4ff86bade7bde95aaab8c6bf892548e748d93a8

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
<<<<<<< HEAD


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile project"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
=======
>>>>>>> b4ff86bade7bde95aaab8c6bf892548e748d93a8
