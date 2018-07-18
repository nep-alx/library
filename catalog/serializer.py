from rest_framework import serializers
from .models import Book, File, Loan, Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'id')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('book', 'file')


class LoanSerializer(serializers.ModelSerializer):
    loanStart = serializers.DateField(format='%Y-%m-%d', required=True)

    class Meta:
        model = Loan
        fields = ('book', 'loanStart', 'loanDuration', 'student')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'groups')