import fuzzywuzzy
from fuzzywuzzy import fuzz

str_a='FuzzyWuzzy is a lifesaver!'
str_b='Fuzzy Wuzzy is a lifE SAVEr.'
ratio=fuzz.ratio(str_a.lower(),str_b.lower())
print('Similarity score:{}'.format(ratio))

str_a='Chicago,Illinois'
str_b='Chicago'
ratio=fuzz.partial_ratio(str_a.lower(),str_b.lower())
print('partial_ratio:{}'.format(ratio))

str_a='Gunner William Kline'
str_b='Kline , Gunner William'
ratio=fuzz.token_sort_ratio(str_a,str_b)
print('token_sort_ratio:{}'.format(ratio))

str_a='The 3000 meter steeplechase winner, Soufian El Bakkali'
str_b='Soufian El Bakkali'
ratio=fuzz.token_set_ratio(str_a,str_b)
print('token_set_ratio:{}'.format(ratio))
