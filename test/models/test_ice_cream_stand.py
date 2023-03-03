from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def setup(self):
        self.restaurant_name = "Sorveteria Kigelo"
        self.cuisine_type = "sorvete artesanal"
        self.flavors_list = ["Chocolate", "Nata Goiaba", "Delícia de Abacaxi"]
        self.ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

    def test_flavors_available(self):
        result = self.ice_cream_stand.flavors_available()
        assert result == self.flavors_list

    def test_flavors_available_out_of_stock(self):
        message = "Estamos sem estoque atualmente!"
        flavor_empty_list = []
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, flavor_empty_list)
        result = ice_cream_stand.flavors_available()
        assert result == message
        assert ice_cream_stand.flavors == flavor_empty_list

    def test_find_flavor(self):
        flavor = "Delícia de Abacaxi"
        message = f"Temos no momento {flavor}!"
        result = self.ice_cream_stand.find_flavor(flavor)
        assert result == message

    def test_find_flavor_there_is_no_flavor(self):
        flavor = "Morango"
        message = f"Não temos no momento {flavor}!"
        result = self.ice_cream_stand.find_flavor(flavor)
        assert result == message

    def test_find_flavor_out_of_stock(self):
        flavor_empty_list = []
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, flavor_empty_list)
        flavor = "Morango"
        message = f"Não temos no momento {flavor}!"
        result = self.ice_cream_stand.find_flavor(flavor)
        assert result == message
        assert ice_cream_stand.flavors == flavor_empty_list

    def test_add_flavor(self):
        new_flavor = "Milho verde"
        message = f"{new_flavor} adicionado ao estoque!"
        result = self.ice_cream_stand.add_flavor(new_flavor)
        assert result == message
        assert new_flavor in self.ice_cream_stand.flavors

    def test_add_flavor_existing_flavor(self):
        flavor = "Delícia de Abacaxi"
        message = "Sabor já disponivel!"
        result = self.ice_cream_stand.add_flavor(flavor)
        assert result == message

    def test_add_flavor_invalid_flavor(self):
        new_flavor_existing = "   "
        message = "Sabor Inválido"
        result = self.ice_cream_stand.add_flavor(new_flavor_existing)
        assert result == message

    def test_validate_flavor_string(self):
        flavor = "Chocolate"
        expected_result = True
        result = self.ice_cream_stand.validate_flavor(flavor)
        assert result == expected_result

    def test_validate_flavor_int(self):
        flavor = 11
        expected_result = False
        result = self.ice_cream_stand.validate_flavor(flavor)
        assert result == expected_result

    def test_validate_flavor_none(self):
        flavor = None
        expected_result = False
        result = self.ice_cream_stand.validate_flavor(flavor)
        assert result == expected_result

    def test_validate_flavor_blank_space(self):
        flavor = "   "
        expected_result = False
        result = self.ice_cream_stand.validate_flavor(flavor)
        assert result == expected_result
