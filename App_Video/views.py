from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from App_Video.forms import CommentForm
from App_Video.models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.contrib.auth.decorators import login_required

# Create your views here.


def VideoList(request):
    videos = Video.objects.all()
    if request.method == "GET":
        search = request.GET.get("search", "")
        result = Video.objects.filter(video_title__icontains=search)
    dict = {"title": "Home . Instagram", "search": search,
            "result": result, "videos": videos}
    return render(request, 'App_Video/video_list_t.html', context=dict)


class UploadVideo(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'App_Video/upload_video.html'
    fields = ('video_title', 'video_description',
              'video_thumbnail', 'video_file')

    def form_valid(self, form):
        video_obj = form.save(commit=False)
        video_obj.author = self.request.user
        title = video_obj.video_title
        video_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        video_obj.save()
        return HttpResponseRedirect(reverse('index'))


def video_details(request, slug):
    video = Video.objects.get(slug=slug)
    comment_form = CommentForm()

    if request.method == 'POST':
        def post_comment():
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.video = video
                comment.user = request.user
                comment.save()
                return HttpResponseRedirect(reverse('App_Video:video_details', kwargs={'slug': slug}))
            return render(request, 'App_Video/video_details.html', context={'video': video, 'comment_form': comment_form})

        if not request.user.is_authenticated:
            return login_required(post_comment)(request)

        return post_comment()

    return render(request, 'App_Video/video_details.html', context={'video': video, 'comment_form': comment_form})
