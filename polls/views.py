from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Create your views here.
def index(request):
    return HttpResponse("HELLO, world. You're at the polls index.")

def scape_data(request):

    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Firefox(options=firefox_options)

    url = 'https://mahakim.ma/Ar/Services/SuiviAffaires_new/TPI/?Page=ServicesElectronique&TypJur=TPI'
    url1 = 'https://news.ycombinator.com/login'
    driver.get(url)

    courtSelectElement =  driver.find_element(by=By.ID, value='ListCA')
    courtSelect = Select(courtSelectElement)
    courtSelect.select_by_value('18')
    data = {
        'isSelected':'',
        'title':driver.title,
        'court':str(courtSelect.options),
        'message': 'Scrapping completed successfully!'

    }
    driver.quit()
    return JsonResponse(data)