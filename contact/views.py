from django.shortcuts import render, redirect
from .forms import CreateGetInTouchForm
from .models import GetInTouch, Subscribe


def contact_view(request):
    form = CreateGetInTouchForm(request.POST or None)
    obj = GetInTouch.objects.order_by('-id')[:2]
    if form.is_valid():
        comment = form.save(commit=False)
        comment.obj = obj
        comment.save()
        return redirect('.')
    ctx = {
        'form': form,
        'objects': obj
    }
    return render(request, 'contact/contact.html', ctx)

