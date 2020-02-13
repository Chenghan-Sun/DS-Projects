# Data Science Projects

## Projects overview and explanation

### Project 1: Fast-Q
* Overview

  * A fastq file is a way of encoding short genomic reads from high throughput sequencing technology, such as Illumina next generation sequencers. It consists of:
    * A sequence identifier which for this sequencer starts with an @, then followed by a long name, and a length tag.
    * The sequence (the base calls; A, C, T, G and N), N stands for not able to read, due to insufficient quality.
    * A separator, which is simply a plus (+) sign, perhaps followed by the identifier.
    * The base call quality scores. These are Phred +33 encoded, using ASCII characters to represent the numerical quality      scores (more later).

    **Note: focus on memory and time complexity**
    
### Project 2: Reinforcement Learning -- The multi-armed bandit framework 
* Overview

  * The multi-armed bandit framework assumes that you are in a two player game where you select a number from 1 to K (we call this number the arm that you pulled). Then the other player selects a reward, $r_{i,t}$ based on the arm, $i$, at time $t$ that you selected and reveals that to you. Your job is to come up with a policy which determines which arm to pull at a given time based on the past performances of the arms. It consists of:
  
