import phonenumbers
from phonenumbers import geocoder

phone_no = phonenumbers.porse("Number with Country code")
print(geocoder.description_for_number(phone_no,'en'))

# get service provider name to that phone number

from phonenumbers import carrier
service_pro = phonenumber.porse('Number with Country code')

print(carrier.name_for_number(service_pro,'en'))