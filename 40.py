# Generate a funcyion with yield: wa generate function that yields even numbers up to a specified limit.
def even_generator(limit):
    for i in range(2 , limit+1, 2):
        yield i
      
for num in even_generator(21):
    print(num)