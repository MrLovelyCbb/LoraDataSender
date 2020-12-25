#!/usr/bin/python3

import requests
import time
import random
import json
import datetime
import string
import threading

# payload random mac
data_macs = [
    "004a77012e130209",
    "004a770124008ffa",
    "004a77012400ce7b",
    "004a77012400ce44",
    "004a77012400dac5",
    "004a77012400edba"
]


def get_data_macs():
    return random.sample(data_macs, 1)[0]


# payload random appeui
data_appeuis = [
    "2c26c50124194000",
    "2c26c50124194001",
    "2c26c50124194002",
    "2c26c50124194003",
    "2c26c50124194004",
    "2c26c50124194005",
    "2c26c50124194006",
    "2c26c50124194007",
    "2c26c50124194008",
    "2c26c50124194009"
]


def get_data_appeuis():
    return random.sample(data_appeuis, 1)[0]


# payload get nowTime
def get_nowTime():
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time, '%Y%m%d%H%M%S')
    times = time.time()
    # print(time_str)
    # 毫秒级时间戳
    print(int(round(times * 1000)))
    # 微秒级时间戳
    # print(int(round(times * 1000000)))
    return time_str


def currentNowTime():
    times = time.time()
    return int(round(times * 1000))


# payload random data

# 无线烟感 020000
# 020400
# 020402
# 020002
# 020000

data_datas = [
    "130164640024",
    "020001",
    "020002",
    "020003",
    "020004",
    "020005"
]


def get_datas():
    return random.sample(data_datas, 1)[0]


# payload get reserver
def get_reserver():
    return "";


# payload random data_type

data_types = [
    "223",
    "002",
    "22"
]


def get_data_type():
    return random.sample(data_types, 1)[0]


def get_gateways():
    gatewaysObj = {}
    gatewaysObj["fcntdown"] = random.randrange(100, 400, 2)
    gatewaysObj["fcntup"] = random.randrange(400, 450, 1)
    gatewaysObj["gweui"] = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    gatewaysObj["rssi"] = random.randrange(-100, 100, 1)
    gatewaysObj["lsnr"] = round(random.uniform(1, 10), 2)
    gatewaysObj["alti"] = random.randrange(1, 100)
    gatewaysObj["lng"] = "114.33754"
    gatewaysObj["lati"] = "30.35769"
    return gatewaysObj


def send_Http_Post(mac="004A77012400D871"):
    # url = "http://localhost:8080/device/getUrlData2Str"
    # url = "http://192.168.0.103:63401/api/monitoring_api/receiveEvent"
    # url = "http://192.168.0.131:50000/agent"
    url = "http://192.168.2.26:55000/agent"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }

    dataObj = {}
    dataObj["mac"] = get_data_macs()
    dataObj["appeui"] = get_data_appeuis()
    dataObj["last_update_time"] = get_nowTime()
    dataObj["data"] = get_datas()
    dataObj["reserver"] = get_reserver()
    dataObj["data_type"] = get_data_type()

    gatewaysObj = get_gateways()
    gatewaysArr = [gatewaysObj, gatewaysObj, gatewaysObj]

    dataObj["gateways"] = gatewaysArr
    dataObj["times"] = currentNowTime()

    jsonDataStr = json.dumps(dataObj)
    print(jsonDataStr)

    # payload = {
    # 	"mac":"004A77012400D871","appeui":"2c26c50124194000","last_update_time":"20190604184310","data":"020000","reserver":"null","data_type":2,"gateways":[{"fcntdown":"410","fcntup":"408","gweui":"70B3D5FFFE88B684","rssi":"-83","lsnr":"7.8","alti":"64","lng":"114.33754","lati":"30.35769"},{"fcntdown":"410","fcntup":"408","gweui":"70B3D5FFFE88B689","rssi":"-71","lsnr":"8.2","alti":"70","lng":"114.33693","lati":"30.35826"},{"fcntdown":"410","fcntup":"408","gweui":"70B3D5FFFE88B68A","rssi":"-88","lsnr":"4.2","alti":"83","lng":"114.33657","lati":"30.35724"}]
    # }
    response = requests.post(url, data=json.dumps(dataObj), headers=headers).text

    # 2019 06 04 18 43 10
    # print("Server response ", response)


def loop_send_req(mac, num):
    while True:
        time.sleep(1)
        for i in range(num):
            send_Http_Post(mac)


# def loop_send_request(mac, num):
#     sendCount = num
#     while True:
#         time.sleep(1)
#         sendCount = num
#         while sendCount >= 1:
#             try:
#                 send_Http_Post(mac)
#                 sendCount = sendCount - 1
#             except Exception:
#                 print("exception")
#                 time.sleep(20)


# for num in range(1, 100):
#     send_Http_Post("004A77012400D872")


if __name__ == '__main__':

    try:
        t1 = threading.Thread(target=loop_send_req, args=("004A77012400D871", 200,))
        t2 = threading.Thread(target=loop_send_req, args=("004A77012400D872", 200,))
        t3 = threading.Thread(target=loop_send_req, args=("004A77012400D873", 200,))
        t4 = threading.Thread(target=loop_send_req, args=("004A77012400D874", 200,))
        t5 = threading.Thread(target=loop_send_req, args=("004A77012400D875", 200,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
    except Exception:
        print("Error: 无法启动线程")
