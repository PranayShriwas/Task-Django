from django.db import models

class UserInput(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_quantity = models.IntegerField()
    lot_size = models.IntegerField()
    interval = models.IntegerField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    trade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.start_time