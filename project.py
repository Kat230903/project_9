import csv
def func_pinakas(list31):
    """
    Eκτυπώνει το ταμπλό του παιχνιδιού
    >>> list31=[[A|,    |,    |,    |,    |,    |],[B|,    |,    |,    |,    |,    |],[C|,    |,    |,    |,    |,    |],[D|,    |,    |,    |,    |,    |],[E|,    |,    |,    |,    |,    |]]
    >>> ar='   1    2    3    4    5'
    >>> ar2='--------------------------'
    >>> func_pinakas(list31)
      1    2    3    4    5
   --------------------------
   A|    |    |    |    |    |
   B|    |    |    |    |    |
   C|    |    |    |    |    |
   D|    |    |    |    |    |
   E|    |    |    |    |    |
   --------------------------

    """
    print('   '+ar+'\n'+ar2)
    y=''
    for i in range(0,len(list31),1):
        for j in range(0,len(list31[i]),1):
            y+=str(list31[i][j])
        if i!=len(list31)-1:
            y+='\n'
    print(y)
    print(ar2)
    return
def func_check(pioni,paiktis,i,j,list31):
    """
    Ελέγχει αν υπάρχει συνεχόμενη τετράδα κάθετα και αν συνορεύουν επιπλέον πίονια προς την διεύθυνση
    σχηματισμού της τετράδας, σημειώνει τα πιόνια, εμφανίζει τον ανανεομένο πίνακα και πραγματοποιεί ολίσθηση
    >>> list31=[[A|,    |,    |,    |,    |,    |],[B|,  O |,    |,    |,    |,    |],[C|,  O |,    |,    |,    |,    |],[D|,  O |,    |,    |,    |,    |],[E|,  O |,  X |,  X |,  X |,    |]] 
    >>> i,j=1,1
    >>> pioni='  O |'
    >>> paiktis=0 #pontoi1
    >>> ar='   1    2    3    4    5'
    >>> ar2='--------------------------'
    >>> func_check(pioni,paiktis,i,j,list31)
       1    2    3    4    5
    --------------------------
    A|    |    |    |    |    |
    B|  * |    |    |    |    |
    C|  * |    |    |    |    |
    D|  * |    |    |    |    |
    E|  * |  X |  X |  X |    |
    --------------------------
    """
    if list31[i+1][j]==pioni and list31[i+2][j]==pioni and list31[i+3][j]==pioni:
        list31[i][j]='  * |'    
        list31[i+1][j]='  * |'
        list31[i+2][j]='  * |'
        list31[i+3][j]='  * |'
        flag=True
        paiktis+=4
        keno=False
        edw=i+3
        pos=i+4
        while not keno and pos<=len(list31)-1:
            if list31[pos][j]==pioni:
                edw=pos
                paiktis+=1
                list31[pos][j]='  * |'
            else:
                keno=True
            pos+=1
        pos=i-1#εδώ αρχίζει η ολίσθηση
        func_pinakas(list31)
        keno=False
        while not keno and pos>=0:
            if list31[pos][j]!='    |':
                list31[pos+(edw-pos)][j]=list31[pos][j]
                list31[pos][j]='    |'
            else:
                keno=True
            pos-=1
        for y in range(i,edw+1,1):
            if list31[y][j]=='  * |':
                list31[y][j]='    |'
        list31.append(paiktis)
        list31.append(flag)
        return list31
    return 
def func_check2(pioni,paiktis,i,j,list31):
    """
    Ελέγχει αν υπάρχει συνεχόμενη τετράδα οριζόντια και αν συνορεύουν επιπλέον πίονια προς την διεύθυνση
    σχηματισμού της τετράδας, σημειώνει τα πιόνια, εμφανίζει τον ανανεομένο πίνακα και πραγματοποιεί ολίσθηση
    >>> list31=[[A|,    |,    |,    |,    |,    |],[B|,    |,    |,    |,    |,    |],[C|,    |,    |,    |,    |,    |],[D|,  X |,  X |,  X |,    |,    |],[E|,  O |,  O |,  O |,  O |,    |]]
    >>> i,j=4,1
    >>> pioni='  O |' 
    >>> paiktis=1 #pontoi1
    >>> sthles=5
    >>> ar='   1    2    3    4    5'
    >>> ar2='--------------------------'
    >>> func_check2(pioni,paiktis,i,j,list31)
       1    2    3    4    5
    --------------------------
    A|    |    |    |    |    |
    B|    |    |    |    |    |
    C|    |    |    |    |    |
    D|  X |  X |  X |    |    |
    E|  * |  * |  * |  * |    |
    --------------------------
    """
    if list31[i][j+1]==pioni and list31[i][j+2]==pioni  and list31[i][j+3]==pioni:
        list31[i][j]='  * |'
        list31[i][j+1]='  * |'
        list31[i][j+2]='  * |'
        list31[i][j+3]='  * |'
        flag=True
        pos=j+4
        keno=False
        paiktis+=4
        edw=j+3
        while keno==False and pos<=sthles-1:
            if list31[i][pos]==pioni:
                edw=pos
                paiktis+=1
                list31[i][pos]='  * |'
            else:
                keno=True
            pos+=1
        func_pinakas(list31)
        for k in range(j,edw+1,1):#αρχίζει η ολίσθηση
            for m in range(i-1,-1,-1):
                if list31[m][k]!='    |':
                    list31[m+1][k]=list31[m][k]
                    list31[m][k]='    |'
        if i==0:
            for k in range(j,edw+1,1):
                list31[i][k]='    |'
        for k in range(j,edw+1,1):
            if list31[i][k]=='  * |':
                list31[i][k]='    |'
        list31.append(paiktis)
        list31.append(flag)
        return list31
    return
def func_check3(pioni,paiktis,i,j,list31):
    """
    Ελέγχει αν υπάρχει συνεχόμενη τετράδα διαγώνια πάνω ή παράλληλα προς την δευτερεύουσα διαγώνιο και αν συνορεύουν επιπλέον πίονια προς την διεύθυνση
    σχηματισμού της τετράδας, σημειώνει τα πιόνια, εμφανίζει τον ανανεομένο πίνακα και πραγματοποιεί ολίσθηση
    >>> list31=[[A|,    |,    |,    |,    |,    |],[B|,    |,    |,    |,  O |,    |],[C|,    |,    |,  O |,  X |,    |],[D|,    |,  O |,  X |,  X |,    |],[E|,  O |,  X |  X |,  O |,  O |]]
    >>> i,j=1,4
    >>> pioni='  O |'
    >>> paiktis=2 #pontoi1
    >>> sthles=5
    >>> ar='   1    2    3    4    5'
    >>> ar2='--------------------------'
    >>> func_check3(pioni,paiktis,i,j,list31)
       1    2    3    4    5
    --------------------------
    A|    |    |    |    |    |
    B|    |    |    |  * |    |
    C|    |    |  * |  X |    |
    D|    |  * |  X |  X |    |
    E|  * |  X |  X |  O |  O |
    --------------------------
    """
    if list31[i+1][j-1]==pioni and list31[i+2][j-2]==pioni and list31[i+3][j-3]==pioni:
        list31[i][j]='  * |'
        list31[i+1][j-1]='  * |'
        list31[i+2][j-2]='  * |'
        list31[i+3][j-3]='  * |'
        flag=True
        paiktis+=4
        pos1=i+4
        pos2=j-4
        edw1=i+3
        edw2=j-3
        keno=False
        while not keno and pos1<=sthles-1 and pos2>=1:
            if list31[pos1][pos2]==pioni:
                edw1=pos1
                edw2=pos2
                paiktis+=1
                list31[pos1][pos2]='  * |'
            else:
                keno=True
            pos1+=1
            pos2-=1
        func_pinakas(list31)
        for k in range(edw1,i-1,-1):#εδω αρχίζει η ολίσθηση
            for y in range(edw2,j+1,1):
                if list31[k][y]=='  * |':
                    for h in range(k-1,-1,-1):
                        if list31[h][y]!='    |':
                            list31[h+1][y]=list31[h][y]
                            list31[h][y]='    |'
        for k in range(edw1,i-1,-1):
            for y in range (edw2,j+1,1):
                if list31[k][y]=='  * |':
                    list31[k][y]='    |'
        list31.append(paiktis)
        list31.append(flag)
        return list31
    return 
def func_check4(pioni,paiktis,i,j,list31):
    """
    Ελέγχει αν υπάρχει συνεχόμενη τετράδα διαγώνια πάνω ή παράλληλα προς την κύρια διαγώνιο και αν συνορεύουν επιπλέον πίονια προς την διεύθυνση
    σχηματισμού της τετράδας, σημειώνει τα πιόνια, εμφανίζει τον ανανεομένο πίνακα και πραγματοποιεί ολίσθηση
    >>> list31=[[A|,  O |,    |,    |,    |,    |],[B|,  O |,  O |,    |,    |,    |],[C|,  X |,  O |,  O |,    |,    |],[D|,  X |,  X |,  X |,  O |,    |],[E|,  O |,  X |,  O |,  X |,  X |]]
    >>> i,j=0,1
    >>> pioni='  O |'
    >>> paiktis=4 #pontoi1
    >>> sthles=5
    >>> ar='   1    2    3    4    5'
    >>> ar2='--------------------------'
    >>> func_check4(pioni,paiktis,i,j,list31)
       1    2    3    4    5
    --------------------------
    A|  * |    |    |    |    |
    B|  O |  * |    |    |    |
    C|  X |  O |  * |    |    |
    D|  X |  X |  X |  * |    |
    E|  O |  X |  O |  X |  X |
    --------------------------
    """
    if list31[i+1][j+1]==pioni and list31[i+2][j+2]==pioni and list31[i+3][j+3]== pioni:
        list31[i][j]='  * |'
        list31[i+1][j+1]='  * |'
        list31[i+2][j+2]='  * |'
        list31[i+3][j+3]='  * |'
        flag=True
        paiktis+=4
        pos1=i+4
        pos2=j+4
        edw1=i+3
        edw2=j+3
        keno=False
        while not keno and pos1<=sthles-1 and pos2<=sthles:
            if list31[pos1][pos2]==pioni:
                edw1=pos1
                edw2=pos2
                paiktis+=1
                list31[pos1][pos2]='  * |'
            else:
                keno=True
            pos1+=1
            pos2+=1
        func_pinakas(list31)
        for k in range(edw1,i-1,-1):
            for y in range(edw2,j-1,-1):
                if list31[k][y]=='  * |':
                    for h in range(k-1,-1,-1):
                        if list31[h][y]!='    |':
                            list31[h+1][y]=list31[h][y]
                            list31[h][y]='    |'
        for k in range (edw1,i-1,-1):
            for y in range(edw2,j-1,-1):
                if list31[k][y]=='  * |':
                    list31[k][y]='    |'
        list31.append(paiktis)
        list31.append(flag)
        return list31
    return    
print('Καλώς ήλθατε στο παιχνίδι!')
answer=input('Επιθυμείτε νέο παιχνίδι (N) ή φόρτωση παιχνιδιού από αρχείο (S) ?')
if answer=='N' or answer=='Ν':#είτε αγγλικό Ν είτε ελληνικό
    sthles=int(input('Δώστε αριθμό στηλών:'))
    while sthles<5 or sthles>10:
        sthles=int(input('Ο αριθμός στηλών που δώσατε είναι λάθος.Παρακαλώ εισάγετε έναν αριθμό μεγαλύτερου ή ίσου του 5 και μικρότερου ή ίσου του 10 :'))
    lis=['A','B','C','D','E','F','G','H','I','J']
    pontoi1=0
    pontoi2=0
    ar='1'
    for i in range(2,sthles+1,1):
        ar=ar+'    '+str(i)
    ar2='-'
    for i in range(1,sthles+1,1):
        ar2+='-----'
    list31=[]
    for i in range(0,sthles,1):
        list4=[lis[i]+'|']
        for y in range(0,sthles,1):
            list4.append('    |')
        list31.append(list4)
        list4=[]
    func_pinakas(list31)
    round=1
    winner=False
    while answer !='s' and winner==False:
        paiktis1=int(input('Επέλεξε στήλη για το πιόνι σου παίκτη 1:'))
        while paiktis1<1 or paiktis1>sthles:
            paiktis1=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))
        i=0
        while list31[0][paiktis1]!='    |' and i<=sthles:
            i+=1
            paiktis1=int(input('Η στήλη που επιλέξατε είναι πληρης. Παρακαλώ εισάγετε νέο αριθμό στήλης:'))
            while paiktis1<1 or paiktis1>sthles:
                paiktis1=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))   
        flag=True
        i=sthles
        while flag and i>=0:
            k=list31[i-1]
            for j in range(1,sthles+1,1):#προσπέλαση στηλών
                if j==paiktis1:
                    if k[j]=='    |' and flag==True:
                        
                        k[j]='  O |'
                        flag=False        
            i-=1
        func_pinakas(list31)    
        flag=False
        for i in range(0,sthles,1):
            j=1
            while j<=sthles and not(flag):
                if list31[i][j]=='  O |' and flag==False:
                    if i+3<=sthles-1:
                        func_check('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)      
                    if not flag and j+3<=sthles:
                        func_check2('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1) 
                    if not flag and i+3<=len(list31)-1 and j>=4:
                        func_check3('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)
                    if not flag and i+3<=sthles-1 and j+3<=sthles:
                        func_check4('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)       
                j+=1
        if flag:
            print('Νικητής του '+str(round)+'ου γύρου είναι ο παίκτης 1')
            round+=1
            func_pinakas(list31)
        else:
            gemise=True
            for k in range(0,sthles,1):
                for h in range(0,sthles+1,1):
                    if list31[k][h]=='    |':
                        gemise=False
            if gemise:
                if pontoi1==0 and pontoi2==0:
                    print('Το παιχνίδι τελείωσε χωρίς νικητή')
                elif pontoi1>pontoi2:
                    print('Νικητής του παιχνιδιού ήταν ο παίκτης1 με βαθμολογία :'+str(pontoi1))
                elif pontoi2>pontoi1:
                    print('Νικητής του παιχνιδιού είναι ο παίκτης2 με βαθμολογία :'+str(pontoi2))
                else:
                    print('Το παιχνίδι τελείωσε με ισοπαλία')
                winner=True
        if winner==False:
            paiktis2=int(input('Επέλεξε στήλη για το πιόνι σου παίκτη 2:'))
            while paiktis2<1 or paiktis2>sthles:
                paiktis2=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))
            i=0
            while list31[0][paiktis2]!='    |' and i<=sthles:
                i+=1
                paiktis2=int(input('Η στήλη που επιλέξατε είναι πληρης. Παρακαλώ εισάγετε νέο αριθμό στήλης:'))
                while paiktis2<1 or paiktis2>sthles:
                    paiktis2=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))
            flag=True
            i=sthles
            while flag and i>=0:
                k=list31[i-1]
                for j in range(1,sthles+1,1):
                    if j==paiktis2:
                        if k[j]=='    |' and flag==True:
                            k[j]='  X |'
                            flag=False
                i-=1
            func_pinakas(list31)
            flag=False
            for i in range(0,len(list31),1):
                j=1
                while j<=sthles and not(flag):
                    if list31[i][j]=='  X |': 
                        if i+3<=len(list31)-1:
                            func_check('  X |',pontoi2,i,j,list31)
                            if len(list31)==sthles+2:
                                flag=True
                                list31.remove(True)
                                pontoi2=list31[-1]
                                list31.remove(pontoi2)
                        if flag==False and j+3<=sthles:
                            func_check2('  X |',pontoi2,i,j,list31)
                            if len(list31)==sthles+2:
                                flag=True
                                list31.remove(True)
                                pontoi2=list31[-1]
                                list31.remove(pontoi2)
                        if flag==False and i+3<=len(list31)-1 and j>=4:
                            func_check3('  X |',pontoi2,i,j,list31)
                            if len(list31)==sthles+2:
                                flag=True
                                list31.remove(True)
                                pontoi2=list31[-1]
                                list31.remove(pontoi2)
                        if flag==False and i+3<=sthles-1 and j+3<=sthles:
                            func_check4('  X |',pontoi2,i,j,list31)
                            if len(list31)==sthles+2:
                               flag=True
                               list31.remove(True)
                               pontoi2=list31[-1]
                               list31.remove(pontoi2)
                    j+=1  
            if flag:
                print('Νικητής του '+str(round)+'ου γύρου είναι ο παίκτης 2')
                round+=1
                func_pinakas(list31)
            else:
                gemise=True
                for k in range(0,sthles,1):
                    for h in range(0,sthles+1,1):
                        if list31[k][h]=='    |':
                            gemise=False
                if gemise:
                    if pontoi1==0 and pontoi2==0:
                        print('Το παιχνίδι τελείωσε χωρίς νικητή')
                    elif pontoi1>pontoi2:
                        print('Νικητής του παιχνιδιού ήταν ο παίκτης1 με βαθμολογία :'+str(pontoi1))
                    elif pontoi2>pontoi1:
                        print('Νικητής του παιχνιδιού είναι ο παίκτης2 με βαθμολογία :'+str(pontoi2))
                    else:
                        print('Το παιχνίδι τελείωσε με ισοπαλία')
                    winner=True
            answer=input('Πατήστε οποιοδήποτε πλήκτρο για να συνεχίσετε."\n"Για παύση του παιχνιδιού και αποθήκευση σε αρχείο πατήστε "s": ')
    if winner==False:
        list4=[]
        for i in range(0,sthles,1):
            for j in range(1,sthles+1,1):
                if list31[i][j]=='    |':
                    list31[i][j]='0'
                elif list31[i][j]=='  O |':
                    list31[i][j]='1'
                else:
                    list31[i][j]='2'
        for i in range(0,sthles,1):
            list5=[]
            for j in range(1,sthles+1,1):
                list5.append(list31[i][j])
            list4.append(list5)
        pontoi=[str(pontoi1),str(pontoi2)]
        list4.append(pontoi)
        filename=input('Δώστε όνομα αρχείου:')
        if filename[-4:]!='.csv':
            filename+='.csv'
        with open(filename,'w') as csvfile:
            filewriter=csv.writer(csvfile,delimiter=',')
            for i in range(0,sthles+1,1):
                filewriter.writerow(list4[i])
        print('Το παιχνίδι αποθηκεύτηκε !')
elif answer=='S':
    file=input('Δώστε όνομα αρχείου:')
    if file[-4:]!='.csv':
        file+='.csv'
    count=0
    with open(file,'r+') as f:
        reader=csv.reader(f)
        x=[]
        for row in reader:
            if row!=[]:
                
                count+=1
                x.append(row)
    lis=['A','B','C','D','E','F','G','H','I','J']
    ar='1'
    for i in range(2,count,1):
        ar=ar+'    '+str(i)
    ar2='-'
    for i in range(1,count,1):
        ar2+='-----'
    
    for i in range(0,count-1,1):
        for y in range(0,count-1,1):
            if x[i][y]=='0':
                x[i][y]='    |'
            elif x[i][y]=='1':
                x[i][y]='  O |'
            else:
                x[i][y]='  X |'
    pontoi1=int(x[count-1][0])
    pontoi2=int(x[count-1][1])
    list31=[]
    for i in range(0,count-1,1):
        list4=[lis[i]+'|']
        for y in range(0,count-1,1):
            list4.append(x[i][y])
        list31.append(list4)
        list4=[]
    func_pinakas(list31)
    round=1
    winner=False
    sthles=len(list31)
    while answer !='s' and winner==False:
        paiktis1=int(input('Επέλεξε στήλη για το πιόνι σου παίκτη 1:'))
        while paiktis1<1 or paiktis1>sthles:
            paiktis1=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))
        i=0
        while list31[0][paiktis1]!='    |' and i<=sthles:
            i+=1
            paiktis1=int(input('Η στήλη που επιλέξατε είναι πληρης. Παρακαλώ εισάγετε νέο αριθμό στήλης:'))
            while paiktis1<1 or paiktis1>sthles:
                paiktis1=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))    
        flag=True
        i=sthles
        while flag and i>=0:
            k=list31[i-1]
            for j in range(1,sthles+1,1):
                if j==paiktis1:
                    if k[j]=='    |' and flag==True:
                        
                        k[j]='  O |'
                        flag=False        
            i-=1
        func_pinakas(list31)    
        flag=False
        for i in range(0,sthles,1):
            j=1
            while j<=sthles and not(flag):
                if list31[i][j]=='  O |' and flag==False:
                    if i+3<=sthles-1:
                        func_check('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)
                if not flag and j+3<=sthles:
                        func_check2('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)
                if flag==False and i+3<=len(list31)-1 and j>=4:
                        func_check3('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)
                if flag==False and i+3<=sthles-1 and j+3<=sthles:
                        func_check4('  O |',pontoi1,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi1=list31[-1]
                            list31.remove(pontoi1)
                j+=1
        if flag:
            print('Νικητής του '+str(round)+'ου γύρου είναι ο παίκτης 1')
            round+=1
            func_pinakas(list31)
        else:
            gemise=True
            for k in range(0,sthles,1):
                for h in range(0,sthles+1,1):
                    if list31[k][h]=='    |':
                        gemise=False
            if gemise:
                winner=True
                if pontoi2==0 and pontoi1==0:
                    print('Το παιχνίδι τελείωσε χωρίςνικητή')
                elif pontoi1>pontoi2:
                    print('Νικητής του παιχνιδιού ήταν ο παίκτης1 με βαθμολογία :'+str(pontoi1))
                elif pontoi2>pontoi1:
                    print('Νικητής του παιχνιδιού είναι ο παίκτης2 με βαθμολογία :'+str(pontoi2))
                else:
                    print('Το παιχνίδι τελείωσε με ισοπαλία')
        paiktis2=int(input('Επέλεξε στήλη για το πιόνι σου παίκτη 2:'))
        while paiktis2<1 or paiktis2>sthles:
            
            paiktis2=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:'))
            i=0
            while list31[0][paiktis1]!='    |' and i<=sthles:
                i+=1
                paiktis2=int(input('Η στήλη που επιλέξατε είναι πληρης. Παρακαλώ εισάγετε νέο αριθμό στήλης:'))
                while paiktis2<1 or paiktis2>sthles:
                    paiktis2=int(input('Ο αριθμός στήλης που διαλέξατε δεν υπάρχει.Παρακαλώ εισάγετε καινούριο:')) 
        flag=True
        i=sthles
        while flag and i>=0:
            k=list31[i-1]
            for j in range(1,sthles+1,1):
                if j==paiktis2:
                    if k[j]=='    |' and flag==True:
                        k[j]='  X |'
                        flag=False
            i-=1
        func_pinakas(list31)
        flag=False
        for i in range(0,len(list31),1):
            j=1
            while j<=sthles and not(flag):
                if list31[i][j]=='  X |': 
                    if i+3<=len(list31)-1:
                        func_check('  X |',pontoi2,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi2=list31[-1]
                            list31.remove(pontoi2)
                    if flag==False and j+3<=sthles:
                        func_check2('  X |',pontoi2,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi2=list31[-1]
                            list31.remove(pontoi2)
                    if flag==False and i+3<=len(list31)-1 and j>=4:
                        func_check3('  X |',pontoi2,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi2=list31[-1]
                            list31.remove(pontoi2)
                    if flag==False and i+3<=sthles-1 and j+3<=sthles:
                        func_check4('  X |',pontoi2,i,j,list31)
                        if len(list31)==sthles+2:
                            flag=True
                            list31.remove(True)
                            pontoi2=list31[-1]
                            list31.remove(pontoi2)
                j+=1
        if flag:
            print('Νικητής του '+str(round)+'ου γύρου είναι ο παίκτης 2')
            round+=1
            func_pinakas(list31)
        else:
            gemise=True
            for k in range(0,sthles,1):
                for h in range(0,sthles+1,1):
                    if list31[k][h]=='    |':
                        gemise=False
            if gemise:
                winner=True
                if pontoi1==0 and pontoi2==0:
                    print('Το παιχνίδι τελείωσε χωρίς νικητή')
                elif pontoi1>pontoi2:
                    print('Νικητής του παιχνιδιού ήταν ο παίκτης1 με βαθμολογία :'+str(pontoi1))
                elif pontoi2>pontoi1:
                    print('Νικητής του παιχνιδιού είναι ο παίκτης2 με βαθμολογία :'+str(pontoi2))
                else:
                    print('Το παιχνίδι τελείωσε με ισοπαλία')
        answer=input('Πατήστε οποιοδήποτε πλήκτρο για να συνεχίσετε."\n"Για παύση του παιχνιδιού και αποθήκευση σε αρχείο πατήστε "s": ')
    if winner==False:
        list4=[]
        for i in range(0,sthles,1):
            for j in range(1,sthles+1,1):
                if list31[i][j]=='    |':
                    list31[i][j]='0'
                elif list31[i][j]=='  O |':
                    list31[i][j]='1'
                else:
                    list31[i][j]='2'
        for i in range(0,sthles,1):
            list5=[]
            for j in range(1,sthles+1,1):
                list5.append(list31[i][j])
            list4.append(list5)
        pontoi=[str(pontoi1),str(pontoi2)]
        list4.append(pontoi)
        filename=input('Δώστε όνομα αρχείου:')
        if filename[-4:]!='.csv':
            filename+='.csv'
        with open(filename,'w') as csvfile:
            filewriter=csv.writer(csvfile,delimiter=',')
            for i in range(0,sthles+1,1):
                filewriter.writerow(list4[i])
        print('Το παιχνίδι αποθηκεύτηκε !') 