#area of the circle
r=float(input("Input the radius of the circle :"))
area=math.pi*r*r
print("The area of the circle with radius 1.1 is: %.16f" %area)




#extension of the file
fn=input("Input the Filename:")
ext=fn.split(".")
print("The extension of the file is:" +repr(ext[-1]))
