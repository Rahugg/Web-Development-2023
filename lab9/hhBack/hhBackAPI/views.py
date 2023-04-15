from django.http.response import JsonResponse
from .models import *


# Create your views here.
def all_companies(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)


def company(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except Company.DoesNotExist as error:
        return JsonResponse({'message: {error}'})
    return JsonResponse(c.to_json())


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy(request, vacancy_id):
    try:
        v = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as error:
        return JsonResponse({'message: {error}'})
    return JsonResponse(v.to_json())


def vacancies_by_company(request, company_id):
    vacancies_json = [v.to_json() for v in Vacancy.objects.all() if v.company and v.company.id == company_id]
    return JsonResponse(vacancies_json, safe=False)


def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    return JsonResponse([v.to_json() for v in vacancies], safe=False)


def name_vacancy(request):
    try:
        name_vacan = "Python"
        "Jun Python Dev"
        "PyTHon"
        vacancies = Vacancy.objects.filter(name__icontains=name_vacan).values()
    except Vacancy.DoesNotExist as error:
        return JsonResponse({'message: {error}'})

    return JsonResponse({'vacancies': list(vacancies)}, safe=False)
