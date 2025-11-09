from django.db import models


class BlogPost(models.Model):
    title = models.CharField(verbose_name="სათაური", max_length=255)
    text = models.TextField(verbose_name="ტექსტი")
    active=models.BooleanField(default=True, verbose_name='აქტიურია')
    create_date=models.DateTimeField(verbose_name='შექმნის თარიღი', auto_now_add=True, null=True)
    update_date=models.DateTimeField(verbose_name='განახლების თარიღი', auto_now=True,null=True)
    picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)


    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering=['title']

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
