class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children

  def get_net_salary(self):
    tax = self.salary * 0.15 - self.children * 1500
    tax = int(tax)
    net_salary = self.salary - tax
    return (f"{self.name} má čistou mzdu ve výši {net_salary} Kč")

frantisek = Employee("František Novák", "sklář", 25000, 3)

print (frantisek.get_net_salary())