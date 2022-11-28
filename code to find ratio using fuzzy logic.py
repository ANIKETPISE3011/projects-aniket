import fuzzywuzzy
from fuzzywuzzy import fuzz
str_A='FuzzyWuzzy is a lifesaver!'
str_B='Fuzzy Wuzzy is a Life SAVER.'
ratio=fuzz.ratio(str_A.lower(),str_B.lower())
print('Similarity score:()',format(ratio))

str_A=' Chicago ,Illinois'
str_B='Chicago'
ratio=fuzz.ratio(str_A.lower(),str_B.lower())
print('partial score :()', format (ratio))

str_A='Gunner William Kline'
str_B='Kline,Gunner William'
ratio=fuzz.ratio(str_A,str_B)
print('token_sort_ratio:()',format (ratio))

str_A='The 3000 meter steeplechase winner, Soufian El Bakkali'
str_B='Soufian El Bakkali'
ratio= fuzz.token_set_ratio(str_A,str_B)
print('token_set_ratio:()',format(ratio))
      
      
