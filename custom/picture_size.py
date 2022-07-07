"""Picture validator function - used in models"""
from django.core.exceptions import ValidationError


def picture_size(value):
    limit = 1024 * 1024
    if value.size > limit:
        raise ValidationError('Image too large. Size should not exceed 1 MB.')
