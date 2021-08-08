def largest_palindrome_num(digits):
    palindromes = []
    for num1 in range(int('9'*digits)+1):
        for num2 in range(int('9'*digits)+1):
            product = str(num1 * num2)

            if len(product) % 2 == 0:
                mid = int(len(product)/2)
                if product[:mid][::-1] == product[mid:]:
                    palindromes.append(int(product))
            else:
                mid = int(len(product)/2)
                if product[:mid-1][::-1] == product[mid+1:]:
                    palindromes.append(int(product))

    return max(palindromes)

print(largest_palindrome_num(3))
