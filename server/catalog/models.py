import uuid

from django.db import models
from django.contrib.postgres.indexes import GinIndex


class Wine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    variety = models.CharField(max_length=255)
    winery = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to="wines", blank=True)

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        indexes = [
            GinIndex(
                name="variety_gin_idx",
                fields=["variety"],
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                name="winery_gin_idx",
                fields=["winery"],
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                name="description_gin_idx",
                fields=["description"],
                opclasses=["gin_trgm_ops"],
            ),
        ]
