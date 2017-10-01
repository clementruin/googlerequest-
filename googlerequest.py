from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.google.fr/search?client=safari&rls=en&q=patrick+balkany&ie=UTF-8&oe=UTF-8&gfe_rd=cr&dcr=0&ei=jtzPWYTuBuPAXrmrq7AN')
soup = BeautifulSoup(r.text, "html.parser")

request_boxes = soup.find_all("div", class_="g", limit=2)

for box in request_boxes:
	title_tag = box.find("a")
	title = title_tag.text
	description_tag = box.find("span", class_="st")
	description = description_tag.text
	print("Title: {} \nDescription: {}\n\n".format(title, description))

	