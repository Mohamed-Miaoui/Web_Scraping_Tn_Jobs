from bs4 import BeautifulSoup

# web scraping basics from a local html file -----------------------------
with open("local_WS_test/home.html", "r") as html_file:
    content = html_file.read()
    # lxml is py lib to manage html and wml documents (parser)
    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all("div", class_="card")
    for cs in course_cards:
        course_name = cs.h5.text
        course_price = cs.a.text.split()[-1]  # -1 last element

        print(f"{course_name} costs {course_price}")
