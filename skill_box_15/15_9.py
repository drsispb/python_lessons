'''Задача 9. Анализ слова 2

Продолжите писать анализаторы для текста. Теперь необходимо реализовать код, с помощью
которого можно определять палиндромы. То есть нужно находить слова, которые одинаково читается слева направо и справа налево.
Напишите такую программу.



Пример 1:
Введите слово: мадам
Слово является палиндромом

Пример 2:
Введите слово: abccba
Слово является палиндромом

Пример 3:
Введите слово: abbd
Слово не является палиндромом'''


word = str(input('Введите слово: '))
un_word = ''
for a in word[::-1]:
    un_word += a
if word == un_word:
  print('Слово является палиндромом')
else:
  print('Слово не является палиндромом')