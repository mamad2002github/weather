from django.contrib.auth.models import User
from django.db import models

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField()  # زمان ثبت لاگ
    ip = models.GenericIPAddressField()  # آدرس IP کاربر
    endpoint = models.CharField(max_length=255)  # مسیر درخواست‌شده
    method = models.CharField(max_length=10)  # نوع متد
    name_city = models.CharField(max_length=255, null=True, blank=True)  # نام شهر (اختیاری)

    def __str__(self):
        user_display = self.user.username if self.user else 'Anonymous'
        return f"[{self.timestamp:%Y-%m-%d %H:%M:%S}] {self.method} request to {self.endpoint} by {user_display}"
