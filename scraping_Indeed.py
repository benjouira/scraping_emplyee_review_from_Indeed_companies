from bs4 import BeautifulSoup
import requests
import csv

url = f"https://www.indeed.com/cmp"
page_Limit = 500

def build_url(base_url = url , company="Meta", page = 0):
    # page 2 url exemple 
    # https://www.indeed.com/cmp/Dollar-General/reviews?start=20
    # page 1 start=0 / page 2 start=20 /page 3 start=40 / ect...
    return f"{base_url}/{company}/reviews?start={page}"

def scrape_page(page=0,company="Meta"):
    # Function to scrape a single page in indeed
    response = requests.get(build_url(company=company, page=page ))
    reviews = []
    soup = BeautifulSoup(response.text,"html.parser")
    reviewsfeild = soup.find_all("div", class_="css-5cqmw8")

    for r in reviewsfeild:
        title = r.find(class_= "css-82l4gy").text
        review = r.find(class_= "css-1cxc9zk").find(class_="css-82l4gy").text
    # employee info contains the job title, employee current satet, 
    # the company branch location and the review date 
    # ex: "Assistant Store Manager/Cashier (Former Employee) - Ahoskie, NC - December 30, 2021"
        employee_Info = r.find(class_= "css-xvmbeo").text
        rating = r.find(class_= "css-1c33izo").text
        reviews.append(
            
            {
                "title" : title,
                "review" : review,
                "employee_Info" : employee_Info,
                "rating" : rating,
            }
        )
    return (reviews)


def scrape(company):
    # Functio to scrape to page_limit
    questions = []
    for i in range(0,page_Limit+1,20):
        page_questions = scrape_page (i,company)
        if page_questions in questions:
            break
        questions.append(page_questions)
    return questions
# *****************************************************************
def scrape_company_info(company="Meta"):
    url = f"https://www.indeed.com/cmp/{company}/reviews?start=00"

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    company_image = soup.find("div", class_="css-1268hzc").find("img")['src']
    company_rating = soup.find("span", class_="css-htn3vt").text

    return (company_image, company_rating)

if __name__ == "__main__":
    company = 'instagram'
    reviews = scrape(company)
    cmpInfo = scrape_company_info(company)
    print(reviews)
    print(len(reviews))
    print(cmpInfo)
    pass
