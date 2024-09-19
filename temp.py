import requests
from bs4 import BeautifulSoup
import json
import re

# session = requests.Session()
# login_url = 'https://www.residencyexplorer.org/saml/initiatesinglesignon'
# payload = {
#     'username': 'bhavinthakkar15',
#     'password': '********'
# }
#
# # Perform login
# loginresponse=session.post(login_url, data=payload)
#
# print(loginresponse.text)
#
# # session.get('https://www.residencyexplorer.org/')
# response = session.get('https://www.residencyexplorer.org/Program/GetByIdWithMedicalSpecialty/823', headers={'Referer': 'https://www.residencyexplorer.org/Explore'})
#
# # print(response.text)
# # Parse the response with BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')
#
# titles = soup.find_all('h2')
# for title in titles:
#     print(title.text)
#
# data = soup.find_all('td', attrs={'role':'gridcell', 'aria-colindex':3})
#
# print(data)

# Failed attempt at SAML above

cookies = {
    '_ga': 'GA1.2.1612393910.1726611954',
    '_gid': 'GA1.2.412284900.1726611954',
    'saml-session': '476c7bb7-fd71-4e9c-a523-56d6b63fcf3b',
    '_gat_UA-120102284-1': '1',
    '.MyApp.Security.Cookie': 'CfDJ8GHbvU6klDxKus49WJfVAAvDHsX-O_eb488KpmMEzzdYvaabBm3-ZJ2Uh4X6-O9_EKn720dL2wpIYUsUOhrl4oaQMZlJdr0xPpnQEqnyTO-BJl9lO2OTdZBNToF1-c4Z4tlN_MXKyz7-RP9n4KxMIMihHNZBpl5JJ2VcLKzpBeM0BEGnMaXgEISdN5_ylwbgeL-wPOuZF2hDQsohM4pN2in7eZyHV_lmNgaQbKYg9LR05cRsxPaq1dy6ay9WRIN0YL8uSZyICACbrbHGc-HuUAZJkbtU8VsdBkQWdxdy9PQb5tVubFSYjP4MAm1KX-lW3-LrnDoos4P4YNL519OuZtI73vJ2vDJr30J1kT0PM9hAs3RDAqQ062K2_683juZ55P-1tYaJalLdIkPB65ATRnqyJD81IceeL80-vDzgRKwhXtdq9kqZld40dcylfVsOj2SgpsekvPFM0gXwXWMztM17dGyj8DlIXHiIZ9UtoAXOqTvUE0zygQvglpHNZyuMeajCfIdUeLrtnw8g8CS0ZLdqENjQ54L7vm_9VHDviLwsLXpuc5-Y0t9CvMJb4JGHMC-hICmEl-IGoa1NKyW32IP0Ko7BPKsuDspgCcRhsXTskloikuwy4Waofnrw3tfeYpiddbzzeKW4UaqZrKSCBeGV_mF2K0KXta-r74c0gVFYaW2CuEnL0df8zZVEGupLVMAuaqE9RrICV1JsmniLQ1bUB00P6q0lzHBlkN8s5SBCTAsbbVic01S-ACUtbV1AQfdG-P0kiaveTstPd76D2hER7hZGpU1dAZ9ocfOz5xn5NAdduOvXVCOhqjyPwG0Fa3020zGheRSm74DnaKGXWpI3Xx9WAGD-4JN0kT7021VBO_PJHrKufAkPyP0qdBdqWEE6P5jtRIqKFhn2JA-YiQCUYxQ0j7NPlq3TrMdZRyKVKZ-FWIT6FuXXHxuUHKRGA_VVadcv85Q-y_iVu-weXL0',
    '.AspNetCore.Antiforgery.mEZFPqlrlZ8': 'CfDJ8GHbvU6klDxKus49WJfVAAvsLjDX4a-bcsuykjPG_e1mgOqQpHimRcYvZWVQF-tg416qp4gkzxDPqmOgPDS9Y-dopIzPTLHAwxQW57lz0gi5NGjXovE0ZpUpxco2EQ27Y6SVNjfDPpGEwEyDgf0qQ2M',
    'AWSALB': 'le7yQhWUaWsbl6mCTPK2as4KeS/QCy/FY6qUzVQ4hYHglwo0qQzKxTIdjqPevXG8UNJ70ran3mSKBSswvAc5GwJboodavc6ElIHrvl+FtP+rHzb0oF/hHrNIMPTW',
    'AWSALBCORS': 'le7yQhWUaWsbl6mCTPK2as4KeS/QCy/FY6qUzVQ4hYHglwo0qQzKxTIdjqPevXG8UNJ70ran3mSKBSswvAc5GwJboodavc6ElIHrvl+FtP+rHzb0oF/hHrNIMPTW',
    '_ga_32W01K6L23': 'GS1.2.1726715318.6.1.1726724683.0.0.0',
    '_gali': 'ce56de23-5eec-4265-82e4-f38db9c69d08',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '_ga=GA1.2.1612393910.1726611954; _gid=GA1.2.412284900.1726611954; saml-session=476c7bb7-fd71-4e9c-a523-56d6b63fcf3b; _gat_UA-120102284-1=1; .MyApp.Security.Cookie=CfDJ8GHbvU6klDxKus49WJfVAAvDHsX-O_eb488KpmMEzzdYvaabBm3-ZJ2Uh4X6-O9_EKn720dL2wpIYUsUOhrl4oaQMZlJdr0xPpnQEqnyTO-BJl9lO2OTdZBNToF1-c4Z4tlN_MXKyz7-RP9n4KxMIMihHNZBpl5JJ2VcLKzpBeM0BEGnMaXgEISdN5_ylwbgeL-wPOuZF2hDQsohM4pN2in7eZyHV_lmNgaQbKYg9LR05cRsxPaq1dy6ay9WRIN0YL8uSZyICACbrbHGc-HuUAZJkbtU8VsdBkQWdxdy9PQb5tVubFSYjP4MAm1KX-lW3-LrnDoos4P4YNL519OuZtI73vJ2vDJr30J1kT0PM9hAs3RDAqQ062K2_683juZ55P-1tYaJalLdIkPB65ATRnqyJD81IceeL80-vDzgRKwhXtdq9kqZld40dcylfVsOj2SgpsekvPFM0gXwXWMztM17dGyj8DlIXHiIZ9UtoAXOqTvUE0zygQvglpHNZyuMeajCfIdUeLrtnw8g8CS0ZLdqENjQ54L7vm_9VHDviLwsLXpuc5-Y0t9CvMJb4JGHMC-hICmEl-IGoa1NKyW32IP0Ko7BPKsuDspgCcRhsXTskloikuwy4Waofnrw3tfeYpiddbzzeKW4UaqZrKSCBeGV_mF2K0KXta-r74c0gVFYaW2CuEnL0df8zZVEGupLVMAuaqE9RrICV1JsmniLQ1bUB00P6q0lzHBlkN8s5SBCTAsbbVic01S-ACUtbV1AQfdG-P0kiaveTstPd76D2hER7hZGpU1dAZ9ocfOz5xn5NAdduOvXVCOhqjyPwG0Fa3020zGheRSm74DnaKGXWpI3Xx9WAGD-4JN0kT7021VBO_PJHrKufAkPyP0qdBdqWEE6P5jtRIqKFhn2JA-YiQCUYxQ0j7NPlq3TrMdZRyKVKZ-FWIT6FuXXHxuUHKRGA_VVadcv85Q-y_iVu-weXL0; .AspNetCore.Antiforgery.mEZFPqlrlZ8=CfDJ8GHbvU6klDxKus49WJfVAAvsLjDX4a-bcsuykjPG_e1mgOqQpHimRcYvZWVQF-tg416qp4gkzxDPqmOgPDS9Y-dopIzPTLHAwxQW57lz0gi5NGjXovE0ZpUpxco2EQ27Y6SVNjfDPpGEwEyDgf0qQ2M; AWSALB=le7yQhWUaWsbl6mCTPK2as4KeS/QCy/FY6qUzVQ4hYHglwo0qQzKxTIdjqPevXG8UNJ70ran3mSKBSswvAc5GwJboodavc6ElIHrvl+FtP+rHzb0oF/hHrNIMPTW; AWSALBCORS=le7yQhWUaWsbl6mCTPK2as4KeS/QCy/FY6qUzVQ4hYHglwo0qQzKxTIdjqPevXG8UNJ70ran3mSKBSswvAc5GwJboodavc6ElIHrvl+FtP+rHzb0oF/hHrNIMPTW; _ga_32W01K6L23=GS1.2.1726715318.6.1.1726724683.0.0.0; _gali=ce56de23-5eec-4265-82e4-f38db9c69d08',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.residencyexplorer.org/Explore',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'wm_consumer.id': '7dbaa194-8094-4b99-aa5e-f33452a30e0e',
    'wm_svc.env': 'prod',
    'wm_svc.name': 'MELO-BATCH',
}

# 1500 such programs
response = requests.get(
    'https://www.residencyexplorer.org/Program/GetByIdWithMedicalSpecialty/875',
    cookies=cookies,
    headers=headers,
)

soup = BeautifulSoup(response.text, 'html.parser')

# The only DOM element I have had luck with
names = soup.find_all('h1', class_='program-detail-name')

for name in names:
    print(name.text)


main_element = soup.find('main')

scripts = main_element.find_all('script',attrs={'type':'text/javascript'})


constant_name = 'locals'  # Replace with the actual constant name
pattern = r'var|let|const\s+' + constant_name + r'\s*=\s*([^;]+)'
match = re.search(pattern, scripts[0].text)

if match:
    constant_value = match.group(1)
    #This json has useful stuff. Need to parse and put in CSV along with other DOM elements
    print(f"Constant '{constant_name}' value: {constant_value}")
else:
    print(f"Constant '{constant_name}' not found.")




# tds = soup.find_all('td')
# for td in tds:
#     print(td.text)

# alignment_grid = soup.find_all('div', attrs={'id': 'alignment-grid'})
#
# for alignment in alignment_grid:
#
#     print(alignment)
    # table=alignment.find_all()
    # print(table)
    # children = alignment.find('tr', attrs={'class': 'k-master-row'})
    # for child in children:
    #     print(child.text)
