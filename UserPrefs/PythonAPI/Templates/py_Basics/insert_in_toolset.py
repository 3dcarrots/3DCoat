# The tool insertion example - insert the tool that shows the  "Hello world!"
import coat
# add the translation of the identifier "test_script"
coat.ui.addTranslation("test_tool", "The Tool")
# if the command is not inserted into the toolset, we insert it there
if not coat.ui.checkIfMenuItemInserted("test_tool"):
    coat.ui.insertInToolset("Voxels","Adjust","test_tool")
    coat.dialog().text("The 'test_tool' inserted into the Sculpt->Adjust->The tool.").ok().show()
else:
    # ... if inserted, we execute the action
    coat.dialog().text("Hello world!").ok().show()
