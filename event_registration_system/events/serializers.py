from rest_framework import serializers
from .models import EventRegistration

class EventRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRegistration
        fields = '__all__'

    def validate_full_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Full name must be at least 5 characters."
            )
        return value

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError(
                "Email must end with @gmail.com"
            )
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError(
                "Age must be 18 and above."
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters."
            )
        return value