from collections import defaultdict 
MAX_CHARS = 256

def substring(str): 
    n = len(str)  
    dist_c1 = len(set([x for x in str])) 
    c1=0
    start=0
    start_ind=-1
    mlen=100000
    curr_c1 = defaultdict(lambda:0) 
    for j in range(n): 
        curr_c1[str[j]] += 1
  
        if curr_c1[str[j]] == 1: 
            c1 += 1 
  
        if c1 == dist_c1: 
            while curr_c1[str[start]] > 1: 
                if curr_c1[str[start]] > 1: 
                    curr_c1[str[start]] -= 1
                start += 1
   
            len_window = j - start + 1
            if mlen > len_window: 
                mlen = len_window 
                start_ind = start
                
    return str[start_ind: start_ind + mlen] 
      
if __name__=='__main__':
    a=input()
    print(len(substring(a))) 
