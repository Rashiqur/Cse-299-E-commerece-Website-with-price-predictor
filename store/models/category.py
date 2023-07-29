from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_cattegories():
        return Category.objects.all()

    def __str__(self):
        return self.name