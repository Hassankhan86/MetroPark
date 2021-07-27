# from urllib import request
# from django.http import request
#
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
#
# from django.contrib.auth.models import Group
#
# from dashboard.models import customer
# from dashboard.views import *
# from dashboard.forms import *
#
#
# @receiver(post_save, sender=User)
# def customer_profile(sender, instance, created, **kwargs):
#
#
#
#
#     if created:
#         print('<-------------------------------------->')
#         # from_date = request.session['from_date1']
#         # from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
#         # to_date = request.session['to_date1']
#         # to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
#         # hours = request.session['hourspass']
#         #
#         # print(from_date)
#         # print(to_date)
#         # print('Total', hours)
#         # dur = Slot_duration_table(to_date=to_date, from_date=from_date)
#         # dur.save()
#
#         # cust_name_ar = request.session['cust_name_ar']
#         # hours = request.session['hourspass']
#         # print(hours)
#         # print(cust_name_ar)
#         print('<-------------------------------------->')
#         customer.objects.create(
#             user=instance,
#             customer_name=instance.cust_name_ar,
#             customer_email=instance.email,
#             # customer_phone=instance.Customer_details.customer_phone,
#
#         )
#         # group = Group.objects.get(name='customer')
#         # instance.groups.add(group)
#         # customer.objects.create(
#         #     user=instance,
#         #     name=instance.username,
#         # )
#         # print('Profile Created')
#
# post_save.connect(customer_profile,sender=User)