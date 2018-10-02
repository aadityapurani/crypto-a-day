def split_str(s,length):
    len_s = len(s)
    arr = [s[i*length:(i+1)*length] for i in range(0,len_s,length)]
    if(len(arr[-1])==0):
        arr.pop()
    return arr