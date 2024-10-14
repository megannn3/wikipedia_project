import wikipediaapi
import time
from queue import Queue

user_agent = "wikipedia_project (possiblymegansinclair@gmail.com)"
wiki= wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list=[]
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page,target_page):
    print("working on it")
    start_time = time.time()

    queue = Queue() #which items to check next
    visited = set() #keep track of visited links
    parent = {} #keep track of parent

    queue.put(start_page.title)
    visited.add(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        
        if current_page_title == target_page.title:
            break
    
    
        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link]= current_page_title
    
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("this algorithm took", end_time - start_time, "seconds.")
    return path

start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("National Defense Act of 1916")
path = wikipedia_game_solver(start_page, target_page)
print(path)
