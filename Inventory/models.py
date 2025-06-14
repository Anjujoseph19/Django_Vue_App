from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Only reduce stock if this is a new order (not update)
        if not self.pk:
            if self.product.stock < self.quantity:
                raise ValueError("Insufficient stock.")
            self.product.stock -= self.quantity
            self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id}"
