from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    content=models.CharField(max_length=300)
    image=models.ImageField(upload_to='product')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __srt__(self):
        return self.title