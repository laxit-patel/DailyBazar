# This Module Generates Next key based on previous value from database along with its creation time and  initials

# run this in shell to see the maximum number of record this generator can generate per day
# while key_generator('User') != 'Invalid Entity':
#     key = key_generator("User")
#     record = User(user_id=key)
#     record.save()


import datetime

from numpy import base_repr
from user.models import User
from vendor.models import Vendor
from django.db import connection

keychan_models = [
    #[app name, models name, 4 digit that you want to assign to primary key]
    [ "user", "User", "USER" ],
    
]

def date_generator():
    fullday = datetime.datetime.now().strftime("%d")
    fullmonth = datetime.datetime.now().strftime("%m")
    fullyear = datetime.datetime.now().strftime('%Y')[2:4]
    day = ""
    month = ""
    day_dict = {'01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U', '31': 'V'}

    month_dict = {'01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '10': 'A', '11': 'B', '12': 'C'}

    for day_data in day_dict:
        if day_data == fullday:
            day = day_dict[day_data]

    for month_data in month_dict:
        if month_data == fullmonth:
            month = month_dict[month_data]  

    if day == "":
        return "Invalid Day"
    elif month == "":
        return "Invalid Month"
    else:
        date = day + month + fullyear

    return date



def key_generator(entity):

    status = "ok"

    if entity == "User":
        initial = "USER"
        if User.objects.count() == 0:
            counter = str('0000')
        else:
            last_row = User.objects.values().last()
            prev_day = str(last_row['user_id']).split("_")[0][0:4]
            prev_counter = str(last_row['user_id']).split("_")[2][0:4]
            new_counter = int(prev_counter, 36) + 1
            counter = base_repr(new_counter, 36).zfill(4)
            if counter == '10000':
                status = "exceeded"   
            if prev_day != date_generator():
                counter = str('0000')           
    elif entity == "Vendor": 
        initial = "VNDR"
        if Vendor.objects.count() == 0:
            counter = str('0000')
        else:
            last_row = Vendor.objects.values().last()
            prev_day = str(last_row['vendor_id']).split("_")[0][0:4]
            prev_counter = str(last_row['vendor_id']).split("_")[2][0:4]
            new_counter = int(prev_counter, 36) + 1
            counter = base_repr(new_counter, 36).zfill(4)
            if counter == '10000':
                status = "exceeded"   
            if prev_day != date_generator():
                counter = str('0000') 
    else:
        status = "Invalid Entity"


    if status == "Invalid Entity":      
        return "Invalid Entity"
    elif status == "exceeded":
        return "Limit Exceeded"
    else:
        date = date_generator()
        key = date + "_" + initial + "_" + counter
        return key





# for entity in keychan_models:

#     app_name = entity[0]
#     model_name = entity[1]
#     initial = entity[2]

#     table = app_name + "_" + model_name
#     table = table.lower()
    
#     column = app_name + '_id'
    
#     query_count = f"SELECT COUNT(*) from {table}"
#     with connection.cursor() as cursor:
#         cursor.execute(query_count)
#         count = cursor.fetchone()
    
#     print(count[0])
    
#     if count[0] == 0:
#         print("New Counter")
#     else:
#         query = f"SELECT {column} from {table} ORDER BY {column} DESC limit 1"
#         with connection.cursor() as cursor:
#                 cursor.execute(query)
#                 last_row = cursor.fetchone()

#         prev_day = str(last_row[0]).split("_")[0][0:4]

#         prev_counter = str(last_row[0]).split("_")[2][0:4]
     
#         new_counter = int(prev_counter, 36) + 1

#         counter = base_repr(new_counter, 36).zfill(4)

#         if counter == '10000':
#             status = "exceeded"

#         if prev_day != date_generator():
#             counter = str('0000')       
    
                                        
