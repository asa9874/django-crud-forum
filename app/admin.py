from django.contrib import admin

from .models import Voca
# Register your models here.
class VocaAdmin(admin.ModelAdmin):
    search_fields=['english_vo']

admin.site.register(Voca,VocaAdmin)