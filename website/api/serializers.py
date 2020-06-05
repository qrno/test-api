from rest_framework import serializers
from api.models import Student, Dict, Word

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'war_name', 'number']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'gender', 'word', 'translation']

class DictSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)
    class Meta:
        model = Dict
        fields = ['id', 'name', 'description', 'words']
