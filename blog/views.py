from django.shortcuts import render
from .models import Post, Category, SearchList
from django.views.generic import ListView, DetailView
from django.db.models import Q


# Create your views here.
# [CBV : Class Based View] --------------------------------
class Search(ListView):
    model = SearchList

    def get_queryset(self):
        lt = SearchList.objects.order_by('-data')
        print('searchList >>', lt)

        return lt


class PostList(ListView):
    model = Post

    #작성일 기준으로 내림차순 정렬(최신글)
    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        print('context 1) : **kwargs >> ', context)

        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()
        print('context 2) >> ', context)

        return context


class PostSearch(PostList):
    def get_queryset(self):
        q = self.kwargs['question']
        object_list = Post.objects.filter(Q(title__contains=q) | Q(content__contains=q))
        return object_list
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostSearch, self).get_context_data()
        context['search_info'] = 'Search Result >> {}'.format(self.kwargs['question'])

        s = SearchList(searchword=self.kwargs['question'])
        s.save()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostListByCategory(PostList):
    def get_queryset(self):
        slug = self.kwargs['slug']
        print('slug >>', slug)

        category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListByCategory, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)

        return context


# [FBV : Function Based View] --------------------------------
# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#     context = {
#         'blog_post': blog_post,
#     }
#
#     return render(request, 'blog/post_detail.html', context)


# def index(request):
#     post = Post.objects.all()
#     context = {
#         'post': post,
#     }
#
#     return render(request, 'blog/index.html', context)
#
# -------------------------------------------------------------

