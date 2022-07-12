
# import pdb;
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from .models import empregister_model
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import get_user_model


from django.contrib.auth import login,authenticate

# Create your views here.
def empregister_view(request):
    # print(request.user)

    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['unm']
        password=request.POST['pswd']
        confirm_password=request.POST['pswd2']

        #validation..

        if name and email and username and password and confirm_password == ' ':
            return HttpResponse ('all fields required..')
            # return redirect('empregister')



        if len(name)>10:
            messages.error(request,'username must be under 10 character')
            return redirect('empregister')

        if not name.isalpha():
            messages.error(request,'username should only contain 10 characters')
            return redirect('empregister')


        if password!=confirm_password:
            messages.error(request,'Confirm Password do not match with Password')
            return redirect('empregister')

        

        create_user=User.objects.create_user(username,email,password)
        create_user.first_name=name
        create_user.save()
        messages.success(request,'user registered successfully..')
        return redirect('emplogin')

    else:
        return render(request,'emp_register.html')


def emplogin_view(request):
    if request.method=='POST':
        username=request.POST['unm']
        password=request.POST['pswd']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            # pdb. set_trace()
            if username == 'riti':
                login(request,user)
                print(user)
                return redirect('displayadmin')
            else:
                messages.success(request,'you have successfully logged in...')
                return redirect('displayuser')
        
            
        
    else:
        return render(request,'emp_login.html')





def displayuser_view(request):
    
    getdata=User.objects.get(pk=request.user.pk)

        
    
    
    context={'getdata':getdata}
    return render(request,'display_user.html',context)




def displayadmin_view(request):

    
        getuserdata =User.objects.all()
        # getuserdata=User.objects.filter(is_superuser=True)

        user_count = User.objects.count()
        print(getuserdata)
        return render(request,'display_admin.html' ,{'getuserdata':getuserdata, 'user_count':user_count})

    
    
    
