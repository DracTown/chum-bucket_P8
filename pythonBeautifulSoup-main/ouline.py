#import beautifulsoup and request here
from pip._vendor import requests
from bs4 import BeautifulSoup


def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role, location):
    def getJobList(role, location):
    # Complete the missing part of this function here
    jobResults = []
    searchResultsjobTitle = []
    searchResultscompanyName = []
    searchResultsjobDescription = []
    searchResultssalary = []

    url = "https://www.indeed.com/jobs?q=" + role + "&l=" + location

    payload = {}
    headers = {
        'Cookie': 'CTK=1fvqtabopq05p800; INDEED_CSRF_TOKEN=zObWlBjnc0oLVAS3aidx8lvSAZOgVukr; JSESSIONID=627D0DD3248349B13DE876D0883448E6; PREF="TM=1649096863522:L=Charlotte"; RQ="q=Software+Developer&l=+Charlotte&ts=1649703016594:q=+Software+Developer+&l=+Charlotte&ts=1649699917805&pts=1649129121573"; UD="LA=1649703016:LV=1649127002:CV=1649698419:TS=1649096863:SG=8138e1e8a2add6bf3bc2dced46849fdb"; indeed_rcc="PREF:CTK:UD:RQ"; jaSerpCount=2'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobTitle = soup.find_all('h2', attrs={'class': 'jobTitle'})
    companyName = soup.find_all('span', attrs={'class': 'companyName'})
    jobDescription = soup.find_all('div', attrs={'class': 'job-snippet'})
    salary = soup.find_all('div', attrs={'class': 'salary-snippet-container'})
   
    for title in jobTitle:
        searchResultsjobTitle.append(title.text)
    for name in companyName:
        searchResultscompanyName.append(name.text)
        print(name.text)
    for des in jobDescription:
        searchResultsjobDescription.append(des.text)
        print(des.text)
    for sal in salary:
        searchResultssalary.append(sal.text)
        print(sal.text)

    print(len(salary))
    
    
#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the Location to serch")
    location=input()
    getJobList(role,location)    
if __name__ == '__main__':
    main()