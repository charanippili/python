class company:
    company_name = 'apple'
    def data(self):
        print(f"{self.name} works in {self.company_name}")
        
    @classmethod
    def changename(self, newname):
        self.company_name = newname

a = company()
a.name = "charan"
a.data()

a.changename("google")
a.data()

print(company.company_name)
