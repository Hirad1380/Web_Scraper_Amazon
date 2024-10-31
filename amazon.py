# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()

# url = "https://www.amazon.co.uk/s?k=laptop"
# driver.get(url)

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# titles = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
# prices = soup.find_all('span', class_='a-price-whole')
# images = soup.find_all('img', class_='s-image')


# print("Length Title: ", len(titles))
# print("Length Price: ", len(prices))
# print("Length Image: ", len(images))


# results = []

# min_length = min(len(titles), len(prices), len(images))
# print("Minimum: ", min_length)

# try:
#     for i in range(min_length):
#         result = {
#             'ID': i+1,
#             'TITLE': titles[i].text.strip() if i < len(titles) else '',
#             'PRICE': prices[i].text.strip() if i < len(prices) else '',
#             'IMAGE': images[i]['src'] if i < len(images) else ''
#         }
#         results.append(result)

#     with open('laptops_1.csv', mode='w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['ID', 'TITLE', 'PRICE', 'IMAGE']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         for result in results:
#             writer.writerow(result)

#     driver.quit()

# except Exception as e:
#     print("Error: ", e)


# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# # wait = WebDriverWait(driver, 10)

# # url = "https://www.amazon.co.uk/s?k=laptop&page=2&qid=1714320925&ref=sr_pg_{}"
# url = "https://www.amazon.nl/s?k=Laptops&rh=n%3A16497142031&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
# for page in range(1, 3):
#     # driver.get(url.format(page))
#     driver.get(url)

#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     titles = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
#     prices = soup.find_all('span', class_='a-price-whole')
#     images = soup.find_all('img', class_='s-image')

#     print("Page: ", page)
#     print("Length Title: ", len(titles))
#     print("Length Price: ", len(prices))
#     print("Length Image: ", len(images))
    

#     results = []

#     min_length = min(len(titles), len(prices), len(images))
#     print("Minimum: ", min_length)
#     print("-----------------------------------------------")

#     try:
#         for i in range(min_length):
#             result = {
#                 'ID': i+1,
#                 'TITLE': titles[i].text.strip().replace('"',' ').replace(',','-') if i < len(titles) else '',
#                 'PRICE': prices[i].text.strip().replace('"','').replace(',','').replace('.','') if i < len(prices) else '',
#                 'IMAGE': images[i]['src'] if i < len(images) else ''
#             }
#             results.append(result)

#         with open('laptops_{}.csv'.format(page), mode='w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ['ID', 'TITLE', 'PRICE', 'IMAGE']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#             writer.writeheader()
#             for result in results:
#                 writer.writerow(result)

#     except Exception as e:
#         print("Error: ", e)

# driver.quit()



# ------------------------It is working------------------------



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()



# url = "https://www.amazon.com/s?k=laptops&crid=2X83JEYIU2H5X&sprefix=lapt%2Caps%2C848&ref=nb_sb_noss_2"

# for page in range(1, 3):
#     driver.get(url)

#     # element = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[34]/div/div/span/a[3]')
#     # )
#     # element.click()

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     titles = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
#     prices = soup.find_all('span', class_='a-price-whole')
#     images = soup.find_all('img', class_='s-image')

#     print("Page:", page)
#     print("Length Title:", len(titles))
#     print("Length Price:", len(prices))
#     print("Length Image:", len(images))

#     results = []

#     min_length = min(len(titles), len(prices), len(images))
#     print("Minimum:", min_length)
#     print("-----------------------------------------------")

#     try:
#         for i in range(min_length):
#             result = {
#                 'ID': i + 1,
#                 'TITLE': titles[i].text.strip().replace('"', ' ').replace(',', '-') if i < len(titles) else '',
#                 'PRICE': prices[i].text.strip().replace('"', '').replace(',', '').replace('.', '') if i < len(prices) else '',
#                 'IMAGE': images[i]['src'] if i < len(images) else ''
#             }
#             results.append(result)

#         with open('laptops_{}.csv'.format(page), mode='w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ['ID', 'TITLE', 'PRICE', 'IMAGE']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for result in results:
#                 writer.writerow(result)


#         page = soup.find('a', class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
#         url = url + str(page)


#         # element = WebDriverWait(driver, 10).until(
#         #     EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[34]/div/div/span/a[3]'))
#         # )
#         # element.click()
            
#     except Exception as e:
#         print("Error:", e)


# driver.quit()



import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()




url = "https://www.amazon.nl/s?k=laptops&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=MSIQ17BQX24K&sprefix=laptop%2Caps%2C1454&ref=nb_sb_noss_1"

for page in range(1, 3):
    driver.get(url)

    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[34]/div/div/span/a[3]')
    # )
    # element.click()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
    prices = soup.find_all('span', class_='a-price-whole')
    images = soup.find_all('img', class_='s-image')

    print("Page:", page)
    print("Length Title:", len(titles))
    print("Length Price:", len(prices))
    print("Length Image:", len(images))

    results = []

    min_length = min(len(titles), len(prices), len(images))
    print("Minimum:", min_length)
    print("-----------------------------------------------")

    try:
        for i in range(min_length):
            result = {
                'ID': i + 1,
                'TITLE': titles[i].text.strip().replace('"', ' ').replace(',', '-') if i < len(titles) else '',
                'PRICE': prices[i].text.strip().replace('"', '').replace(',', '').replace('.', '') if i < len(prices) else '',
                'IMAGE': images[i]['src'] if i < len(images) else ''
            }
            results.append(result)

        with open('laptops_{}.csv'.format(page), mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ID', 'TITLE', 'PRICE', 'IMAGE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow(result)


        page = soup.find('a', class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
        url = url + str(page)


        # element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[34]/div/div/span/a[3]'))
        # )
        # element.click()
            
    except Exception as e:
        print("Error:", e)

driver.quit()