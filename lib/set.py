def first_repeated_value(list):
    number_set = set()
    for i in range (0, len(list)):
        # for j in range(i+1, len(list)):
            # if list[i]==list[j]:
            if list[i] in number_set:
                return list[i]
            number_set.add(list[i])    
    return None

print(first_repeated_value([1,2, 4, 3, 4, 3]))