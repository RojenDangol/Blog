from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('We will keep blog here ')


def blogPost(request, slug):
    return HttpResponse('This is blogPost')