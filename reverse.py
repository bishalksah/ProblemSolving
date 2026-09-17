

# enter a sentence and count the letter in the sentence and print the letter with their count in the sentence

sentence = input("Enter a sentence: ")
letter_count = {}
for ch in sentence:
    if ch in letter_count:
        letter_count[ch] += 1
    else:
        letter_count[ch] = 1
for letter, count in letter_count.items():
    print(f"'{letter}': {count}")

print(letter_count)

def firstmost_frequent_letter(letter_count):
    if letter_count:
        max_count = max(letter_count.values())
        firstmost_frequent = [letter for letter, count in letter_count.items() if count == max_count]
    return firstmost_frequent, max_count

print(firstmost_frequent_letter(letter_count))
print("The firstmost frequent letter is:", firstmost_frequent_letter(letter_count)[0], "with a count of:", firstmost_frequent_letter(letter_count)[1])



def secondmost_frequent_letter(letter_count):
    if letter_count:
        secondmax_count = max(count for count in letter_count.values() if count < max(letter_count.values()))
        second_most_frequent = [letter for letter, count in letter_count.items() if count == secondmax_count]
    return second_most_frequent, secondmax_count

print(secondmost_frequent_letter(letter_count))
print("The second most frequent letter is:", secondmost_frequent_letter(letter_count)[0], "with a count of:", secondmost_frequent_letter(letter_count)[1])      


def lastmost_frequent_letter(letter_count):
    if letter_count:
        lastmax_count = min(letter_count.values())
        last_most_frequent = [letter for letter, count in letter_count.items() if count == lastmax_count]
    return last_most_frequent, lastmax_count

print (lastmost_frequent_letter(letter_count))
print("The last most frequent letter is:", lastmost_frequent_letter(letter_count)[0], "with a count of:", lastmost_frequent_letter(letter_count)[1])

def secondlastmost_frequent_letter(letter_count):
    if letter_count:
        secondlastmax_count = min(count for count in letter_count.values() if count > min(letter_count.values()))
        secondlast_most_frequent = [letter for letter, count in letter_count.items() if count == secondlastmax_count]
    return secondlast_most_frequent, secondlastmax_count   

print(secondlastmost_frequent_letter(letter_count))
print("The second last most frequent letter is:", secondlastmost_frequent_letter(letter_count)[0], "with a count of:", secondlastmost_frequent_letter(letter_count)[1])    





#1 distinct letters in a sentence 







#2 count of distinct letter in a sentence
 