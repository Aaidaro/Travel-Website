from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_main_view(request, cat_name=None):
    posts = Post.get_published_posts()
    if cat_name:
        posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def single_blog_view(request, pid):
    published_posts = Post.get_published_posts()
    post = get_object_or_404(published_posts, pk=pid)
    next_post = post.get_next_id(pid)
    previous_post = post.get_previous_id(pid)
    post.counted_view += 1
    post.save()
    context = {'post':post, 'next_post':next_post, 'previous_post':previous_post}
    return render(request, 'blog/blog-single.html', context)

def test_view(request):
    return render(request, 'test.html')
