from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


# Create your models here.
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')

# @deconstructible
# def MaxFileSizeInMBValidator:
#     def __init__(self, max_size):
#         self.max_size = max_size
#
#     def __call__(self, value):
#         filesize = value.file.size
#         if filesize > self.max_size * 1024 * 1024:
#             raise ValidationError('Max file size is 5.00 MB')


class Profile(models.Model):
    IMAGE_MAX_SIZE = 5

    first_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        )
    )
    budget = models.IntegerField(
        default=0,
        validators=(
            MinValueValidator(0),
        ),
    )
    image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        # validators=(
        #     MaxFileSizeInMBValidator(IMAGE_MAX_SIZE),
        # )
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=50
    )
    image_url = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()


