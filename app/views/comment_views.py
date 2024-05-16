from django.shortcuts import render,get_object_or_404, redirect, resolve_url
from ..models import Voca,Comment
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required




@login_required(login_url='common:login')
def answer_create(request, voca_id):
    voca = get_object_or_404(Voca, pk=voca_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.voca = voca
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('detail', voca_id=voca.id), answer.id))
    else:
        form = CommentForm()
    context = {'voca': voca, 'form': form}
    return render(request, 'app/voca_detail.html', context)