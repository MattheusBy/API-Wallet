from django.contrib import admin

from wallet.models import UserBalance, Transaction

# Register your models here.
admin.site.register(UserBalance)
admin.site.register(Transaction)
