import os


class Capital:
    def __init__(self):
        pass

    def get_list_of_countries(self):
        countries = {}

        with open('Jarvan/Files/countrylist.txt', 'r') as country_data:
            try:
                for each_line in country_data:
                    (country_name, capital_city) = each_line.split(':', 1)
                    country_name = country_name.strip()
                    capital_city = capital_city.strip()
                    countries[country_name] = capital_city
                country_data.close()
                return countries

            except ValueError:
                pass

    def check_if_country(self, command, countries):
        for country in countries:
            if country in command:
                return country

    def capital(self, command):
        data = None
        countries = self.get_list_of_countries()

        country = self.check_if_country(command, countries)

        if country:
            try:
                if country:
                    data = "The Capital city of %s is %s." % (
                        country.title(), countries[country])
            except Exception as e:
                data = "What? I don't know the capital of that or maybe you just suck."
        else:
            data = "That's not a country, I guess."

        return data
