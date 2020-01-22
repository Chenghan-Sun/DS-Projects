from fastq_reader import *
import numpy as np

def cal_seq_quality(file_path, k=0):
    """ Summary:
            Part I: Main function for Exercise 3
            Calculate the average qualify score of all sequences
        Parameters: 
            file_path: relative path of the text file
        Returns:
            seq_avg_dict: dictionary of average qualify score of all sequences 
    """
    seq_avg_dict = {} 
    with open(file_path) as f: 
        for i, line in enumerate(f):
            flag = k%4 
            if flag == 0:
                seq_index = line.split()[0] # get the required sequence index name 
            if flag == 3: # loop through each sequence 
                target = [char for char in line.strip()] # split sequence into single characters
                seq_qua = [quality_score(char) for char in target]
                seq_qua_avg = np.mean(seq_qua) # avg quality score of a sequence
                seq_avg_dict[seq_index] = seq_qua_avg # stored into the dictionary
            k+=1
    return seq_avg_dict

def find_extreme_qua(file_path, seq_avg_dict):
    """ Summary:
            Part II: Main function for Exercise 3
            Add functionality for finding the sequences with highest and lowest average quality 
        Parameters: 
            file_path: relative path of the text file
            seq_avg_list: dictionary of average qualify score of all sequences 
        Returns:
            seq_qua_high: highest average quality
            seq_qua_low: lowest average quality
            seq_high: the sequence with the highest average quality
            seq_low: the sequence with the lowest average quality
    """
    seq_min_val = min(seq_avg_dict.items(), key=lambda x : x[1]) # get the minimum element in the dictionary
    # Iterate over all the items in dictionary to find keys with max value
    for key, val in seq_avg_dict.items():
        if val == seq_min_val[1]:
            print("Lowest quality seq: {}, quality: {}".format(key, seq_min_val[1]))
            
    seq_max_val = max(seq_avg_dict.items(), key=lambda x : x[1]) # get the maximum element in the dictionary
    for key, val in seq_avg_dict.items():
        if val == seq_max_val[1]:
            print("Highest quality seq: {}, quality: {}".format(key, seq_max_val[1]))
            

# Test: 
cleaned_file = '../data/cleaned_file.fastq'
seq_avg_dict = cal_seq_quality(cleaned_file)
find_extreme_qua(cleaned_file, seq_avg_dict)


