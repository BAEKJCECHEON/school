

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


# 용소중학교
YONGSO_URLS = {
    "03": "https://school.jbedu.kr/yongso/M01030404/list.do?ymd=20260331",
    "04": "https://school.jbedu.kr/yongso/M01030404/list.do?ymd=20260401",
    "05": "https://school.jbedu.kr/yongso/M01030404/list.do?ymd=20260501",
}

YOUNGGWANG_URLS = {
    "03": "https://school.jbedu.kr/higlory/M01060401/",
    "04": "https://school.jbedu.kr/higlory/M01060401/list?ymd=20260401",
    "05": "https://school.jbedu.kr/higlory/M01060401/list?ymd=20260501",
}


def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


#  용소중 parser
def parse_meal_yongso(html, year, month):
    soup = BeautifulSoup(html, "html.parser")
    result = {}

    days = soup.select("td.tch-has")

    for day in days:
        date_tag = day.select_one("span")
        if not date_tag:
            continue

        date_num = date_tag.text.strip().zfill(2)
        full_date = f"{year}-{month}-{date_num}"

        menu = [li.text.strip() for li in day.select("li")]
        result[full_date] = menu

    return result


#  영광고 parser
def parse_meal_younggwang(html, year, month):
    soup = BeautifulSoup(html, "html.parser")
    result = {}

    days = soup.select("td.tch-has")

    for day in days:
        date_tag = day.select_one("span")
        if not date_tag:
            continue

        date_num = date_tag.text.strip().zfill(2)
        full_date = f"{year}-{month}-{date_num}"

        meals = []

        dls = day.select("dl")

        for dl in dls:
            title = dl.select_one("dt").text.strip()
            items = [li.text.strip() for li in dl.select("li")]

            meals.append(f"[{title}]")
            meals.extend(items)

        result[full_date] = meals

    return result


#  파일명 변경 핵심
def save_json(data, year, month, school):
    filename = f"{school}_{year}{month}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{school} 저장 완료: {filename}")


def crawl_school(urls, school_name, parser):
    now = datetime.now()
    year = now.year

    for month, url in urls.items():
        print(f"[{school_name}] {month}월 크롤링 중...")

        html = fetch_html(url)
        data = parser(html, year, month)

        save_json(data, year, month, school_name)


def main():
    crawl_school(YONGSO_URLS, "yongso", parse_meal_yongso)
    crawl_school(YOUNGGWANG_URLS, "younggwang", parse_meal_younggwang)


if __name__ == "__main__":
    main()