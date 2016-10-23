from django.contrib import admin
from models import Tenant, Contract, Local, Payment, Property

myModels = [Tenant, Contract, Local, Payment, Property]
admin.site.register(myModels)
