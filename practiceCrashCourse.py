#d = {'key1': [1,2,3]}

#print(d)

#print(d['key1'][0])

# i = 0
# while i < len(d['key1']):
#     print(d['key1'][i])
#     i+=1

# d2 = {'key1':{'innerkey':[1,2,3]}}
# print(d2['key1']['innerkey'][1])

# s = {1,1,1,3,3,5}
# print(s)

# print('hi'!='hi')

# i = 0
# out = [i**2 for i in range(5)]
# print(out)

# def my_func(param1, param2):
#     print('Hello '+ param1 + '. You are age '+param2)

# my_func(param2='22', param1='raquael') #right

# my_func('22', 'raquael') #wrong order

# my_func('raquael','22') #right

##### MAP FUNCTION #####
# def times2(var):
#     return var*2
# seq = [1,2,3,4,5]
# times2_ex = list(map(times2, seq))
# print(times2_ex)

##### LAMBDA FUNCTION - called the "no name" or "no return" function #####
# def times2(var): return var*2 TO lambda >>>
# t = lambda var: var*2
# seq = [1,2,3,4,5]
# print(list(map(lambda var: var*2, seq))) # all printed in one step

##### FILTER FUNCTION - returns only elements in the seq that meets the lambda condition (TRUE) #####
# seq = [1,2,3,4,5]
# print(list(filter(lambda num: num**2 >= 10, seq)))

##### CRASH COURSE EXERCISES #####
# print(7**4)

# s = "Hi there Sam!"
# lst = list(s.split())
# print(lst)

# planet = "Earth"
# diameter = 12742
# print('The diameter of {}, is {} km.'.format(planet, diameter))

# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3][1][2])

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]['tricky'][3]['target'][3])

# def get_domain(email):
#     print(email.split('@')[1])

# get_domain('user@domain.com')

# def findDog(s):
#     if 'DOG' in s.upper():
#         return True
#     else:
#         return False
# print(findDog('Is there a dog here?'))

# def countDog(s):
#     i = 0
#     for word in s.upper().split():
#         if word == 'DOG':
#             i+=1
#     return i

# print(countDog('This dog runs faster than the other dog dude'))

# seq = ['soup','dog','salad','cat','great']
# print(list(filter(lambda x: x[0]=='s', seq)))

# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         speed = speed-5
#     if speed <= 60:
#         return "No Ticket"
#     elif speed >= 61 and speed <= 80:
#         return "Small Ticket"
#     else:
#         return "Big Ticket"

# print(caught_speeding(81, False))

