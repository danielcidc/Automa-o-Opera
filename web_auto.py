import webbrowser as wb 

def webauto():
    opera_path = r'c:\\Users\\Usuario\\AppData\\Local\\Programs\\Opera\\opera.exe %s' #caminho do navegador utilizado
    URLS = (
        'https://www.google.com/',
        'https://www.youtube.com/',
        'https://www.instagram.com/',
        'https://www.github.com/'
    )

    for url in URLS:
        print("Abrindo :", url)
        wb.get(opera_path).open(url)

webauto()