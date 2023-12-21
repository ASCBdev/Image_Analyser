img="Image Analyser"
print(img)

img_analysis=input("Is this image an artwork?: ")
print(img_analysis)
x=img_analysis
a="yes"
b="Yes"
c="y"
d="Y"
e="YES"

yes_list=[a,b,c,d,e]
#print(yes_list)

for element in yes_list:
    if element==x:
        print("This is an artwork.")
    #else:
        #print("This is not an artwork.")

f="no"
g="No"
h="n"
i="Y"
j="NO"            

no_list=[f,g,h,i,j]

for element in no_list:
    if element==x:
        print("This is not an artwork")

comp_list=[a,b,c,d,e,f,g,h,i,j]

for element in comp_list:
    if element==x:
        print("Thank you for your input.")

   

#for element in comp_list:
    #if element not x:
        #print("Input not valid.")    

        

#for element in x:
    #if x==a:
        #print(a +"This is an artwork")
    #elif x==b:    
        #print(b +"This is an artwork")
    #elif x==c:    
        #print(c +"This is an artwork")
    #elif x==d:
        #print(d +"This is an artwork")
    #elif x==e:
        #print(e +"This is an artwork")    
    #else:
        #print("This is not an artwork")


