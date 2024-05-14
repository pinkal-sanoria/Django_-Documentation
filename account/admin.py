from django.contrib import admin
from .models import CustomUser ,Author,Course

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Course)

# Register your models here.
