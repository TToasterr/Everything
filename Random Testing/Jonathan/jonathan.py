import webbrowser

new = 2
url = 'https://www.youtube.com/channel/UChHVMv5AxM6DcgVuY6skTXg'

def ohNo(amount):
    global url
    global new

    amm = amount

    while amm > 0:
        amm -= 1
        webbrowser.open(url, new=new)

ohNo(100)
