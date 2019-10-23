#%%

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# (xoeu)*

#%%
import re
txt = "xaxaxaxaxaxa xa"
x = re.search("xa",txt)
print(x)
# x*
#

#%% 
import re 
# US Zip code (either 5 or 5+4)
zipcode1 = "31245"
zipcode2 = "32124-2432"
zipcode3 = "3214"
zipcode4 = "oue23"
# \d = [0-9]
# \d = [0123456789]

print(re.search("\d", zipcode1))
print(re.search("\d", zipcode2))
print(re.search("\d", zipcode3))
print(re.search("\d", zipcode4))
print (x)

#%%
