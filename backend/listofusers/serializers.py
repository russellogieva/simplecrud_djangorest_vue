from rest_framework import serializers

from .models import Users, Role


class UsersSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field="rolename", style={'base_template': 'input.html'})

    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'created_at', 'role')


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'rolename')
