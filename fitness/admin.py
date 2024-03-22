from django.contrib import admin
from django.contrib import admin
from .models import course,Trainer,blog,category,profile,course_buy,Itemcart,Booking
from django.utils.html import format_html  # Import format_html for rendering HTML

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_name','price')

# class Course_buyAdmin(admin.ModelAdmin):
#       list_filter = [
#          "",
#          "paid",
#          'completed',
#          'country']
#       list_display=('id','puja_date','puja_name','name','country','address','contact','payment','paid')


class ItemcartAdmin(admin.ModelAdmin):
    list_display=('id','total_price','name','country','contact','location','is_completed','is_purchased')


class TrainerAdmin(admin.ModelAdmin):
     list_filter=[
         'expertise',
         'country',
     ]
     list_display=('id','trainer_name','expertise','country','location','contact')
     
     def display_trainer_pic(self, obj):
         if obj.trainer_pic:
            return format_html('<img src="{}" width="50" height="50" />', obj.trainer_pic.url)
         else:
             return ''
        #  display_trainer_pic.short_description = 'Trainer Picture'
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','Date','username','category')
    list_filter=[
        'Date',
        'username',
    ]


admin.site.register(Trainer,TrainerAdmin)
admin.site.register(course,CourseAdmin)
admin.site.register(blog,BlogAdmin)
admin.site.register(category)
admin.site.register(Booking)
admin.site.register(profile)
# admin.site.register(email_subscription)
admin.site.register(course_buy)
admin.site.register(Itemcart,ItemcartAdmin)

admin.site.site_header = 'Fitness Dashboard'
admin.site.index_title = 'Fitness site adminstration'

