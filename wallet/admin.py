from django.contrib import admin

from wallet.models import UserBalance, Transaction

admin.site.register(UserBalance)
admin.site.register(Transaction)
