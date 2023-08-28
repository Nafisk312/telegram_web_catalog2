from browser import html, document
import parsercurs

curs = parsercurs.exchange("9afbe13e92d995dfc17befa52e6af754", "398", "643")
price = 5999 // curs

document['sell5'] <= html.H4(price)