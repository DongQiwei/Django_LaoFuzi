from django.shortcuts import render
from django.views.generic.base import View
from .models import Art, Chapter,Tag
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class BookDetail(View):
    # 书籍详情页
    def get(self, request, a_id):
        art = Art.objects.get(a_id=a_id)
        art_capters = Chapter.objects.filter(a_id=a_id)
        return render(request, 'detail_handler.html', {'art': art, 'art_capters': art_capters})

    def post(self, request):
        pass


class BookSearch(View):
    def get(self, request):
        name = request.GET.get('key', '')
        data = Art.objects.filter(a_title__contains=name).all()
        count = data.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(data, 3, request=request)

        arts = p.page(page)
        return render(request, 'search_handler.html', {"name": name, "data": arts, 'count': count})

    def post(self, request):
        pass
