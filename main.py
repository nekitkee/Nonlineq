
from input import *
from nonlineq import nonlinequation , methtype

nonlinequation(fn, a, b, eps1, methtype.BISECTION)
nonlinequation(fn, a, b, eps1, methtype.GOLDEN_RATION)

nonlinequation(fn, a, b, eps2, methtype.BISECTION)
nonlinequation(fn, a, b, eps2, methtype.GOLDEN_RATION)




