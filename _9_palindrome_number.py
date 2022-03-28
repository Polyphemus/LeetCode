# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Seems I did this one in JS

""""
var isPalindrome = function(x) {
    if (x < 0){
        return false;
    }
    y = x.toString();
    for (var i = 0; i < Math.ceil(y.length/2); i++){
        if (y[i] !== y[y.length - 1 - i]){
            return false;
        }
    }
    return true;
};
"""