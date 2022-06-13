from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag, Comment, Category
from .forms import CreateCommentForm
from contact.models import Subscribe
from django.core.paginator import Paginator


def home_view(request):
    objects = Post.objects.order_by('-id')
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    comments = Comment.objects.all()
    last_3_posts = Post.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    q = request.GET.get('search')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    sbb = request.POST.get('sbb')

    if q:
        objects = objects.filter(title__icontains=q)
    if cat:
        objects = objects.filter(category__title__exact=cat)
    if tag:
        objects = objects.filter(tags__tag__exact=tag)

    if request.method == 'POST':
        Subscribe.objects.create(email=sbb)
    dates = list()
    [('yanvar', 2020), ('aprel', 2021)]
    for i in objects:
        month = i.created_at.strftime("%B")
        year = i.created_at.strftime("%Y")
        mydate = i.created_at.strftime("%B %Y")
        if mydate not in dates:
            dates.append((f'{month}', year))
        print(dates)
    month = request.GET.get('month')
    year = request.GET.get('year')

    if month and year:
        objects = objects.filter(created_at__year=year)
    context = {
        'objects': objects,
        'page_obj': page_obj,
        'comments': comments,
        'last_3_posts': last_3_posts,
        'tags': tags,
        'categories': categories,
        "dates": dates
    }
    return render(request, 'posts/index.html', context)


def single_view(request, slug):
    objects = get_object_or_404(Post, slug=slug)
    posts = Post.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    last_3_post = Post.objects.order_by('-id')[:3]
    comments = Comment.objects.filter(posts__slug__exact=slug).order_by('-id')
    form = CreateCommentForm(request.POST or None, request.FILES or None, instance=objects)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.objects = objects
        comment.author = request.user
        comment.save()
        return redirect(f'/single/{objects.slug}#comments')

    email = request.POST.get('subs')
    if email:
        Subscribe.objects.create(email)

    ctx = {
        'tags': tags,
        'form': form,
        'posts': posts,
        'objects': objects,
        'comments': comments,
        'categories': categories,
        'last_3_posts': last_3_post,

    }
    return render(request, 'posts/single.html', ctx)


def about_view(request):
    return render(request, 'posts/about.html')


def fashion_view(request):
    post = Post.objects.filter(type=0).order_by('-id')
    ctx = {
        'objects': post
    }
    return render(request, 'posts/fashion.html', ctx)


def travel_view(request):
    post = Post.objects.filter(type=1).order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    last_3_post = Post.objects.order_by('-id')[:3]
    email = request.POST.get('subs')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if email:
        Subscribe.objects.create(email=email)
    ctx = {
        'objects': page_obj,
        'tags': tags,
        'categories': categories,
        'last_3_posts': last_3_post
    }
    return render(request, 'posts/travel.html', ctx)
