from rest_framework import serializers
from account import models


# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'

## tag 기능  추가 필요함
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccounts
        fields = ('id', 'user_id', 'name', 'password')
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
