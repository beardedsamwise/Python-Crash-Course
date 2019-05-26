from django.db import models

class Pizza(models.Model):
    """Different pizzas available to customers."""
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Toppings that go on the Pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)
    topping = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        """Return a string representation of the model."""
        return str(self.topping)