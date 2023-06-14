import requests
from bs4 import BeautifulSoup #helps in doing static scraping 

# sending get request to the URL 
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

# save the response inside the page variable
page = requests.get(URL)

# it is going to print normal byte data
# print(page.content)


def get_citations_needed_count(page):
    # to parse it from byte to html 
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    citations_needed = soup.find_all(text="citation needed")
    return len(citations_needed)

def get_citations_needed_report(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    citations_needed = soup.find_all(text="citation needed")
    
    # Open the output file in write mode
    with open('citations_report.txt', 'w') as file:
        # Iterate over the citations and retrieve their parent <p> tags
        for citation in citations_needed:
            paragraphs = citation.find_parent('p').text.strip()
            file.write(f"{paragraphs}\n")
            print(f"{paragraphs}\n")
            file.write("\n")
            print("\n")
            file.write("***************")
            print("***************")
            file.write("\n")
            print("\n")
    
    print("report is ready inside citations_report.txt file.")
    
print(get_citations_needed_count(page))
get_citations_needed_report(page)  