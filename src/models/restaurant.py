class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        - MELHORIA: title() coloca todas as primeiras letras, tornando o nome do restaurante diferente do nome inserido,
                    por isso foi removido.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        """
        - BUG: O método está exibindo o tipo da comida em dois pontos. Para resolver o defeito, o primeiro 
               {self.cuisine_type} foi substituido por {self.restaurant_name}
        - BUG: A mensagem de retorno está errada. Pra resolver o defeito, a palavra "and" foi substituida por "e" e 
               a palavra "restaturante" por "restaurante"
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        """

        return(f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.\nEsse restaurante está "
               f"servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""

        """
        - BUG: O restaurante está sendo instanciado como fechado, para resolver o defeito o self.open fica como True
        - BUG: A quantidade de consumidores servidos está iniciando negativa, para resolver o defeito o number.served 
               fica como 0
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        """
        if not self.open:
            self.open = True
            self.number_served = 0
            return(f"{self.restaurant_name} agora está aberto!")
        else:
            return(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""

        """
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        """
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        """
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        - MELHORIA: Não havia validação se o total_customers era um número válido. Então foi criado um método para 
                    realizar essa validação.
        - MELHORIA: A quantidade de number_served não era retornada. Agora essa quantidade é retornada.
        """
        if self.validate_number(total_customers) and self.open:
            self.number_served = total_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""

        """
        - BUG: O more_costumers estava substituindo o valor total. Para resolver o defeito, agora o number_served está 
               somando o seu valor com o more_customers
        - MELHORIA: As mensagens estão sendo "printadas" diretamente no método. Agora as mensagens passam a ser
                    retornadas pelo método.
        - MELHORIA: A quantidade de number_served não era retornada. Agora essa quantidade é retornada.
        """
        if self.validate_number(more_customers) and self.open:
            self.number_served += more_customers
            return self.number_served
        else:
            return f"{self.restaurant_name} está fechado!"

    def validate_number(self, value):
        """Valida se o valor passado é maior que zero, se é um inteiro e se não é NONE."""
        if type(value) is int and value > 0 and value is not None:
            return True
        return False
