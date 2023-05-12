from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import SensorData
from app.serializers import SensorDataSerializer


class SensorDataViewSet(ModelViewSet):
    queryset = SensorData.objects.all().order_by("-id")
    serializer_class = SensorDataSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        request_data = {k: v for k, v in request.data.items()}
        latest_spray_status = SensorData.objects.latest("id").spray_status
        request_data["spray_status"] = latest_spray_status
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=["post"], detail=False)
    def change_spray_status(self, request):
        spray_status = request.data.get("spray_status")
        if spray_status is None:
            return Response({"error": "spray_status parameter is missing"}, status=400)
        latest_data = SensorData.objects.latest("id")
        latest_data.spray_status = spray_status
        latest_data.save()
        serializer = SensorDataSerializer(latest_data)
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def get_latest_spray_status(self, request):
        latest_data = SensorData.objects.latest("id")
        spray_status = latest_data.spray_status
        return Response({"sw": spray_status})


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
