from django.db import models

class Cuisine(models.Model):
    type_name = models.CharField(max_length=255, db_index=True)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'cuisine.cuisine'
        ordering = ['-datetime_create']

    def __str__(self):
        return self.type_name


class Dishes(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField(blank=True, null=True, default='')
    image = models.ImageField(upload_to='dishes')

    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'cuisine.dishes'
        ordering = ['-datetime_update']

    def __str__(self):
        return '%s: %s' % (self.cuisine, self.name)
