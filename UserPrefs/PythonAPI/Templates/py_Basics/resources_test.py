# This example demostrates the resources management in 3DCoat
# See the coat.resource class for the full list of functions
import coat

#show the console (if hidden)
coat.io.showPythonConsole()

# list all resources types like Alphas, Strips, ...
res = coat.resource.listAllResourcesTypes()
print("The list of all resources types:\n", res)

# for each resource type:
for r in res:
    # create the resource object by it's name
    current = coat.resource(r)
    # get the list of foldes
    folders = current.listFolders()
    # get the list of supported extensions
    exts = current.supportedExtensions()
    print("\n", r,":", exts)
    print(folders)
    # current folder and current item (if availabble)
    print("\tcurrent folder:", current.currentFolder(), "current item:", current.getCurrentItem())
    # print the list of all items in current folder of this resource
    items = current.listCurrentFolderItems()
    for i in items:
        print("\t\t",i)

# example of getting Alphas
alphas = coat.resource("Alphas")

# we remove folder
alphas.removeFolder("TestAlphas")

# add new folder and switch there
alphas.createFolder("TestAlphas")

# add item to the new folder
alphas.addItem('data/textures/arrow_up.png')

# the new item becomes current:
print("Current alpha:", alphas.getCurrentItem(), "in folder",alphas.currentFolder())