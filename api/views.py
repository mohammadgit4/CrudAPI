from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSLR
from .models import Student
from rest_framework import status

class StudentView(APIView):
        def get(self, request, pk=None):
            if pk is not None:
                slr = StudentSLR(Student.objects.get(id=pk))
                return Response({'Message':'Show Specific Data...', 'data':slr.data}, status=status.HTTP_200_OK)
            slr = StudentSLR(Student.objects.all(), many=True)
            return Response({'Message':'Show All Data', 'data':slr.data}, status=status.HTTP_200_OK)
    
        def post(self, request):
            slr = StudentSLR(data=request.data)
            slr.is_valid(raise_exception=True)
            slr.save()
            return Response({'Message':'Data Created !', 'data':slr.data}, status=status.HTTP_201_CREATED)

        def put(self, request ,pk=None):
            slr = StudentSLR(Student.objects.get(id=pk), data=request.data)
            slr.is_valid(raise_exception=True)
            slr.save()
            return Response({'Message':'Complate Data Updated', 'Data':slr.data}, status=status.HTTP_201_CREATED)

        def patch(self, request, pk=None):
            slr = StudentSLR(Student.objects.get(id=pk), data=request.data, partial=True)
            slr.is_valid(raise_exception=True)
            slr.save()
            return Response({'Message':'Specific Data Updated', 'Data':slr.data}, status=status.HTTP_201_CREATED)

        def delete(self, request, pk=None):
            Student.objects.get(id=pk).delete()
            return Response({'Message':'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)