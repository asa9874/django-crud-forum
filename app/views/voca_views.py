from django.shortcuts import render,get_object_or_404, redirect
from ..models import Voca
from ..forms import VocaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone




@login_required(login_url='common:login')
def voca_create(request):
    if request.method == 'POST':
        form = VocaForm(request.POST)
        if form.is_valid():
            voca = form.save(commit=False)
            voca.author = request.user  # author 속성에 로그인 계정 저장
            voca.save()
            return redirect('index')
    else:
        form = VocaForm()
    context = {'form': form}
    return render(request, 'app/voca_form.html', context)



@login_required(login_url='common:login')
def voca_modify(request, voca_id):
    voca = get_object_or_404(Voca, pk=voca_id)
    if request.user != voca.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('detail', voca_id=voca.id)
    if request.method == "POST":
        form = VocaForm(request.POST, instance=voca)
        if form.is_valid():
            voca = form.save(commit=False)
            voca.modify_date = timezone.now()  # 수정일시 저장
            voca.save()
            return redirect('detail', voca_id=voca.id)
    else:
        form = VocaForm(instance=voca)
    context = {'form': form}
    return render(request, 'app/voca_form.html', context)



@login_required(login_url='common:login')
def voca_delete(request, voca_id):
    voca = get_object_or_404(Voca, pk=voca_id)
    if request.user != voca.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('detail', voca_id=voca.id)
    voca.delete()
    return redirect('index')


@login_required(login_url='common:login')
def voca_vote(request, voca_id):
    voca = get_object_or_404(Voca, pk=voca_id)
    if request.user == voca.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        voca.voter.add(request.user)
    return redirect('detail', voca_id=voca.id)