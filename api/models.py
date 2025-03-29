from django.contrib.auth.models import User
from django.db import models

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField()
    ip = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    name_city = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        user_display = self.user.username if self.user else 'Anonymous'
        return f"[{self.timestamp:%Y-%m-%d %H:%M:%S}] {self.method} request to {self.endpoint} by {user_display}"
