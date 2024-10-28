from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Corporation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    corporation_name = models.CharField(max_length=100, blank=False, null=False)
    sector = models.CharField(max_length=255, blank=True, default="")
    founding_date = models.DateField(default=timezone.now, editable=True)
    address = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    url = models.URLField(max_length=255, blank=True, default="")
    linkedin = models.URLField(max_length=255, blank=True, default="")

    def get_absolute_url(self):
        """
        Returns the absolute URL for the detail view of this Corporation instance.

        This method uses Django's reverse function to generate a URL to the 
        'corporation:detail' view, which displays details of a specific Corporation 
        instance. The 'pk' of the instance is passed as a keyword argument to 
        identify which Corporation's detail view should be rendered.

        Returns:
            str: The URL path to the detail page of this Corporation instance.
        """
        return reverse("corporation:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.corporation_name
