from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect(reverse("App_Video:video_list_t"))
