#Solution 1 (Jackson)
# import re

# characters = 'ThisIsMyWeeklyKata'
# # Splitting text and joining

# words = re.findall('[A-Z][a-z]*', characters)
# # print (words)import re

# characters = 'ThisIsMyWeeklyKata'
# # Splitting text and joining

# words = re.findall('[A-Z][a-z]*', characters)
# # print (words)

# results = ' '.join(words)
# # print (results)

# # getting text to lower case
# lower_case = results.lower()
# # print (lower_case)

# #Splitting 
# splitted = lower_case.split()
# print (splitted)


# def solution(splitted_words):
#     # Reverse each word
#     reversed_words = []
#     for words in splitted_words:
#         reversed_word = words[::-1]
        
#         reversed_words.append(reversed_word)
#     joined_words = ' '.join(reversed_words)
#     print (joined_words)
# solution(splitted_words='ThisIsMyWeeklyKata') 

                #Solution 2
# def solution(splitted_words):
#     # Reverse each word
#     reversed_words = []
#     for words in splitted_words:
#         reversed_word = words[::-1]
        
#         reversed_words.append(reversed_word)
#         print (reversed_words)
# solution('This is my weekly katas')   

                #Solution 3
def solution(S):
    # Split the string into a list of words
    words = S.split()

    # Reverse each word and join them back into a string
#     reversed_string = ' '.join(word[::-1] for word in words)

#     return reversed_string
# solution('This is my weekly katas')
def solution(S):
    # Split the string into words
    words = S.split()
    
    # Reverse each word and join them with spaces
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string
solution('This is my weekly kata')