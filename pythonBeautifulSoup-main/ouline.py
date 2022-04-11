#import beautifulsoup and request here
from pip._vendor import requests
from bs4 import BeautifulSoup


def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here 

    
    jobTitle = url.find('h2',class_='jobTitle').text
    companyName= url.find('span',class_='companyName').text
    jobDescription = url.find('div',class_='job-snippet').text
    salary = url.find('div',class_='salary-snippet-container').text
    
    jobs = [jobTitle, companyName, jobDescription, salary]
    
    print(jobs)

    
#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the Location to serch")
    location=input()
    getJobList(role, location)    
if __name__ == '__main__':
    main()