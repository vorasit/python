from covid19openapi import ThaiCovid19
import json
import requests

if __name__ == '__main__':
    thai = ThaiCovid19()
    today = thai.get('today')
    timeline = thai.get('timeline')
    all_field = thai.get_all()

    print(today)
    con = str(today['Confirmed'])
    print("ติดเชื้อสะสม " + con)

    area = thai.get('cases_sum')
    province = area['Province']
    p1 = str(province['Lampang'])
    p2 = str(province['Prachinburi'])
    print("จังหวัด ลำปาง มีคนรวมติดเชื้อภายในจังหวัด = " + p1)
    print("จังหวัด ปราจีนบุรี มีคนรวมติดเชื้อภายในจังหวัด = "+ p2)
    #print(all_field)