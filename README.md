# AES_Cypher by Truong Minh Hieu CNTT 17-07 

**Chủ đề: Xây dựng chương trình mã, giải mã file dữ liệu bằng sử dụng thuật toán AES**
**Yêu cầu:** 
	+ phân tích ý tưởng
	+ phân tích sơ đồ hoạt động
	+ hoạt động web
	+ có ô nhập mã khóa
	+ có chức năng upload và download
**1.	Phân tích ý tưởng**
Một chương trình với giao diện web đơn giản với chức năng mã hóa hoặc giải mã file sử dụng thuật toán AES Cypher. Sử dụng thư viện flask và pycryptodome để tạo môi trường hoạt động và giao diện cho web

**2.	Phân tích sơ đồ hoạt động**
Người dùng truy cập - > index.html hoạt động hiển thị khóa, file và button -> nhập dữ liệu (khóa, file upload, action gồm encrypt hoặc decrypt) -> xử lý khóa nhập (đệm thành 16 bytes) 

**Có chức năng download và upload**
![image](https://github.com/user-attachments/assets/e8d38164-8a48-4bcc-848e-9ecf24310583)
![image](https://github.com/user-attachments/assets/9de37bd8-8239-4c97-91c7-9420ec6b181f)

**+ Encrypt:**
-	Tạo AES Cypher, IV mới với pad dữ liệu
-	Mã hóa bằng AES CBC (cypher = IP + data)
-	Gửi file cho người dùng
  
**+ Decrypt:**
-	Tạo IV từ 16 bytes đầu
-	Tạo AES cipher từ IV
-	Giải mã và unpad dữ liệu
-	Gửi file về client

