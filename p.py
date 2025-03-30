def greeting(name="user"):
    print("hello",name ,"\nNice to meet you")

greeting()
greeting("Saanvi")


def factorial(n):
    if (n==1):
        return 1
    
    return n* factorial(n-1)

print(factorial(2))

def factorial_using_loop(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    return pro
print("the factorial obtained using loop:",factorial_using_loop(5))
print("the factorial obtained using recursion:",factorial(5))
    