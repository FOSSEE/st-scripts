from find_gcd import gcd

if __name__ == '__main__':
    for line in open('testcases.txt'): 
        numbers = line.split() 
        x, y = int(numbers[0]) , int(numbers[1]) 
        result = int(numbers[2]) 
        if gcd(x, y) != result: 
            print "Failed gcd test for", x, y 
        else: 
            print "Test passed", result                                        