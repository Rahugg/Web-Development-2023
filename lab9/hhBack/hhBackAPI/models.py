from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField
    city = models.CharField(max_length=20)
    address = models.TextField

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    salary = models.FloatField(null=True, blank=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'description': self.description,
            'company_name': self.company.name,
            'company_description': self.company.description,
            'company_city': self.company.city,
            'company_address': self.company.address,
        }
