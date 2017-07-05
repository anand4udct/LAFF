# dot product of two vectors x and y, written into y
# please provide inputs in the form -- np.matrix([1,2,3])

def laff_dot(x,y):
    
    sx = x.size; sy = y.size
        
    if (x.shape[0] == 1):              # if x is row vector
        if (y.shape[0] == 1):          # if y is also row vector
            if sx == sy:               # if x,y are of same size
                for i in range(0,sy):
                    y[0,i] = x[0,i] * y[0,i]
                return y
            else:
                print('x,y are row vectors, but of differnt size')                
        else:
            print('x is row vector, but y is not')            
    elif (x.shape[1] == 1):             # if x is column vector
        if (y.shape[1] == 1):           # if y is column vector
            if sx == sy:                # if x,y are of same size
                for i in range(0,sy):
                    y[i,0] = x[i,0] * y[i,0]
                return y
            else:
                print('x,y are column vectors, but of differnt size')                
        else:
            print('x is column vector, but y is not')            
    else:
        print('either x or y is not a vector')         

x = (np.matrix([1,2,3,8,3]))
y = (np.matrix([6,5,4,0]))
print("y = ",laff_dot(x,y))

