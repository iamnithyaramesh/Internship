with open('Portal Script.txt','r') as f:
    data=f.readlines()
    l=[]
    for i in data:
        j=i.strip()
        if j.startswith('<td>') and j[4] in '0123456789':
                 l.append(j[4:10])
    print(l[:6])
                 
          
           
            
