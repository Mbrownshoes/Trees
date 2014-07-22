# from django.db import models
# from django.utils import timezone
# from simple_history.models import HistoricalRecords

# class User(models.Model):
#     email = models.EmailField(primary_key=True)
#     last_login = models.DateTimeField(default=timezone.now)
#     REQUIRED_FIELDS = ()
#     USERNAME_FIELD = 'email'
#     history = HistoricalRecords()

#     def is_authenticated(self):
#         return True