from rest_framework import serializers
from .models import Query
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields='__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token