from django.shortcuts import render
from polls import models

# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
    if request.method == "POST":
        studentName = request.POST.get("studentName", None)
        score = request.POST.get("score", None)
        models.UserInfo.objects.create(studentName=studentName, score=score)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data":user_list})