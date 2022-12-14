import random
from typing import List


def read_file(file_name):
    '''
    opens and reads selected file
    '''
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    '''
    takes in user input
    '''
    return input('Guess the missing letter: ')


def ask_file_name():
    '''
    asks user if user would like to use different text files and searches for it 
    '''
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    '''
    takes a random letter from the word and takes it out the word
    '''
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word

######################################################################################
# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    '''
    gets a random word from the list
    takes the random letter and every letter besides the 
    selected letter gets replaced by an underscore
    '''
    ranword = list(word)

    
    letter = random.randint(0 , len(ranword)-1)
    
    i = 0    
    while i <= len(ranword)-1 :
        if i != letter :
            ranword[i] = "_"           
        i +=1
    yourword = "".join(ranword)
    
    return yourword    
######################################################################################

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    '''
    checks if any letters are still missing
    '''
    if char in original_word and char not in answer_word:
        return True
    return False 


######################################################################################
# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    '''
    loops through the word and replaces underscore letter if it matches
    '''
    answer= list(answer_word)
    i = 0 
    while i <= len(answer_word) -1 :
        if original_word[i] == char:
            answer[i] = char
        i += 1
    CompleteWord = "".join(answer)
    return CompleteWord

def do_correct_answer(original_word, answer, guess):
    '''
    prints the word after the check process
    '''
    answer = fill_in_char(original_word, answer, guess)

    print(answer)
    return answer

######################################################################################

######################################################################################
# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    '''
    if the user gets it wrong this function is called
    '''
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses) 
######################################################################################
# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    '''
    creates a stick man for the game based on amount of guesses left
    '''
    if number_guesses == 4:
        print("/----\n", "|\n" * 4, "_______", sep="")
    elif number_guesses == 3:
        print("/----\n", "|   0\n", "|\n" * 3, "_______", sep="")
    elif number_guesses == 2:
        print("/----\n", "|   0\n", "|  /|\\\n", "|\n" * 2, "_______", sep="")
    elif number_guesses == 1:
        print("/----\n", "|   0\n", "|  /|\\\n", "|   |\n", "|\n" * 1, "_______", sep="")
    elif number_guesses == 0:
        print("/----\n", "|   0\n", "|  /|\\\n", "|   |\n", "|  / \\\n", "_______", sep="")

# TODO: Step 2 - update to loop over getting input and checking until whole word guess
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    '''
    runs the game and goes through a loop if the
     answer is correct the program break 
     if the user tries to quit the game will break and stop
    Depending on users amount OF guesses certain actions will take place   
    '''
    number_guesses = 5
    print("Guess the word: " + answer)
    while answer != word :
        guess = get_user_input()
        if guess == 'exit' or guess == 'quit':
            print("Bye!")
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_guesses -= 1
            do_wrong_answer(answer, number_guesses)
        if number_guesses == 0:
            print(f"Sorry, you are out of guesses. The word was: {word}")
            break    
    

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

