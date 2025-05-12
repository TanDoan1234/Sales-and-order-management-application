# 🛍️ Ứng Dụng Quản Lý Bán Hàng và Đặt Hàng

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)]()

## 📝 Mô tả

Đây là một ứng dụng quản lý bán hàng và đặt hàng được phát triển bằng Python, sử dụng thư viện Tkinter để xây dựng giao diện người dùng. Ứng dụng cho phép người dùng quản lý sản phẩm, đặt hàng, và theo dõi đơn hàng một cách dễ dàng.

## ✨ Tính năng chính

- 👤 **Quản lý tài khoản**

  - Đăng ký và đăng nhập
  - Thay đổi mật khẩu
  - Xóa tài khoản
  - Quản lý thông tin cá nhân

- 🛍️ **Quản lý sản phẩm**

  - Thêm sản phẩm mới
  - Chỉnh sửa thông tin sản phẩm
  - Xóa sản phẩm
  - Tìm kiếm sản phẩm
  - Xem danh sách sản phẩm

- 🛒 **Giỏ hàng và đặt hàng**

  - Thêm sản phẩm vào giỏ hàng
  - Xem giỏ hàng
  - Đặt hàng
  - Theo dõi trạng thái đơn hàng

- ⭐ **Đánh giá và phản hồi**
  - Đánh giá sản phẩm
  - Xem đánh giá của người dùng khác
  - Gửi tin nhắn phản hồi

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ lập trình**: Python 3.8+
- **GUI Framework**: Tkinter
- **Lưu trữ dữ liệu**: JSON
- **Thư viện chính**:
  - `tkinter`: Xây dựng giao diện người dùng
  - `json`: Xử lý dữ liệu
  - `re`: Xử lý chuỗi và validation

## 💻 Yêu cầu hệ thống

- Python 3.8 hoặc cao hơn
- Hệ điều hành: Windows, macOS, hoặc Linux
- RAM: Tối thiểu 4GB
- Ổ cứng: 100MB trống

## 🚀 Cài đặt

1. Clone repository:

```bash
git clone https://github.com/your-username/sales-management-app.git
cd sales-management-app
```

2. Tạo môi trường ảo (khuyến nghị):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:

Có hai cách để cài đặt các thư viện:

**Cách 1: Cài đặt tất cả thư viện từ file requirements.txt**

```bash
pip install -r requirements.txt
```

**Cách 2: Cài đặt từng thư viện theo nhóm**

- Cài đặt thư viện chính:

```bash
pip install tk==0.1.0
```

- Cài đặt thư viện phát triển:

```bash
pip install pylint==3.0.3 black==24.1.1 pytest==8.0.0 pytest-cov==4.1.0
```

- Cài đặt thư viện tiện ích:

```bash
pip install python-dotenv==1.0.1 tqdm==4.66.1 colorama==0.4.6
```

- Cài đặt thư viện bảo mật:

```bash
pip install bcrypt==4.1.2 cryptography==42.0.2
```

- Cài đặt thư viện xử lý dữ liệu:

```bash
pip install pandas==2.2.0 numpy==1.26.3
```

- Cài đặt thư viện báo cáo:

```bash
pip install reportlab==4.1.0 openpyxl==3.1.2
```

> 💡 **Lưu ý**:
>
> - Nên sử dụng **Cách 1** để đảm bảo cài đặt đúng phiên bản của tất cả thư viện
> - Nếu gặp lỗi khi cài đặt, hãy thử cập nhật pip lên phiên bản mới nhất:
>   ```bash
>   python -m pip install --upgrade pip
>   ```
> - Đối với Windows, nếu gặp lỗi khi cài đặt một số thư viện, bạn có thể cần cài đặt Visual C++ Build Tools

## 🏃‍♂️ Chạy ứng dụng

1. Kích hoạt môi trường ảo (nếu chưa kích hoạt):

```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. Chạy ứng dụng:

```bash
python main.py
```

## 📁 Cấu trúc thư mục

```
sales-management-app/
├── main.py              # File khởi chạy chính
├── gui/                 # Thư mục chứa code giao diện
│   └── gui.py          # Class xử lý giao diện chính
├── data/               # Thư mục chứa dữ liệu và xử lý
│   ├── data_handler.py # Class quản lý dữ liệu
│   └── db.json        # File lưu trữ dữ liệu
└── report/            # Thư mục chứa báo cáo và tài liệu
```

## 🎯 Các lệnh phát triển

- **Chạy ứng dụng**: `python main.py`
- **Kiểm tra lỗi**: `pylint *.py`
- **Format code**: `black *.py`
- **Tạo requirements**: `pip freeze > requirements.txt`

## 🔮 Kế hoạch phát triển

- [ ] Thêm tính năng thanh toán trực tuyến
- [ ] Tích hợp cơ sở dữ liệu SQLite
- [ ] Thêm tính năng xuất báo cáo PDF
- [ ] Tối ưu hóa hiệu suất
- [ ] Thêm tính năng thống kê doanh thu
- [ ] Hỗ trợ đa ngôn ngữ
- [ ] Thêm tính năng quản lý kho hàng
- [ ] Tích hợp API bên thứ ba

## 👥 Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request để đóng góp.

## 📄 Giấy phép

Dự án này được cấp phép theo giấy phép MIT - xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📞 Liên hệ

Nếu bạn có bất kỳ câu hỏi hoặc góp ý nào, vui lòng tạo issue trong repository hoặc liên hệ qua email.
