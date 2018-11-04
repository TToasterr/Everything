import webbrowser

new = 2
url = 'https://www.youtube.com/channel/UChHVMv5AxM6DcgVuY6skTXg'

def ohNo(amount):
    global url
    global new

    for i in range(amount):
        webbrowser.open(url, new=new)

ohNo(100)
