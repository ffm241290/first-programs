from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import os
import sys
import subprocess


def main ():
      
    try : 
        print("""\nWelcome, here you can find out how many times a word appears in a  text file 
and the most frequent word.""")
        print()
        book_inp = input('Please enter the name of the file (new_testament.txt) or (book_of_mormon.txt): ')           
        book_inp = book_inp.lower()
        stop_words = set(stopwords.words('english'))
        stop_words.add('ye')
        stop_words.add('said')
        stop_words.add('thou')
        stop_words.add('things')
        stop_words.add('one')
        stop_words.add('also')
        stop_words.add('hath')
        with open(book_inp,'rt') as txt_file:
        
            list = []
            for word in txt_file:
                word = word.lower()
                word = word.replace('&','')
                word = word.replace('$','')
                word = word.replace('#','')
                word = word.replace(".","")
                word = word.replace(",","")
                word = word.replace(":","")
                word = word.replace(';','')
                word = word.replace("\"","")
                word = word.replace("!","")
                word = word.replace('¡','')
                word = word.replace("*","")
                word = word.replace('?','')
                word = word.replace('¿','')
                word = word.replace('(','')
                word = word.replace(")","")
                word = word.strip().split()
                list.append(word)

            final_list = []
            for j in list : 
                for n in j:
                    if not n in stop_words:
                        final_list.append(n)
            print()
            if book_inp == 'new_testament.txt' : 
                word_inp = input('Please enter a word from the New Testament: ')
                book_string = 'New Testament'
    
            if book_inp == 'book_of_mormon.txt' :
                word_inp = input('Please enter a word from the Book of Mormon: ')
                book_string = 'Book of Mormon'

            else : 
                word_inp = input('Please enter a word from the text file: ')
                book_string = 'Text File'
    
            quantity = input('Please enter a number to print the number most frequent word: ')
            quantity = int(quantity)
            word_inp = word_inp.lower()
            count_word = get_word(final_list,word_inp)
            most_comm = get_most_common(final_list,quantity)
            print(f'\nThe word {word_inp} appears {count_word} times in the {book_string}')
            print(f'\nThe {quantity} most frequent word in the {book_string} is: {most_comm}')
            

    except FileNotFoundError as file_not_found : 
        print()
        print(type(file_not_found).__name__,file_not_found, sep=': ')
        print(f'The file {book_inp} does not exist.')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    except ValueError as value_error : 
        print()
        print(type(value_error).__name__,value_error, sep=': ')
        print('You must enter an integer number')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

def get_word(list,word):
    counter = Counter(list)
    count = counter.get(word)
    return count

def get_most_common(list,quantity):
    counter = Counter(list)
    count = counter.most_common(quantity)
    return count
        

        
if __name__ == '__main__':          
    main()