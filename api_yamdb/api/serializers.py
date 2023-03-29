from rest_framework import serializers

from reviews.models import User


class AuthSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if self.context.get('request').username == 'me':
            raise serializers.ValidationError(
                'Юзернейм не может быть "me".'
            )
        return value

    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username', 'email')
            )
        ]
