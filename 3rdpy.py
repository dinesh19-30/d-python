import phonenumbers

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country_code = parsed_number.country_code
        country_name = phonenumbers.region_code_for_number(parsed_number)
        carrier_name = phonenumbers.carrier.name_for_number(parsed_number, "en")

        print("Country Code:", country_code)
        print("Country Name:", country_name)
        print("Carrier Name:", carrier_name)

    except phonenumbers.NumberParseException as e:
        print("Invalid phone number:", e)

if __name__ == "__main__":
    phone_number = input("Enter a phone number: 9025119360")
    get_phone_number_info(phone_number)
