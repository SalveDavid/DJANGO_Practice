from django.contrib import admin
from .models import Employee


class EmplolyeeAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'salary']


admin.site.register(Employee, EmplolyeeAdmin)
