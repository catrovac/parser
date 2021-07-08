from bs4 import BeautifulSoup
import requests
import fake_useragent
import time
import lxml
import os
import csv


class Parrser(object):
    user = fake_useragent.UserAgent().data_browsers['chrome'][0]
    links_auto = {}
    url = ""
    ip_port = []
    proxy_url = 'https://hidemy.name/ru/proxy-list/'
    no_search_auto = ["matiz", "Smart" "qq", "Daewoo", "Lada", "Matiz"]
    mark_auto = {}

    def proxy(self):
        ress = requests.get(self.proxy_url, headers={"user-agent": self.user}).text
        soup = BeautifulSoup(ress, "lxml")
        data_text = soup.find("tbody").find_all("tr")
        for i in data_text:
            x_ip = str(i.find_all("td")[0].text) + ":" + str(i.find_all("td")[1].text)
            self.ip_port.append(x_ip)
        # print(self.ip_port)

    def autoria(self):
        try:
            x = 0
            ip_list = self.ip_port[0]
            x_ip = ip_list.split(":")
            ip = x_ip[0]
            port = x_ip[1]
            print(ip, port)
            for num_page in range(1, 14):
                self.url = f"https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&year[0].gte=2005&categories.main.id=1&country.import.usa.not=-1&price.USD.gte=3500&price.USD.lte=4000&price.currency=1&gearbox.id[1]=2&abroad.not=0&custom.not=1&page={num_page}&size=10"
                ress = requests.get(self.url, headers={"user-agent": self.user}, proxies={ip: port})
                if ress.status_code == 200:
                    ress = ress.text
                    with open("index.html", "w", encoding="UTF-8-sig") as file:
                        file.write(ress)

                    with open("index.html", encoding="UTF-8-sig") as file:
                        index_data = file.read()

                    soup = BeautifulSoup(index_data, "lxml")
                    data_page = soup.find("div", class_="app-content").find_all("div", class_="content-bar")
                    for auto in data_page:
                        links = str(auto.find("a").get("href")).strip()
                        mark_auto = str(auto.find("span", class_="blue bold").text).strip()
                        if mark_auto not in self.links_auto:
                            self.links_auto[mark_auto] = links
                        else:
                            if links not in self.links_auto.values():
                                mark_auto = mark_auto+str("_1")
                                self.links_auto[mark_auto] = links
                            else:
                                continue
                    #print(self.links_auto)
                    time.sleep(2)
            self.data_auto(self, ip, port)
        except ConnectionError as conn:
            x += 1
            print(conn)

    def data_auto(self, ip, port):
        for key, value in self.links_auto.items():
            if not os.path.exists(f"{key}"):
                os.mkdir(f"{key}")
                print(key, value)

            res = requests.get(value,headers={"user-agent":self.user},proxies={ip:port})
            if res.status_code == 200:
                res = res.text
                soup = BeautifulSoup(res,"lxml")
                with open(f"{key}/{key}.html", "w",encoding="UTF-8-sig") as file:
                    file.write(res)
            with open(f"{key}/{key}.html", encoding="UTF-8-sig") as file:
                data_one_auto = file.read()

            soup = BeautifulSoup(data_one_auto, "lxml")
            name_auto = soup.find("h3", class_="auto-content_title").text
            try:
                auto_number = soup.find("div", class_="t-check").find_all("span")[0].text[:10]
                xstr = str(auto_number).split(" ")
                auto_number = "".join(xstr).upper()
            except AttributeError as errortype:
                auto_number = "Не указано"
            except IndexError as out:
                auto_number = "Не указанно"
            try:
                disel = soup.find_all("dd")[2].find("span", class_="argument").text  # .find("span", class_="argument")
            except AttributeError as erortype:
                print(erortype)
                disel = "Не указанно"
            except IndexError as out:
                disel ="Не указано"
            try:
                operations = soup.find_all("dd")[4].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                operations = "Не указанно"
            except IndexError as out:
                operations ="Не указано"
            try:
                prob = soup.find_all("dd")[7].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                prob = "Не указанно"
            except IndexError as out:
                prob ="Не указано"
            try:
                fuel_consumption = soup.find_all("dd")[9].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                fuel_consumption = "Не указанно"
            except IndexError as out:
                fuel_consumption ="Не указано"
            try:
                kpp = soup.find_all("dd")[10].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                kpp = "Не указанно"
            except IndexError as out:
                kpp ="Не указано"
            # try:
            #     colors = soup.find_all("dd")[11].find("span", class_="argument").text
            # except AttributeError as errortype:
            #     print(errortype)
            #     colors = "Не указанно"
            try:
                ads_auto = soup.find_all("dd")[13].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                ads_auto = "Не указанно"
            except IndexError as out:
                all_ads ="Не указано"
            try:
                ads_auto2 = soup.find_all("dd")[14].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                ads_auto2 = "Не указанно"
            except IndexError as out:
                ads_auto2 ="Не указано"
            try:
                ads_auto3 = soup.find_all("dd")[15].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                ads_auto3 = "Не указанно"
            except IndexError as out:
                ads_auto3 ="Не указано"
            try:
                ads_auto4 = soup.find_all("dd")[16].find("span", class_="argument").text
            except AttributeError as errortype:
                print(errortype)
                ads_auto4 = "Не указанно"
            except IndexError as out:
                ads_auto4 ="Не указано"

            all_ads = ads_auto +" "+ ads_auto2 +" " + ads_auto3 + " "+ads_auto4
            try:
                user_name = soup.find("h4", class_="seller_info_name bold").text
                user_name = str(user_name).strip()
            except AttributeError as errortype:
                print(errortype)
                user_name = "Не указанно"
            except IndexError as out:
                user_name ="Не указано"
            try:
                num_phone = soup.find("div", class_="popup-successful-call-desk size24 bold green mhide green").text
            except AttributeError as errortype:
                print(errortype)
                num_phone = "Не указанно"
            except IndexError as out:
                num_phone="Не указано"
            print(num_phone,user_name,name_auto,auto_number,disel,operations,prob,kpp,fuel_consumption,all_ads)
            # for nn in dvig:
            #     print(nn)
            # print(name_auto,auto_number,disel)
            # print(soup)
            with open("index_auto.csv","a",encoding="utf-8-sig",newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    [
                        num_phone,
                        user_name,
                        name_auto,
                        auto_number,
                        disel,
                        operations,
                        #colors,
                        prob,
                        kpp,
                        fuel_consumption,
                        all_ads
                    ]
                )
            time.sleep(3)


proxy = Parrser
proxy.proxy(self=proxy)
proxy.autoria(self=proxy)
