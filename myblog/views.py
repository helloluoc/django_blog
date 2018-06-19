from django.shortcuts import render
from django.views import View
# Create your views here.
from myblog.models import Blog, Tag
from pure_pagination import PageNotAnInteger, Paginator

class IndexView(View):
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        blog_nums = all_blog.count()


        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  #5为每页展示的博客数目

        return render(request, 'index.html', {
            'all_blog': all_blog,
            'blog_nums': blog_nums,
        })

class ArichiveView(View):
    def get(self,request):
        all_blog = Blog.objects.all().order_by('-create_time')
        blog_nums = all_blog.count()
        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_blog, 5,request=request)
        all_blog = p.page(page)

        return render(request, 'archieve.html', {
            'all_blog':all_blog,
            'blog_nums': blog_nums,
        })

class TagView(View):

    def get(self, request):
        all_tag = Tag.objects.all()
        tag_nums = all_tag.count()

        return render(request, 'tags.html', {
            'all_tag': all_tag,
            'tag_nums': tag_nums,
        })

class TagDetailView(View):
    def get(self,request, tag_name):
        tag = Tag.objects.filter(name = tag_name).first()
        tag_blogs = tag.blog_set.all()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 5, request=request)
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html', {
            'tag_blogs': tag_blogs,
            'tag_name': tag_name,
        })

class BlogDetailView(View):
    """
    博客详情页
    """
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        return render(request, 'blog-detail.html', {
            'blog': blog,

        })