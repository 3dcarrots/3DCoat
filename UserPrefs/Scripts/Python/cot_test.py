import coat
class Test:
	def __init__(self):
		self.x=1
		self.y=2
		self.str = "text1"
		self.bb = True
		self.aa = False
		self.cc = False
		self.ff = 1.256
		self.case="case1";
	def increment(self):
		self.x+=1
	def ui(self):
		if(self.bb): return ["#image:data/StartMenu/images/header.png", "#icon:sphere", "increment", "[1 1]", "x,'x coor'", "y,'y coor'", "---", "aa,group1", "bb,group1", "cc,'CCCC',group2", "str,save:*.txt", "ff"]
		else: return ["increment", "[1 1]", "x,[0,30]", "y,[-100,100]", "---", "bb", "str,save:*.txt", "case,[case1|case2|case3]"]
t= Test()

d = coat.dialog()
d.text("abc").caption("header").params(t).ok().cancel().show()
print(t.x, t.y, t.str, t.bb, t.ff)

"""
# get to sculpt room
coat.ui.toRoom("Sculpt")
# add new volume
current = coat.Scene.sculptRoot().addChild("Wind rose")
volume = current.Volume()
# turn to surface
volume.toSurface()
height = 100
radius = 20
cone1 = coat.cone(height,radius,0)
cone2 = coat.cone(height/2,radius/2,0)
matrix = coat.mat4.Identity
for i in range(0,4):
	alpha = i*90
	print(alpha)
	matrix = coat.mat4.RotationZ(alpha)
	print(matrix)
	cone1.transform(matrix)
	cone1.details(0.5)
	cone1.add(volume)
	
	matrix = coat.mat4.RotationZ(alpha+45)
	cone2.transform(matrix)
	cone2.details(0.5)
	cone2.add(volume)
"""
