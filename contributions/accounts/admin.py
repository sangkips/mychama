from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'mobile']
	list_display = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'mobile' ]
	class Meta:
		model = User


admin.site.register(User, UserAdmin)
