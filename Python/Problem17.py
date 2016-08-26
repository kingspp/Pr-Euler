"""
@Created on: 25/08/16,
@author: Prathyush SP

"""
import time

start = time.time()

num_word_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                 90: 'Ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred',
                 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred',
                 0: ''}


def number_to_word(n):
    try:
        return num_word_dict[n]
    except KeyError:
        try:
            if len(str(n)) == 2:
                return num_word_dict[n - n % 10] + num_word_dict[n % 10].lower()
            elif len(str(n)) < 4:
                words = num_word_dict[n - n % 100] + 'and'
                if n % 100 in range(11, 21):
                    return words + num_word_dict[n % 100]
                else:
                    words += num_word_dict[n % 100 - (n % 10)]
                    words += num_word_dict[n % 10].lower()
                return words
        except KeyError:
            print('Number out of range: ', len(str(n)))


print(sum([len(number_to_word(number)) for number in range(1, 1000)]) + len('onethousand'))

end = time.time()
print('Elapsed test: ' + str(end - start) + 's')
