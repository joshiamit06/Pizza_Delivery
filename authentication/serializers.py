from .models import User
from rest_framework import serializers
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=40,allow_blank=True)
    email=serializers.EmailField(max_length=80,allow_blank=False)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username = User.objects.filter(username=attrs['username']).exists()
        if username:
            raise ValidationError(detail='User with username already exists')

        email = User.objects.filter(email=attrs['email']).exists()
        if email:
            raise ValidationError(detail='User with email already exists')

        phonenumber = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phonenumber:
            raise ValidationError(detail='User with phonenumber already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user