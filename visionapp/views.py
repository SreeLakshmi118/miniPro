from django.shortcuts import render
from .models import Books
from .models import Song

from django.contrib.auth.decorators import login_required
# Create your views here.

# def home(request):
#     demo=Book.objects.all()
#     for i in demo:
#         print(i.b_name)
#     return render(request, 'home.html', context={'demo':demo})
@login_required(login_url='login') 
def home(request):
    obj=Books.objects.all()
    sng=Song.objects.all()
    context={'obj':obj, 'sng':sng}
    for i in obj:
        print(i.b_name)
    return render(request,'home.html',context)


# @login_required(login_url='login') 
# def home(request):
#     obj=Song.objects.all()
#     context={'obj':obj}
#     for j in obj:
#         print(j.s_name)
#     return render(request,'home.html',context) 



# def change_password(request):
#     if request.method == 'POST':
#         current_password = request.POST['current_password']
#         new_password = request.POST['new_password']
#         confirm_password = request.POST['confirm_password']

#         user = User.objects.get(email__exact=request.user.email)
#         success = user.check_password(current_password)
#         if success:
#             user.set_password(new_password)
#             user.save()
#             messages.success(request, 'Password updated successfully.')
#             return redirect('login')
#         else:
#             messages.error(request, 'Password does not match!')
#             return redirect('change_password')
#     return render(request, 'change_password.html')