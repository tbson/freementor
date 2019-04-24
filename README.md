Vì Nginx sẽ được sử dụng bở nhiều services nên chúng ta sẽ để Nginx bên ngoài docker container của các dự án cụ thể.
Lý do cho hành động này: Vì mỗi server chỉ có 1 port `80` do đó nếu 1 server host nhiều hơn 1 service cùng hứng port 80 như:

```
- https://service1.com
- https://service2.com
```

Nếu chúng ta chỉ dùng trong nội bộ 1 doanh nghiệp hoặc tổ chức mà chúng ta có thể thông báo với người dùng rằng muốn truy cập vào
service nào thì nên vào port nào ví dụ như:

```
- https://192.168.1.11:8000 // For service 1
- https://192.168.1.11:8001 / For service 2
```

Thì chúng ta có thể gộp cả Nginx vào cùng 1 file `docker-compose.yml`, vì nằm chung 1 file `docker-compose` nên các service
mặc định đã share chung 1 network, có thể connect với nhau thông qua service name, chúng ta không cần phải setup 1 network proxy chung nữa.

Nhưng trong trường hợp phổ biến hơn, ví dụ 1 developer chạy nhiều website cho khách trên cùng 1 service, việc build 1 Nginx container
riêng cho cả server là không thể tránh khỏi. Để bắt đầu ta cần tạo 1 network để Nginx có thể nhận ra các service khác cùng dùng chung
network này:

```
docker network create common_proxy
```

Sau đó ta có thể bắt đầu build:

```
docker-compose build
```

Chạy thử:

```
./up
```

Kiểm tra xem container này có đang chạy không:

```
docker ps
```

Nếu thấy có dòng tương tự dòng này thì xem như setup thành công:

```
f27d9cffa321        nginx_nginx          "nginx -g 'daemon of…"   4 days ago          Up 25 hours             0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp   nginx
```
