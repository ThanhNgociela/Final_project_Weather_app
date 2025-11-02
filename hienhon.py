import sys #python tương tác với hệ điều hành
import requests #thư viện để giao tiếp giữa Python với API thời tiết
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from giaodienWeather import Ui_Form_giaodienWeather #Import giao diện từ file .ui của Qt Designer
#Lớp quản lí giao diện
from Xu_ly import * #import hàm weather_emoji bên Xu_ly

class MainWindow():
    def __init__(self):
        self.main_win = QWidget() #Khởi tạo Qwidget trống và gán vào main_win
        self.ui = Ui_Form_giaodienWeather() #Khởi tạo giao diện được dịch sang .py từ .ui
        self.ui.setupUi(self.main_win) #gắn các thành phần từ self.ui lên self.main_win
        self.lienketnutlenh() #kết nối sác sự kiện hàm nút bấm


#Hàm hiển thị cửa sổ
    def show(self):
        self.main_win.show()

#Hàm liên kết nut Tìm với hàm xử lý
    def lienketnutlenh(self):
        self.ui.btnTim.clicked.connect(self.xuly)

#Hàm thông báo lỗi
    def hien_loi(self, message):
        self.ui.txtTemp.setText("N/A")
        self.ui.txtIcon.setText("❓")
        self.ui.txtDes.setText(message)

#Hàm lấy và hiện dữ liệu
    def hien_thoitiet(self, data):
        temperature_c = data["main"]["temp"] #truy cập vào khóa main (dict con), khóa temp để lấy giá trị temp đã ở độ C (units=metric ở url)
        weather_id = data["weather"][0]["id"] #truy cập khóa weather (list) lấy phần tử đầu [0], truy cập khóa id (số dùng để xác định loại thời tiết)
        weather_description = data["weather"][0]["description"] #truy cập cùng đối tượng thời tiết, lấy khóa description
#xuất ra kết quả trên giao diện
        self.ui.txtTemp.setText(f"{temperature_c:}°C")
        self.ui.txtIcon.setText(weather_emoji(weather_id)) #Gọi hàm get_weather emoji
        self.ui.txtDes.setText(weather_description.capitalize())  #capitalize để viết hoa chữ cái đầu

    def xuly(self):
        api_key = "8089a847e3d2871d80a885c4667527c2" #gán api với api của tài khoản cá nhân trên web Open Weather
        city = self.ui.txtCity.text() #lấy dữ liệu đầu vào từ giao diện
        #Lỗi nếu nhập ô rỗng
        if not city:
            self.display_error("Vui lòng nhập tên thành phố.")
            return
        #tạo URL API, chèn tên thành phố và khóa API KEY, lấy dữ liệu từ địa chỉ
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=vi"
        response = requests.get(url, timeout=5) #gửi yêu cầu GET đến URL API trên, nếu máy chủ không phản hồi trong 5s, yêu cầu bị hủy
        # KIỂM TRA MÃ CODE API TRƯỚC KHI TRUY CẬP DỮ LIỆU
        if response.status_code == 200: #code = 200 là lấy dữ liệu thành công
            data = response.json() #trả về dữ liệu được chuyển từ chuỗi JSON thành dictionary
            self.hien_thoitiet(data)
        else:
            self.hien_loi(f"Lỗi truy cập dữ liệu (Code {response.status_code})")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()  # Tạo đối tượng quản lý widget
    window.show()
    app.exec()