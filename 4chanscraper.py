import requests
from bs4 import BeautifulSoup

def list_boards():
    url = "https://a.4cdn.org/boards.json"
    r = requests.get(url)

    if r.status_code != 200:
        print("Error fetching boards")
        return None

    data = r.json()
    boards = data["boards"]

    print("\n--- AVAILABLE BOARDS ---\n")

    for i, b in enumerate(boards):
        print(f"{i}) /{b['board']}/ - {b['title']}")

        
    	
while True:

    d = input("\n1) Scrape a board\n2) Scrape a thread\n3) List Boards\n4) Quit\n> ")

    # OPTION 1: Scrape board (list threads)
    if d == "1":

        board = input("Enter board: ").strip()

        url = f"https://a.4cdn.org/{board}/catalog.json"
        r = requests.get(url)

        if r.status_code != 200:
            print("Error: invalid board")
            continue

        data = r.json()

        for page in data:
            for thread in page["threads"]:
                thread_id = thread["no"]

                title = thread.get("sub") or thread.get("com", "")
                clean = BeautifulSoup(title, "html.parser").get_text()

                print(thread_id, "|", clean)


    elif d == "2":
	
        board = input("Enter board: ").strip()
        thread_id = input("Enter thread ID: ").strip()

        url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
        r = requests.get(url)

        if r.status_code != 200:
            print("Error: thread not found")
            continue

        data = r.json()

        print("\n--- THREAD ---\n")

        for post in data["posts"]:
            post_id = post["no"]

            html = post.get("com", "")
            text = BeautifulSoup(html, "html.parser").get_text()

            print(f"[{post_id}]")
            print(text)
            print("-" * 50)
	

    elif d == "3":
        board = list_boards()
        if board:
            print(f"\nSelected board: /{board}/")

    # OPTION 3: Quit
    elif d == "4":
        break

    else:
        print("Invalid option")
