class Home:
    def new(self, value):
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Аргумент должен быть целым числом.")
