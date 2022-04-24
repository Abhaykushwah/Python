#code 1

person={'name':'Henry','age':19}
age =person.setdefault('age')
print('person =',person)
print('Age = ',age)

#code 2
person={'name':'Henry'}
salary =person.setdefault('salary')
print('person =',person)
print('Salary = ',salary)