from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news')  # Виправлено related_name
    publication_date = models.DateTimeField('Дата публікації')
    content = models.TextField()

    def __str__(self):
        return self.title  # Можна повертати заголовок новини
