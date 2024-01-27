import requests
import re

cookies = {
    'ZHE': '1629fa76c1b52ab713db1fd980073c87',
    'PHPSESSID': '2t7g1e4ulfpfgt96lfuvcgs7n4',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.zone-h.org/archive/published=0',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}
notf = input("Notif : ")
# response = requests.get('https://www.zone-h.org/archive/notifier=1915', cookies=cookies, headers=headers)
for i in range(1, 50):
    dz = requests.get('https://www.zone-h.org/archive/notifier=' + notf +"/page=" + str(i), cookies=cookies)
    dzz = dz.content.decode('utf-8')  # Décodez le contenu ici
    print('https://www.zone-h.org/archive/notifier=' + notf +"/page=" + str(i))
    Hunt_urls = re.findall('<td>(.*)\n\s+</td>', dzz)
    if '/mirror/id/' in dzz:
        for xx in Hunt_urls:
            qqq = xx.replace('...', '')
            print('    [' + '*' + '] ' + qqq.split('/')[0])
            with open(notf + '.txt', 'a+') as rr:
                rr.write("http://" + qqq.split('/')[0] + '\n')
