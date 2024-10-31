import requests

def fetch_station_data():
    url = "https://datagov.mot.go.th/api/3/action/datastore_search"
    params = {
        "resource_id": "169ba151-f992-4cfc-8f7b-1662e1abc5c9",  # ID ของข้อมูลที่ต้องการ
        "limit": 10  # จำนวนผลลัพธ์ที่ต้องการดึง
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # ตรวจสอบข้อผิดพลาด HTTP

        data = response.json()
        return data  # ส่งคืนข้อมูล
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

# เรียกใช้ฟังก์ชันและแสดงผลข้อมูล
if __name__ == "__main__":
    station_data = fetch_station_data()
    if station_data:
        print(station_data)
