from django.shortcuts import render

# Create your views here.
def video_capture(request):
    return render(request, 'videoCapture.html')

