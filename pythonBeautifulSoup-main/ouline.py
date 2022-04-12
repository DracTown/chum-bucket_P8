from pip._vendor import requests
from bs4 import BeautifulSoup
import json

def displayJobDetails():
    print("Display job details")

jobResults = []
def getJobList(role, location):
    # Complete the missing part of this function here
    url = "https://www.indeed.com/jobs?q=" + role + "&l=" + location
    payload = {}
     headers = {
        'Cookie': 'CTK=1fvqtabopq05p800; INDEED_CSRF_TOKEN=zObWlBjnc0oLVAS3aidx8lvSAZOgVukr; JSESSIONID=627D0DD3248349B13DE876D0883448E6; PREF="TM=1649096863522:L=' + location + '"; RQ="q=' + role + '&l=+' + location + '&ts=1649703016594:q=+' + role + '+&l=+' + location + '&ts=1649699917805&pts=1649129121573"; UD="LA=1649703016:LV=1649127002:CV=1649698419:TS=1649096863:SG=8138e1e8a2add6bf3bc2dced46849fdb"; indeed_rcc="PREF:CTK:UD:RQ"; jaSerpCount=2'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    for job in soup.find_all('div', attrs={'class': 'slider_container css-11g4k3a eu4oa1w0'}):
        jobTitle = job.find_next('h2', class_='jobTitle')
        companyName = job.find_next('span', class_='companyName')
        jobDescription = job.find_next('div', class_='job-snippet')
        salary = job.find_next('div', class_='salary-snippet-container')
        if salary:
            salary=salary.text
        else:
         salary="None listed"
        jobs = [jobTitle.text, companyName.text, jobDescription.text, salary]
        jobResults.append(jobs)

   def saveDataInJSON(jobDetails):
    # Complete the missing part of this function here
   
    print("Saving data to JSON")
    
    
#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the Location to serch")
    location=input()
    getJobList(role,location)
    for i in jobResults:
     print(i)    
if __name__ == '__main__':
    main()