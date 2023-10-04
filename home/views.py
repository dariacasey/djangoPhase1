from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm
from accounts.models import Profile


class HomePage(ListView):
    model = Post
    template_name = 'home/home_page.html'

    # Passes post count
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get anonymous user error if not
        if self.request.user.is_authenticated:
            user = self.request.user

            # Passes post count in context
            post_count_context = self.get_post_count(user)
            context.update(post_count_context)

        return context

    # gets post count (might be able to combine both functions in future if there's time)
    def get_post_count(self, user):
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            user_profile = None

        if user_profile and user_profile.is_student:
            post_count = Post.objects.filter(class_field__students=user).count()
        elif user_profile and user_profile.is_teacher:
            post_count = Post.objects.filter(class_field__teacher=user).count()
        else:
            post_count = 0

        return {'post_count': post_count}

    # Only display posts from classmates/teacher
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_profile = user.profile
        else:
            user_profile = None

        if user_profile and user_profile.is_student:
            return Post.objects.filter(class_field__students=user).order_by('-date_created')
        elif user_profile and user_profile.is_teacher:
            return Post.objects.filter(class_field__teacher=user).order_by('-date_created')
        else:
            return Post.objects.none()


class ArticleDetail(DetailView):
    model = Post
    template_name = 'home/article_detail.html'

    # Does post views
    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)

        post.views += 1
        post.save()

        return post


class AddPostView(CreateView):
    model = Post
    template_name = "home/add_post.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Fixed Anonymous User error
        try:
            user_profile = self.request.user.profile
        except AttributeError:
            user_profile = None

        if user_profile:
            form.instance.class_field = user_profile.class_field

        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = "home/edit_post.html"
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "home/delete_post.html"
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "home/add_comment.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

