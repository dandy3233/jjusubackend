from rest_framework import serializers
from .models import StaffMember, ImageCollage  # Import ImageCollage model

class StaffMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Ensures the image URL is included

    class Meta:
        model = StaffMember
        fields = '__all__'  # You can specify the fields here, e.g., ['id', 'name', 'role']

class ImageCollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollage
        fields = ['id', 'image', 'title', 'instagram', 'tiktok']  # Fields to include in the API response
