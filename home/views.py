from django.shortcuts import render,HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        context={
            'isim':'İrem kömürcü',
        }
    else:
        context={
            'isim':'misafir',
        }
    return render(request,'home.html', context)





