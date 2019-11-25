
def bisection(fun,a,b,x):
    x = (a + b) / 2
    return x

def goldenratio(fun,a,b,x):
    if abs(fun(a))>=abs(fun(b)):
        x=a+0.618*(b-a)
    else:
        x=a+0.382*(b-a)
    return x

class methtype:
    BISECTION = 1
    GOLDEN_RATION = 2


def nonlinequation(fun , a , b , eps , method = methtype.BISECTION):

    if method == methtype.BISECTION:
        method=bisection
    if method == methtype.GOLDEN_RATION:
        method=goldenratio

    if fun(a)*fun(b) >0:
        print("There is no roots on interval [{}:{}]".format(a,b))
        return None
    else:
        x,n=0,0

        while True:

            x=method(fun,a,b,x)
            if fun(x) * fun(a) <= 0:
                b = x
            else:
                a = x
            n+=1
            delt = abs(b-a)
            print("{}. Error = {}".format(n,delt))
            if delt < eps:
                break

    print("Answer = {} , Loops = {}".format(x,n))
    return x



