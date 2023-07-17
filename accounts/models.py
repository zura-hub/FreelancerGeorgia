from django.db import models

class Vacancy(models.Model):
    title = models.CharField('Jobs TiTle', max_length=50)
    description = models.TextField('Job Description')
    currency = models.CharField('Specify the Currency', max_length=10)
    budget = models.CharField('Budget', max_length=10)
    data = models.DateTimeField('Publishing Data')

    def __str__(self):
        return self.title