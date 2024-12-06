from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StaffMember, ImageCollage
from .serializers import StaffMemberSerializer, ImageCollageSerializer

class StaffListView(APIView):
    def get(self, request):
        staff = StaffMember.objects.all()
        serializer = StaffMemberSerializer(staff, many=True)

        for staff_member in serializer.data:
            staff_member['image'] = request.build_absolute_uri(staff_member['image'])

        return Response(serializer.data)

class ImageCollageListView(APIView):
    def get(self, request):
        images = ImageCollage.objects.all()
        serializer = ImageCollageSerializer(images, many=True)
        return Response(serializer.data)
