from django.contrib import admin
from .models import User,Query
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id',)


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display=('id','name','query')