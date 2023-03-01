## Write a report that specifies and justifies the worst-case space complexity of your solution

The worst-case space complexity of the sayNumber function is O(N), where N is the number of digits in the input number.

In the worst case, the input number is 999,999,999,999,999, which has 15 digits. In this case, the function will need to create a string representation of the entire input number, which will require O(N) space.

The function also creates several lists and dictionaries to store mappings between numbers and their corresponding words. However, the size of these lists and dictionaries is fixed and does not depend on the size of the input number. Therefore, their space complexity is constant, O(1).

In summary, the worst-case space complexity of the sayNumber function is O(N), where N is the number of digits in the input number. However, since the input number is limited to a maximum of 15 digits, the actual space used by the function is also limited and is unlikely to cause memory issues on modern computers.