from browser import document
from browser.widgets.dialog import InfoDialog

def click(ev):
    InfoDialog("Hello", f"Hello, {document['btn6'].value} !")

# bind event 'click' on button to function echo
document["echo"].bind("click", click)