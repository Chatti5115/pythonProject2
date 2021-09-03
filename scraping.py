import requests
url = "http://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010021&q_fdate=2020"

html_text = requests.get(url).text

# print(html_text)



from bs4 import BeautifulSoup

soup = bs4(html_text, "html.parent")

tab = soup.find("table" , {"class": "listtbl_c100"})
print(tab)