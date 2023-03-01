def sayNumber(num):
    # Define dictionaries to map integer values to words
    ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens_multi = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
                          7: 'seventy', 8: 'eighty', 9: 'ninety'}
    scale_dict = {100: 'hundred', 1000: 'thousand', 1000000: 'million',
                  1000000000: 'billion', 1000000000000: 'trillion',
                  1000000000000000: 'quadrillion', 1000000000000000000: 'quintillion'}
 
    if num < 0 or num > 999999999999999:
        return "Number out of range!"
    elif num < 10:
        return ones[num]
    elif num < 20:
        return tens[num]
    elif num < 100:
        tens = tens_multi[num // 10]
        ones = ones[num % 10]
        return tens + " " + ones if ones != 'zero' else tens
    else:
        for scale in sorted(scale_dict.keys(), reverse=True):
            if num >= scale:
                word = sayNumber(num // scale) + " " + scale_dict[scale]
                remainder = num % scale
                if remainder > 0:
                    word += " and " + sayNumber(remainder)
                return word.strip()
 
        # If the number is greater than or equal to 100 but doesn't match any of the scales,
        # then it must be in the range 100-999.
        hundreds = ones[num // 100] + " " + scale_dict[100]
        tens = sayNumber(num % 100)
        return hundreds + " and " + tens if tens != 'zero' else hundreds

# # Prompt user to enter a number
numeral = int(input("Enter a number (0-999,999,999,999,999): "))
print(sayNumber(numeral))


# Option 1 :  test suite for your solution.
# if number is 5 the function sayNumber should return 'five'
# Test if the function give the correct output 
# Answer should be five 
def test_sayNumber():
    answer = sayNumber(5)
    if answer == 'five': 
        print('Test Passed')
    else: 
        print('Test Failed')


# Option 2: Test using tesing framework 
def test2_sayNumber():
    assert sayNumber(789) == 'seven hundred and eighty nine'
    assert sayNumber(54321) == 'fifty four thousand three hundred and twenty one'

test_sayNumber() 
test2_sayNumber()