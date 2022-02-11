from Goods import Goods
import uuid


class Product(Goods):
    def __init__(self, name, price, quantity, category, discount, description, top):
        super().__init__(name, description, price, quantity)
        self.product_id = self.generate_product_id()
        self.__discount = discount
        self.__discounted_price = price - price * self.__discount
        self.__category = category
        self.__sold_units = 0
        self.__top = top
        self.__picture = None

    def set_picture(self, picture):
        self.__picture = picture

    def get_picture(self):
        return self.__picture

    def set_category(self, category):
        self.__category = category

    def set_discount(self, discount):
        self.__discount = discount

    def set_top(self, top):
        self.__top = top

    def get_top(self):
        return self.__top

    def increase_sold_units(self, sold):
        self.__sold_units += sold
        self.decrease_quantity(sold)

    def get_category(self):
        return self.__category

    def get_discount(self):
        return self.__discount

    def get_sold_units(self):
        return self.__sold_units

    def get_product_id(self):
        return self.product_id

    def calculate_new_price(self):
        self.__discounted_price = self.get_price() - self.get_price() * self.__discount

    def get_discounted_price(self):
        return self.__discounted_price

    def generate_product_id(self):
        return "".join(str(uuid.uuid4())[::2].split("-"))

    def __str__(self):
        return f"{self.get_product_id(), self.get_name(), self.get_description(), self.get_price(), self.get_quantity(), self.get_category(), self.get_discount(), self.get_top()}"
