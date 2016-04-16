from .models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	wods = serializers.StringRelatedField(many=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'wods')