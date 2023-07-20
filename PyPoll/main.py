import os
import csv


csvpath = os.path.join("C:/Users/arnol/OneDrive/Documents/SMU/GitSMU/python-challenge/PyPoll/Resources/election_data.csv")
csvoutput = os.path.join("C:/Users/arnol/OneDrive/Documents/SMU/GitSMU/python-challenge/PyPoll/analysis/ResultsPyPoll.txt")

##Variable set to 0 and defining list and dictionaries to save the data and process it
total_number_of_votes = 0
max_votes = 0
all_candidates = []
vote_count = {}
individual_votes = []



##open the file as csvfile to then read it and get from it its headers

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)


    ##start iteration into the data
    for x in csvreader:
        
        
        
        ## total_number_of_votes will start incrementing and adding the total number of iterations or votes
        ## name will be indexed to the Candidate column, where x will iterate for each row
        total_number_of_votes += 1
        name = x[2]
        

        # if the name of the candidate is not in the list all_candidates, which is not, it will save it, once
        #then it will recognize the name and do ELSE adding a vote+=1 into its name .ending up with a 
        #dictionary with their names and total votes.
        
        if name not in all_candidates:
            all_candidates.append(name)
            vote_count[name] = 1
        else: 
            vote_count[name] += 1
        
        
        #created lists of the items recolected
        namelist = list(vote_count.keys())
        votelist = list(vote_count.values())
        
        
        
        
    #in this iteration will extract the biggest number of votes, if max_votes is less than the Value v it will be saved 
    #in its own variable, when iteration finish it will hold the greates v with the corresponding k and will scape the loop.
    
    
    
    for k,v in vote_count.items():

        if max_votes < v: 
            max_votes = v
            winner = k
        else:
            continue



    print(f"\n                  ELECTION RESULTS\n\n")
    print(f"-"*20)
    print(f"Total Votes : {total_number_of_votes} ")
    print(f"-"*20)

    print(f"\n{namelist[0]} :  { round(votelist[0]/total_number_of_votes*100, 3 )} %      ({votelist[0]}) \n"
          f"{namelist[1]}           :  { round(votelist[1]/total_number_of_votes*100, 3 )} %     ({votelist[1]}) \n"
          f"{namelist[2]}    :   { round(votelist[2]/total_number_of_votes*100, 3 )} %      ({votelist[2]}) \n\n"
         )
    print(f"-"*60)  
    
    print(f"                WINNER  :  {winner}   ")
         
    print(f"-"*60)      
     
        
        
        
        
    with open(csvoutput, "a") as txtfile:
            txtfile.write(
                
f"""
\n                                ELECTION RESULTS \n


                {"-"*20}
                Total Votes : {total_number_of_votes}
                {"-"*20}
                
                {namelist[0]} :  { round(votelist[0]/total_number_of_votes*100, 3 )} %      ({votelist[0]})
                {namelist[1]}           :  { round(votelist[1]/total_number_of_votes*100, 3 )} %     ({votelist[1]})
                {namelist[2]}    :   { round(votelist[2]/total_number_of_votes*100, 3 )} %      ({votelist[2]})
                
                
                {"-"*60} 
                              WINNER  :  {winner} 
                {"-"*60}


                             """) 
