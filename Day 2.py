import string
st = input("Enter a string:  ")
st = st.lower()
alpha=list(string.ascii_lowercase)
em_list = []
for i in range(0,26): 
    em_list.append(st.count(alpha[i]))
for i in range (0,26):
    if em_list[i] != 0:
       print(str(alpha[i].lower())+ "-" + str(em_list[i]))