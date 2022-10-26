from rest_framework import serializers
from .models import Session
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'cohort', 'email')
        
class SessionSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Session 
        fields = ('id', 'issue', 'description', 'duration', 'unit', 'status', 'student')
