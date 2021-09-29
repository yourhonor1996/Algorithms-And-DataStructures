
def set_generator(input_set:set):
    for item in input_set:
        yield item
        
        
a = {1, 2, 3 ,4, 5, 6}
gen = set_generator(a)
# it = iter(a)
print(next(gen))
print(next(gen))
print(next(gen))

