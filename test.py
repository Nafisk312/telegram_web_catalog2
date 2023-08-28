from browser import html, document
from browser.widgets.dialog import InfoDialog

def click(ev):
    InfoDialog("Hello", f"Hello, {document['btn1'].value} !")

# bind event 'click' on button to function echo
document["echo"].bind("click", click)

document['sell'] <= html.H4('4999')