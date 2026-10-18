# # To run and test the code you need to update 4 places:
# # 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# # 2. Go to your email provider and make it allow less secure apps.
# # 3. Update the SMTP ADDRESS to match your email provider.
# # 4. Update birthdays.csv to contain today's month and day.
# # See the solution video in the 100 Days of Python Course for explainations.


# from datetime import datetime
# import pandas
# import random
# import smtplib
# import os

# # import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )

import os

MY_LAT = 49.280704 # Your latitude
MY_LONG = -122.796441 # Your longitude
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters= {
   "lat" : MY_LAT,
   "lon" : MY_LONG,
   "appid" : api_key,
   "cnt" : 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
# print(response.status_code)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
list_weather= []
for i in range(0,4):
   weather = weather_data["list"][i]["weather"][0]["id"]
   list_weather.append(weather)
print(list_weather)
if any (i <700 for i in list_weather):
   print("Bring an umbrella!")
   client = Client(account_sid, auth_token)
   message = client.messages.create(
       body="sms_appointment_reminders",
       from_="+17372508034",
       to="+17785989012",
   )
   print(message.body)
