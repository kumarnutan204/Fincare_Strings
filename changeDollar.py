st= "restart"
def change(st):
    char = st[0]
    st = st.replace(char,'$')
    st = char + st[1:]
    print(st)
change(st)
# print(st)
