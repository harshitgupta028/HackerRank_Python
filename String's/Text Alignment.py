#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
    
#                Python String | ljust(), rjust(), center()
# String alignment is frequently used in many day-day applications. Python in its 
# language offers several functions that helps to align string. Also, offers a way 
# to add user specified padding instead of blank space.

#                 These functions are :

# str.ljust(s, width[, fillchar])
# str.rjust(s, width[, fillchar])
# str.center(s, width[, fillchar])
# These functions respectively left-justify, right-justify and center a string in 
# a field of given width. They return a string that is at least width characters wide, 
# created by padding the string s with the character fillchar (default is a space) until 
# the given width on the right, left or both sides. The string is never truncated.

