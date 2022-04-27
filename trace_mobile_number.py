# importing phonenumbers module
import phonenumbers

# importing timezone, geocoder, carrier from phonenumbers package
from phonenumbers import timezone, geocoder, carrier

# Entering the number
number = input("Enter your number with +__: ")

# prints the country code along with the number
phone = phonenumbers.parse(number)

# prints the region to which the phone number belongs
time = timezone.time_zones_for_number(phone)

# prints the carrier of the respective mobile number(such as airtel, jio, BSNL)
car = carrier.name_for_number(phone, "en")

# prints the country to which the mobile number belongs
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(car)
print(reg)
