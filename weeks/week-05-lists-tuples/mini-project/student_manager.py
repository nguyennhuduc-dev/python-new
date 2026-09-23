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

    if lua_chon == "1":
        print("Bạn đã chọn thêm sinh viên")
        so_luong = int(input("Nhập sô lượng sinh viên cần thêm: "))
        if so_luong <= 0:
            print("Số lượng phải lớn hơn 0")
        for i in range(so_luong):
            print("Nhập thông tin sinh viên thứ ", i + 1, ":\n")
            masv = input("Nhập mã số sinh viên: ")
            hoten = input("Nhập họ tên sinh viên: ")
            tuoi = int(input("Nhập tuổi: "))
            ngay_sinh = input("Nhập ngày sinh: ")
            gioi_tinh = input("Nhập giới tính: ")
            sinh_vien = [masv, hoten, tuoi, ngay_sinh, gioi_tinh]
            danh_sach.append(sinh_vien)
            print("Bạn đã thêm sinh viên thành công")

    elif lua_chon == "2":
        print("Bạn đã chọn xem danh sách")
        for i in range(len(danh_sach)):
            print("Sinh viên thứ", i + 1, ":\n")
            sv = danh_sach[i]
            print(f"Mã sv: {sv[0]}\nHọ tên: {sv[1]}\nTuổi: {sv[2]}\nNgày sinh: {sv[3]}\nGiới tính: {sv[4]}\n")

    elif lua_chon == "3":
        print("Bạn đã chọn cập nhật thông tin")
        masv = input("Nhập mã số sinh viên cần cập nhật: ")
        for i in range(len(danh_sach)):
            if danh_sach[i][0] == masv:
                print("Bạn đã tìm thấy sinh viên")
                print("Nhập thông tin mới:\n")
                masv = input("Nhập mã số sinh viên: ")
                hoten = input("Nhập họ tên sinh viên: ")
                tuoi = int(input("Nhập tuổi: "))
                ngay_sinh = input("Nhập ngày sinh: ")
                gioi_tinh = input("Nhập giới tính: ")
                danh_sach[i] = [masv, hoten, tuoi, ngay_sinh, gioi_tinh]
                print("Bạn đã cập nhật thông tin sinh viên thành công")
                break  
            else:
                print("Không tìm thấy sinh viên") 
                
    elif lua_chon == "4":
        print("Bạn đã chọn xóa sinh viên")
        masv = input("Nhập mã số sinh viên cần xóa: ")
        for i in range(len(danh_sach)):
            if danh_sach[i][0] == masv:
                danh_sach.remove(danh_sach[i])
                print("Bạn đã xóa sinh viên thành công")
                break       

    elif lua_chon == "0":
        print("Kết thúc chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")

