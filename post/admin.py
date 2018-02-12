from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title','content']
    list_editable = ['title']


    class Meta:
        model=Post



# Register your models here.
admin.site.register(Post,PostAdmin)
