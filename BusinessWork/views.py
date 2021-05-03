from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout


def signupPage(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']

        passwd=request.POST['password']
        s_passwd=request.POST['super_password']
        url='/signup/'
        my_passwd='L1a2k3h4a5@n#Gupta'
        if my_passwd==s_passwd:

                url='/signup/'
                try:

                    u=User(username=uname,email=email,password=make_password(passwd))
                    u.save()
                    return redirect('/login/')
                except:
                    return HttpResponse('<script>alert("Username is not available.");\
                    window.location="%s"</script>'%url)
                return redirect('/signup/')
        else:
            return HttpResponse('<script>alert("Super password not matched, Contact to admin.");\
                    window.location="%s"</script>'%url)
            

    return render(request,'signup.html')
    
def loginPage(request):
    url='/login/'
    if request.method=='POST':
        uname=request.POST['username']
        passwd=request.POST['password']
        currentUser=authenticate(username=uname,password=passwd)
        if currentUser:
            login(request,currentUser)
            #return render(request,'index.html')
            return redirect('/vendor/businesswork/')
        else:
            return HttpResponse('<script>alert("Invalid username or password.");\
			window.location="%s"</script>'%url)
        return redirect('/login/')

		
    return render(request,'login.html')
def logoutCall(request):
    logout(request)
    
    return redirect('/login/')