from django.db import models

from shop.categories.models import Category


class Product(models.Model):
    use_in_migration = True
    product_id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.TextField()
    image_url = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "s_products"

    def __str__(self):
        return f'{self.pk} {self.name} {self.price} {self.image_url}'
