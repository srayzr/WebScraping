from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
from django.http import HttpResponse


def scrape_and_print_jobs(request):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = bs(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    job_data_list = []

    for job in jobs:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        job_data_list.append({'company_name': company_name, 'skills': skills})

    print(job_data_list)  # Add this line to print the scraped data

    context = {'job_data': job_data_list}
    return render(request, 'polls/index.html', context)


def index(request):
    job_data_list = scrape_and_print_jobs(request)  # Pass the request object
    context = {'job_data': job_data_list}
    return render(request, 'polls/index.html', context)


