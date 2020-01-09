#	Об’єкт “Автомобіль” (використати члени-класи)
import datetime

class Date:
    def __init__(self, year, month, day):
        if month > 12 or month < 1:
            raise Exception("wrong month")

        if day > 31 or day < 1:
            raise Exception("wrong day")

        self.__year = year
        self.__month = month
        self.__day = day
        self.__date = datetime.date(year, month, day)

    def __str__(self):
        return "{0:02}.{1:02}.{2}".format(self.__day, self.__month, self.__year)

    def get_date(self):
        return self.__date


class Producer:
    def __init__(self, prod_name, prod_year, prod_phone, production):
        self.prod_name = prod_name
        self.prod_year = prod_year
        self.prod_phone = prod_phone
        self.production = production

    def __str__(self):
        return " Назва виробника: {0}\n Рік заснування: {1}\n " \
               "Телефон: {2}\n обсяг виробництва: {3}".format(self.prod_name,
                            self.prod_year, self.prod_phone, self.production)


class Seller:
    def __init__(self, sell_name, sell_year, sell_phone, sales):
        self.sell_name = sell_name
        self.sell_year = sell_year
        self.sell_phone = sell_phone
        self.sales = sales

    def __str__(self):
        return " Прізвище продавця: {0}\n Рік заснування: {1}\n" \
               " Телефон: {2}\n Продажі: {3}".format(self.sell_name, self.sell_year,
                                                 self.sell_phone, self.sales)


class Owner:
    def __init__(self, full_name, code):
        self.full_name = full_name
        self.code = code

    def __str__(self):
        return " Ім'я власника: {0}\n код: {1}".format(self.full_name, self.code)


class Automobile:
    def __init__(self, brand, color, number,  production_date, producer, seller, owner):
        self.brand = brand
        self.color = color
        self.number = number
        self.production_date = production_date
        self.producer = producer
        self.seller = seller
        self.owner = owner

    def get_age(self):
        return abs((datetime.date.today() - self.production_date.get_date()).days)//365

    def change_owner(self, changed_user):
        self.owner = changed_user
        return self.owner


date = Date(2017, 5, 21)
prod = Producer('Kia Sorento Group', 2012, 3134775, 4000000)
seller = Seller('SellingCars', 2014, 22579, 80000)
own = Owner('Когут Нікіта', 113)

auto = Automobile('Kia', 'black', 2016, date, prod, seller, own)
print('Вік машини cтановить {0} років'.format(auto.get_age()))
print('Новий власник автомобіля {0}'.format(auto.change_owner('Марія')))