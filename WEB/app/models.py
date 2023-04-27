from django.db import models


class SensorData(models.Model):
    class Meta:
        verbose_name = "数据"
        verbose_name_plural = "数据"

    temperature = models.FloatField(verbose_name="温度")
    humidity = models.FloatField(verbose_name="湿度")
    water_level = models.FloatField(verbose_name="水位")
    wifi_status = models.BooleanField(verbose_name="WiFi状态")
    spray_status = models.IntegerField(verbose_name="喷雾状态")

    def __str__(self):
        return f"温度: {self.temperature:.1f},湿度: {self.humidity:.1f},水位: {self.water_level:.1f}"
