# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:16:26 2024

@author: User
"""

class Person:
    def __init__(self, first_name, last_name, age, email, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_day = birth_day

    @property
    def birth_day(self):
        return self._birth_day

    def get_info(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}, Email: {self.email}, Tug'ilgan kun: {self.birth_day}"
    
    def get_life_path_number(self):
        day, month, year = self.birth_day
        
        def reduce_to_single_digit(n):
            while n > 9:
                n = sum(int(digit) for digit in str(n))
            return n
        
        day_sum = reduce_to_single_digit(day)
        month_sum = reduce_to_single_digit(month)
        year_sum = reduce_to_single_digit(year)
        
        life_path_number = reduce_to_single_digit(day_sum + month_sum + year_sum)
        return life_path_number

    def get_info_by_number(self, number):
        try:
            with open('life_path_info.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(f"#{number}"):
                        return line.strip().split("#")[1].strip()
        except FileNotFoundError:
            return "Fayl topilmadi."
        return "Ma'lumot topilmadi."

# Foydalanuvchidan ma'lumotlarni olish
first_name = input("Ismingizni kiriting: ")
last_name = input("Familiyangizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
email = input("Emailingizni kiriting: ")
birth_day = tuple(map(int, input("Tug'ilgan kuningizni kiriting (kun, oy, yil formatida): ").split(',')))

# Person obyekti yaratish
person = Person(first_name, last_name, age, email, birth_day)

# Foydalanuvchi haqida ma'lumotni chiqarish
print("\nKishi haqida ma'lumotlar:")
print(person.get_info())

# Life path number ni hisoblash
life_path_number = person.get_life_path_number()
print(f"\nSizning life path number: {life_path_number}")

# Life path number ga mos maslahatni chiqarish
print("\nSizning life path number ga mos ta'rif:")
print(person.get_info_by_number(life_path_number))
