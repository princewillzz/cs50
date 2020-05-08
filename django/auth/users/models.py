from django.db import models



user = models.ForeignKey('auth.User', on_delete=models.CASCADE)