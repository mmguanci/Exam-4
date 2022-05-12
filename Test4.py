# 1: Possible Kmers
# Defines possible Kmers as lesser of two potential values

def Poss_Kmer(String, length):
    '''Ensure length is positive and a whole number'''
    assert length>=0
    assert type(length) is int
    poss1=(len(String)**(length))
    poss2=(len(String)-(length)+1)
    '''takes the two potential values for possible kmers and selects the minimum one'''
    poss_kmer=(min(poss1,poss2))
    return poss_kmer

'''does not run this on command line'''

if__name__=='__main__':
print(Poss_Kmer('ATTTGGATT',5))

# 2 Observed Kmers
# Observed Kmers. I did not solve this one on my own, much as I tried. Most of the code was found at https://www.voorloopnul.com/blog/kmer-analysis-with-python/. In order to ger an onserved kmers number I 
#took the length og the resulting dataset and divided it by 3 to get rid of the associated counts fro each unique kmer.
def Obs_kmers(String, length):
    '''ensures lenght inputs are positive whole numbers'''
    assert length>=0
    assert type(length) is int
    '''adds dictionary'''
    data = {}
    size = len(String)
    for i in range(size - length + 1):
        kmer = String[i: i + length]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    '''converts to string caue that is the only way I could get thsi to work'''
    stringy=str(data)
    result = len(stringy.split())
    return result/2
'''does not run this on command line'''

if__name__=='__main__':
Obs_kmers("ATTTGGATT", 8)

# 3 Linguistic Complexity
# defines the linguistic complexity of a given set of observed and possible Kmers. Values for Observers and possible Kmers should be taken from results from above scripts
'''Oberved Kmers=Obs_kmers, Possible Kmers=Poss_Kmer'''
def Ling_Comp(Obs_Kmer1,Poss_Kmer1):
    comp=(Obs_Kmer1/Poss_Kmer1)
    '''ensures Linguistic comp value is a positive number'''
    assert comp>=0
    return comp
Ling_Comp(34,40)
'''does not run this on command line'''
if__name__=='__main__':
Ling_Comp(35,40)



