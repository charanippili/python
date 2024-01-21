class company:
    company_name = "Apple"     #class variable
    company_code = 500000
    def __init__(self,location):
        self.location = location  #instance variable
        company.company_code += 10

    def statement(self):
        print(f"{self.company_name}-{self.company_code} is located in {self.location}")

a = company("hyderabad")
a.statement()

b = company("banglore")
b.company_name="google"
b.statement()

        
        
