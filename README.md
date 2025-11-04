# 🌦️ ỨNG DỤNG LẤY DỮ LIỆU THỜI TIẾT TỪ OPENWEATHER BẰNG PYTHON

## 🧩 Giới thiệu
Ứng dụng này sử dụng **API của OpenWeather** kết hợp với thư viện **`requests`** trong Python để lấy dữ liệu thời tiết theo tên thành phố.  
Kết quả được trả về dưới dạng **JSON**, sau đó được chuyển sang **dictionary** (`dict`) để trích xuất các thông tin như:  
- Nhiệt độ  
- Hiện tượng 
- Mô tả thời tiết  
và hiển thị lên **giao diện người dùng (UI)** bằng PyQt hoặc console.

Hướng ứng dụng: ứng dụng dùng để tích hợp với những chương trình lớn hơn trong tương lai

---

# Mô tả chi tiết cách thực hiện
## 1. Cú pháp API
**Cú pháp**: https://api.openweathermap.org/data/2.5/weather?q=<tên_thành_phố>
**Endpoint gốc**: https://api.openweathermap.org/data/2.5/weather 
**Các tham số truy vấn**: Các tham số được nối vào sau dấu ? và cách nhau bằng &, tạo nên yêu cầu tùy chỉnh:
-q={city}: Chỉ định đối tượng cần tìm kiếm (Thành phố).
-units=metric: Yêu cầu đơn vị đo lường theo hệ mét (nhiệt độ theo độ C).
-appid={api_key}: Khóa API dùng để xác thực ứng dụng của bạn với máy chủ.
-lang=vi: Yêu cầu mô tả thời tiết được trả về bằng Tiếng Việt.
-F-string: Việc sử dụng f"..." là phương pháp hiệu quả nhất trong Python để chèn biến (city, api_key) vào URL, tạo ra một yêu cầu động.
## 2. Cú pháp API và cách gửi yêu cầu đến API và nhận phản hồi từ server:
Khai báo Client HTTP: Nhập thư viện chuẩn để biến Python thành một máy khách (client) có khả năng gửi và nhận yêu cầu HTTP.
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
### ➜ <Response [200]> Đây là kết quả đầu ra quan trọng nhất. Mã Trạng thái HTTP 200 (OK) xác nhận rằng:
-Giao tiếp mạng thành công.
-Máy chủ đã xử lý yêu cầu (bao gồm cả xác thực API Key).
-Phần thân (body) của phản hồi hiện đã chứa chuỗi dữ liệu JSON mong muốn, sẵn sàng cho bước xử lý tiếp theo (response.json()).
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
weather_id = data["weather"][0]["id"] #truy cập khóa weather (list) lấy phần tử đầu [0], truy cập khóa id (số dùng để xác định loại thời tiết) Mã ID này là đầu vào cho hàm weather_emoji(), tách biệt logic chọn biểu tượng khỏi logic lấy dữ liệu. <br>
weather_description = data["weather"][0]["description"] #truy cập cùng đối tượng thời tiết, lấy khóa description <br>

---

**##🧩 3. Tiềm năng Tích hợp và Mở rộng**
**Khả năng Tái sử dụng (Reusability**): Toàn bộ logic API có thể dễ dàng đóng gói thành một hàm hoặc lớp (ví dụ: WeatherService) và được import vào bất kỳ dự án Python lớn nào khác (như web framework Django/Flask, hay các ứng dụng phân tích dữ liệu).
**Dễ dàng Mở rộng:** Nếu sau này ta muốn lấy thêm dữ liệu như áp suất, độ ẩm, hoặc tốc độ gió, ta chỉ cần thêm một dòng trích xuất dữ liệu (ví dụ: data["main"]["humidity"]) vào module dịch vụ mà không cần thay đổi giao diện PyQt hiện tại.
**Trừu tượng hóa (Abstraction):** Lớp giao diện (PyQt) chỉ cần biết rằng nó gọi một hàm và nhận lại nhiệt độ, ID, và mô tả. Nó không cần quan tâm đến URL, API key, hay cách JSON được xử lý. Điều này giúp code sạch sẽ và dễ bảo trì.


