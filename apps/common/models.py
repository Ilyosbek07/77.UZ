from django.db import models

class ApplicateUser(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('moderation', 'Moderation'),
        ('cancelled', 'Cancelled'),
    )

    full_name = models.CharField(max_length=600)
    project_name = models.CharField(max_length=600)
    category = models.ForeignKey()
    phone_number = models.CharField(max_length=600)
    address = models.TextField()
    status = models.CharField(choices=STATUS, max_length=300)

    def __str__(self):
        return self.full_name