from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    meta_name = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=250, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name