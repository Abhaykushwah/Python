# dict init
my_dict = {'x':500, 'y':5874, 'z': 560}

# finding the key of min and Max value
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

## printing result
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])
