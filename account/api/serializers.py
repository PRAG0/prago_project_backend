from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from account import models

## tag 기능  추가 필요함
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccounts
        fields = ('user_id', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ 유저를 만들고 유저 리턴"""
        user = models.UserAccounts(
            user_id=validated_data['user_id'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
    user_id = serializers.CharField(label=_("user_id"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        password = attrs.get('password')

        if user_id and password:
            user = authenticate(request=self.context.get('request'),
                                username=user_id, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "user_id" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
