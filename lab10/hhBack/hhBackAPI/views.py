from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .models import *
from .serializers import *


@api_view(['GET'])
def all_companies(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


# def all_companies(request):
#     companies = Company.objects.all()
#     companies_json = [c.to_json() for c in companies]
#     return JsonResponse(companies_json, safe=False)

@api_view(['GET'])
def company(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except Company.DoesNotExist as error:
        return JsonResponse({'message: {error}'})
    if request.method == 'GET':
        serializer = CompanySerializer(c)
        return Response(serializer.data)


# def company(request, company_id):
#     try:
#         c = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as error:
#         return JsonResponse({'message: {error}'})
#     return JsonResponse(c.to_json())

@api_view(['GET'])
def all_vacancies(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


# def all_vacancies(request):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [v.to_json() for v in vacancies]
#     return JsonResponse(vacancies_json, safe=False)

@api_view(['GET'])
def vacancy(request, vacancy_id):
    if request.method == "GET":
        try:
            v = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as error:
            return JsonResponse({'message: {error}'})
        if request.method == 'GET':
            serializer = VacancySerializer(v)
            return Response(serializer.data)


# def vacancy(request, vacancy_id):
#     try:
#         v = Vacancy.objects.get(id=vacancy_id)
#     except Vacancy.DoesNotExist as error:
#         return JsonResponse({'message: {error}'})
#     return JsonResponse(v.to_json())


@api_view(['GET'])
def vacancies_by_company(request, company_id):
    if request.method == "GET":
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


# def vacancies_by_company(request, company_id):
#     vacancies_json = [v.to_json() for v in Vacancy.objects.all() if v.company and v.company.id == company_id]
#     return JsonResponse(vacancies_json, safe=False)

@api_view(['GET'])
def top_ten_vacancies(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        return Response(VacancySerializer(vacancies, many=True).data)
