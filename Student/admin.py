from django.contrib import admin
from .models import Student,Contact,Address

class StudentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['user__username','user__email']
    
    class Meta:
        model = Student

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, StudentAdmin)
admin.site.register(Address, StudentAdmin)

