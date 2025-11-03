# 🌦️ ỨNG DỤNG LẤY DỮ LIỆU THỜI TIẾT TỪ OPENWEATHER BẰNG PYTHON

## 🧩 Giới thiệu
Ứng dụng này sử dụng **API của OpenWeather** kết hợp với thư viện **`requests`** trong Python để lấy dữ liệu thời tiết theo tên thành phố.  
Kết quả được trả về dưới dạng **JSON**, sau đó được chuyển sang **dictionary** (`dict`) để trích xuất các thông tin như:  
- Nhiệt độ  
- Hiện tượng 
- Mô tả thời tiết  

và hiển thị lên **giao diện người dùng (UI)** bằng PyQt hoặc console.

---

# Mô tả chi tiết cách thực hiện
## 1. Cú pháp API
https://api.openweathermap.org/data/2.5/weather?q=<tên_thành_phố>
    &units=<đơn_vị>
    &appid=<API_key>
    &lang=<mã_ngôn_ngữ>
    <bt>
    ?q=<tên_thành_phố> ví dụ: Hanoi, Ho Chi Minh City <br>
    &units=<đơn_vị>    ví dụ: metric (°C, m/s), imperial (°F, mph) <br>
    &appid=<API_key>   ví dụ: 8089a847e3d2871d80a885c4667527c2 <br>
    &lang=<mã_ngôn_ngữ>ví dụ: vi (tiếng Việt), en (tiếng Anh) <br>

## 2. Cú pháp API và cách gửi yêu cầu đến API và nhận phản hồi từ server:
**import requests**

city = "Hà Nội"
api_key = "8089a847e3d2871d80a885c4667527c2"

### Tạo URL API: chèn tên thành phố, đơn vị đo, khóa API và ngôn ngữ
**url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=vi"
**
### Gửi yêu cầu GET đến API (để lấy dữ liệu mà không thay đổi máy chủ)
**response = requests.get(url)
**
print(response)
### ➜ <Response [200]> nghĩa là yêu cầu thành công, server phản hồi OK

## 3.Server gửi phản hồi với phần thân phản hồi (body) chứa dữ liệu dưới dạng JSON (trong trường hợp đã kết nổi thành công: <Response [200]> ) :
{
  "coord": {"lon": 105.8412, "lat": 21.0245}, <br>
  "weather": [{"id": 804, "main": "Clouds", "description": "mây đen u ám", "icon": "04d"}], <br>
  "base": "stations", <br>
  "main": {"temp": 18, "feels_like": 18.05, "temp_min": 18, "temp_max": 18, "pressure": 1019, "humidity": 84}, <br>
  "visibility": 10000, <br>
  "wind": {"speed": 4.91, "deg": 11, "gust": 10.87}, <br>
  "clouds": {"all": 100}, <br>
  "dt": 1762131024, <br>
  "sys": {"country": "VN", "sunrise": 1762124408, "sunset": 1762165210}, <br>
  "timezone": 25200, <br>
  "id": 1581130, <br>
  "name": "Hà Nội", <br>
  "cod": 200 <br>
} <br>

## 4. Chuyển dữ liệu từ chuỗi JSON thành dictionary của Python bằng thư viện Requests:
**if response.status_code == 200**: #Thực hiện khi đã thiết lập kết nối thành công với máy chủ web và máy chủ trả phần thân phản hồi với phần thân (body) chứa dữ liệu dưới dạng JSON. <br>
data = response.json() #trả về dữ liệu được chuyển từ chuỗi JSON thành dictionary <br>
print (data) <br>
### --> Kết quả: 
{'coord': {'lon': 105.8412, 'lat': 21.0245}, <br>
'weather': [{'id': 804, 'main': 'Clouds', 'description': 'mây đen u ám', 'icon': '04d'}], <br>
'base': 'stations', <br>
'main': {'temp': 18, 'feels_like': 18.05, 'temp_min': 18, 'temp_max': 18, 'pressure': 1019, 'humidity': 84, 'sea_level': 1019, 'grnd_level': 1019}, <br>
'visibility': 10000, <br>
'wind': {'speed': 4.91, 'deg': 11, 'gust': 10.87}, <br>
'clouds': {'all': 100}, <br>
'dt': 1762131024, <br>
'sys': {'type': 1, 'id': 9308, 'country': 'VN', 'sunrise': 1762124408, 'sunset': 1762165210}, <br>
'timezone': 25200, 'id': 1581130, 'name': 'Hà Nội', 'cod': 200} <br>

## 5. Hiện dữ liệu:
#Khi này, nếu như ta muốn cho giao diện hiện dữ liệu nào thì cứ lấy và bỏ dữ liệu vào 1 biến: <br>
temperature_c = data["main"]["temp"] #truy cập vào khóa main (dict con), khóa temp để lấy giá trị temp đã ở độ C (units=metric ở url) <br>
weather_id = data["weather"][0]["id"] #truy cập khóa weather (list) lấy phần tử đầu [0], truy cập khóa id (số dùng để xác định loại thời tiết) <br>
weather_description = data["weather"][0]["description"] #truy cập cùng đối tượng thời tiết, lấy khóa description <br>
