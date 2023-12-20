import csv
from itertools import product
      
leet_dict = {
        'a': ['@', '4', '/\\', '^', '(L', 'Д', '/-\\', '/~\\', 'à', 'á', 'â', 'ä', 'ã', 'å', 'ā'],
        'b': ['l3', '8', '|3', 'ß', '6', '!3', '(3', '/3', ')3', '|-]', 'j3'],
        'c': ['[', '¢', '{', '<', '(', '©', 'ç', 'ć', 'č'],
        'd': [')', '|)', '(|', '[)', 'l>', '|>','?', 'T)', 'l7', 'cl', '|}', '>', '|]'],
        'e': ['3', '&', '£', '€', '[-', '|=-', 'ë', 'è', 'é', 'ê', 'ē', 'ė', 'ę'], 
        'f': ['|=', 'ƒ', '|#', '/='],
        'g': ['&', '6', '(_+', '9', 'C-', '(?,', '[', '{', '<-', '(.'],
        'h': ['#', '/-/', '[-]', ']-[', ')-(', '(-),', ':-:', '|~|', '|-|', ']~[', '}{', '!-!','1-1', '\\-/', '|+|', '/-\\'],
        'i': ['1', '[]', '|', '!', '][', 'î', 'ï', 'í', 'ī', 'į', 'ì'],             
        'j': [',_|', '_|', '._|', '._]', '_]', ']', ',_]', ';', '1', 'j'],
        'k': ['>|', '|<', '/>', '1>', '|c', '|(', '|{'],
        'l': ['1', '£', '7', '!_', '|_', '|', '!', 'ł'],
        'm': ['/\\/\\', '/V\\', 'JVI', 'JV|', '[V]', '[]V[]', '|\\/|', '^^', '<\\/>', '{V\}', '(V)', '|V|', 'nn', '|\\/|', '|\\|', ']\\/[', '1^1', 'ITI'],
        'n': ['^/', '|\|', '/\\/', '[\\]', '{\\}', '<\\>', '|V', '/V', '^', 'И', 'ท', 'ñ', 'ń', 'n'],
        'o': ['0', 'Q', '()', '[]', 'p', '<>', 'Ø', 'ô', 'ö', 'ò', 'ó', 'ø', 'ō', 'õ'],        
        'p': ['|*', '|o', '|º', '?', '|^', '|>', '|\"', '9', '[]D', '|°', '|7', 'p'],
        'q': ['(_,)', '9', '()_', '2', '0_', '<|', '&', 'Q'],
        'r': ['l2', '|\'', '|?', '/2', '|^', 'lz', '|9', '2', '12', '®', 'Я', '[z', '.-', '|2', '|-'],
        's': ['5', '$', '§', '2', 'z', 's', 'ś', 'š'],   
        't': ['7', '+', '-|-', '\',][\'', '†', '\"|\"', '~|~'],
        'u': ['(_)', '|_|', 'v', 'L|', 'µ', 'บ', 'û', 'ü', 'ù', 'ú', 'ū', 'u'],     
        'v': ['\\/', '|/', '\\|', 'v', 'V'],
        'w': ['\\/\\/', 'VV', '\\N', '\'//', '\\\\\'', '\\^/', '\\V/', '\\X/', '\\|/', '\\_|_/', '\_:_/', 'Ш', 'Щ', 'uu', '2u', '\\\\//\\\\//', 'พ'],
        'x': ['><', '>|<', '}{', '×', ')(', '][', '%'],
        'y': ['j', '`/', 'Ч', '7', '\\|/', '¥', '\\//', 'ÿ'],
        'z': ['2', '7_', '-/_', '%', '>_', '~/_', '-\\_', '-|_', 's', 'z', 'ž', 'ź', 'ż']     
    }

#load the list of words from the common words csv file for faster lookup and make all lowercase
def load_common_words(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return {row[0].lower() for row in reader}

#function to remove selected punctuation characters from the passed word
def remove_punctuation(word):
    punctuation = '!"#$%&\'()*+,-./:;<=>?[\\]^_`{|}~'
    return ''.join(char for char in word if char not in punctuation)

def generate_translations(word, leet_dict):
    def expand_word(word, index=0):
        if index >= len(word):
            return ['']
        
        expanded_words = []
        for length in range(1, min(4, len(word) - index + 1)):  # Check up to 3-character sequences
            subword = word[index:index+length]
            # Find all possible translations for the substring
            translations = []
            for eng_char, leet_symbols in leet_dict.items():
                if subword in leet_symbols:
                    translations.append(eng_char)

            # If the substring is a leetspeak symbol, recurse for the rest of the word
            if translations:
                for rest in expand_word(word, index+length):
                    expanded_words.extend([trans + rest for trans in translations])
            elif length == 1:  # If no translation found, keep the character as is
                for rest in expand_word(word, index+1):
                    expanded_words.append(subword + rest)

        return expanded_words

    return expand_word(word)

#main leetspeak translator algorithm
def leetspeak_to_text(word, leet_dict, common_words):
    #check that word is within bounds
    if len(word)>16:
        return word
    
    #first, check if word is in common words
    if word.lower() in common_words:
        return word

    #if not, translate from leetspeak
    all_translations = generate_translations(word, leet_dict)
    print(all_translations)

    # Check each translation against the common words
    for translation in all_translations:
        if translation.lower() in common_words:
            return translation

    #if translated version is not in common words, remove punctuation
    no_punc = remove_punctuation(word)
    #now check if in list of common words
    if no_punc.lower() in common_words:
        return no_punc
    
    #otherwise translate again with no punctuation and check if in common words
    translated_no_punc = no_punc
    for alpha, leet_list in leet_dict.items():
        for leet in leet_list:
            translated_no_punc = translated_no_punc.replace(leet, alpha)

    if translated_no_punc.lower() in common_words:
        return translated_no_punc

    # If not found, return original word
    return word


#########
#main function for quick testing
# load common words from a CSV file
def caller(word):
    common_words = load_common_words('commonWords.csv')
    leetspeak_to_text(word, leet_dict, common_words)

#input_words = ["@bstract", "3x/-\\mpl3", "1o0k", "C-reat"]
#output_words = [leetspeak_to_text(word, leet_dict, common_words) for word in input_words]

#for original, converted in zip(input_words, output_words):
   # print(f"Original: {original}, Converted: {converted}")


