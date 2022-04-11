#import beautifulsoup and request here
from pip._vendor import requests
from bs4 import BeautifulSoup




    
    
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