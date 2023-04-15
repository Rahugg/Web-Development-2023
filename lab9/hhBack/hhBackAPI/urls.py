from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.all_companies, name='all_companies'),
    path('companies/<int:company_id>/', views.company, name='company'),
    path('companies/<int:company_id>/vacancies/', views.vacancies_by_company, name='vacancies_by_company'),
    path('vacancies/', views.all_vacancies, name='all_vacancies'),
    path('vacancies/<int:vacancy_id>/', views.vacancy, name='vacancy'),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top_ten_vacancies'),
    path('vacancies_python/', views.name_vacancy, name='name_vacancy')
]

# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
