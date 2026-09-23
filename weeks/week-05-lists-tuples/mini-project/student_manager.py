danh_sach = []
while True:
    print("\n" + "="*30)
    print("===QUẢN LÝ SINH VIÊN===")
    print("1. Thêm sinh viên")
    print("2. Xem danh sách")
    print("3. Cập nhật thông tin")
    print("4. Xóa sinh viên")
    print("0. Kết thúc chương trình")
    print("="*30)

    lua_chon = input("Vui lòng chọn chức năng (0-4): ")

    if lua_chon == '1':
        print("Bạn đã chọn thêm sinh viên")
        masv = input("Nhập mã số sinh viên: ")
        hoten = input("Nhập họ tên sinh viên: ")
        tuoi = int(input("Nhập tuổi: "))
        ngay_sinh = input("Nhập ngày sinh: ")
        gioi_tinh = input("Nhập giới tính: ")
        sinh_vien = [masv, hoten, tuoi, ngay_sinh, gioi_tinh]
        danh_sach.append(sinh_vien)
        print("Bạn đã thêm sinh viên thành công")

    elif lua_chon == '2':
        print("Bạn đã chọn xem danh sách")
        print("Danh sách: ", danh_sach)

    elif lua_chon == '3':
        print("Bạn đã chọn cập nhật thông tin")
        masv = input("Nhập mã số sinh viên cần cập nhật: ")
        for sinh_vien in danh_sach:
            if sinh_vien[0] == masv:
                print("Nhập thông tin mới")
                hoten = input("Nhập họ tên sinh viên: ")
                tuoi = int(input("Nhập tuổi: "))
                ngay_sinh = input("Nhập ngày sinh: ")
                gioi_tinh = input("Nhập giới tính: ")
                sinh_vien[1] = hoten
                sinh_vien[2] = tuoi
                sinh_vien[3] = ngay_sinh
                sinh_vien[4] = gioi_tinh
                print("Bạn đã cập nhật thông tin thành công")
                break
        else:
            print("Không tìm thấy sinh viên với mã số", masv)

    elif lua_chon == '4':
        print("Bạn đã chọn xóa sinh viên")
        masv = input("Nhập mã số sinh viên cần xóa: ")
        for sinh_vien in danh_sach:
            if sinh_vien[0] == masv:
                danh_sach.remove(sinh_vien)
                print("Bạn đã xóa sinh viên thành công")
                break
        else:
            print("Không tìm thấy sinh viên với mã số", masv)

    elif lua_chon == '0':
        print("Kết thúc chương trình")
        break
