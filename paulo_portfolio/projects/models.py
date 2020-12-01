from django.db import models

# Create your models here.
# create a table


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return self.title, self.technology

    # def description(self):
    #     return self.description[:50] + "..." # says 0-50 characters + concatenation ...