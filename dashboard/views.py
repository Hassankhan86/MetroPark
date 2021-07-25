from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from datetime import datetime

from . import forms

# Create your views here.
from .forms import Customer_details
from .models import parking_spaces, slots_booking_table, Slot_duration_table,customer

def contact_us(request):
    return render(request, 'dashboard/contact_us.html')

def services(request):
    return render(request, 'dashboard/services.html')

def career(request):
    return render(request, 'dashboard/career.html')

# @login_required(login_required, name='dispatch')
# @login_required(login_url='/accounts/login')
# def booking(request):
#     parking_space1 = parking_spaces.objects.get(space_name='Link Road')
#     slb = slots_booking_table.objects.all()
#
#     if request.method == 'POST':
#
#         print("method is post")
#         form = forms.Customer_details(request.POST, request.FILES)
#
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             print("inside form is valid")
#             form.save()
#
#             # # parking_space.slot_booking.add(form)
#             # abc = slots_booking_table.customer_info.add(form)
#             # parking_space1.slot_booking.add(abc)
#             # # @login_required(login_url='/accounts/login')
#             # return details(request)
#             return details(request)
#             # return HttpResponse("hjk")
#
#     form = forms.Customer_details()
#     print("inside Else")
#
#     return render(request, 'dashboard/search_form.html', {'form': form})
#
#
# @login_required(login_url='/accounts/login')
# def details(request):
#     return render(request, 'dashboard/details.html')
#
#
# def bk_form(request, location, duration, from_date):
#     sp = parking_spaces.objects.filter(space_name=location)
#
#     # x = datetime.datetime(2018, 6, 1)
#     # print(x)
#     # slout_bk = slots_booking_table.objects.all()
#     print(location)
#     print(from_date)
#     if request.method == 'POST':
#         form = forms.Customer_details()
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             print("inside form is valid")
#             form.save()
#
#             # parking_space.slot_booking.add(form)
#             # abc = slots_booking_table.customer_info.add(form)
#             # sp.slot_booking.add(abc)
#         # abc = slout_bk.customer_info.save(form)
#         # sp.slot_booking.add(abc)
#         # print(duration, from_date)
#
#         return render(request, 'dashboard/search_form.html', {'form': form, 'sp': sp})
#     return HttpResponse("ghjk")
#
#
# # @login_required(login_url='/accounts/login')
# def homepage(request):
#     live = parking_spaces.objects.all()
#     duration = request.POST.get('options-outlined')
#
#     print(duration)
#     location = request.POST.get('location_address')
#     date = request.POST.get('date')
#     print(location)
#
#     if request.method == 'POST':
#         return bk_form(request, location, duration, date)
#
#     #     sp = parking_spaces.objects.all()
#     #
#     #
#     #
#     #
#     #     sp = parking_spaces.objects.filter(space_name=location)
#     #
#     #
#     #     print("inside Else22")
#     #     request.method = 'GET'
#     #     return render(request, 'dashboard/search_form.html', {'form': form,'sp':sp})
#     return render(request, 'dashboard/homepage.html', {'live': live})

def booking(request):
    live = parking_spaces.objects.all()
    # parking_space1  = parking_spaces.objects.get(space_name='Link Road')


    if request.method == 'POST':

    #     print("method is post")
        form = forms.Customer_details(request.POST,request.FILES)
        form1 = forms.slots_booking(request.POST, None)
        form2 = forms.parking_spaces_form(request.POST, None)



        if form.is_valid() and form1.is_valid():
            # instance = form.save(commit=False)
            print("inside form is valid")



            # ss = Temp.objects.get()
            # print('ss',ss )


            print('----------------------')

            from_date = request.session['from_date1']
            from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
            to_date = request.session['to_date1']
            to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
            hours = request.session['hourspass']

            print(from_date)
            print(to_date)
            print('Total',hours)

            print('----------------------')

            dur = Slot_duration_table(to_date=to_date, from_date=from_date)
            dur.save()

            form  = form.save()
            ms = form1.save(commit=False)
            ms.customer_info = form
            ms.Slot_duration = dur


            ok1 = request.session['location_address1']
            print(ok1)

            ob = parking_spaces.objects.get(space_name=ok1)

            toobb =  ob.total_slots
            print('toobb',toobb)



            rt = ob.slot_rates
            Total_Hr =  rt * hours
            # tsr = slots_booking_table(total_price=Total_Hr)
            ms.total_price = Total_Hr
            print(Total_Hr)

            request.session['Total_Price'] = Total_Hr



            # ob .save()
            ms.save()
            ob.slot_booking.add(ms)
            ob.save()
            print(ob)

            Remeaning = toobb - 1
            print('Total Objects', Remeaning)
            ob.total_slots = Remeaning
            ob.save()


            return details(request,pk_test=94)


    form = forms.Customer_details()
    print("inside Else")


    return render(request, 'dashboard/search_form.html', {'form': form,'form1': form1,'live': live})


# @login_required(login_url='/accounts/login')
def details(request,pk_test):

    customers = customer.objects.get(id=pk_test)
    slot_booking = customers.slots_booking_table_set.all()
    
    print(customers)
    print(slot_booking)

    context = {"customers":customers,"slot_booking":slot_booking}

    return render(request, 'dashboard/details.html',context)

# @login_required(login_url='/accounts/login')
def homepage(request):

    live = parking_spaces.objects.all()


    if request.method == 'POST':

        sp = parking_spaces.objects.all()
        ss = slots_booking_table.objects.all()



        slot_dur = Slot_duration_table.objects.filter()

        # Temp1 = Temp.objects.all()


        # print(Temp1)
        # duration = request.POST.get('options-outlined')
        # print(duration)



        # Temp.search_name.clear()


        location = request.POST.get('location_address')
        request.session['location_address1'] = location
        print(location)

        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        request.session['from_date1'] = from_date
        request.session['to_date1'] = to_date

        from_date1 = request.POST.get('from_date')
        from_date1 = datetime.strptime(from_date1, '%Y-%m-%dT%H:%M')
        print(from_date1)

        to_date1 = request.POST.get('to_date')
        to_date1 = datetime.strptime(to_date1, '%Y-%m-%dT%H:%M')
        print(to_date1)

        diff = to_date1 - from_date1
        print("Diff : ", diff)
        sec = diff.total_seconds()
        hours = sec / 3600
        print("Hours", hours)
        # Hrro = round(hours, 2)
        # print(Hrro)
        request.session['hourspass'] = hours

        # Temp1.delete()
        # search = Temp(search_name=location)
        # search.save()



        # from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
        # print(from_date)
        # #
        # to_date = request.POST.get('to_date')
        # to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
        # #
        # diff = to_date - from_date
        # print("Diff : ", diff)
        # from_date2 = request.POST.get('from_date2')
        # print(from_date2)





        #
        # dur =  Slot_duration_table(from_date=from_date)
        # dur.save()




        sp = parking_spaces.objects.filter(space_name=location)

        # request.session['Total_Price'] = Total_Hr
        # Total_Hr = request.session['Total_Price']






        form = forms.Customer_details()
        form1 = forms.slots_booking()
        print("inside Else22")
        # request.method = 'GET
        # return location
        return render(request, 'dashboard/search_form.html', {'form1': form1,'form': form,'sp':sp,'ss':ss,"from_date1":from_date1,"to_date1":to_date1,"hours":hours})
    return render(request, 'dashboard/homepage.html', {'live': live})
