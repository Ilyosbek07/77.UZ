from django.db import models
# from apps.products.models import Category


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class ApplicationUser(BaseModel):
#     STATUS = (
#         ('active', 'Active'),
#         ('moderation', 'Moderation'),
#         ('cancelled', 'Cancelled'),
#     )
#
#     full_name = models.CharField(max_length=600)
#     project_name = models.CharField(max_length=600)
#     category = models.ForeignKey(
#         Category,
#         related_name='product_category',
#         on_delete=models.CASCADE
#     )
#     phone_number = models.CharField(max_length=600)
#     address = models.TextField()
#     status = models.CharField(choices=STATUS, max_length=300)
#
#     def __str__(self):
#         return self.full_name
