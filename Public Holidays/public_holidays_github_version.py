import requests



API_KEY = "get_your_API_key-https://calendarific.com/"
TOP_20_GDP_COUNTRIES = ["US", "CN", "JP", "DE", "GB", "IN", "FR", "IT", "CA", "KR", "RU", "BR", "AU", "ES", "ID", "MX", "NL", "CH", "TR", "SA", "CZ"]#+CZ
VISEGRAD_COUNTRIES = ["CZ", "SK", "PL", "HU"]

def format_response(json_response):
    formatted_response = {}
    holidays_list = json_response["response"]["holidays"]
    country = holidays_list[0]["country"]["id"]
    formatted_response["country"] = country
    for public_holiday in holidays_list:
        name = public_holiday["name"]
        date = public_holiday["date"]["iso"]
        formatted_response[date] = name
    return formatted_response

def get_list_of_public_holidays(country_list, year):
    result = []
    for country in country_list:
        url = f"https://calendarific.com/api/v2/holidays?&api_key={API_KEY}&country={country}&year={year}&type=national"
        r = requests.get(url=url)
        response = r.json()
        result.append(format_response(response))
    return result

#print(get_list_of_public_holidays(VISEGRAD_COUNTRIES, 2022))
#print(get_list_of_public_holidays(TOP_20_GDP_COUNTRIES, 2022))
