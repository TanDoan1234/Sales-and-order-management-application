import os
import json
import re
import uuid
from typing import Dict, List, Optional, Tuple, Union, Any

def data_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)

def ensure_data_dir():
    data_dir = os.path.dirname(data_path("users.json"))
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

class DataManager:
    """
    Lớp quản lý dữ liệu cho ứng dụng bán hàng và quản lý đơn hàng.
    Xử lý việc quản lý người dùng, sản phẩm, đơn hàng và lưu trữ dữ liệu.
    """
    def __init__(self):
        """
        Khởi tạo DataManager bằng cách tải tất cả dữ liệu từ các file JSON.
        Thiết lập người dùng, sản phẩm, đơn hàng, giỏ hàng, tin nhắn, đánh giá và người dùng hiện tại.
        """
        self.users: Dict[str, Dict[str, str]] = self.load_users()
        self.main_products: List[Dict[str, Any]] = self.load_main_products()
        self.user_products: Dict[str, List[Dict[str, Any]]] = self.load_user_products()
        self.orders: Dict[str, List[Dict[str, Any]]] = self.load_orders()
        self.user_orders: Dict[str, List[Dict[str, Any]]] = self.load_user_orders()
        self.carts: Dict[str, List[Dict[str, Any]]] = self.load_carts()
        self.messages: Dict[str, List[str]] = self.load_messages()
        self.reviews: Dict[str, List[Dict[str, Any]]] = self.load_reviews()
        self.current_user: Optional[str] = self.load_current_user()

    def load_users(self) -> Dict[str, Dict[str, str]]:
        try:
            with open(data_path("users.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        ensure_data_dir()
        with open(data_path("users.json"), "w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4, ensure_ascii=False)

    def load_main_products(self):
        try:
            with open(data_path("main_products.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_main_products(self):
        ensure_data_dir()
        with open(data_path("main_products.json"), "w", encoding="utf-8") as file:
            json.dump(self.main_products, file, indent=4, ensure_ascii=False)

    def load_user_products(self):
        try:
            with open(data_path("user_products.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_user_products(self):
        ensure_data_dir()
        with open(data_path("user_products.json"), "w", encoding="utf-8") as file:
            json.dump(self.user_products, file, indent=4, ensure_ascii=False)

    def load_orders(self):
        try:
            with open(data_path("orders.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_orders(self):
        ensure_data_dir()
        with open(data_path("orders.json"), "w", encoding="utf-8") as file:
            json.dump(self.orders, file, indent=4, ensure_ascii=False)

    def load_user_orders(self):
        try:
            with open(data_path("user_orders.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_user_orders(self):
        ensure_data_dir()
        with open(data_path("user_orders.json"), "w", encoding="utf-8") as file:
            json.dump(self.user_orders, file, indent=4, ensure_ascii=False)

    def load_carts(self):
        try:
            with open(data_path("carts.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_carts(self):
        ensure_data_dir()
        with open(data_path("carts.json"), "w", encoding="utf-8") as file:
            json.dump(self.carts, file, indent=4, ensure_ascii=False)

    def load_messages(self):
        try:
            with open(data_path("messages.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_messages(self):
        ensure_data_dir()
        with open(data_path("messages.json"), "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4, ensure_ascii=False)

    def load_reviews(self):
        try:
            with open(data_path("reviews.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_reviews(self):
        ensure_data_dir()
        with open(data_path("reviews.json"), "w", encoding="utf-8") as file:
            json.dump(self.reviews, file, indent=4, ensure_ascii=False)

    def load_current_user(self):
        try:
            with open(data_path("current_user.json"), "r", encoding="utf-8") as file:
                data = json.load(file)
                username = data.get("username")
                if username in self.users:
                    return username
                return None
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def save_current_user(self):
        ensure_data_dir()
        with open(data_path("current_user.json"), "w", encoding="utf-8") as file:
            json.dump({"username": self.current_user}, file, indent=4, ensure_ascii=False)

    def add_message(self, message, user=None):
        target_user = user if user else self.current_user
        if target_user:
            if target_user not in self.messages:
                self.messages[target_user] = []
            self.messages[target_user].append(message)
            self.save_messages()

    def login(self, username: str, password: str) -> bool:
        """
        Xác thực người dùng và đặt họ làm người dùng hiện tại.

        Args:
            username (str): Tên đăng nhập
            password (str): Mật khẩu

        Returns:
            bool: True nếu đăng nhập thành công, False nếu thất bại
        """
        if username in self.users and self.users[username]['password'] == password:
            self.current_user = username
            self.carts.setdefault(self.current_user, [])
            self.messages.setdefault(self.current_user, [])
            self.reviews.setdefault(self.current_user, [])
            self.user_products.setdefault(self.current_user, [])
            self.user_orders.setdefault(self.current_user, [])
            self.save_carts()
            self.save_messages()
            self.save_current_user()
            return True
        return False

    def register(self, username: str, password: str, phone: str, email: str) -> Tuple[bool, str]:
        """
        Đăng ký tài khoản người dùng mới với các điều kiện kiểm tra.

        Args:
            username (str): Tên đăng nhập
            password (str): Mật khẩu
            phone (str): Số điện thoại (phải bắt đầu bằng 0 và có 10 chữ số)
            email (str): Email (phải kết thúc bằng @gmail.com)

        Returns:
            tuple: (bool, str) - (trạng thái thành công, thông báo)
        """
        if not username or not password or not phone or not email:
            return False, "Vui lòng nhập đầy đủ thông tin!"
        if username in self.users:
            return False, "Tên đăng nhập đã tồn tại! Vui lòng chọn tên khác."
        if any(user_data['phone'] == phone for user_data in self.users.values()):
            return False, "Số điện thoại đã được đăng ký! Vui lòng chọn số khác."
        if not re.match(r"^0\d{9}$", phone):
            return False, "Số điện thoại phải có 10 chữ số và bắt đầu bằng 0!"
        if not email.endswith("@gmail.com"):
            return False, "Email phải kết thúc bằng @gmail.com!"

        self.users[username] = {"password": password, "phone": phone, "email": email}
        self.save_users()
        self.current_user = username
        self.carts.setdefault(self.current_user, [])
        self.messages.setdefault(self.current_user, [])
        self.reviews.setdefault(self.current_user, [])
        self.user_products.setdefault(self.current_user, [])
        self.user_orders.setdefault(self.current_user, [])
        self.save_carts()
        self.save_messages()
        self.save_current_user()
        return True, "Đăng ký thành công!"

    def logout(self):
        self.current_user = None
        self.save_current_user()

    def add_to_cart(self, product: Dict[str, Any]) -> None:
        """
        Thêm sản phẩm vào giỏ hàng của người dùng hiện tại.

        Args:
            product (dict): Sản phẩm cần thêm vào giỏ hàng
        """
        if self.current_user not in self.carts:
            self.carts[self.current_user] = []
        self.carts[self.current_user].append(product)
        self.save_carts()
        self.add_message(f"Thêm {product['name']} vào giỏ hàng!")

    def remove_from_cart(self, index):
        cart = self.carts.get(self.current_user, [])
        if index < len(cart):
            product = cart.pop(index)
            self.carts[self.current_user] = cart
            self.save_carts()
            self.add_message(f"Xóa {product['name']} khỏi giỏ hàng!")
            return True
        return False

    def buy_single_product(self, product: Dict[str, Any], quantity: int, address: str) -> None:
        """
        Xử lý việc mua một sản phẩm.

        Args:
            product (dict): Sản phẩm cần mua
            quantity (int): Số lượng mua
            address (str): Địa chỉ giao hàng
        """
        if self.current_user not in self.orders:
            self.orders[self.current_user] = []
        order = {"product": product, "quantity": quantity, "address": address}
        self.orders[self.current_user].append(order)
        self.save_orders()

        seller = product['booth']
        if seller != "Admin":
            if seller not in self.user_orders:
                self.user_orders[seller] = []
            seller_order = {
                "product_id": product['id'],
                "quantity": quantity,
                "total_price": product['price'] * quantity
            }
            self.user_orders[seller].append(seller_order)
            self.save_user_orders()
            self.add_message(f"Tài khoản {self.current_user} đã mua {product['name']} ({quantity} cái) từ gian hàng của bạn!", user=seller)

        self.add_message(f"Mua {product['name']} ({quantity} cái) từ gian hàng {product['booth']} thành công!")

    def add_user_product(self, name: str, price: float) -> bool:
        """
        Thêm sản phẩm mới vào gian hàng của người dùng hiện tại.

        Args:
            name (str): Tên sản phẩm
            price (float): Giá sản phẩm

        Returns:
            bool: True nếu thêm sản phẩm thành công
        """
        if self.current_user not in self.user_products:
            self.user_products[self.current_user] = []

        new_product = {"id": str(uuid.uuid4()), "name": name, "price": price, "booth": self.current_user}
        self.user_products[self.current_user].append(new_product)
        self.save_user_products()
        self.add_message(f"Đã đăng sản phẩm {name} để bán!")
        return True

    def edit_user_product(self, index, new_name, new_price):
        user_prods = self.user_products.get(self.current_user, [])
        if index < len(user_prods):
            user_prods[index]['name'] = new_name
            user_prods[index]['price'] = new_price
            self.save_user_products()
            self.add_message(f"Đã sửa sản phẩm {new_name}!")
            return True
        return False

    def remove_user_product(self, index):
        user_prods = self.user_products.get(self.current_user, [])
        if index < len(user_prods):
            product = user_prods.pop(index)
            self.user_products[self.current_user] = user_prods
            self.save_user_products()
            self.add_message(f"Đã gỡ sản phẩm {product['name']}!")
            return True
        return False

    def submit_review(self, product: Dict[str, Any], rating: int) -> bool:
        """
        Gửi đánh giá cho sản phẩm.

        Args:
            product (dict): Sản phẩm cần đánh giá
            rating (int): Số sao đánh giá (thường từ 1-5)

        Returns:
            bool: True nếu gửi đánh giá thành công
        """
        if self.current_user not in self.reviews:
            self.reviews[self.current_user] = []

        user_reviews = self.reviews[self.current_user]
        for review in user_reviews:
            if review['product_id'] == product['id']:
                review['rating'] = rating
                break
        else:
            user_reviews.append({"product_id": product['id'], "rating": rating})

        self.save_reviews()
        self.add_message(f"Đã đánh giá {product['name']}: {rating} sao")
        return True

    def change_password(self, old_password: str, new_password: str) -> Tuple[bool, str]:
        """
        Thay đổi mật khẩu của người dùng hiện tại.

        Args:
            old_password (str): Mật khẩu cũ
            new_password (str): Mật khẩu mới

        Returns:
            tuple: (bool, str) - (trạng thái thành công, thông báo)
        """
        if self.users[self.current_user]['password'] != old_password:
            return False, "Mật khẩu cũ không đúng!"
        if not new_password:
            return False, "Mật khẩu mới không được để trống!"

        self.users[self.current_user]['password'] = new_password
        self.save_users()
        self.add_message("Thay đổi mật khẩu thành công!")
        return True, "Thay đổi mật khẩu thành công!"

    def delete_account(self) -> bool:
        """
        Xóa tài khoản người dùng hiện tại và tất cả dữ liệu liên quan.

        Returns:
            bool: True nếu xóa tài khoản thành công
        """
        if self.current_user in self.users:
            del self.users[self.current_user]
        if self.current_user in self.carts:
            del self.carts[self.current_user]
        if self.current_user in self.orders:
            del self.orders[self.current_user]
        if self.current_user in self.messages:
            del self.messages[self.current_user]
        if self.current_user in self.reviews:
            del self.reviews[self.current_user]
        if self.current_user in self.user_products:
            del self.user_products[self.current_user]
        if self.current_user in self.user_orders:
            del self.user_orders[self.current_user]

        self.save_users()
        self.save_carts()
        self.save_orders()
        self.save_messages()
        self.save_reviews()
        self.save_user_products()
        self.save_user_orders()
        self.current_user = None
        self.save_current_user()
        return True 