# Iterate over the sculpt tree, show the basic stats - square, volume 
import coat

# This class represents the one line in the info box, the square and volume of one sculpt object
class OneLine :
	def __init__(self):
		self.name = ""
		self.Square = 0
		self.Volume = 0
	
	def __init__(self, el) :
		self.name = el.name()
		self.Square = el.Volume().getSquare()
		self.Volume = el.Volume().getVolume()

	def ui(self):
		return [
               "[3]",
               "name,'!name'", #"!identifier" means that it is readonly and it's name does not appear in UI
               "Square,'!Square'",
               "Volume,'!Volume'"
		]
	
# This is the class to represent the information about all volumes
class Stats:
	def __init__(self):
		self.lines = []
        
	def Calculate(self):
		# get the sculpt root
		r = coat.Scene.sculptRoot()
		# iterate through all sculpt objects
		def walker(el):
			# adding the element to ClassArray to represent in UI
			line = OneLine(el)
			if el.isSculptObject() : self.lines.append(line)
			print(line.name, line.Square, line.Volume)
			return False
                
		r.iterateVisibleSubtree(walker)
		print(self.lines)

	# This is the list of volumes, ClassArray is the array of pointers to BaseClass-derived items
	def ui(self):
		return [
			# making the header, 3 columns
			"[3]",
			# "*name" means it is left-aligned text
			"#*Name",
			"#*Square",
			"#*Volume",
			"---",
            "lines",
	    	"---"      
		]
		
stats = Stats()
# calculate the stats
stats.Calculate()
coat.dialog().ok().params(stats).show()