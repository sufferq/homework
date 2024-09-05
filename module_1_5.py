immutable_var = 1, 2, 3, 'string', 'a', 'b'
print (immutable_var)
#immutable_var[0] = 5
#TypeError: 'tuple' object does not support item assignment
# Кортеж нельзя изменить потому что он не изменяем.
mutable_list = ['carrot', 'potato', 'tomato']
print (mutable_list)
mutable_list [0] = 'cucumber'
print (mutable_list)
mutable_list.append ('car',)
print (mutable_list)