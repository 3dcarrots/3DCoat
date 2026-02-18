# This example demonstrates the power of the dialogs and UI. It describes how to register the elements into the UI.
import coat

# This example demonstrates the dialogs power. What we do?
# Try to load previously stored settings, show dialog, save settings if user pressed Ok

# let's define the class. Then we create the ui function that exposes the ui elements list
	
class MyClass :
	def __init__(self) :
		self.Integer = 0
		self.IntSlider = 0
		self.Float = 0.0
		self.FloatSlider = 0.5
		self.Checkbox = False
		self.Radio1 = True
		self.Radio2 = False
		self.Droplist = 0
		self.String = "text"
		self.Coordinate = coat.vec3(1, 2, 3)
		self.Color = 'FF0000' # red
		self.String = ''
		self.OpenFilepath = ''
		self.SaveFilepath = ''
		self.Droplist = "Case2"
		self.idx=1
		self.items=[]

	def One(self) :
		self.Coordinate = coat.vec3(1)

	def Two(self) :
		self.Coordinate = coat.vec3(2)

	def ZeroCoordinate(self) :
		self.Coordinate = coat.vec3(0)

	def add(self):
		self.items.append(Item(self.idx))
		self.idx+=1

	# this section used for the class serialization and visual presentation in the UI
	# pay attention that visualization and serialization may be separated if need.	
	def ui(self) :
		# there you define the list of variables and functions to show in the dialog.
		# This list is dynamic, this function is constantly called, any changes in list
		# will be exposed immediately
		return [
			"#image:data/StartMenu/images/header.png", # the image example
			"#Just centered text message there", # centered text
			"#*Left-aligned text", # left-aligned text
			"Integer", # we write there the name of variable we want to expose to the UI 
			"IntSlider,[0,100]", # this is the integer slider definition
			"Float, Rename variable in UI if need", # we may use different name for the variable in UI
			"FloatSlider,[-1,1]", # we defined range there
			"Checkbox", # boolean variables visible as checkboxes
			"Radio1, group1", # the radio button, we set the group there
			"Radio2, group1", # same group for radio button
			"Droplist,[Case1|Case2|Case3]",
			"Color, color", # the color value editor
			"OpenFilepath,load:*.tif;*.tiff;*.exr;*.tga;*.bmp;*.png", # the open file dialog
			"SaveFilepath,save:*.tif;*.tiff;*.exr;*.tga;*.bmp;*.png", # save file dialog
			"[1 []]", # the layout control for the next UI items, the number is relative width of each item, the [] means automatical width
			"Coordinate", # the vec3 representation
			"ZeroCoordinate,'{maticon close}'", # the X icon. You may refer icons in text using {maticon icon_name}. Look for icons at data/meterial.io/icons/black/
			"[1 1]", # define 2 columns
			"One", # set 1 to the vector
			"Two", # set 2 to the vector
			"---",
			"items",
			"add,'{maticon add}'"
		]
# this chass is example of the list of clases within the parent class. If you prees the add button, the item will appear in the list.
# Pay attention, the Item.__init__(self) should be callable without additional parameters to be abloe to be savel/loaded as json correctly.
class Item:
	def __init__(self, i = 0):
		self.point = coat.vec3.RandNormal()
		self.index = i
	# remove the element
	def X(self):
		p.items.remove(self)
	# the list of UI elements for the item
	def ui(self):
		return [
			"[[%30] 1 []]",
			"index,''",
			"point,''",
			"X,'{maticon close}'"
			]
	
p = MyClass()
# restore the object from json if the file exists
coat.io.fromJsonFile(p,"dialogs.json")
# The on_press called each time user press Ok or other button on the dialog's bottom
def on_press(button):
	print("pressed: ", button)
	if(button == 1) : #Ok pressed
		# save the settings into the Documents/3DCoat/dialogs.json
		coat.io.toJson(p,"dialogs.json")
def process_fn():
	# do some action within the dialog
	# for exmple, you may click over some controls within the dialog
	# like coat.ui.cmd("$BaseClass::Integer")
	p.Float+=1
	

# show the dialog		
coat.dialog().ok().cancel().params(p).caption("caption").process(process_fn).onPress(on_press).show(); # the on_press will be called when used press ok(1) or cancel(2)		