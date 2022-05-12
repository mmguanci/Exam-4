from Test4 import*

def test_simple():
    assert Poss_Kmer('ATTTGGATT',4)==6
def test_zero():
    assert Poss_Kmer('ATTTGGATT',-2)==12, 'There is a negative value'
def test_decimal():
    assert Poss_Kmer('ATTTGGATT',3.6)==6, 'There is a decimal Kmer value'
def test_negative_obs():
    assert Poss_Kmer('ATTTGGATT', r)==6, 'Letter used as kmer value'

    def test_simple_obs():
    assert Obs_kmers('ATTTGGATT', 4)==6
def test_interger_obs():    
    assert Obs_kmers('ATTTGGATT', 4.5)==6, 'Non interger kmer length'
def test_negative_obs():
    assert Obs_kmers('ATTTGGATT', -2)==6, 'Non positive kmer length'
def test_non_number_obs():    
    assert Obs_kmers('ATTTGGATT', r)==6, 'Letter used as kmer value'
    
def test_simple_LC():
    assert Ling_Comp(35,40)==0.875
def test_interger_LC():    
    assert Obs_kmers('ATTTGGATT', 4.5)==6, 'Non interger observation'
def test_negative_obs():
    assert Ling_Comp(-35,40)==-0.875, 'Negative observation'
def test_non_number_obs():    
    assert Ling_Comp(35,d)==0.875, 'Non interger value for observation'