print('imported')

from requests_html import HTML, HTMLSession
from tkinter import *

def getCurrencyRatios():
    ratios = {}
    session = HTMLSession()
    r = session.get('https://www.google.com/search?q=currency+exchange+rate+ratio&oq=currency+exchange+ratio&aqs=chrome.2.69i57j0l7.16938j1j7&sourceid=chrome&ie=UTF-8')
    sel = '#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.vk_bk.gsrt > span.DFlfde.SwHCTb'
    block = r.html.find(sel, first=True)
    ratios['USD'] = float(block.text)

    r = session.get('https://www.google.com/search?q=pounds+to+aud&oq=pounds&aqs=chrome.1.69i57j35i39j0l6.4019j1j7&sourceid=chrome&ie=UTF-8')
    sel = '#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.vk_bk.gsrt > span.DFlfde.SwHCTb'
    block = r.html.find(sel, first=True)
    ratios['Pounds'] = float(block.text)

    return ratios


ratios = getCurrencyRatios()



def getJunoPrice(module):
    name = '+'.join(module.split())
    session = HTMLSession()
    r = session.get(f'https://www.juno.co.uk/search/?q%5Ball%5D%5B%5D={name}&solrorder=relevancy&hide_forthcoming=0')
    try:
        block = r.html.find('.pl-big-price', first=True)
        return round(float(block.text.split()[-1].replace('£','')) * ratios['Pounds'], 2)
    except Exception:
        return 'Module not found.'

def getPCPrice(module):
    pc_name = '%20'.join(module.split())

    session = HTMLSession()
    r = session.get(f'https://www.perfectcircuit.com/catalogsearch/result/?q={pc_name}')
    try:
        sel = '#amasty-shopby-product-list > div.products.wrapper.grid.products-grid > ol > li:nth-child(1) > div > div > div.badges-prices-wrapper > div'
        block = r.html.find(sel, first=True)
        return round(float(block.text.split()[-1].replace('$','')) / ratios['USD'], 2)
    except Exception:
        return 'Module not found.'

def getFSPrice(module):
    fs_name = '+'.join(module.split())
    session3 = HTMLSession()
    r3 = session3.get(f'https://foundsound.com.au/search?q={fs_name}+AND+tag%3Avisible')

    try:
        block3 = r3.html.find('.list-view-item__price-column', first=True)
        return block3.text.split()[0].replace('$','')
    except Exception:
        return 'Module not found.'





root = Tk()
root.title('Module Price Lookup')
root.geometry('640x640+0+0')

label1 = Label(root, text='Enter a module name and manufacturer').place(x=10, y=200)


module = StringVar()
entry_box = Entry(root, textvariable=module, width=25)
entry_box.place(x=280, y=200)
def getPrices():
    name = entry_box.get()
    label5['text'] = getJunoPrice(name)
    label6['text'] = getPCPrice(name)
    label7['text'] = getFSPrice(name)

work = Button(root, text='Find prices', width=25, height=2, command=getPrices).place(x=280, y=250)
label2 = Label(root, text='Juno in AUD')
label2.place(x=10, y=300)
label3 = Label(root, text='Perfect Circuit in AUD')
label3.place(x=10, y=330)
label4 = Label(root, text='Found Sound in AUD')
label4.place(x=10, y=360)
label5 = Label(root)
label5.place(x=280, y=300)
label6 = Label(root)
label6.place(x=280, y=330)
label7 = Label(root)
label7.place(x=280, y=360)
root.mainloop()
