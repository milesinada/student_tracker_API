from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Session
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id',  'name', 'url', 'cohort', 'email')

class SessionSerializer(WritableNestedModelSerializer,serializers.HyperlinkedModelSerializer):
#     student = serializers.SlugRelatedField(
#     many=True,
#     read_only=True,
#     slug_field="name"
#   )
    student_name = serializers.CharField(source='student.name')
    student = StudentSerializer()
    class Meta:
        model = Session
        fields = ('id', 'url', 'issue', 'description', 'duration', 'unit', 'status', 'student', 'student_name')