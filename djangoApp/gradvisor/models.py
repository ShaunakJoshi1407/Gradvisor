from django.db import models

# Create your models here.
class Applicant(models.Model):
    username = models.CharField(max_length=100, default=False)
    passwordVal = models.CharField(max_length=100, default=False)
    greQuantitativeScore = models.IntegerField()
    greVerbalScore = models.IntegerField()
    toeflScore = models.IntegerField()
    underGraduateUniversity = models.CharField(max_length=200)
    GPA = models.FloatField()
    workExperience = models.IntegerField()
    greAWAScore = models.FloatField()

    class Meta:
        app_label = 'gradvisor'

    def __str__(self):
        return self.university_name