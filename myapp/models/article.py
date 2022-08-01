from django.db import models
from tinymce.models import HTMLField
from myapp.models import *
from django.urls import reverse
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(
    	null=True, upload_to='article_images'
    )
    body = HTMLField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    meta_name = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(
    	max_length=250, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cr_date']
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug title
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)