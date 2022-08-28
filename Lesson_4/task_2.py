user_input = int(input('Enter your number: '))
elements_to_operate = []
index_of_max = 0
addition = 1
max_1 = 0
number_of_biggest_element = 0

while user_input != 0:
    if user_input > max_1:
        max_1 = user_input

    elements_to_operate.append(user_input)
    user_input = int(input('Enter your number:'))
    #elements_to_operate.append(user_input)

for i in range(1, len(elements_to_operate)):
    if elements_to_operate[i] > elements_to_operate[index_of_max]:
            index_of_max = i
for x in elements_to_operate:
    addition = addition * x
for c in range(len(elements_to_operate)):
    if elements_to_operate[c] == max_1:
        number_of_biggest_element += 1




#- кількість введених чисел (завершальний 0 не рахується)
print('Number of elements', len(elements_to_operate))
#- їхню суму
print('Sum: ', sum(elements_to_operate))
#- добуток
print('Multiplication : ', addition)
#- середнє арифметичне (крім завершального числа 0)
print('Average: ', sum(elements_to_operate)/len(elements_to_operate))
#- Визначити значення та порядковий номер найбільшого елемента послідовності. Якщо найбільших елементів є кілька,виведіть порядковий номер першого з них. Нумерація елементів починається з 1 (однини)
print('Biggest elemen: ', elements_to_operate[index_of_max], ' His Index: ', index_of_max)
#- визначити кількість парних та непарних елементів у послідовності
print('кількість парних', sum(1 for x in elements_to_operate if x % 2 == 0))
print('кількість парних та непарних', sum(1 for x in elements_to_operate if x % 2 != 0))
#- Визначити значення другого за величиною елемента в цій послідовності
print('Значення другого за величиною елемента: ', max(elements_to_operate)-1)
#- визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
print('Кiлькiсть елементiв дорівнюють найбільшому елементу: ', number_of_biggest_element)


