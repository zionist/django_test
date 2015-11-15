from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_test.models.models import Person


class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)
