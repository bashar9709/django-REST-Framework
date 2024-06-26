from .models import BookStoreModel
from .serializers import BookStotrSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Method 1 : APIView

# class BookListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = BookStoreModel.objects.all()
#         serializer = BookStotrSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookStotrSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookListUpdateDelete(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return BookStoreModel.objects.get(pk=pk)
#         except BookStoreModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStotrSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStotrSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Method 2 : concreteapi view

# from rest_framework import generics


# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStotrSerializer


# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStotrSerializer



# Method 3 : Shortcut / Model View Set

from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStotrSerializer