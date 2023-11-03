from django.contrib import admin
from.models import User, App, AppTask

# Register your models here.

@admin.register(User)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name','username','password','role']

@admin.register(App)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','app_pic','app_name','app_link','catagory','sub_catagory','points']

@admin.register(AppTask)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','uid','aid','screenshot']