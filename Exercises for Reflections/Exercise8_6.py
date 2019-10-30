#%%
def disevowel(manytimes):
    List = list(manytimes)
    Vowels = ["a","e","i","o","u"]
    for letter in List:
        if letter.lower() in Vowels:
        List remove(letter)
    manytimes = '' .join(List)
    return manytimes