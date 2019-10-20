from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView.
    Converts and validates the inputs to the methods
    of an API
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes an user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = { # Making exceptions in the password filed
            'password': {
                'write_only': True,   # can only be writable and not readable
                'style': {'input_type': 'password'} # treat as a password field in the input form
            }
        }

    def create(self, validated_data):
        """
        After validating the data by the serializer,
        Django will run the default create() function.
        Overwriting the function create() so that Django
        can write the password hashed to the database
        """

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on') #id is automatically set, and created_on
        extra_kwargs = {'user_profile': {'read_only': True}}
