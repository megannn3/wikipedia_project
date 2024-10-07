import wikipediaapi
import time

user_agent = "wikipedia_project (possiblymegansinclair@gmail.com)"
wiki= wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list=[]
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page,target_page):
    links = fetch_links(start_page)
    for link in links:
        if link == target_page.title:
            print("found link")


start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")
wikipedia_game_solver(start_page, target_page)
