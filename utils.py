import  time
import  numpy as  np

def performance(f):
    def fn(*args,**kw):
        t_start=time.time()
        r=f(*args,**kw)
        t_end=time.time()
        print('call %s() in %fs'%(f.__name__,t_end-t_start))
        return  r
    return  fn

@performance
def  random_array(array_len):
    array_len=int(array_len)
    return  np.random.randint(array_len,size=array_len)