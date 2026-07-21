---
title: "Bản đề xuất"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Kiến trúc Backend Serverless & Spot Instance cho Game Live-Service trên AWS
## Hạ tầng đám mây hiệu năng cao, mở rộng linh hoạt và tối ưu chi phí cho Game Multiplayer

---

### 1. Tóm tắt điều hành
Dự án đề xuất một kiến trúc backend chuẩn cloud-native dành cho các tựa game multiplayer dạng live-service chạy trên điện toán đám mây Amazon Web Services (AWS). Thay vì duy trì một cụm server game đắt đỏ chạy 24/7 bất kể có người chơi hay không, hệ thống được thiết kế để chỉ bật tài nguyên tính toán (compute) khi thực sự cần thiết: đăng nhập, ghép trận (matchmaking), và trong suốt thời gian diễn ra trận đấu.

Toàn bộ phần metagame—bao gồm xác thực người dùng, phân phối tài nguyên game, ghép trận và xử lý dữ liệu sau trận đấu—được vận hành 100% trên kiến trúc **Serverless**. Phần xử lý trận đấu thực tế (live game session) nằm trong fleet **EC2 Spot** được bảo vệ bởi ranh giới mạng VPC riêng biệt và chỉ được khởi tạo (spin up) khi dịch vụ Matchmaker yêu cầu. Quá trình triển khai và cập nhật mã nguồn tuân thủ tuyệt đối quy trình **GitOps**, đảm bảo việc phát hành diễn ra tự động, không gây gián đoạn hệ thống (zero-downtime) và không yêu cầu can thiệp thủ công trên môi trường production.

---

### 2. Tuyên bố vấn đề

#### Vấn đề hiện tại là gì?
Các hệ thống game server truyền thống thường duy trì các cụm máy chủ EC2 chạy liên tục 24/7. Vào các khung giờ thấp điểm hoặc khi lượng người chơi giảm, doanh nghiệp phải gánh chịu chi phí hạ tầng rỗng vô cùng lớn. Bên cạnh đó, việc cập nhật mã nguồn thủ công tiềm ẩn nhiều rủi ro vận hành như làm gián đoạn trận đấu đang diễn ra, thời gian downtime kéo dài và quy trình rollback phức tạp. Việc mở sẵn các cổng (port) kết nối công khai trên server game cũng làm tăng nguy cơ bị tấn công mạng và DDoS.

#### Giải pháp đề xuất
Hệ thống vận hành theo một quy tắc cốt lõi: **Serverless cho mọi thứ trừ phiên chơi game thực tế (live game session)**.
- Các tác vụ metagame độ độ trễ thấp (Xác thực, Tải tài nguyên, Ghép trận, Phân tích dữ liệu) được đảm nhận bởi các dịch vụ AWS Serverless (Cognito, API Gateway, Lambda, DynamoDB).
- Các phiên chơi game thực tế chạy trên cụm EC2 Spot Instance (chíp Graviton ARM64) nằm trong cấu trúc VPC linh hoạt.
- Quyền truy cập vào server game được bảo vệ bởi các quy tắc Security Group động do Matchmaker Lambda quản lý, chỉ mở port cho đúng IP người chơi trong thời gian diễn ra trận đấu và tự động thu hồi ngay khi trận đấu kết thúc.
- Việc triển khai mã nguồn và hạ tầng được tự động hóa hoàn toàn qua GitHub Actions và AWS CodeDeploy theo mô hình GitOps.

#### Lợi ích và Hoàn vốn đầu tư (ROI)
* **Tiết kiệm tới 80% chi phí hạ tầng**: Loại bỏ hoàn toàn chi phí máy chủ chạy rỗng bằng cách kết hợp EC2 Spot Instance với vi xử lý Graviton ARM64, chỉ trả phí compute khi có trận đấu diễn ra.
* **Không tốn chi phí NAT Gateway & Truyền dữ liệu nội bộ**: Tránh phí NAT Gateway bằng cách điều hướng lưu lượng từ Lambda tới DynamoDB và EC2 API thông qua các VPC Endpoint riêng tư.
* **Triển khai tự động không gián đoạn (Zero-Downtime)**: Triển khai Blue/Green qua CodeDeploy giúp chuyển dịch lưu lượng truy cập từ từ và tự động rollback nếu có lỗi, không làm sập các phiên ghép trận đang chạy.
* **Bảo mật tối đa**: Áp dụng ranh giới tin cậy nghiêm ngặt, cấp quyền IAM tạm thời có giới hạn phạm vi để tải tài nguyên, và quản lý mở/đóng cổng kết nối dynamically.

---

### 3. Kiến trúc giải pháp

Kiến trúc được chia thành bốn luồng xử lý độc lập, mỗi luồng có cơ chế kích hoạt (trigger) và ranh giới tin cậy (trust boundary) riêng biệt.

![Kiến trúc Backend Game Live-Service trên AWS](/images/2-Proposal/architecture.png)

#### Phân tích chi tiết các luồng xử lý

##### **Flow C: GitOps Deployment Loop (Luồng CI/CD)**
* Chạy hoàn toàn lúc triển khai (deploy) và không chạm vào các trận đấu đang diễn ra.
* Developer push mã nguồn và Infrastructure as Code (IaC) lên Git. Pipeline GitOps (GitHub Actions) đóng gói artifact và gọi **AWS CodeDeploy**.
* CodeDeploy thực hiện chuyển dịch lưu lượng (traffic shift) sang phiên bản **AWS Lambda** alias mới và cập nhật AMI/Launch Template cho cụm **EC2 Auto Scaling Group (ASG)** Spot fleet.
* Đồng thời, pipeline upload các bản build client, bản patch và server bundle lên **Amazon S3** asset bucket—đây là nguồn lưu trữ artifact tập trung cho cả client lẫn game server khi instance khởi động.
* Nếu bản release gặp lỗi, hệ thống tự động rollback từ từ mà không ảnh hưởng tới luồng matchmaking đang chạy.

##### **Flow A: Xác thực người chơi & Phân phối Asset (Player Auth & Security)**
* Người chơi đăng nhập qua **Cognito User Pool** (A1) và nhận chuỗi JWT (A2).
* **Cognito Identity Pool** đổi JWT lấy IAM credentials tạm thời có phân quyền theo prefix (A3).
* Client sử dụng credentials tạm thời này để tải trực tiếp asset từ S3 (A4): các bản build client, patch và file launcher cần thiết trước khi vào game.
* JWT cũng được gửi sang Flow R (A5)—đây là điểm giao nhau duy nhất giữa luồng Auth và Matchmaking—để **API Gateway** xác thực trước khi cho phép gọi dịch vụ ghép trận.

##### **Flow R: Luồng ghép trận đồng bộ & Khởi tạo phiên chơi (Matchmaking & Session)**
* Client gửi yêu cầu ghép trận qua **Amazon CloudFront** (được bảo vệ bởi **AWS WAF**) tới **Amazon API Gateway** (R1).
* Sau khi Cognito Authorizer xác thực JWT hợp lệ, **Matchmaker Lambda** (nằm trong private subnet) tiến hành xử lý (R2):
  1. Ghi trạng thái trận đấu vào **Amazon DynamoDB** thông qua **VPC Gateway Endpoint** (R4).
  2. Gọi EC2 control plane qua **VPC Interface Endpoint** riêng (R3) để yêu cầu warm instance từ cụm ASG Spot fleet (G1).
  3. Gán phòng chơi và cấu hình các quy tắc **Security Group** động chỉ mở cổng cho đúng IP của người chơi tham gia.
* Matchmaker Lambda trả IP và port về cho client. Client kết nối trực tiếp tới game instance qua **Internet Gateway** (G3).
* Khi ASG khởi tạo EC2 mới, script User Data chạy lúc boot sẽ dùng **IAM Instance Profile** gọi S3 để pull binary server, file cấu hình và bản patch mới nhất (G4). Instance khởi động xong liền sẵn sàng nhận người chơi theo phòng đã gán.

##### **Flow E: Xử lý dữ liệu bất đồng bộ sau trận đấu (Post-Match Processing)**
* Khi trận đấu kết thúc, kết quả được ghi vào DynamoDB.
* **DynamoDB Streams** tự động kích hoạt **Lambda function** chạy ngầm (E2) để thu thập log post-match, tính toán chỉ số người chơi và đẩy dữ liệu sang kho phân tích analytics (E3).
* Luồng này hoàn toàn tách biệt khỏi Flow R, đảm bảo việc xử lý dữ liệu sau trận đấu không làm ảnh hưởng tới độ trễ (latency) của dịch vụ ghép trận.

#### Các dịch vụ AWS sử dụng
* **Amazon Cognito**: User Pool (Xác thực người dùng) & Identity Pool (Ủy quyền / Cấp IAM Credentials tạm thời).
* **AWS WAF & Amazon CloudFront**: Bảo mật bề mặt mạng, chống DDoS và định tuyến yêu cầu toàn cầu.
* **Amazon API Gateway**: Cổng API Serverless tiếp nhận yêu cầu từ ứng dụng game.
* **AWS Lambda**: Thực thi logic Matchmaker, quản lý traffic CodeDeploy và xử lý log ngầm.
* **Amazon DynamoDB & DynamoDB Streams**: Thiết kế Single-table lưu trữ trạng thái trận đấu & capture log thời gian thực.
* **Amazon EC2 Spot Fleet (Graviton ARM64)**: Cụm máy chủ game hiệu năng cao, tối ưu chi phí cho các phiên chơi live.
* **AWS CodeDeploy & GitHub Actions**: Pipeline tự động hóa triển khai theo mô hình GitOps.
* **Amazon S3 & AWS KMS**: Nguồn lưu trữ tài nguyên tập trung tích hợp mã hóa dữ liệu.
* **VPC Endpoints (Gateway & Interface)**: Kết nối mạng riêng tư không qua internet công khai.

---

### 4. Triển khai kỹ thuật

#### Các giai đoạn triển khai
1. **Giai đoạn 1: Thiết kế kiến trúc & Ranh giới bảo mật (Tháng 1)**  
   Thiết kế cấu trúc mạng VPC, subnet, route table, IAM roles, tự động hóa Security Group và KMS keys.
2. **Giai đoạn 2: Xây dựng Serverless Metagame & Auth (Tháng 1-2)**  
   Triển khai Cognito User/Identity Pools, cấu hình chính sách S3 bucket, API Gateway và cấu trúc bảng DynamoDB Single-table.
3. **Giai đoạn 3: Tự động hóa Matchmaker & EC2 Spot Fleet (Tháng 2)**  
   Phát triển Matchmaker Lambda trong private subnet, cấu hình ASG Launch Template với chíp Graviton ARM64 và viết script User Data.
4. **Giai đoạn 4: Tích hợp GitOps CI/CD & Phân tích bất đồng bộ (Tháng 3)**  
   Thiết lập GitHub Actions workflows, cấu hình CodeDeploy Blue/Green, DynamoDB Streams xử lý post-match và kiểm thử chịu tải (stress test).

#### Yêu cầu kỹ thuật
* **Infrastructure as Code (IaC)**: Sử dụng AWS CDK / Terraform để quản lý và tái tạo môi trường tự động.
* **Game Server Build**: Mã nguồn máy chủ game được đóng gói Container/Binary biên dịch cho kiến trúc Graviton (ARM64 Linux).
* **Tiêu chuẩn bảo mật**: Mã hóa TLS 1.3 khi truyền tải, mã hóa KMS cho dữ liệu lưu trữ, áp dụng nguyên tắc quyền tối thiểu (Least Privilege).

---

### 5. Lộ trình & Mốc triển khai
* **Tháng 1**: Phân tích yêu cầu, thiết kế kiến trúc hệ thống, khởi tạo tài nguyên mạng VPC và ranh giới IAM.
* **Tháng 2**: Phát triển dịch vụ ghép trận Serverless, tích hợp Cognito và tự động hóa EC2 Spot ASG.
* **Tháng 3**: Hoàn thiện pipeline GitOps, kiểm thử chịu tải toàn diện, tối ưu hiệu năng và đưa vào vận hành.

---

### 6. Ước tính ngân sách & Tối ưu chi phí

#### Điểm sáng về tối ưu chi phí
* **Zero Idle Compute**: Máy chủ EC2 chỉ chạy khi có trận đấu thực tế. Các dịch vụ Auth và Matchmaking chỉ tốn chi phí cực nhỏ theo lưu lượng sử dụng thực tế (On-Demand).
* **Giảm 70-90% chi phí máy chủ nhờ Spot & Graviton**: Việc sử dụng EC2 Spot Instance trên nền tảng Graviton ARM64 mang lại hiệu năng vượt trội với mức giá rẻ nhất trên AWS.
* **Loại bỏ hoàn toàn chi phí NAT Gateway**: Matchmaker Lambda giao tiếp với DynamoDB và EC2 API hoàn toàn qua VPC Endpoint nội bộ, không tốn chi phí dữ liệu qua NAT Gateway.
* **Chiến lược AMI mỏng (Thin AMI)**: Server binary và bản patch được tự động tải từ S3 khi máy chủ boot, giúp tiết kiệm chi phí lưu trữ và không cần rebake AMI mỗi khi có bản cập nhật nhỏ.

---

### 7. Đánh giá rủi ro

| Rủi ro | Mức độ | Xác suất | Chiến lược giảm thiểu |
| :--- | :--- | :--- | :--- |
| **Gián đoạn Spot Instance** | Trung bình | Thấp | ASG duy trì warm pool nhỏ và áp dụng chiến lược đa vùng (Multi-AZ) để thay thế máy chủ tức thì. |
| **Lỗi khi triển khai code** | Cao | Thấp | AWS CodeDeploy chuyển dịch lưu lượng từ từ và tự động rollback ngay khi có cảnh báo lỗi. |
| **Truy cập trái phép vào Game Server** | Cao | Thấp | API Gateway xác thực JWT bắt buộc; Security Group tự động mở/đóng cổng theo đúng IP người chơi trong trận. |

---

### 8. Kết quả kỳ vọng
* **Khả năng mở rộng vượt trội**: Đáp ứng mượt mà từ 10 đến 10.000+ người chơi đồng thời mà không cần can thiệp thủ công.
* **Tối ưu chi phí vận hành**: Giảm tới 80% chi phí hạ tầng so với mô hình máy chủ truyền thống chạy 24/7.
* **Bảo mật & Tin cậy chuẩn Enterprise**: Đảm bảo an toàn mạng lưới với ranh giới VPC khép kín, quy trình phát hành GitOps an toàn và phân tích dữ liệu tự động.