def maxRepeatingOn2(str): 
    l = len(str) 
    count = 0
    res = str[0]
    # print(res)
    for i in range(l):           
        cur_count = 1
        for j in range(i + 1, l): 
            if (str[i] != str[j]): 
                break
            cur_count += 1
        if cur_count > count : 
            count = cur_count 
            res = str[i] 
    return res     

def maxRepeating(str): 
  
    n = len(str) 
    count = 0
    res = str[0] 
    cur_count = 1
  
    # Traverse string except  
    # last character 
    for i in range(n): 
          
        # If current character  
        # matches with next 
        if (i < n - 1 and str[i] == str[i + 1]): 
            cur_count += 1
  
        # If doesn't match, update result 
        # (if required) and reset count 
        else: 
            if cur_count > count: 
                count = cur_count 
                res = str[i] 
            cur_count = 1
    return res 

if __name__ == "__main__":
    string = "saa"
    print("Max occurring " + maxRepeating(string))

    # print(getMax('daniel'))