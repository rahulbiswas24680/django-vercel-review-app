from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Variant)
admin.site.register(Model)
admin.site.register(Question)
admin.site.register(QuestionCluster)
admin.site.register(PlatformAndUserConnector)
admin.site.register(ProductUser)
admin.site.register(ReviewBuyer)

