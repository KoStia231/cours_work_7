from django.contrib import admin

from users.models import User


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'email', 'phone_number',
    )
    search_fields = ('id', 'first_name', 'email', 'phone_number',)
    list_filter = ('id', 'first_name', 'email', 'phone_number',)
