from django.contrib import admin
from .models import Post, Category, SearchList


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SearchList)