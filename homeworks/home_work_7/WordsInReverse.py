#5. Написать программу, которая вернет строку со словами в обратном порядке
#Например: "The greatest victory is that which requires no battle"
#Ответ: "battle no requires which that is victory greatest The"
#Строку ввести с клавиатуры

s = input("Enter string: ").replace('"', "").split()[::-1]
s_lst =' '.join(str(i) for i in s)
print(f'"{s_lst}"')