from rest_framework import serializers
from fixture.models import Fixture

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = '__all__'