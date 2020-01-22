import re
from collections import Counter

def quality_score(quality_chr):
    """ Summary:
            Main function for Exercise 2
            Takes in the quality character and returns a number between 0 and 1
        Parameters:
            quality_chr: single charactor from each sequence 
        Returns:
            q_score: transferred quality score
    """
    q_score_raw = ord(quality_chr)
    q_score = (q_score_raw - 33)/40
    
    return q_score

def ngram_freq(sequence, n):
    """ Summary: 
            Main function for Exercise 5
            Take a sequence string and n as an input and output a dictionary
        Parameters:
            sequence: a sequence string
            n: n-gram
        Returns:
            c: target dictionary which has keys that are n-grams and values 
                which are the frequency of that n-gram in the sequence
    """
    ngrams = [sequence[i:i+n] for i in range(len(sequence)-n+1)]
    c = Counter(ngrams)
    for ngram in c:
        c[ngram] *= 1/ (len(sequence)-n+1)
        
    return c

def ngram_sim(seq1, seq2, n, sim_score = 0):
    """ Summary:
            Main function for Exercise 6
            Takes two sequences and outputs the notion of similarity as defined in the notebook
        Parameters:
            seq1: sequence string 1
            seq2: sequence string 2
            n: n-gram
        Returns:
            sim_score: notion of similarity for two sequences
    """
    c1 = ngram_freq(seq1, n)
    c2 = ngram_freq(seq2, n)
    for key, val in c1.items():
        if key not in c2:
            c1[key] = 0
        sim_score += (val * c2[key])**(1/2)
    
    return sim_score

def fastqReader(filename, seq_name="", seq="", seq_qua="", k=0):
    """ Summary:
            Main function for Exercise 7
            Create a custom iterator that iterates through the file (line by line) and for each 
            read should yield a tuple of (sequence name, sequence, quality) where each are strings
        Parameters:
            filename: relative path of the data file
        Returns:
            fastq_tuple: generator of a tuple of (sequence name, sequence, quality)
    """
    with open(filename) as f: 
        for i, line in enumerate(f): 
            flag = k%4
            if flag == 0:
                seq_name = line.split()[0]
            elif flag == 1:
                seq = line.strip()
            elif flag == 3:
                seq_qua = line.strip()
                fastq_tuple = (seq_name, seq, seq_qua)
                yield fastq_tuple
            else:
                pass
            k += 1
