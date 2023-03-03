from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        """
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        - MELHORIA: O FOR foi retirado, para poder ser retornado a lista inteira com os sabores ao invés de printar 
                    diretamente no método..
        """
        if self.flavors:
            return self.flavors
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        """
        - BUG: O retorno estava retornando todos os sabores, para resolver o defeito o self.flavors foi substituido pelo
               flavor criado no IF
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        - MELHORIA: Foi removido o if self.flavors porque o método deve verificar se existe o sabor pesquisado e não se 
                    existe estoque.        
        """
        if flavor in self.flavors:
            return f"Temos no momento {flavor}!"
        else:
            return f"Não temos no momento {flavor}!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""

        """
        - MELHORIA: Não existe validação para saber se o flavor é um nome válido. Para resolver o defeito, foi criado o método
               validate_flavor e adicionado um IF para realizar essa validação.
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        """
        if self.validate_flavor(flavor):
            if flavor in self.flavors:
                return "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Sabor Inválido"

    def validate_flavor(self, flavor):
        """Valida se o nome do sabor é string, se não está vazio ou se não é apenas espaços em branco"""

        if (type(flavor) == str) and (flavor is not None) and (len(flavor.strip()) > 0):
            return True
        return False
