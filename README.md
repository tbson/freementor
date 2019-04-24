Sắp xếp cấu trúc các folder như sau:

Giả sử ta có 1 folder chứa tất cả những thứ liên quan đến code nằm tại: `/home/someuser/code`

Folder chứa `nginx` sẽ nằm tại: `/home/someuser/code/nginx`

Folder chứa dự án chuẩn bị chạy sẽ nằm tại: `/home/someuser/web/freementor`, `freementor` có thể là bất kì tên gì chúng ta muốn dùng.


Bước 1 setup:

```
cd docker
./setup freementor freementor.test dev
docker-compose build --no-cache
./restart
./yarn start
```
Edit file host trỏ domain `freementor.test` trỏ về `127.0.0.1`

Bước 2: Kiểm tra:

```
http://freementor.test
http://freementor.test/admin
http://freementor.test/user
```
