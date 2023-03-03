from src.models.restaurant import Restaurant


class TestRestaurant:

    def setup(self):
        self.restaurant_name = "Restaurante do Jacquin"
        self.cuisine_type = "Comida Italiana"
        self.restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

    def test_describe_restaurant(self):
        message = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.\nEsse restaurante está " \
                  f"servindo 0 consumidores desde que está aberto."
        result = self.restaurant.describe_restaurant()
        assert result == message

    def test_open_restaurant(self):
        message = f"{self.restaurant_name} agora está aberto!"
        result = self.restaurant.open_restaurant()
        assert result == message
        assert self.restaurant.open is True
        assert self.restaurant.number_served == 0

    def test_close_restaurant(self):
        message = f"{self.restaurant_name} agora está fechado!"
        self.restaurant.open_restaurant()
        result = self.restaurant.close_restaurant()
        assert result == message
        assert self.restaurant.open is False
        assert self.restaurant.number_served == 0

    def test_close_restaurant_with_closed_restaurant(self):
        message = f"{self.restaurant_name} já está fechado!"
        result = self.restaurant.close_restaurant()
        assert result == message
        assert self.restaurant.open is False
        assert self.restaurant.number_served == 0

    def test_set_number_served(self):
        number_served = 10
        self.restaurant.open_restaurant()
        result = self.restaurant.set_number_served(number_served)
        assert result == number_served

    def test_set_number_served_with_closed_restaurant(self):
        message = f"{self.restaurant_name} está fechado!"
        number_served = 10
        result = self.restaurant.set_number_served(number_served)
        assert result == message

    def test_increment_number_served(self):
        customers = 2
        more_customers = 10
        message = customers + more_customers
        self.restaurant.open_restaurant()
        self.restaurant.set_number_served(customers)
        result = self.restaurant.increment_number_served(more_customers)
        assert result == message

    def test_increment_number_served_with_closed_restaurant(self):
        message = f"{self.restaurant_name} está fechado!"
        more_customers = 10
        result = self.restaurant.increment_number_served(more_customers)
        assert result == message

    def test_validate_number_int(self):
        expected_result = True
        number = 1
        result = self.restaurant.validate_number(number)
        assert result == expected_result

    def test_validate_number_string(self):
        expected_result = False
        number = "1"
        result = self.restaurant.validate_number(number)
        assert result == expected_result

    def test_validate_number_negative(self):
        expected_result = False
        number = -1
        result = self.restaurant.validate_number(number)
        assert result == expected_result

    def test_validate_number_none(self):
        expected_result = False
        number = None
        result = self.restaurant.validate_number(number)
        assert result == expected_result
