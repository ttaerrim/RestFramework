from rest.models import Post
from rest.serializers import PostSerializer
from rest_framework import viewsets
# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")