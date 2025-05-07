import requests
from bs4 import BeautifulSoup
import pyodbc


page = requests.get("https://eng.iugaza.edu.ps/%d8%a7%d9%84%d8%a3%d9%82%d8%b3%d8%a7%d9%85/%d9%87%d9%86%d8%af%d8%b3%d8%a9-%d8%a7%d9%84%d8%ad%d8%a7%d8%b3%d9%88%d8%a8/%d8%a7%d9%84%d9%87%d9%8a%d8%a6%d8%a9-%d8%a7%d9%84%d8%aa%d8%af%d8%b1%d9%8a%d8%b3%d9%8a%d8%a9/")

def main(page):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'  # أو اسم السيرفر حسب جهازك
        'DATABASE=FacultyDB;'
        'UID=sa;'  # مثل sa
        'PWD=xxxxxxxxx;'  # كلمة المرور
    )
    cursor = conn.cursor()
    src = page.content
    soup = BeautifulSoup(src, "lxml")


    surAllStaff = soup.find_all("div", {'class': 'col-lg-6'})
    surStuffData = soup.find_all("tbody", {'id':'accordion'})
    decrStuff = surAllStaff[0].find_all("tr", {"class": "bg-dark text-white"})
    for i in range(len(surAllStaff[0].find_all("table"))-1):

        name = ""  # الاسم
        rank =  "" # الرتبة
        email = ""
        website = ""
        phone = ""
        office = ""

        for j in range(len(surStuffData[i].find_all("h5"))):

            cardBodyStuff = surStuffData[i].contents[j*2 +1].find_all("b")



            rank = decrStuff[i].text.strip()
            name = surStuffData[i].contents[j * 2 + 1].find('h5').text.strip()
            email = cardBodyStuff[0].text.strip()
            website = cardBodyStuff[1].text.strip()
            phone = cardBodyStuff[2].text.strip()
            office = cardBodyStuff[3].text.strip()
            print(rank)
            print(name)
            print(email)
            print(website)
            print(phone)
            print(office)





            cursor.execute("""
                INSERT INTO FacultyMembers (FullName, Rank, Email, Website, Phone, OfficeNumber)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [
                name,
                rank,
                email,
                website,
                phone,
                office
            ])

    conn.commit()
    conn.close()






















main(page)
