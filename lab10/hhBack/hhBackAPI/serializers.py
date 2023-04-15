from abc import ABC

from rest_framework import serializers

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'city', 'address']


# class VacancySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vacancy
#         fields = ['id', 'name', 'description', 'salary', 'company']

class VacancySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    description = serializers.CharField()
    salary = serializers.FloatField(default=0)
    company = CompanySerializer()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        company_data = validated_data.pop('company')
        company_serializer = CompanySerializer(data=company_data)
        company_serializer.is_valid(raise_exception=True)
        company = company_serializer.save()
        vacancy_data = Vacancy.objects.create(**validated_data)
        return vacancy_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        company_data = validated_data.pop('company')
        company_serializer = CompanySerializer(instance.company, data=company_data)
        company_serializer.is_valid(raise_exception=True)
        company = company_serializer.save()
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
