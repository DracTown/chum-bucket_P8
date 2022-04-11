#import beautifulsoup and request here
from pip._vendor import requests
from bs4 import BeautifulSoup


def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
   
    # Complete the missing part of this function here 

    url = "https://www.indeed.com/jobs?q="+ role + "&l=" + location

    payload={}
    headers = {
  'Cookie': 'CTK=1g0crhisekugl800; INDEED_CSRF_TOKEN=H1dD6yjOnmqLbnGqzb4t1a4sPlqW24Bu; JSESSIONID=65BE99942E4DF1EFC32EE45594493F11; PREF="TM=1649698982807:L=Charlotte"; RQ="q=+Software+Developer+&l=+Charlotte&ts=1649698982831"; UD="LA=1649698982:CV=1649698982:TS=1649698982:SG=56e8f01539738038954d8124c56dd2be"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}
    
   response = requests.request("GET", url, headers=headers, data=payload)
    soup=BeautifulSoup(response.text,'html.parser')
    jobTitle = soup.find('h2', class_='jobTitle').text
    companyName = soup.find('span', class_='companyName').text
    jobDescription = soup.find('div', class_='job-snippet').text
    salary = soup.find('div', class_='salary-snippet-container').text
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
    getJobList(role,location)    
if __name__ == '__main__':
    main()