from fastq_reader import *

def extract_seq(fastq_iter, target1=0, seq_target1="", target2=0, seq_target2="", 
                flag=0, target3=0, seq_target3=""):
    """ Summary:
            Main function for Exercise 8
            Target 1. Find the longest continuous sequence of repeated "TCC"s
            Target 2. The most matches to G_G where _ is any base
            Target 3. The longest sequence of any one base
        Parameters: 
            fastq_iter: text custom iterator from Exercise 7 
        Returns:
            printed information about Target 1, 2, 3
    """
    for seq_name, seq, seq_qua in fastq_iter: # import from fastq_reader/fastqReader
        TCC_pattern = re.findall('(TCC)', seq) # target 1
        G_G_pattern = re.findall('(G[ANTCG]G)', seq) # target 2
        len_TCC = len(TCC_pattern)
        len_G_G = len(G_G_pattern)
        lon_pattern = re.findall(r'((\w)\2{3,})', seq) # target 3
        
        if len_TCC >= target1: # target 1: "TCC"
            target1 = len_TCC
            seq_target1 = seq_name
        elif len_TCC < target1:
            pass
        
        if len_G_G >= target2: # target 2: "G_G"
            target2 = len_G_G
            seq_target2 = seq_name
        elif len_G_G < target2:
            pass
        
        for lon, char in lon_pattern: # extract the longest continuous char in a sequence 
            len_lon = len(lon)
            if len_lon >= flag:
                flag = len_lon # flag: length of the longest continuous char 
                if flag >= target3: # target 3: longest sequence of any one base
                    target3 = flag
                    seq_target3 = seq_name
                elif flag < target3:
                    pass
            elif len_lon < flag:
                pass 
            
    print("Seq with longest TCC repeat: {}; repeat times = {}".format(seq_target1, target1))
    print("Seq with most matches to G_G: {}; repeat times = {}".format(seq_target2, target2))
    print("Seq with longest of any one base: {}; repeat times = {}".format(seq_target3, target3))

# Test:
cleaned_file = '../data/cleaned_file.fastq'
fastq_iter = fastqReader(cleaned_file)
extract_seq(fastq_iter)
