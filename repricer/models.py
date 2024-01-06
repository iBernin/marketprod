from django.db import models


class MonitorIds(models.Model):
    class Meta:
        verbose_name_plural = "Мониторинг артикулов"
    nmId = models.IntegerField(unique=True)
    price = models.IntegerField()
    # article = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return str(self.nmId)

