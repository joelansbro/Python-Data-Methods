import requests
from bs4 import BeautifulSoup

# script to scrape job listings off of indeed - could go further and add these now into an object to print it out into an excel sheet for analytics or something

def webParam(options):
    base = 'https://uk.indeed.com/jobs?'
    url = base + options
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def parsingResponse(soup):
    job_all = []
    job_list = []
    result = soup.find(id="mosaic-zone-jobcards")

    job_elements = result.find_all("td", class_="resultContent")

    for job_element in job_elements:
        try:
            company_location = job_element.find("div", class_="companyLocation")
            job_title = job_element.find("h2", class_="jobTitle")
            salary_range = job_element.find("div", class_="salary-snippet" )
            job_list.append(job_title.text + "\n")
            job_list.append(company_location.text + "\n")
            job_list.append(salary_range.text + "\n")
            job_all.append(job_list)
            job_list = []
        except AttributeError:
            print("Attribute error!")
        except StopIteration:
            break
    return job_all

if __name__ == "__main__":
    job = input("What is the job title you are looking for?\n")
    location = input("What is your job location?\n")
    options = 'q=' + job.replace(' ','%20') + '&l=' + location
    soup = webParam(options)
    job_all = parsingResponse(soup)
    print(job_all)