class Order():
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher ):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""

    def calculate_total_amount(self):
        self.total_amount = self.unit_price * self.quantity + self.voucher - self.shipping_fee

    def classify_order(self):
        if self.total_amount < 500000:
            self.order_type = "Nhỏ"
        elif self.total_amount < 2000000:
            self.order_type = "Trung Bình"
        elif self.total_amount < 10000000:
            self.order_type = "lớn"
        else:
            self.order_type = "VIP"

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self):
        id = input("Mời nhập mã đơn hàng mới: ")
        customer_name = input("Mời nhập tên khách hàng của đơn hàng mới: ")
        product_name = input("Mời nhập tên đơn hàng mới: ")
        unit_price = float(input("Mời nhập giá đơn hàng mới: "))
        quantity = int(input("Mời nhập số lượng đơn hàng mới: "))
        shipping_fee = float(input("Mời nhập phí vận chuyển đơn hàng mới: "))
        voucher = float(input("Mời nhập voucher đơn hàng mới: "))
        new_order = Order(id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher)
        new_order.calculate_total_amount()
        new_order.classify_order()
        self.orders.append(new_order)
        print("thêm đơn hàng thành công!")

    def show_all(self):
        if not self.orders:
            print("Danh sách đơn hàng trống!")
            return

        print("--- Danh sách đơn hàng ---")
        print(f"{"Mã đơn hàng":<15} | {"Tên khách hàng":<20} | {"Tên sản phẩm":<20} | {"Đơn giá":<15} | {"Số lượng":<15} | {"Phí vận chuyển":<20} | {"Voucher":<10} | {"Tổng tiền":<15} | {"Phân loại đơn hàng":<25}")
        print("-" * 170)
        for order in self.orders:
            print(f"{order.id:<15} | {order.customer_name:<20} | {order.product_name:<20} | {order.unit_price:<15} | {order.quantity:<15} | {order.shipping_fee:<20} | {order.voucher:<10} | {order.total_amount:<15} | {order.order_type:<25}")
        print("-" * 170)

    def update_order(self):
        update_id = input("nhập id đơn hàng muốn sửa: ")
        for order in self.orders:
            if order.id == update_id:
                order.unit_price = float(input("mời bạn nhập đơn giá mới: "))
                order.quantity = int(input("mời bạn nhập số lượng đơn hàng mới: "))
                order.shipping_fee = float(input("mời bạn nhập phí vận chuyển mới: "))
                order.voucher = float(input("mời bạn nhập voucher mới: "))
                print("Cập nhật đơn hàng thành công!")
                return
        print("không tìm thấy đơn hàng!")

    def delete_order(self):
        delete_id = input("mời bạn nhập mã đơn hàng muốn xóa: ")
        for order in self.orders:
            if order.id == delete_id:
                confirm = input ("Bạn có chắc muốn xóa đơn hàng này không? (Y/N):")
                if (confirm == "Y" or "y"):
                    self.orders.remove(order)
                    print("xóa đơn hàng thành công!")
                    return
        print("không tìm thấy mã sản phẩm cần xóa!")

    def search_order(self):
        search_name = input("mời nhập tên khách hàng hoặc tên sản phẩm cần tìm: ")
        search_rerult = []
        for order in self.orders:
            if search_name == order.customer_name or search_name == order.product_name:
                search_rerult.append(order)
                for order in search_rerult:
                    if not search_rerult:
                        print("không tìm thấy sản phẩm: ")
                    else:
                        print("-" * 170)
                        print(f"{order.id:<15} | {order.customer_name:<20} | {order.product_name:<20} | {order.unit_price:<15} | {order.quantity:<15} | {order.shipping_fee:<20} | {order.voucher:<10} | {order.total_amount:<15} | {order.order_type:<25}")
                        print("-" *170)

main = OrderManager()
while True:
    choice = input("""
================ MENU ================
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Cập nhật đơn hàng
4. Xóa đơn hàng
5. Tìm kiếm đơn hàng
6. Thoát
=====================================
Nhập lựa chọn của bạn:
""")
    match choice:
        case "1":
            main.show_all()
        case "2":
            main.add_order()
        case "3":
            main.update_order()
        case "4":
            main.delete_order()
        case "5":
            main.search_order()
        case "6":
            print("thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")