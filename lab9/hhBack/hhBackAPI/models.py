from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True)
    city = models.CharField(max_length=10)
    address = models.TextField(max_length=15, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    zipNumber = models.CharField(max_length=20, null=True)

    def to_json(self):
        # company_json = self.company.to_json()
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'zipNumber': self.zipNumber,
            'company': self.company.to_json(),
        }
#
