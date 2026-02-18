# The simplest program - just show the Hello world!
import coat
# add the translation of the identifier "test_script"
coat.ui.addTranslation("test_script", "The example command")
# if the command is not inserted in the file menu, we insert it there
if not coat.ui.checkIfMenuItemInserted("test_script"):
    coat.ui.insertInMenu("File","test_script","")
    coat.dialog().text("The 'test_script' inserted into the File menu.").ok().show()
else:
    # ... if inserted, we execute the action
    coat.dialog().text("Hello world!").ok().show()
