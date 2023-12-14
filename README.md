# Paternity Testing Simulator with Genetic Marker Matching Algorithm for Alleged Father and Child DNA Sequence in Comparison to Alternative Algorithms
Paternity Test are widely recognized by almost everyone, however, the intricacies and actual processes behind a paternity test often remain unfamiliar to many. In its nature, paternity tests are more complex than it seems, a single test can consist of many tests in determining biological affinity where each test then consists of many different methods or techniques of calculating the parentage probability. Naturally, there exist several different approaches in computational biology to assess and calculate parternity probabiliy, including several algorithms and computation techniques such as Levenstein Distance, Hamming Distance, Bayesian Interference, and Genetic Marker Matching. 

With the goal of providing a simplified simulation of how these algorithms can be used in paternity testing, we compared them to each other to find one that has the best accuracy to simulate paternity tests. We found that Genetic Marker Matching offers the most understandable, accurate, and logical approaches to simulating a paternity test. Thus, we programmed it to come with a GUI that is able to read DNA sequences of an alleged father and a child and calculate their parentage probability. This simulator allows users to get a better understanding of paternity tests, probability calculations, genetic markers, basics of DNA sequence comparison, DNA alignment, and the overall structure of human DNA. In addition to the algorithm, we also provided test data for anyone to use in FASTA format.

## Group Details 
Class: L5AC</br>
Course: Computational Biology (SCIE6062001) </br>
Members: </br>
* Arish Madataly (2502049706)
* Ferdinand Jacques (2501982600)
* Maria Clarin (2501990331) 

## Repo Directory
* GUI.py : main program file, run this file to run the simulator.
* paternity_test.py : main methods file for the genetic markers matching paternity test. 
* Test Data Folder : folder containing data usable for the DNA inputs of the child and alleged father, in FASTA format.
* Alternative algorithm Folder : folder containing various algorithms used to compare with the genetic markers matching paternity test
* images Folder : folder containing images used as UI elements. 

## External Links:
* Final Project Report :

## How to install
1. Clone the repository
```
git clone https://github.com/mariaclarin/CompBio-FinalProject 
```
2. Install dependencies and libraries
* tkinter
* PIL/pillow
* pandas
* tabulate
3. Run GUI.py

## Screenshots and program features
### Landing Page 
![landing](https://cdn.discordapp.com/attachments/794551109523341353/1184923259200884796/Screen_Shot_2023-12-15_at_01.19.13.png?ex=658dbcc7&is=657b47c7&hm=222a3f7345ea1956c50b80eb7b456e0fa381c3cd56ee486a906704e9910c26e3&)

### Input Page 
![input](https://cdn.discordapp.com/attachments/794551109523341353/1184923259758710864/Screen_Shot_2023-12-15_at_01.19.38.png?ex=658dbcc7&is=657b47c7&hm=29d835f33b80c335ee6bd3c6555523c7f9431466f45033ce777a5e21bbee0aa6&)
![input](https://cdn.discordapp.com/attachments/794551109523341353/1184923260241072179/Screen_Shot_2023-12-15_at_01.19.56.png?ex=658dbcc8&is=657b47c8&hm=38308038d9c6c89cc9375c1ea193d60aad9e73bbe4e36484db11eebad4822f0d&)
![input](https://cdn.discordapp.com/attachments/794551109523341353/1184923260685651978/Screen_Shot_2023-12-15_at_01.20.09.png?ex=658dbcc8&is=657b47c8&hm=7e1deda33992d5db3ab5c4ab8d3f7a7838cccc7146b7ae69f3afe2c6918117d3&)

* Input fields are mutable on screen and users also have an option to upload DNA files.

### Results Page and Export 
![results](https://cdn.discordapp.com/attachments/794551109523341353/1184923261151232111/Screen_Shot_2023-12-15_at_01.20.45.png?ex=658dbcc8&is=657b47c8&hm=9d019451895a15fe7b1e2ea2c62696d5212f7cb6816046310ea9e068f7dd184e&) 
![results](https://cdn.discordapp.com/attachments/794551109523341353/1184923261528723516/Screen_Shot_2023-12-15_at_01.20.59.png?ex=658dbcc8&is=657b47c8&hm=5b87c5e7a5a65c82142a3eb51e4014ba0336a91a537f0e4eb0652254365ad681&)
![results](https://cdn.discordapp.com/attachments/794551109523341353/1184923261893611601/Screen_Shot_2023-12-15_at_01.21.29.png?ex=658dbcc8&is=657b47c8&hm=a6026b8019e02a405f933b5674d054c7f61cc03200d006eae5b5f5668db0aab9&)

* Results can be exported in a report.txt format.


## References
The testing data are *Homo sapiens* genome FASTA, derived from 
```
https://download.cncb.ac.cn/gwh/Animals/
```
and is synthetically mutated/altered to simulate parentage probability