from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'Название блога:{self.title}\nОписание: {self.description}\nДата создания: {self.date}'
