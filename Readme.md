# 📘 Đồ án Python: Ứng dụng Quản lý Bán hàng và Đặt hàng bằng Tkinter

## 🎯 Mục tiêu đề tài

Xây dựng ứng dụng quản lý bán hàng với các chức năng chính:

- Quản lý sản phẩm (thêm, sửa, xóa, tìm kiếm)
- Quản lý đơn đặt hàng (tạo đơn hàng, tính tổng tiền)
- Giao diện người dùng bằng Tkinter
- Lưu trữ dữ liệu bằng JSON hoặc SQLite

---

## 👥 Thành viên nhóm và phân công công việc

### 👤 Thành viên 1 – Phân tích, thiết kế và báo cáo

- Phân tích yêu cầu chức năng
- Thiết kế sơ đồ Use Case, luồng giao diện
- Lên ý tưởng bố cục giao diện người dùng
- Viết tài liệu báo cáo: mở đầu, phân tích, kết luận
- Chuẩn bị slide trình bày

---

### 👤 Thành viên 2 – Thiết kế giao diện (GUI) với Tkinter

- Thiết kế giao diện chính (Main window)
- Tạo giao diện quản lý sản phẩm
- Tạo giao diện đặt hàng (giỏ hàng, hóa đơn)
- Điều hướng và xử lý sự kiện các button

---

### 👤 Thành viên 3 – Xử lý dữ liệu và logic

- Tạo và thao tác với file JSON hoặc SQLite
- Viết hàm xử lý: thêm/xóa/sửa sản phẩm, tính tiền
- Kết nối dữ liệu với giao diện Tkinter
- Kiểm tra lỗi, tối ưu thao tác dữ liệu

---

## 🗂️ Cấu trúc thư mục dự án

```plaintext
do_an_quan_ly_ban_hang/
├── main.py                  # Tập tin khởi chạy chính
├── gui/
│   ├── main_window.py       # Giao diện chính
│   ├── product_gui.py       # Giao diện quản lý sản phẩm
│   └── order_gui.py         # Giao diện đặt hàng
├── data/
│   ├── db.json              # File lưu dữ liệu
│   └── data_handler.py      # Xử lý đọc/ghi dữ liệu
├── report/
│   ├── bao_cao.docx         # Tài liệu báo cáo
│   └── slide.pptx           # Slide thuyết trình
```
