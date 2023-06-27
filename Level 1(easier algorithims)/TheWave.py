def wave(people): 
    peopleArr = []
    n = len(people)
    for i in range(n):
        peopleArr.append(people.replace(people[i],(people[i:i+1].upper())))  
    return peopleArr


print(wave("heya"))










            




        


                
                
          
        
