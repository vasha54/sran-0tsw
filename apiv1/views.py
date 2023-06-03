from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from touristresource.models import ResourceTourist
from apiv1.serializers import ResourceTouristSerializer
from rest_framework import permissions


class ResourceTouristDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = []

    def get_object(self, pk):
        try:
            return ResourceTourist.objects.get(pk=pk)
        except ResourceTourist.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        rt_instance = self.get_object(pk)
        if not rt_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ResourceTouristSerializer(rt_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # # 4. Update
    # def put(self, request, pk, *args, **kwargs):
    #     '''
    #     Updates the todo item with given todo_id if exists
    #     '''
    #     todo_instance = self.get_object(todo_id, request.user.id)
    #     if not todo_instance:
    #         return Response(
    #             {"res": "Object with todo id does not exists"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # 5. Delete
    # def delete(self, request, todo_id, *args, **kwargs):
    #     '''
    #     Deletes the todo item with given todo_id if exists
    #     '''
    #     todo_instance = self.get_object(todo_id, request.user.id)
    #     if not todo_instance:
    #         return Response(
    #             {"res": "Object with todo id does not exists"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     todo_instance.delete()
    #     return Response(
    #         {"res": "Object deleted!"},
    #         status=status.HTTP_200_OK
    #     )