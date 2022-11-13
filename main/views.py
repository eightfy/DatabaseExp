from django.shortcuts import render

# Create your views here.
#主界面
def mainview(request):
    return render(request, 'main.html')
#添加新订单
def addview(request):
    return render(request, 'add.html')
