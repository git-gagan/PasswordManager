from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import tbl_users, tbl_userdata

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user_exists = tbl_users.objects.filter(email=email)
        if not user_exists:
            print(f"User with ${email} does not exist")
            user = tbl_users(email=email, password=password)
            user.save()
            print("User Saved")
        else:
            print("User exists")
        return redirect("loginUser")
    return render(request, 'registerUser.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        is_authenticated = tbl_users.objects.filter(email=email, password=password)
        print(is_authenticated[0].id)
        if not is_authenticated:
            print(f"User with ${email} does not exist")
            return redirect('registerUser')
        else:
            print("authentication successful")
            request.session['name'] = email 
            request.session['id'] = str(is_authenticated[0].id)
            return redirect('dashboard')
    return render(request, 'loginUser.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    print(request.session)
    if 'name' in request.session:
        userdata = tbl_userdata.objects.filter(user_id=request.session['id']) 
        print(userdata)
        if not userdata:
            return HttpResponse(f"No data for {request.session['name']}")
        else:
            # return HttpResponse(userdata)
            print(list(userdata)[0].website)
            return render(request, 'dashboard.html', {'data':list(userdata)})
    return redirect('loginUser')

def insertData(request):
    if 'name' in request.session:
        if request.method == "POST":
            website = request.POST['website']
            identity = request.POST['identity']
            password = request.POST['password']
            data = tbl_userdata(website=website, email=identity, password=password, user_id=request.session['id'])
            data.save()
            return redirect('dashboard')
        return render(request, 'insertData.html')
    return redirect('loginUser')
        