from rest_framework import serializers

from . import models

class FlowersSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.Flower
        fields = '__all__'

class GiftsSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.Gift
        fields = '__all__'

    #def create(self, validated_data):
    #    """Create and return a new user."""
#
#        user = models.UserProfile(
#            email=validated_data['email'],
#            name=validated_data['name']
#        )
#
#        user.set_password(validated_data['password'])
#        user.save()
#
#        return user
