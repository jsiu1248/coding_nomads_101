# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


string=input("Enter a string: ")



a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for i in string:
    if i=="a":
        a_count=a_count+1
    elif i=="e":
        e_count=e_count+1
    elif i=="i":
        i_count=i_count+1
    elif i=="o":
        o_count=o_count+1
    elif i=="u":
        u_count=u_count+1
print(f"a:{a_count}, e:{e_count}, i:{i_count}, o:{o_count}, u:{u_count}")
