from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #implementing CRUD on blog post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #mixins to control access to views
from .models import Post, Comment
from django.db.models import Q

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.isvalid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'form': form, 'profile_form': profile_form})

#class to implement CRUD operations
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    seccess_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

#comment view classes
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['post_id'])
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class =CommentForm

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    seccess_url = '/' #Redirect after deletion

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

#tags and search view
class SearchResultsView(ListView):
    models = Post
    template_name = 'blog/search_results.html'

    def get_querset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)| Q(tags__name__icontains=query)).distinct()

class TaggedPostView(ListView):
    model = Post
    templates_name = 'blog/tagged_posts.html'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))

