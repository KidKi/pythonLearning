from django.shortcuts import render
from polls import models
import xlrd, sqlite3, os, time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
    if request.method == "POST":
        studentName = request.POST.get("studentName", None)
        score = request.POST.get("score", None)
        models.UserInfo.objects.create(studentName=studentName, score=score)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data":user_list})


def importExcel(request):
    if request.method == "POST":
        obj = request.FILES.get('excel')
        position = handle_uploaded_file(obj)
        data = xlrd.open_workbook(position)
        table = data.sheets()[0]
        nrows = table.nrows
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        for i in range(nrows):
            if i == 0:
                continue
            cursor.execute('insert into polls_userinfo(studentName,score) values (?,?)',
                           (table.cell_value(i, 0), table.cell_value(i, 1)))
        cursor.close()
        conn.commit()
        conn.close()
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})

def handle_uploaded_file(f):
    file_name = ""

    path = os.path.join(BASE_DIR, 'static', 'excel')
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, str(int(round(time.time()*1000)))) + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return file_name

