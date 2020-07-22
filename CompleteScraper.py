from bs4 import BeautifulSoup
import urllib.request
import csv

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def CompleteScraper(content):
    file1=open("URL.txt","r")
    line=file1.readlines()

    headers=[]
    required_lines=[]
    for url in line:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html,'html.parser')
        table = soup.findAll('table')[0]
        tr = table.findAll(['tr'])[0:11]
        links=soup.find_all('a')
        csvFile = open("OutputData.csv",'a',newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        f=open("OutputLinks.txt","a")
        try:   
            for l in links:
                if content in l.text:
                    required_lines.append(str(l))
                    f.write(str(l))
                    
                    
                
            for cell in tr:
                th = cell.find_all('th')
                th_data = [col.text.strip('\n') for col in th]
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                #print(row[4])
                if len(th_data)!=0:
                    required_lines.append(th_data)
                    writer.writerow(th_data)
                for i in row:
                    if content in i:
                        required_lines.append(row)
                        writer.writerow(row)      
            
        finally:   
            csvFile.close()
            f.close()
    return required_lines
