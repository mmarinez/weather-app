def greetting(self):
    print('--------------------------')
    print('        WEATHER APP')
    print('--------------------------')


def set_user_zipcode():
    zip_code = input('What zipcode do you want the weather for (97201)? ')
    return zip_code


def get_html(zip_code):
    url = 'https://www.wunderground.com/weather/us/ma/brimfield/{}'.format(zip_code)
    print(url)


def parse_html(self, parameter_list):
    pass


def display():
    get_html(set_user_zipcode())


if __name__ == "__main__":
    display()
