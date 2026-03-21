from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)           # 標題
    content = models.TextField(blank=True)             # 內容
    photo = models.URLField(blank=True)                # 照片URL
    location = models.CharField(max_length=100)        # 地點
    created_at = models.DateTimeField(auto_now_add=True) # 建立時間

