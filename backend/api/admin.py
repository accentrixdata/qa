from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    pass