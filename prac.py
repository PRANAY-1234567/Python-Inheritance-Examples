'''
class Product:
    def __init__(self, Product_name, Brand, Price):
        self.p = Product_name
        self.b = Brand
        self.price =Price

    def Data(self):
        print(f'Product Name {self.p}\n'
              f'Brand Name {self.b}\n'
              f'Total Amount {self.price}')

class Product_Data(Product):
    def __init__(self, Product_name, Brand, Price,Total_Product, loc):
        super().__init__(Product_name, Brand, Price)
        self.Total_Product = Total_Product
        self.loc =loc

    def Data(self):
        super().Data()
        print(f'Total Product {self.Total_Product}\n'
              f'Current ocation is {self.loc}')
        
e=Product_Data("Laptop", "ASUS",60000,123,"Yavatmal")
e.Data()
'''

'''
class Hospital:
    def __init__(self, Hospital_name, P_Name, d_name):
        self.h = Hospital_name
        self.p = P_Name
        self.d= d_name

    def Hospital_Data(self):
        print(f'Hospital Name is {self.h}\n'
            f'Patient Name is {self.p}\n'
            f'Doctor Name is {self.d}')

class Hospital_Bill(Hospital):
    def __init__(self, Hospital_name, P_Name, d_name, ICU_Bill, Normal_Bill, Total_Bill):
        super().__init__(Hospital_name, P_Name, d_name)
        self.i = ICU_Bill
        self.n = Normal_Bill
        self.t = Total_Bill

    def Hospital_Data(self):
        super().Hospital_Data()
        print(f'Total Hospital is {self.t}\n'
              f'Total Normal Bill {self.n}\n'
              f'Total ICU Bill {self.i}')

h=Hospital_Bill("ABC", "Parag", "Harsh", 123432, 6000, 1200000)
h.Hospital_Data()
'''
