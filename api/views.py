from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from .serializer import AboutSerializer, AlbumSerializer, AlbumDetailSerializer, StorySerializer, StoryDetailSerializer
from .models import AboutModel, AlbumModel, StoryModel
import datetime

class AboutAPIView(generics.ListAPIView):
    serializer_class = AboutSerializer
    def get_queryset(self):
        qs = AboutModel.objects.all()
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class AlbumAPIView(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        qs = AlbumModel.objects.filter(published=True)
        return qs
    
    def get(self, request, *args, **kwargs):
        #try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        #except:
        #    return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class AlbumDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AlbumDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')
    
    def get_queryset(self):
        id = self.get_object()
        qs = AlbumModel.objects.filter(published=True).filter(id=id)
        return qs

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class StoryAPIView(generics.ListAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
        qs = StoryModel.objects.filter(published=True)
        return qs
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class StoryDetailAPIView(generics.RetrieveAPIView):
    serializer_class = StoryDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')
    
    def get_queryset(self):
        id = self.get_object()
        qs = StoryModel.objects.filter(published=True).filter(id=id)
        return qs

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')

'''
class StudentDocxViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    def retrieve(self, request, *args, **kwargs):
        template = webodt.ODFTemplate('test.odt')
        queryset = Pupils.objects.get(id=kwargs['pk'])
        serializer = StudentSerializer(queryset)
        context = dict(serializer.data)
        document = template.render(Context(context))
        doc = converter().convert(document, format='doc')
        p = u'docs/cards/%s/%s_%s.doc' % (datetime.now().date(), context[u'surname'], context[u'name'])
        path = default_storage.save(p, doc)
        return Response(u'/media/' + path)


class VideoView(generics.ListAPIView):

    def get(self, request, format=None):
        serializer = cdx_compositesSerializer(snippets, many=True)
        if format == 'raw':
            video_file = open('/home/krishna/Downloads/test1.mp4', 'rb')
            response = HttpResponse(FileWrapper(video_file), content_type=
            'application/video', base_name='none')
            response['Content-Disposition'] = 'attachment; filename="%s"' % 'test1.mp4'
            return response

        else:
            return Response(serializer.data)
'''