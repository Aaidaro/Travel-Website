from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ["title", "created_date","author", "id", "status", "published_date"]
    list_filter = ["author", "status"]

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)