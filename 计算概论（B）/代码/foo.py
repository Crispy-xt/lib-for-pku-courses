


fact5 = (lambda f, x : f (f,x)) (lambda f, x : 1 if x == 0 else x * f (f, x - 1), 5)

print (fact5)
