from django.contrib import admin

# Register your models here.
from .models import Blog, Comments, Tags, Categories


admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Categories)