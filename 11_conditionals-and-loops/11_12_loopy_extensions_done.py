# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
flag=False
for i in filename:
    if i=="." and flag==False:

        print(i)
        flag=True
    elif i=="p" and flag==True:

        print(i)
        flag=False
    elif i =="d" and flag==False:

        print(i)
    elif i=="f" and flag==False:
        print(i)
        print(True)