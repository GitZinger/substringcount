def count_kmer(haystack, needle):
    count = 0
    
    # Write your code below this line.
    # YOUR CODE HERE
    for i in range(len(haystack)-len(needle)+1):
        #print(haystack[i:i+len(needle)])
        if haystack[i:i+len(needle)]==needle:
            count+=1
            #print(haystack[i:len(needle)-1])
    
    # Write your code above this line.
    
    return count
