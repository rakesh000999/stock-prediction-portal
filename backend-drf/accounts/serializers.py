from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 

    def create(self, validated_data):

        # User.objects.create_user() => automatically hashes the password
        # User.ojects.create() => save the password in plain text

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],  
            validated_data['password']
        )

        # or

        # user = User.objects.create_user(**validated_data)

        return user


        