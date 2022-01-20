from django.db import models
SERVICE_CHOICES = (
    ('web design','WEB DESIGN'),
    ('branding', 'BRANDING'),
    ('web aps','WEB APS'),
    ('graphic','GRAPHIC'),
    ('support','SUPPORT'),
)

class Quotation(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    service= models.CharField(max_length=20, choices=SERVICE_CHOICES, default='web design')
    message= models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)



    def _str_(self):
        return self.name