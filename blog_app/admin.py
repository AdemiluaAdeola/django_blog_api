from django.contrib import admin
from blog_app.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Blog)