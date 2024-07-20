from django.db import models

# Create your models here.
class NippoModel(models.Model):
    # フィールド名 = models.フィールド種類(引数**)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    # auto_now_addは、登録した日付を自動的に格納する
    timestamp = models.DateTimeField(auto_now_add=True)