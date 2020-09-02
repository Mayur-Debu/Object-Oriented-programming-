class India(object):
    def country(self):
        print("Country name is India.")
    def language(self):
        print("Language widely spoken in India is Hindi.")
    def type(self):
        print("India is a developing country.\n")

class USA(India):
    def country(self):
        print("Country name is The United States of America.")
    def language(self):
        print("Language widely spoken in India is English.")
    def type(self):
        print("The United States of America is a developed country.")

india=India()
usa=USA()
for country in (india,usa):
    country.country()
    country.language()
    country.type()