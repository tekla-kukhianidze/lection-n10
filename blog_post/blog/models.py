from django.db import models

class Author(models.Model):
    first_name = models.CharField(verbose_name="სახელი", max_length=100)
    last_name = models.CharField(verbose_name="გვარი", max_length=100)
    email = models.EmailField(verbose_name="მეილი")

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.first_name+" "+self.last_name


class BlogPost(models.Model):
    authors = models.ManyToManyField(to='blog.Author', verbose_name="ავტორები", related_name="blog_posts")
    title = models.CharField(verbose_name="სათაური", max_length=255)
    text = models.TextField(verbose_name="ტექსტი")
    active=models.BooleanField(default=True, verbose_name='აქტიურია')
    create_date=models.DateTimeField(verbose_name='შექმნის თარიღი', auto_now_add=True, null=True)
    update_date=models.DateTimeField(verbose_name='განახლების თარიღი', auto_now=True,null=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)



    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering=['title']

    def __str__(self):
        return self.title


class BannerImage(models.Model):
    blog_post = models.OneToOneField(
        to='blog.BlogPost',
        related_name='banner_image',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='banner_image/', null=True, blank=True)

    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"

    def __str__(self):
        return f'{self.blog_post.title} - {self.id} image'


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(to='blog.BlogPost', related_name='images', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog_image/')


    class Meta:
        verbose_name = "Blog Post Image"
        verbose_name_plural = "Blog Post Images"

    def __str__(self):
        return f'{self.blog_post.title} - {self.id} image'