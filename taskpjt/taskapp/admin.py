from django.contrib import admin

# Register your models here.
from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name', 'slug']
    prepopulated_fields = {'slug': ('branch_name',)}


admin.site.register(Branch, BranchAdmin)