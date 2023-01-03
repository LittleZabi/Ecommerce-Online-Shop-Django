from django.contrib import admin
from .models import Blogs, IpModel
from django_summernote.admin import SummernoteModelAdmin

class BlogsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = '__all__'

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(IpModel)