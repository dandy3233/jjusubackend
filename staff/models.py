from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator

def validate_image_format(image):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
    if not image.name.split('.')[-1].lower() in valid_extensions:
        raise ValidationError("Only jpg, jpeg, png, and gif images are allowed.")

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='staff_images/', validators=[validate_image_format])  # Validation added here
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class ImageCollage(models.Model):
    image = models.ImageField(
        upload_to='image_collage/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)  # Add this
    tiktok = models.URLField(blank=True, null=True)     # Add this

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"




