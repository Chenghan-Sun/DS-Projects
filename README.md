# Data Science Projects

## Projects overview and explanation

### Project 1: Fast-Q
* Overview

  * A fastq file is a way of encoding short genomic reads from high throughput sequencing technology, such as Illumina next    generation sequencers. It consists of
  1. A sequence identifier which for this sequencer starts with an @, then followed by a long name, and a length tag.
  2. The sequence (the base calls; A, C, T, G and N), N stands for not able to read, due to insufficient quality.
  3. A separator, which is simply a plus (+) sign, perhaps followed by the identifier.
  4. The base call quality scores. These are Phred +33 encoded, using ASCII characters to represent the numerical quality      scores (more later).

  **Note: focus on memory and time complexity**
