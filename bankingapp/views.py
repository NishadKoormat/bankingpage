from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.utils import timezone
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('bankingapp:signup')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save()
                print('User created')
                return redirect('bankingapp:login')

        else:
            messages.info(request, "password not matched")
            return redirect('bankingapp:signup')

    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'home.html')
        else:
            messages.info(request, "invalid username or password")
            return redirect('bankingapp:login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def services(request):
    return render(request,'services.html')

def details(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        bankname = request.POST['bankname']
        acnumber = request.POST['acnumber']
        ifsc = request.POST['ifsc']
        zip = request.POST['zip']
        address = request.POST['address']
        city = request.POST['city']
        district = request.POST['district']
        branch = request.POST['branch']
        dob = request.POST['dob']
        age = int(request.POST['age'])
        phone = request.POST['phone']
        email = request.POST['email']
        type_ac = request.POST['account-type']
        gender=request.POST['gender']
        ms = ['Debit Card', 'Credit Card', 'Cheque Book']
        details = request.POST.getlist('materials')

        # Your validation logic here

        if len(ifsc) != 11 or len(acnumber) < 8 or len(acnumber) > 12 or len(zip) != 6 or len(phone) != 10:
            print('validation error')
            return redirect('bankingapp:details')
        else:
            dob_input = request.POST['dob']
            age_input = int(request.POST['age'])

            # Validate Date of Birth and Age

            try:
                dob = datetime.strptime(dob_input, '%Y-%m-%d').date()
                current_date = timezone.now().date()
                # gender = request.POST['gender']

                calculated_age = current_date.year - dob.year - (
                            (current_date.month, current_date.day) < (dob.month, dob.day))
                if age_input == calculated_age:
                    # register = Register(fname=fname, address=address, lname=lname, city=city, zip=zip,
                    #                     district=district, branch=branch, dob=dob, age=age, bankname=bankname,
                    #                     acnumber=acnumber, ifsc=ifsc, gender=gender, phone=phone, email=email,
                    #                     type_ac=type_ac, details=details)
                    # register.save()
                    # print(register)
                    return render(request, 'registration_success.html')
                else:
                    return redirect('bankingapp:details')
            except:
                return redirect('bankingapp:details')

    return render(request,'details.html')

def money(request):
    return render(request,'money_transfer.html')
def registration_success(request):
    return render(request,'registration_success.html')
