from django.shortcuts import render,get_object_or_404
from ..models import Voca
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page= request.GET.get('page','1')#페이지
    voca_list=Voca.objects.order_by('english_vo')
    paginator=Paginator(voca_list, 10)#10개씩 1페이지
    page_obj=paginator.get_page(page)
    context={'voca_list':page_obj}
    return render(request,'app/voca_list.html',context)

def detail(request, voca_id):
    voca=get_object_or_404(Voca,pk=voca_id)
    context={'voca':voca}
    return render(request, 'app/voca_detail.html',context)