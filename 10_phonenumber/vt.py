import phonenumbers

from phonenumbers import geocoder

# phone = input('Digite o telefone no formato: +5511943604897: ')

phone = '+5511943604897'

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt-br'))
print(geocoder.national_significant_number(phone_number))
