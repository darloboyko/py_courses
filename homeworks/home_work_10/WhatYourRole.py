#2. Есть некая система, где есть списки пользователей.
#roles = {
#  'admin' = [...],
# 'maintainer' = [...],
#  'manager' = [...],
# 'developer' = [...],
#}
#При вводе имени необходимо проверить, к какой роли относится этот человек и вывести сообщение вида:
#"Hello, <role>"
#Если имени нет в списках, вывести:
#"Hello, Guest"
user_name = str(input("Enter you name: "))

roles = {
  'admin' : ['Alex', 'Ben', 'Bob'],
  'maintainer' : ['Nik', 'Pol'],
  'manager' : ['Pedro', 'Ron'], 
  'developer' : ['Tuk', 'Gek', 'Kuk']
}
for k, v in roles.items():
    for i in v:
        if i == user_name:
          print(f"Hello, {k}")
          break
        


 
       
       


            

        
      





