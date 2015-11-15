from django.db import models
from django.db.models import QuerySet


class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)

    def delete_real(self):
        super(CustomQuerySet, self).delete()


class CustomManager(models.Manager):

    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)
