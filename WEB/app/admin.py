from django.contrib import admin

from app.models import SensorData

admin.site.site_header = "智能加湿管理系统"
admin.site.site_title = "智能加湿管理系统"
admin.site.index_title = "智能加湿管理系统"

admin.site.register(SensorData)
