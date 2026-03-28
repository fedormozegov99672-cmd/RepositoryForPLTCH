# TODO Найдите количество книг, которое можно разместить на дискете
from symtable import Symbol

Volume_МB = 1.44 # Объем памяти в Мегабайтах
Volume_KB = Volume_МB * 1024 # Объем памяти в Килобайтах
Volume_Byte = Volume_KB * 1024 # Объем памяти в Байтах
Pages = 100 # Количество страниц в книге
Strings = 50 # Количество строк на странице
Symbols = 25 # Количество символов в строке
Symbols_Weight = 4 # Вес одного символа

Symbols_in_Book = Symbols * Strings * Pages # Количество символов в одной книге
Book_Weight = Symbols_Weight * Symbols_in_Book
Book_Amount = int(Volume_Byte // Book_Weight)
print("Количество книг, помещающихся на дискету:", Book_Amount)
