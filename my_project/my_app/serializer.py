# from dataclasses import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '_all_'
    #   fields = ("stu_id", "stu_name")