from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.

#bunun bir view olması için mutlaka bir argüman alması gerekiyor.

def post_index(request):
    posts=Post.objects.all()
    return render(request,'post/index.html',{'posts':posts})

def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    context={
        'post':post,
    }
    return render(request,'post/detail.html',context)


def post_create(request):

#BAŞKA BİR FORM ŞEKLİ AMA DİĞER KODLAR ÇALIŞSIN DİYE YORUM HALİNE GETİRDİM
    #context={
     #   'form':form,
     # }
    #if request.method=="post":
     #   print(request.post)

    #title=request.post.get('title')
    #content=request.post.get('content')
    #Post.objects.create(title=title,content=content)

    #if request.method=='post':
        #formdan gelen bilgileri kaydet
     #   form=PostForm(request.post)
      #  if form.is_valid():
       #     form.save()
    #else:
        #formu kullanıcıya göster
     #   form = PostForm()

#örneğin post oluşturduktan sonra başarılı diye bir mesaj göndermek istiyorum

    form=PostForm(request.POST or None)
    if form.is_valid():
        post=form.save()
        messages.success(request,'başarılı bir şekilde post oluşturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request,'post/form.html',context)


def post_update(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        #update ettiğimizde de saveden hemen sonra bir mesaj gönderelim. bunun içinde;
        messages.success(request,'başarılı bir şekilde update ettiniz')

        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')

