from fastq_reader import *

def cal_base_quality(file_path, base_list, seq_name="", seq_qscore="", k=0):
    """ Summary:
            Main function for Exercise 4
            Iterates through the file, and calculates the average quality of each of the 5 bases (A,T,G,C,N)
        Parameters: 
            file_path: relative path of the text file
            base_list: list of the 5 bases (A,T,G,C,N)
        Returns:
            printout the average quality of each of the 5 bases (A,T,G,C,N)
    """
    base_quality_dict = {}
    num_base = 0 # initialize number of certain type of DNA base
    tq_base = 0 # initialize total quality of certain type of DNA base
    for base in base_list:
        base_quality_dict[base] = [num_base, tq_base] # constrcut dictionary for base quality
    
    with open(file_path) as f: 
        for i, line in enumerate(f):
            flag = k%4
            if flag == 1: # loop through each DNA bases sequence 
                seq_name = [char for char in line.strip()]
            elif flag == 3: # loop through each DNA quality score sequence 
                seq_qscore = [char for char in line.strip()]
                for j, qscore in enumerate(seq_qscore):
                    qscore = quality_score(qscore)
                    target_base = seq_name[j] 
                    base_quality_dict[target_base][0] += 1 # update num_base
                    base_quality_dict[target_base][1] += qscore # update tq_base
            else:
                pass
            k += 1
            
    # Report the average quality of each of the 5 bases (A,T,G,C,N)
    for base in base_list:
        aq_score = base_quality_dict[base][1] / base_quality_dict[base][0] # average quality score 
        print("base: {}, quality: {}".format(base, aq_score))

# Test:
cleaned_file = '../data/cleaned_file.fastq'
base_list = ["A","T","G","C","N"]
cal_base_quality(cleaned_file, base_list)
