from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'autor', 'title', 'place',
        'duration', 'time_action', 'action', 'prize',
        'is_pleasant', 'last_performed', 'execution_interval_day',
        'related', 'is_public',
    )
    search_fields = ('id', 'autor', 'title', 'is_public',)
    list_filter = ('id', 'autor', 'title', 'is_public',)
