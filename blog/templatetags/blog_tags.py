from django import template
from blog.models import Post, Category
register = template.Library()

@register.simple_tag(name='published_posts_num')
def function():
    num_published_posts = Post.get_published_posts().count()
    return num_published_posts

@register.simple_tag(name='published_posts')
def function():
    published_posts = Post.get_published_posts()
    return published_posts

@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."

@register.inclusion_tag('blog/blog-popular-posts.html')
def latest_posts(arg=3):
    latest_posts = Post.get_published_posts().order_by('-published_date')[:arg]
    return {'latest_posts':latest_posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    published_posts = Post.get_published_posts()
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = published_posts.filter(category=cat).count()
    return {'categories':cat_dict}