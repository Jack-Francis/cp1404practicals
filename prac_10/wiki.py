import wikipedia

page_title = input(">>> ")
while page_title != "":
    try:
        selected_page = wikipedia.page(page_title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as choose:
        print(choose.options)
    print(selected_page.title)
    print(selected_page.summary)
    print(selected_page.url)
    page_title = input(">>> ")
