from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from app.models import SensorData
from app.serializers import SensorDataSerializer


class SensorDataViewSet(ModelViewSet):
    queryset = SensorData.objects.all().order_by("-id")
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]


def chart_view(request):
    # 从数据库中获取最新的20条模型数据
    sensor_data = SensorData.objects.order_by('-id')[:20][::-1]

    # 将模型数据传递给模板
    context = {
        'sensor_data': {
            'id': [data.id for data in sensor_data],
            'temperature': [data.temperature for data in sensor_data],
            'humidity': [data.humidity for data in sensor_data],
            'water_level': [data.water_level for data in sensor_data],
            'wifi_status': [1 if data.wifi_status else 0 for data in sensor_data],
            'spray_status': [data.spray_status for data in sensor_data],
        }
    }
    # 呈现包含图表的模板
    return render(request, "chart.html", context)
