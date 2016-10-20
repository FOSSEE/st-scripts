def gcd(a, b):
    if b==0:
       return a
    return gcd(b, a%b)

#if __name__ == '__main__':
#     result = gcd(48, 64)
#     if result!= 16:
#         print "Test failed"
#     print "Test Passed"



#if __name__ == '__main__':
#    for line in open('testcases.txt'):
#        numbers = line.split()
#        x = int(numbers[0])
#        y = int(numbers[1])
#        result = int(numbers[2])
#       	if gcd(x, y) != result:
#            print "Failed gcd test for", x, y
#        else:
#            print "Test passed" , result


