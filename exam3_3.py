class Rectangle:
    def init(self):
        self.lenght = 1
        self.width = 1

    def set_width(self, width):
        self.width = width

    def set_length(self, lenght):
        self.lenght = lenght

    def get_width (self):
        return self.width

    def get_lenght(self):
        return self.lenght


    def get_area(self):
        return self.lenght * self.width

    @property
    def show_info(self):
        return f'lenght = {self.lenght}, width = {self.width}, area = {self.get_area()}'

        
my_rect = Rectangle()
my_rect.set_length(5)
my_rect.set_width(3)
print(my_rect.show_info)