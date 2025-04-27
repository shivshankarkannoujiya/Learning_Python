"""
    String: "", '', """ """
"""

chai = "Masala Chai"
print(chai)


# TODO: get the first char
first_char = chai[0]
print(first_char)


# TODO: Slicing: get the `Masala`
slice_chai = chai[0: 6]
print(slice_chai)


num_list = "0123456789"

#TODO: get whole list: [:] => 0123456789
whole_list = num_list[:]
print(whole_list)


#TODO: get from 3 => last elements[3:]
print(num_list[3:])

# TODO: 0 => 6
print(num_list[0:7])
print(num_list[:7])


#TODO: Hopping: hop by 1 number
print(num_list[0:7:2])

#TODO: Hopping: hop by 2 number
print(num_list[0:7:3])
