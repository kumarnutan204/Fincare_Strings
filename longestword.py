lst=['amir','gatsby', 'reveal','landlord','Customization','devotion']
def longest(lst):
    length=[]
    for i in lst:
        length.append(len(i))
    print(max(length))
    
longest(lst)
