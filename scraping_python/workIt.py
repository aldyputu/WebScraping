import webbrowser

webDaily = [
    "https://sp.morganstanley.com/eu/documents/",
    "https://www.luxse.com/",
    "https://derivatives.cib.barclays/GB/1/en/document-repository.app?themeName=existing-investor",
    "https://www.boerse-frankfurt.de/global-search",
    "https://www.gspriips.eu/",
    "https://www.documentation.ca-cib.com/Document/Search",
]

for link in webDaily:
    webbrowser.open(link, new=2, autoraise=True)
    
