'''A list is an ordered sequence of objects.'''
my_list = ["a", 10, {"clave": "valor"}]
print(my_list[2]["clave"]) #{'valor'}
print(len(my_list)) #3
print(my_list[::-1]) #[{'clave': 'valor'}, 10, 'a']
print(my_list + my_list)#['a', 10, {'clave': 'valor'}, 'a', 10, {'clave': 'valor'}]
print(my_list * 3) #['a', 10, {'clave': 'valor'}, 'a', 10, {'clave': 'valor'}, 'a', 10, {'clave': 'valor'}]

my_list[2] = {"claveSecreta":"shh"}
print(my_list) # -> Modify index 2
my_list.append("Finish")
print(my_list) # ['a', 10, {'claveSecreta': 'shh'}, 'Finish']
my_list.pop(2) #-> remove an element of the list
print(my_list) # ['a', 10, 'Finish']

list = [5,8,9,6,3,2,1,4,7]
list.sort()
print(list) # [1, 2, 3, 4, 5, 6, 7, 8, 9] -> sort has no return


