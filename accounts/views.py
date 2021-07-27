from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dashboard.views import *
from dashboard.forms import *


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard:homepage')
            else:
                messages.info(request, "Username Or Password is Incorrect ")

    # return HttpResponse("ddasdasd")
    return render(request, 'accounts/login.html', )


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        form = CreateUserForm()

        print('<-------------------------------------->')
        cust_name_ar = request.session['cust_name_ar']
        cust_id_no_ar = request.session['cust_id_no_ar']
        cust_phone_ar = request.session['cust_phone_ar']
        cust_mail_ar = request.session['cust_mail_ar']
        vehicle_name_ar = request.session['vehicle_name_ar']
        vehicle_number_plate_ar = request.session['vehicle_number_plate_ar']
        vehicle_color_ar = request.session['vehicle_color_ar']
        vehicle_documents_ar = request.session['vehicle_documents_ar']

        from_date_ar = request.session['from_date1']
        from_date_ar = datetime.strptime(from_date_ar, '%Y-%m-%dT%H:%M')
        to_date_ar = request.session['to_date1']
        to_date_ar = datetime.strptime(to_date_ar, '%Y-%m-%dT%H:%M')

        Total_Hr_ar = request.session['Total_Hr_ar']

        ok1 = request.session['location_address1']
        print(ok1)
        ob = parking_spaces.objects.get(space_name=ok1)
        print('<-------------------------------------->')

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():

                user = form.save()

                cus = customer(customer_name=cust_name_ar,customer_id=cust_id_no_ar,customer_phone=cust_phone_ar,
                               customer_email=cust_mail_ar,vehicle_number=vehicle_number_plate_ar,vehicle_name=vehicle_name_ar,
                               vehicle_color=vehicle_color_ar,vehicle_documents=vehicle_documents_ar
                               )

                cus.user = user
                cus.save()

                dur = Slot_duration_table(to_date=from_date_ar, from_date=to_date_ar)
                dur.save()

                sb = slots_booking_table()
                sb.customer_info = cus
                sb.Slot_duration = dur
                sb.parking_name = ob
                sb.total_price = Total_Hr_ar
                sb.save()



                # a = customer(user=cust_name_ar
                #              )
                # # customer.user =user
                # a.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Accounts was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
    # return HttpResponse("Register")
    return render(request, 'accounts/register.html', context)
