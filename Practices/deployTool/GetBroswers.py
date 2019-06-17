import requests
from bs4 import BeautifulSoup


class GetBrowser:
    ff = "https://chocolatey.org/packages/Firefox"
    opera = 'https://chocolatey.org/packages/Opera'
    chrome = "https://chocolatey.org/packages/GoogleChrome"

    def __init__(self):
        pass

    def get_opera(self):

        response = requests.get(self.opera)
        soup = BeautifulSoup(response.content, "html.parser")
        mydivs = soup.findAll("td", {"class": "version"})
        current = mydivs[0].find('span').text
        with open('opera.txt', 'w') as f:
            f.write(current + '\n')
            for div in mydivs:
                a = div.find("a")
                try:
                    b = a.contents
                    f.write(b.pop(0) + '\n')
                except AttributeError:
                    continue
                    # print("AttributeError: 'NoneType' object has no attribute 'contents'")
            f.close()

    def get_ff(self):

        response = requests.get(self.ff)
        soup = BeautifulSoup(response.content, "html.parser")
        mydivs = soup.findAll("td", {"class": "version"})
        current = mydivs[0].find('span').text
        with open('ff.txt', 'w') as f:
            f.write(current + '\n')
            for div in mydivs:
                a = div.find("a")
                try:
                    b = a.contents
                    f.write(b.pop(0) + '\n')
                except AttributeError:
                    continue
            f.close()

    def get_chrome(self):
        response = requests.get(self.chrome)
        soup = BeautifulSoup(response.content, "html.parser")
        mydivs = soup.findAll("td", {"class": "version"})
        current = mydivs[0].find('span').text
        with open('chrome.txt', 'w') as f:
            f.write(current + '\n')
            for div in mydivs:
                a = div.find("a")
                try:
                    b = a.contents
                    f.write(b.pop(0) + '\n')
                except AttributeError:
                    continue
            f.close()

    def get_ie(self):
        with open('ie.txt', 'w') as f:
            f.write('ie11' + '\n')
            f.write('ie10' + '\n')
            f.write('ie9' + '\n')
            f.close()

    # Parse Version Number
    def get_chrome_version(self):
        response = requests.get(self.chrome)
        soup = BeautifulSoup(response.content, "html.parser")
        mydivs = soup.findAll("td", {"class": "version"})
        current = mydivs[0].find('span').text
        with open('chrome.txt', 'w') as f:
            f.write(current + '\n')
            for div in mydivs:
                a = div.find("a")
                try:
                    b = a.contents
                    s = b.pop(0).split(' ')[-1]
                    print(s)
                    continue
                except AttributeError:
                    continue
            f.close()

# ## Testing
# xhr = GetBrowser()
# # xhr.get_chrome_version()
# xhr.get_chrome()
# xhr.get_ff()
# xhr.get_opera()
# xhr.get_ie()
