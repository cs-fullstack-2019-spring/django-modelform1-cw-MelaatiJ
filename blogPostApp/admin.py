from django.contrib import admin

# Register your models here.


# logging it into my admin
from .models import BlogPost
admin.site.register(BlogPost)