def gcd(a, b):
    if a%b==0:
       return a
    return gcd(b, a%b)

#if __name__ == '__main__':
#     result = gcd(48, 64)
#     if result != 16:
#         print "Test failed"
#     print "Test Passed"

