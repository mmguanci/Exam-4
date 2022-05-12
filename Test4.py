# 1: Possible Kmers
# Defines possible Kmers as lesser of two potential values

def Poss_Kmer(String, length):
    poss1=(len(String)**(length))
    poss2=(len(String)-(length)+1)
    return(min(poss1,poss2))
'''does not run this on command line'''
if__name__=='__main__':
print(Poss_Kmer('ATTTGGATT',4))

# 2 Observed Kmers
# Observed Kmers. I did not solve this one on my own, much as I tried. Most of the code was found at https://www.voorloopnul.com/blog/kmer-analysis-with-python/. In order to ger an onserved kmers number I 
#took the length og the resulting dataset and divided it by 3 to get rid of the associated counts fro each unique kmer.
def Obs_kmers(sequence, k_size):
    '''creates data dictionary'''
    data = {}
    size = len(sequence)
    for i in range(size - k_size + 1):
        kmer = sequence[i: i + k_size]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    stringy=str(data)
    result = len(stringy.split())
    return result/2
Obs_kmers('ATTTGGATT', 4)
'''does not run this on command line'''

if__name__=='__main__':
Obs_kmers("ATTTGGATT", 8)

# 3 Linguistic Complexity
# defines the linguistic complexity of a given set of observed and possible Kmers. Values for Observers and possible Kmers should be taken from results from above scripts
'''Oberved Kmers=Obs_kmers, Possible Kmers=Poss_Kmer'''
def Ling_Comp(Obs_kmers,Poss_Kmer):
    comp=(Obs_kmers/Poss_Kmer)
    return comp
'''does not run this on command line'''
if__name__=='__main__':
Ling_Comp(35,40)



