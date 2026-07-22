import os, shutil

base_dir = r"c:\Study\TranAnhTu-workshop-main"
workshop_dir = os.path.join(base_dir, "content", "5-Workshop")

# Helper function to write a page with optional alwaysopen
def write_page(file_path, title, weight, chapter_num, content, always_open=False):
    always_open_str = ""
    header = f"""---
title: "{title}"
date: 2026-07-21
weight: {weight}
chapter: false
{always_open_str}pre: " <b> {chapter_num}. </b> "
---

"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + content)

# Clean all existing subfolders in content/5-Workshop/
for item in os.listdir(workshop_dir):
    item_path = os.path.join(workshop_dir, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

# --- MAIN WORKSHOP INDEX ---
main_en = """## Live-Service Game Backend Architecture on AWS

### Overview
This workshop provides a complete, step-by-step hands-on implementation guide for building a serverless and Spot Instance backend architecture for live-service multiplayer games on AWS.

* **Demo Web Link:** [http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/](http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/)
* **Source Code Link:** [https://github.com/Nothingtoread/fighting-game/tree/main](https://github.com/Nothingtoread/fighting-game/tree/main)

---

### Table of Contents

1. [5.1 User Authentication with Amazon Cognito](5.1-cognito/)
   - 5.1.1 Create Cognito User Pool
   - 5.1.2 Configure App Client & Identity Pool
   - 5.1.3 Verify User Registration UI
2. [5.2 Database Setup: DynamoDB](5.2-dynamodb/)
   - 5.2.1 Create MatchmakingQueue Table
   - 5.2.2 Create ActiveMatches Table
3. [5.3 Matchmaker Lambda & API Gateway REST API](5.3-lambda-api/)
   - 5.3.1 Build Matchmaker Lambda Function
   - 5.3.2 Deploy REST API & Cognito Authorizer
4. [5.4 EC2 Game Server & Auto Scaling Group Warm Pool](5.4-ec2-asg/)
   - 5.4.1 Launch EC2 Base & Setup Node.js Server
   - 5.4.2 Bake AMI & Create Launch Template
   - 5.4.3 Configure ASG Warm Pool & S3 Bucket
5. [5.5 GitOps CI/CD Pipeline & AWS CodeDeploy](5.5-gitops-codedeploy/)
   - 5.5.1 Setup GitHub OIDC Provider & IAM Roles
   - 5.5.2 Install CodeDeploy Agent on Ubuntu 24.04
   - 5.5.3 Create CodeDeploy App & Execute Pipeline
6. [5.6 Asynchronous Post-Match Processing](5.6-analytics-stream/)
   - 5.6.1 Enable DynamoDB Streams & IAM Roles
   - 5.6.2 Create MatchAnalytic Lambda & Verify Logs
7. [5.7 Resource Cleanup](5.7-cleanup/)
   - 5.7.1 Clean Up Cognito & DynamoDB
   - 5.7.2 Clean Up Lambda & API Gateway
   - 5.7.3 Clean Up CloudFront & WAF
"""

main_vi = """## Xây dựng Kiến trúc Backend Game Live-Service trên AWS

### Tổng quan
Bài lab thực hành (Workshop) này hướng dẫn chi tiết từng bước cách thiết lập và triển khai hệ thống Backend cho Game Live-Service trên đám mây AWS kết hợp kiến trúc Serverless và cụm máy chủ EC2 Spot Instance.

* **Link web demo:** [http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/](http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/)
* **Link source code:** [https://github.com/Nothingtoread/fighting-game/tree/main](https://github.com/Nothingtoread/fighting-game/tree/main)

---

### Nội dung bài Lab

1. [5.1 Xác thực người dùng với Amazon Cognito](5.1-cognito/)
   - 5.1.1 Tạo Cognito User Pool
   - 5.1.2 Cấu hình App Client & Identity Pool
   - 5.1.3 Kiểm thử Giao diện Đăng ký Người dùng
2. [5.2 Khởi tạo Cơ sở dữ liệu DynamoDB](5.2-dynamodb/)
   - 5.2.1 Tạo Bảng MatchmakingQueue
   - 5.2.2 Tạo Bảng ActiveMatches
3. [5.3 Matchmaker Lambda & API Gateway REST API](5.3-lambda-api/)
   - 5.3.1 Xây dựng Matchmaker Lambda Function
   - 5.3.2 Triển khai REST API & Cognito Authorizer
4. [5.4 Cấu hình EC2 Game Server & ASG Warm Pool](5.4-ec2-asg/)
   - 5.4.1 Khởi tạo EC2 Game Server Node.js
   - 5.4.2 Đóng gói AMI & Tạo Launch Template
   - 5.4.3 Cấu hình ASG Warm Pool & S3 Bucket
5. [5.5 Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy](5.5-gitops-codedeploy/)
   - 5.5.1 Cấu hình GitHub OIDC Provider & IAM Roles
   - 5.5.2 Cài đặt CodeDeploy Agent trên Ubuntu 24.04
   - 5.5.3 Tạo CodeDeploy App & Triển khai Pipeline
6. [5.6 Xử lý dữ liệu bất đồng bộ sau trận đấu](5.6-analytics-stream/)
   - 5.6.1 Kích hoạt DynamoDB Streams & IAM Roles
   - 5.6.2 Khởi tạo MatchAnalytic Lambda & Kiểm thử Log
7. [5.7 Dọn dẹp tài nguyên](5.7-cleanup/)
   - 5.7.1 Dọn dẹp Cognito & DynamoDB
   - 5.7.2 Dọn dẹp Lambda & API Gateway
   - 5.7.3 Dọn dẹp CloudFront & WAF
"""

write_page(os.path.join(workshop_dir, "_index.md"), "Workshop", 5, "5", main_en, always_open=True)
write_page(os.path.join(workshop_dir, "_index.vi.md"), "Workshop", 5, "5", main_vi, always_open=True)


# --- CHAPTER 5.1: COGNITO ---
c51_dir = os.path.join(workshop_dir, "5.1-Cognito")
os.makedirs(c51_dir, exist_ok=True)

write_page(os.path.join(c51_dir, "_index.md"), "User Authentication with Amazon Cognito", 1, "5.1",
"""### Overview
In this chapter, you will configure **Amazon Cognito User Pools** and **Cognito Identity Pools** to handle user sign-up, sign-in, and temporary IAM credential generation for downloading game assets.

---

### Sub-modules
- [5.1.1 Create Cognito User Pool](5.1.1-create-user-pool/)
- [5.1.2 Configure App Client & Identity Pool](5.1.2-configure-identity-pool/)
- [5.1.3 Verify User Registration UI](5.1.3-test-user-registration/)
""", always_open=True)

write_page(os.path.join(c51_dir, "_index.vi.md"), "Xác thực người dùng với Amazon Cognito", 1, "5.1",
"""### Tổng quan
Trong chương này, bạn sẽ thực hành cấu hình **Amazon Cognito User Pools** và **Cognito Identity Pools** để xử lý đăng ký, đăng nhập và cấp quyền IAM ngắn hạn cho client tải tài nguyên game.

---

### Các bài học nhỏ
- [5.1.1 Tạo Cognito User Pool](5.1.1-create-user-pool/)
- [5.1.2 Cấu hình App Client & Identity Pool](5.1.2-configure-identity-pool/)
- [5.1.3 Kiểm thử Giao diện Đăng ký Người dùng](5.1.3-test-user-registration/)
""", always_open=True)

# 5.1.1
c511_dir = os.path.join(c51_dir, "5.1.1-create-user-pool")
os.makedirs(c511_dir, exist_ok=True)
write_page(os.path.join(c511_dir, "_index.md"), "Create Cognito User Pool", 1, "5.1.1",
"""### Step-by-Step Implementation

#### Step 1: Select AWS Region
1. Switch your AWS Management Console region to **Singapore (ap-southeast-1)**.

![Select Region Singapore](/images/5-Workshop/img_A/image1.png)

---

#### Step 2: Create Cognito User Pool
1. Search for **Cognito** in the AWS Console search bar.
2. Click **Get started for free**.
3. Select **Single-page application (SPA)** and enter the Application name: `FightingGame`.

![Cognito Console](/images/5-Workshop/img_A/image4.png)
![SPA Configuration](/images/5-Workshop/img_A/image6.png)

4. Under **Configure options**:
   - Check **Username** self-registration.
   - Select **Required attributes**: Select `email` for password recovery.

![Configure Options](/images/5-Workshop/img_A/image7.png)

5. Click **Create user directory**.
   - **User Pool ID**: `ap-southeast-1_phYoaMUPC`
""")

write_page(os.path.join(c511_dir, "_index.vi.md"), "Tạo Cognito User Pool", 1, "5.1.1",
"""### Các bước thực hiện

#### Bước 1: Chọn Region AWS
1. Chuyển đổi vùng làm việc trên AWS Management Console sang **Singapore (ap-southeast-1)**.

![Chọn Region Singapore](/images/5-Workshop/img_A/image1.png)

---

#### Bước 2: Tạo Cognito User Pool
1. Tìm kiếm **Cognito** trên thanh tìm kiếm của AWS Console.
2. Chọn **Get started for free**.
3. Chọn loại ứng dụng **Single-page application (SPA)** và điền tên: `FightingGame`.

![Cognito Console](/images/5-Workshop/img_A/image4.png)
![Cấu hình SPA](/images/5-Workshop/img_A/image6.png)

4. Tại mục **Configure options**:
   - Tích chọn **Username** cho phép người dùng tự đăng ký (Enable Self-registration).
   - Mụcs **Required attributes**: Chọn `email` phục vụ khôi phục mật khẩu.

![Cấu hình lựa chọn](/images/5-Workshop/img_A/image7.png)

5. Bấm **Create user directory**.
   - **User Pool ID**: `ap-southeast-1_phYoaMUPC`
""")

# 5.1.2
c512_dir = os.path.join(c51_dir, "5.1.2-configure-identity-pool")
os.makedirs(c512_dir, exist_ok=True)
write_page(os.path.join(c512_dir, "_index.md"), "Configure App Client & Identity Pool", 2, "5.1.2",
"""### Step-by-Step Implementation

#### Step 1: Configure App Client
1. Navigate to **Applications** -> **App clients**.
2. Select `FightingGame` app client.
3. Under **Authentication flows**, enable `ALLOW_USER_PASSWORD_AUTH`.
4. Save changes.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![App Client Settings](/images/5-Workshop/img_A/image12.png)
![Authentication Flow](/images/5-Workshop/img_A/image14.png)

---

#### Step 2: Create Cognito Identity Pool
1. Return to the Cognito dashboard and select **Identity pools**.
2. Click **Create identity pool**.
3. Select **Authenticated access** -> **Amazon Cognito user pool**.

![Create Identity Pool](/images/5-Workshop/img_A/image17.png)
![Identity Provider Settings](/images/5-Workshop/img_A/image19.png)

4. Under **Configure permissions**:
   - Create a new IAM Role named `FightingGameAuthenticatedRole`.
5. Under **Connect identity providers**:
   - Enter your User Pool ID (`ap-southeast-1_phYoaMUPC`) and App Client ID (`73ipqvvo7h3u0j3elfqlj23jo3`).
6. Name the pool: `FightingGameIdentityPool`.
7. Click **Create identity pool**.
   - **Identity Pool ID**: `ap-southeast-1:a5d743b9-e4a4-45d2-9cb1-9d214cee574c`

![Identity Pool Created](/images/5-Workshop/img_A/image23.png)
""")

write_page(os.path.join(c512_dir, "_index.vi.md"), "Cấu hình App Client & Identity Pool", 2, "5.1.2",
"""### Các bước thực hiện

#### Bước 1: Cấu hình App Client
1. Vào mục **Applications** -> **App clients**.
2. Chọn client `FightingGame` và bấm Edit.
3. Tại **Authentication flows**, tích chọn `ALLOW_USER_PASSWORD_AUTH`.
4. Bấm **Save changes**.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![Cấu hình App Client](/images/5-Workshop/img_A/image12.png)
![Cho phép Password Auth](/images/5-Workshop/img_A/image14.png)

---

#### Bước 2: Tạo Cognito Identity Pool
1. Quay lại trang Cognito và chọn **Identity pools**.
2. Chọn **Create identity pool**.
3. Chọn **Authenticated access** -> **Amazon Cognito user pool**.

![Tạo Identity Pool](/images/5-Workshop/img_A/image17.png)
![Thiết lập Nhà cung cấp xác thực](/images/5-Workshop/img_A/image19.png)

4. Tại **Configure permissions**:
   - Tạo mới IAM Role với tên: `FightingGameAuthenticatedRole`.
5. Tại **Connect identity providers**:
   - Nhập User Pool ID (`ap-southeast-1_phYoaMUPC`) và App Client ID (`73ipqvvo7h3u0j3elfqlj23jo3`).
6. Đặt tên Pool: `FightingGameIdentityPool`.
7. Chọn **Create identity pool**.
   - **Identity Pool ID**: `ap-southeast-1:a5d743b9-e4a4-45d2-9cb1-9d214cee574c`

![Tạo Identity Pool thành công](/images/5-Workshop/img_A/image23.png)
""")

# 5.1.3
c513_dir = os.path.join(c51_dir, "5.1.3-test-user-registration")
os.makedirs(c513_dir, exist_ok=True)
write_page(os.path.join(c513_dir, "_index.md"), "Verify User Registration UI", 3, "5.1.3",
"""### Step-by-Step Implementation

#### Step 1: Open Frontend Game Client
1. Launch the game client web interface.
2. Enter username, email, and password to test account registration.
3. Verify Cognito User Pool receives and stores the new user record.

![User Registration UI](/images/5-Workshop/img_A/image99.png)
""")

write_page(os.path.join(c513_dir, "_index.vi.md"), "Kiểm thử Giao diện Đăng ký Người dùng", 3, "5.1.3",
"""### Các bước thực hiện

#### Bước 1: Mở Giao diện Frontend Game
1. Mở giao diện web ứng dụng game client.
2. Nhập username, email và password để thử nghiệm đăng ký tài khoản.
3. Kiểm tra danh sách người dùng trong Cognito User Pool để xác nhận tài khoản đã được kích hoạt.

![Giao diện Đăng ký người dùng](/images/5-Workshop/img_A/image99.png)
""")


# --- CHAPTER 5.2: DYNAMODB ---
c52_dir = os.path.join(workshop_dir, "5.2-DynamoDB")
os.makedirs(c52_dir, exist_ok=True)

write_page(os.path.join(c52_dir, "_index.md"), "Database Setup: DynamoDB Matchmaking Queue & Active Matches", 2, "5.2",
"""### Overview
In this chapter, you will create two core **Amazon DynamoDB** tables: `MatchmakingQueue` (for pending players) and `ActiveMatches` (for active match sessions).

---

### Sub-modules
- [5.2.1 Create MatchmakingQueue Table](5.2.1-create-queue-table/)
- [5.2.2 Create ActiveMatches Table](5.2.2-create-active-matches-table/)
""", always_open=True)

write_page(os.path.join(c52_dir, "_index.vi.md"), "Cơ sở dữ liệu DynamoDB: MatchmakingQueue & ActiveMatches", 2, "5.2",
"""### Tổng quan
Trong chương này, bạn sẽ tiến hành khởi tạo hai bảng **Amazon DynamoDB** cốt lõi: `MatchmakingQueue` (hàng chờ người chơi) và `ActiveMatches` (lưu phiên trận đấu đang diễn ra).

---

### Các bài học nhỏ
- [5.2.1 Tạo Bảng MatchmakingQueue](5.2.1-create-queue-table/)
- [5.2.2 Tạo Bảng ActiveMatches](5.2.2-create-active-matches-table/)
""", always_open=True)

# 5.2.1
c521_dir = os.path.join(c52_dir, "5.2.1-create-queue-table")
os.makedirs(c521_dir, exist_ok=True)
write_page(os.path.join(c521_dir, "_index.md"), "Create MatchmakingQueue Table", 1, "5.2.1",
"""### Step-by-Step Implementation

#### Step 1: Open Amazon DynamoDB Console
1. Search for **DynamoDB** in the AWS search bar.
2. Click **Get started**.

![DynamoDB Console](/images/5-Workshop/img_A/image25.png)

---

#### Step 2: Create Table `MatchmakingQueue`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `MatchmakingQueue`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create MatchmakingQueue Table](/images/5-Workshop/img_A/image27.png)
""")

write_page(os.path.join(c521_dir, "_index.vi.md"), "Tạo Bảng MatchmakingQueue", 1, "5.2.1",
"""### Các bước thực hiện

#### Bước 1: Truy cập Amazon DynamoDB Console
1. Tìm kiếm **DynamoDB** trên thanh tìm kiếm AWS.
2. Chọn **Get started**.

![DynamoDB Console](/images/5-Workshop/img_A/image25.png)

---

#### Bước 2: Tạo Bảng `MatchmakingQueue`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `MatchmakingQueue`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng MatchmakingQueue](/images/5-Workshop/img_A/image27.png)
""")

# 5.2.2
c522_dir = os.path.join(c52_dir, "5.2.2-create-active-matches-table")
os.makedirs(c522_dir, exist_ok=True)
write_page(os.path.join(c522_dir, "_index.md"), "Create ActiveMatches Table & Verify", 2, "5.2.2",
"""### Step-by-Step Implementation

#### Step 1: Create Table `ActiveMatches`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create ActiveMatches Table](/images/5-Workshop/img_A/image28.png)

---

#### Step 2: Verify Tables Status
1. Check the table list to ensure both `MatchmakingQueue` and `ActiveMatches` have reached `Active` status.

![Active DynamoDB Tables](/images/5-Workshop/img_A/image29.png)
""")

write_page(os.path.join(c522_dir, "_index.vi.md"), "Tạo Bảng ActiveMatches & Kiểm tra", 2, "5.2.2",
"""### Các bước thực hiện

#### Bước 1: Tạo Bảng `ActiveMatches`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng ActiveMatches](/images/5-Workshop/img_A/image28.png)

---

#### Bước 2: Kiểm tra trạng thái Bảng
1. Kiểm tra danh sách bảng đảm bảo cả `MatchmakingQueue` và `ActiveMatches` đều ở trạng thái `Active`.

![Bảng DynamoDB ở trạng thái Active](/images/5-Workshop/img_A/image29.png)
""")


# --- CHAPTER 5.3: LAMBDA & API ---
c53_dir = os.path.join(workshop_dir, "5.3-Lambda-API")
os.makedirs(c53_dir, exist_ok=True)

write_page(os.path.join(c53_dir, "_index.md"), "Matchmaker Lambda & API Gateway REST API", 3, "5.3",
"""### Overview
In this chapter, you will build the **FightingGameMatchmaker** AWS Lambda function to process player queueing (`POST /join`) and match checks (`GET /check`), and expose these endpoints via **Amazon API Gateway** secured by Cognito Authorizer.

---

### Sub-modules
- [5.3.1 Build Matchmaker Lambda Function](5.3.1-create-matchmaker-lambda/)
- [5.3.2 Deploy REST API & Cognito Authorizer](5.3.2-create-api-gateway/)
""", always_open=True)

write_page(os.path.join(c53_dir, "_index.vi.md"), "Matchmaker Lambda & API Gateway REST API", 3, "5.3",
"""### Tổng quan
Trong chương này, bạn sẽ triển khai hàm AWS Lambda **FightingGameMatchmaker** để xử lý yêu cầu tham gia hàng chờ (`POST /join`) và kiểm tra trạng thái trận đấu (`GET /check`), sau đó công khai dịch vụ qua **Amazon API Gateway** tích hợp bảo mật Cognito Authorizer.

---

### Các bài học nhỏ
- [5.3.1 Xây dựng Matchmaker Lambda Function](5.3.1-create-matchmaker-lambda/)
- [5.3.2 Triển khai REST API & Cognito Authorizer](5.3.2-create-api-gateway/)
""", always_open=True)

# 5.3.1
c531_dir = os.path.join(c53_dir, "5.3.1-create-matchmaker-lambda")
os.makedirs(c531_dir, exist_ok=True)
write_page(os.path.join(c531_dir, "_index.md"), "Build Matchmaker Lambda Function", 1, "5.3.1",
"""### Step-by-Step Implementation

#### Step 1: Create AWS Lambda Function
1. Navigate to **AWS Lambda** console -> Click **Create function**.
2. Function name: `FightingGameMatchmaker`.
3. Runtime: **Node.js 20.x**.

![Create Lambda Function](/images/5-Workshop/img_A/image31.png)

---

#### Step 2: Configure Lambda IAM Permissions & Environment Variables
1. Under **Configuration** -> **Permissions**, click the Execution Role link.
2. Add an inline policy granting `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:DeleteItem`, and `ec2:DescribeInstances` access.

![Lambda Permissions](/images/5-Workshop/img_A/image35.png)

3. Under **Environment variables**, click **Edit** and set:
   - `MATCHMAKING_QUEUE_TABLE`: `MatchmakingQueue`
   - `ACTIVE_MATCHES_TABLE`: `ActiveMatches`

![Environment Variables](/images/5-Workshop/img_A/image42.png)

---

#### Step 3: Deploy & Test Lambda Function
1. Paste the Matchmaker Node.js source code into the editor and click **Deploy**.
2. Test payload execution for `Player1` and `Player2`.
3. Verify that players are successfully inserted into `MatchmakingQueue`.

![Lambda Code Editor](/images/5-Workshop/img_A/image44.png)
![Lambda Test Result](/images/5-Workshop/img_A/image47.png)
""")

write_page(os.path.join(c531_dir, "_index.vi.md"), "Xây dựng Matchmaker Lambda Function", 1, "5.3.1",
"""### Các bước thực hiện

#### Bước 1: Tạo AWS Lambda Function
1. Truy cập **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `FightingGameMatchmaker`.
3. Runtime: **Node.js 20.x**.

![Tạo Lambda Function](/images/5-Workshop/img_A/image31.png)

---

#### Bước 2: Cấu hình Phân quyền IAM Role & Biến môi trường
1. Tại tab **Configuration** -> **Permissions**, nhấp vào liên kết Role name để chỉnh sửa.
2. Thêm Policy cấp quyền `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:DeleteItem` và `ec2:DescribeInstances`.

![Cấu hình Permission Role](/images/5-Workshop/img_A/image35.png)

3. Tại **Environment variables**, chọn **Edit** và thêm các biến:
   - `MATCHMAKING_QUEUE_TABLE`: `MatchmakingQueue`
   - `ACTIVE_MATCHES_TABLE`: `ActiveMatches`

![Thêm biến môi trường](/images/5-Workshop/img_A/image42.png)

---

#### Bước 3: Deploy & Kiểm thử Lambda Function
1. Dán mã nguồn Node.js của Matchmaker vào trình chỉnh sửa và chọn **Deploy**.
2. Tạo dữ liệu test thử nghiệm cho `Player1` và `Player2`.
3. Kiểm tra thông báo thành công và xác nhận người chơi đã được thêm vào bảng `MatchmakingQueue`.

![Giao diện Code Lambda](/images/5-Workshop/img_A/image44.png)
![Kiểm thử Lambda thành công](/images/5-Workshop/img_A/image47.png)
""")

# 5.3.2
c532_dir = os.path.join(c53_dir, "5.3.2-create-api-gateway")
os.makedirs(c532_dir, exist_ok=True)
write_page(os.path.join(c532_dir, "_index.md"), "Deploy REST API & Cognito Authorizer", 2, "5.3.2",
"""### Step-by-Step Implementation

#### Step 1: Create Amazon API Gateway REST API
1. Navigate to **API Gateway** console -> Click **Create API**.
2. Select **REST API** -> Build.
3. API Name: `FightingGameAPI`.

![API Gateway Console](/images/5-Workshop/img_A/image56.png)

---

#### Step 2: Create Resources `/join` & `/check`
1. Click **Create resource**:
   - Resource Name: `join` -> Create method `POST` -> Link to `FightingGameMatchmaker` Lambda.
2. Click **Create resource**:
   - Resource Name: `check` -> Create method `GET` -> Link to `FightingGameMatchmaker` Lambda.

![Create Resource Join](/images/5-Workshop/img_A/image61.png)
![Create Resource Check](/images/5-Workshop/img_A/image68.png)

---

#### Step 3: Configure Cognito Authorizer & CORS
1. Under **Authorizers**, click **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Attach `FightinggameCognitoAuthorizer` to `/join` (POST) and `/check` (GET) method request settings.
3. Enable **CORS** for both `/join` and `/check` endpoints.

![Create Cognito Authorizer](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Step 4: Deploy API Gateway
1. Select `/` root resource -> Click **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API](/images/5-Workshop/img_A/image84.png)
""")

write_page(os.path.join(c532_dir, "_index.vi.md"), "Triển khai REST API & Cognito Authorizer", 2, "5.3.2",
"""### Các bước thực hiện

#### Bước 1: Tạo Amazon API Gateway REST API
1. Mở console **API Gateway** -> Chọn **Create API**.
2. Chọn **REST API** -> Bấm Build.
3. Đặt tên API: `FightingGameAPI`.

![Tạo REST API](/images/5-Workshop/img_A/image56.png)

---

#### Bước 2: Khởi tạo Resource `/join` & `/check`
1. Bấm **Create resource**:
   - Resource Name: `join` -> Tạo method `POST` -> Kết nối với `FightingGameMatchmaker` Lambda.
2. Bấm **Create resource**:
   - Resource Name: `check` -> Tạo method `GET` -> Kết nối với `FightingGameMatchmaker` Lambda.

![Tạo Resource /join](/images/5-Workshop/img_A/image61.png)
![Tạo Resource /check](/images/5-Workshop/img_A/image68.png)

---

#### Bước 3: Thêm Cognito Authorizer & Cấu hình CORS
1. Vào mục **Authorizers** -> Bấm **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Gắn `FightinggameCognitoAuthorizer` vào Method Request của `/join` (POST) và `/check` (GET).
3. Bật **Enable CORS** cho cả hai resource `/join` và `/check`.

![Tạo Authorizer Cognito](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Bước 4: Deploy API Gateway
1. Chọn gốc `/` -> Bấm **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API thành công](/images/5-Workshop/img_A/image84.png)
""")


# --- CHAPTER 5.4: EC2 & ASG ---
c54_dir = os.path.join(workshop_dir, "5.4-EC2-ASG")
os.makedirs(c54_dir, exist_ok=True)

write_page(os.path.join(c54_dir, "_index.md"), "EC2 Game Server & Auto Scaling Group Warm Pool", 4, "5.4",
"""### Overview
In this chapter, you will launch the baseline **EC2 Game Server**, bake a customized **AMI**, create a **Launch Template**, configure an **Auto Scaling Group (ASG) Warm Pool**, and set up the **Amazon S3 Asset Bucket**.

---

### Sub-modules
- [5.4.1 Launch EC2 Base & Setup Node.js Server](5.4.1-setup-ec2-game-server/)
- [5.4.2 Bake AMI & Create Launch Template](5.4.2-bake-ami-launch-template/)
- [5.4.3 Configure ASG Warm Pool & S3 Bucket](5.4.3-configure-asg-warmpool/)
""", always_open=True)

write_page(os.path.join(c54_dir, "_index.vi.md"), "Cấu hình EC2 Game Server & ASG Warm Pool", 4, "5.4",
"""### Tổng quan
Trong chương này, bạn sẽ khởi tạo máy chủ game mẫu trên **Amazon EC2**, đóng gói **AMI**, thiết lập **Launch Template**, cấu hình **Auto Scaling Group (ASG) Warm Pool** và khởi tạo **S3 Asset Bucket**.

---

### Các bài học nhỏ
- [5.4.1 Khởi tạo EC2 Game Server Node.js](5.4.1-setup-ec2-game-server/)
- [5.4.2 Đóng gói AMI & Tạo Launch Template](5.4.2-bake-ami-launch-template/)
- [5.4.3 Cấu hình ASG Warm Pool & S3 Bucket](5.4.3-configure-asg-warmpool/)
""", always_open=True)

# 5.4.1
c541_dir = os.path.join(c54_dir, "5.4.1-setup-ec2-game-server")
os.makedirs(c541_dir, exist_ok=True)
write_page(os.path.join(c541_dir, "_index.md"), "Launch EC2 Base & Setup Node.js Server", 1, "5.4.1",
"""### Step-by-Step Implementation

#### Step 1: Launch Base EC2 Instance
1. Navigate to **Amazon EC2** -> Click **Launch Instance**.
2. Name: `FightingGameServer`.
3. AMI: **Ubuntu Server 24.04 LTS**.
4. Instance Type: `t3.medium` (Graviton/x86 compatible).
5. Storage: 8 GB gp3.

![Launch EC2 Instance](/images/5-Workshop/img_A/image86.png)

---

#### Step 2: Set Up Node.js Game Server Environment
1. SSH into the EC2 instance.
2. Install Node.js runtime and dependencies.
3. Start the game server application and verify local port binding.

![Configure Node.js Game Server](/images/5-Workshop/img_A/image91.png)
![Test Game Server Connection](/images/5-Workshop/img_A/image97.png)
""")

write_page(os.path.join(c541_dir, "_index.vi.md"), "Khởi tạo EC2 Game Server Node.js", 1, "5.4.1",
"""### Các bước thực hiện

#### Bước 1: Khởi tạo EC2 Instance gốc
1. Vào **Amazon EC2** console -> Chọn **Launch Instance**.
2. Name: `FightingGameServer`.
3. AMI: **Ubuntu Server 24.04 LTS**.
4. Instance Type: `t3.medium`.
5. Storage: 8 GB gp3.

![Khởi tạo EC2 Instance](/images/5-Workshop/img_A/image86.png)

---

#### Bước 2: Thiết lập môi trường Game Server Node.js
1. Kết nối SSH vào EC2 instance.
2. Cài đặt Node.js runtime và các gói phụ thuộc.
3. Khởi chạy ứng dụng game server và kiểm thử kết nối cổng thành công.

![Cấu hình Node.js Game Server](/images/5-Workshop/img_A/image91.png)
![Kiểm thử kết nối Game Server](/images/5-Workshop/img_A/image97.png)
""")

# 5.4.2
c542_dir = os.path.join(c54_dir, "5.4.2-bake-ami-launch-template")
os.makedirs(c542_dir, exist_ok=True)
write_page(os.path.join(c542_dir, "_index.md"), "Bake AMI & Create Launch Template", 2, "5.4.2",
"""### Step-by-Step Implementation

#### Step 1: Bake Custom AMI
1. Tag the running server instance.
2. Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Create AMI](/images/5-Workshop/img_B/image5.png)

---

#### Step 2: Create Launch Template for Spot Fleet
1. Navigate to **Launch Templates** -> Click **Create launch template**:
   - Select `FightingGameServer-AMI`.
   - Set Purchasing Option: **Spot Instances**.

![Create Launch Template](/images/5-Workshop/img_B/image6.png)
""")

write_page(os.path.join(c542_dir, "_index.vi.md"), "Đóng gói AMI & Tạo Launch Template", 2, "5.4.2",
"""### Các bước thực hiện

#### Bước 1: Gán Tag & Đóng gói AMI
1. Gán Tag định danh cho game server.
2. Chọn Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Tạo AMI](/images/5-Workshop/img_B/image5.png)

---

#### Bước 2: Tạo Launch Template Spot Fleet
1. Vào mục **Launch Templates** -> Bấm **Create launch template**:
   - Chọn AMI vừa tạo (`FightingGameServer-AMI`).
   - Cấu hình tùy chọn mua tài nguyên: **Spot Instances**.

![Tạo Launch Template Spot](/images/5-Workshop/img_B/image6.png)
""")

# 5.4.3
c543_dir = os.path.join(c54_dir, "5.4.3-configure-asg-warmpool")
os.makedirs(c543_dir, exist_ok=True)
write_page(os.path.join(c543_dir, "_index.md"), "Configure ASG Warm Pool & S3 Bucket", 3, "5.4.3",
"""### Step-by-Step Implementation

#### Step 1: Configure Auto Scaling Group (ASG) Warm Pool
1. Create Auto Scaling Group: `FightingGameServerASG`.
2. Attach Launch Template.
3. Configure **Warm Pool** settings to maintain pre-initialized warm instances ready for instant match assignment.

![Configure ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Step 2: Create Amazon S3 Asset Bucket & Policy
1. Create S3 Bucket for client builds, patches, and game server bundles.
2. Configure **Public Read Bucket Policy** and **CORS** rules.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Step 3: Assign IAM Instance Profile
1. Create `FightingGameServerInstanceRole` with S3 read permissions.
2. Attach IAM Instance Profile to EC2 Launch Template.

![Attach Instance Role](/images/5-Workshop/img_B/image18.png)
""")

write_page(os.path.join(c543_dir, "_index.vi.md"), "Cấu hình ASG Warm Pool & S3 Bucket", 3, "5.4.3",
"""### Các bước thực hiện

#### Bước 1: Cấu hình Auto Scaling Group (ASG) Warm Pool
1. Tạo Auto Scaling Group: `FightingGameServerASG`.
2. Gắn Launch Template vừa tạo.
3. Cấu hình **Warm Pool** để duy trì các instance khởi động sẵn (warm), đáp ứng việc gán phòng tức thì khi có trận đấu mới.

![Cấu hình ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Bước 2: Tạo Amazon S3 Asset Bucket & Policy
1. Tạo S3 Bucket lưu trữ các bản build client, patch và server binary.
2. Cấu hình **Bucket Policy** và quy tắc **CORS**.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Bước 3: Cấu hình IAM Instance Profile
1. Tạo IAM Role `FightingGameServerInstanceRole` cấp quyền truy cập S3.
2. Gắn IAM Instance Profile vào EC2 Launch Template.

![Gắn IAM Role cho EC2](/images/5-Workshop/img_B/image18.png)
""")


# --- CHAPTER 5.5: GITOPS & CODEDEPLOY ---
c55_dir = os.path.join(workshop_dir, "5.5-GitOps-CodeDeploy")
os.makedirs(c55_dir, exist_ok=True)

write_page(os.path.join(c55_dir, "_index.md"), "GitOps CI/CD Pipeline & AWS CodeDeploy", 5, "5.5",
"""### Overview
In this chapter, you will integrate **GitHub Actions OIDC** for passwordless authentication, install and patch the **AWS CodeDeploy Agent** on Ubuntu 24.04 LTS, configure CodeDeploy applications, and execute automated zero-downtime deployments.

---

### Sub-modules
- [5.5.1 Setup GitHub OIDC Provider & IAM Roles](5.5.1-setup-github-oidc/)
- [5.5.2 Install CodeDeploy Agent on Ubuntu 24.04](5.5.2-install-codedeploy-agent/)
- [5.5.3 Create CodeDeploy App & Execute Pipeline](5.5.3-execute-gitops-pipeline/)
""", always_open=True)

write_page(os.path.join(c55_dir, "_index.vi.md"), "Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy", 5, "5.5",
"""### Tổng quan
Trong chương này, bạn sẽ cấu hình **GitHub Actions OIDC** để xác thực không dùng access key tĩnh, cài đặt và patch **AWS CodeDeploy Agent** trên Ubuntu 24.04 LTS, cấu hình CodeDeploy Application và thực thi quy trình triển khai tự động không gây gián đoạn.

---

### Các bài học nhỏ
- [5.5.1 Cấu hình GitHub OIDC Provider & IAM Roles](5.5.1-setup-github-oidc/)
- [5.5.2 Cài đặt CodeDeploy Agent trên Ubuntu 24.04](5.5.2-install-codedeploy-agent/)
- [5.5.3 Tạo CodeDeploy App & Triển khai Pipeline](5.5.3-execute-gitops-pipeline/)
""", always_open=True)

# 5.5.1
c551_dir = os.path.join(c55_dir, "5.5.1-setup-github-oidc")
os.makedirs(c551_dir, exist_ok=True)
write_page(os.path.join(c551_dir, "_index.md"), "Setup GitHub OIDC Provider & IAM Roles", 1, "5.5.1",
"""### Step-by-Step Implementation

#### Step 1: Configure GitHub OIDC Provider in AWS IAM
1. Navigate to **IAM** -> **Identity providers** -> Add **GitHub OIDC Provider**.
2. Create an IAM Role for GitHub Actions with trust policy restricted to `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Add GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![GitHub Role Trust Policy](/images/5-Workshop/img_B/image14.png)
""")

write_page(os.path.join(c551_dir, "_index.vi.md"), "Cấu hình GitHub OIDC Provider & IAM Roles", 1, "5.5.1",
"""### Các bước thực hiện

#### Bước 1: Cấu hình GitHub OIDC Provider trong AWS IAM
1. Vào **IAM** -> **Identity providers** -> Thêm **GitHub OIDC Provider**.
2. Tạo IAM Role dành cho GitHub Actions với Trust Policy giới hạn quyền cho repository `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Thêm GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![Cấu hình Trust Policy](/images/5-Workshop/img_B/image14.png)
""")

# 5.5.2
c552_dir = os.path.join(c55_dir, "5.5.2-install-codedeploy-agent")
os.makedirs(c552_dir, exist_ok=True)
write_page(os.path.join(c552_dir, "_index.md"), "Install CodeDeploy Agent on Ubuntu 24.04", 2, "5.5.2",
"""### Step-by-Step Implementation

#### Step 1: Install & Patch AWS CodeDeploy Agent on Ubuntu 24.04 LTS
Execute the following commands on the EC2 instance to patch the Ruby 3.3 dependency compatibility issue:

```bash
# 1. Install prerequisites
sudo apt-get update && sudo apt-get install -y ruby-full ruby-webrick wget gdebi-core

# 2. Download CodeDeploy deb package
cd /tmp
wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/releases/codedeploy-agent_1.8.1-26_all.deb

# 3. Unpack and fix Ruby dependency
dpkg-deb -R codedeploy-agent_1.8.1-26_all.deb /tmp/codedeploy-extracted
sed -i "s/ruby3.2/ruby3.3/g" /tmp/codedeploy-extracted/DEBIAN/control
dpkg-deb -b /tmp/codedeploy-extracted /tmp/codedeploy-agent_fixed.deb

# 4. Install patched package and start service
sudo dpkg -i /tmp/codedeploy-agent_fixed.deb
sudo systemctl enable codedeploy-agent
sudo systemctl start codedeploy-agent
```

![CodeDeploy Installation Script](/images/5-Workshop/img_B/image27.png)
""")

write_page(os.path.join(c552_dir, "_index.vi.md"), "Cài đặt CodeDeploy Agent trên Ubuntu 24.04", 2, "5.5.2",
"""### Các bước thực hiện

#### Bước 1: Cài đặt & Patch CodeDeploy Agent trên Ubuntu 24.04 LTS
Chạy các lệnh sau trên EC2 instance để sửa lỗi tương thích phiên bản Ruby 3.3 trên Ubuntu 24.04:

```bash
# 1. Cài đặt các thư viện tiền đề
sudo apt-get update && sudo apt-get install -y ruby-full ruby-webrick wget gdebi-core

# 2. Tải gói cài đặt CodeDeploy
cd /tmp
wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/releases/codedeploy-agent_1.8.1-26_all.deb

# 3. Giải nén và sửa phụ thuộc Ruby trong file control
dpkg-deb -R codedeploy-agent_1.8.1-26_all.deb /tmp/codedeploy-extracted
sed -i "s/ruby3.2/ruby3.3/g" /tmp/codedeploy-extracted/DEBIAN/control
dpkg-deb -b /tmp/codedeploy-extracted /tmp/codedeploy-agent_fixed.deb

# 4. Cài đặt gói đã sửa và khởi chạy dịch vụ
sudo dpkg -i /tmp/codedeploy-agent_fixed.deb
sudo systemctl enable codedeploy-agent
sudo systemctl start codedeploy-agent
```

![Lệnh cài đặt CodeDeploy Agent](/images/5-Workshop/img_B/image27.png)
""")

# 5.5.3
c553_dir = os.path.join(c55_dir, "5.5.3-execute-gitops-pipeline")
os.makedirs(c553_dir, exist_ok=True)
write_page(os.path.join(c553_dir, "_index.md"), "Create CodeDeploy App & Execute Pipeline", 3, "5.5.3",
"""### Step-by-Step Implementation

#### Step 1: Create AWS CodeDeploy Application & Deployment Group
1. Create CodeDeploy Role for EC2 and Lambda deployments.
2. Create CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Create Deployment Group targeting EC2 Spot instances and Lambda alias traffic shifting.

![CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Deployment Group Config](/images/5-Workshop/img_B/image30.png)

---

#### Step 2: Execute Automated Deployment & Verify Logs
1. Trigger GitHub Actions workflow execution.
2. Monitor CodeDeploy job execution progress and verify deployment history.

![Successful CodeDeploy Job](/images/5-Workshop/img_B/image31.png)
""")

write_page(os.path.join(c553_dir, "_index.vi.md"), "Tạo CodeDeploy App & Triển khai Pipeline", 3, "5.5.3",
"""### Các bước thực hiện

#### Bước 1: Tạo AWS CodeDeploy Application & Deployment Group
1. Tạo IAM Role cho CodeDeploy.
2. Tạo CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Tạo Deployment Group cho cụm EC2 và Lambda.

![Tạo CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Cấu hình Deployment Group](/images/5-Workshop/img_B/image30.png)

---

#### Bước 2: Thực thi Triển khai Tự động & Kiểm tra Lịch sử
1. Chạy GitHub Actions workflow để tự động deploy code mới.
2. Theo dõi tiến độ triển khai và xác nhận trạng thái thành công trong CodeDeploy Deployment History.

![Triển khai CodeDeploy thành công](/images/5-Workshop/img_B/image31.png)
""")


# --- CHAPTER 5.6: ANALYTICS STREAM ---
c56_dir = os.path.join(workshop_dir, "5.6-Analytics-Stream")
os.makedirs(c56_dir, exist_ok=True)

write_page(os.path.join(c56_dir, "_index.md"), "Asynchronous Post-Match Processing with DynamoDB Streams", 6, "5.6",
"""### Overview
In this chapter, you will enable **DynamoDB Streams** on the `ActiveMatches` table, create the **MatchAnalyticLambda** function, and capture post-match events asynchronously to log analytics without affecting matchmaking latency.

---

### Sub-modules
- [5.6.1 Enable DynamoDB Streams & IAM Roles](5.6.1-enable-dynamodb-streams/)
- [5.6.2 Create MatchAnalytic Lambda & Verify Logs](5.6.2-create-analytics-lambda/)
""", always_open=True)

write_page(os.path.join(c56_dir, "_index.vi.md"), "Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams", 6, "5.6",
"""### Tổng quan
Trong chương này, bạn sẽ bật **DynamoDB Streams** trên bảng `ActiveMatches`, khởi tạo hàm **MatchAnalyticLambda** và thu thập sự kiện kết thúc trận đấu bất đồng bộ để ghi log phân tích mà không gây ảnh hưởng tới độ trễ của hệ thống matchmaking.

---

### Các bài học nhỏ
- [5.6.1 Kích hoạt DynamoDB Streams & IAM Roles](5.6.1-enable-dynamodb-streams/)
- [5.6.2 Khởi tạo MatchAnalytic Lambda & Kiểm thử Log](5.6.2-create-analytics-lambda/)
""", always_open=True)

# 5.6.1
c561_dir = os.path.join(c56_dir, "5.6.1-enable-dynamodb-streams")
os.makedirs(c561_dir, exist_ok=True)
write_page(os.path.join(c561_dir, "_index.md"), "Enable DynamoDB Streams & IAM Roles", 1, "5.6.1",
"""### Step-by-Step Implementation

#### Step 1: Enable DynamoDB Streams
1. Navigate to **DynamoDB** -> Select `ActiveMatches` table.
2. Under **Exports and streams**, enable **DynamoDB stream** (View type: `NEW_AND_OLD_IMAGES`).

![Enable DynamoDB Stream](/images/5-Workshop/img_B/image33.png)

---

#### Step 2: Create IAM Role for Analytics Lambda
1. Create IAM Role `MatchAnalyticRole`.
2. Attach policy granting read access to DynamoDB Streams (`dynamodb:GetRecords`, `dynamodb:GetShardIterator`, `dynamodb:DescribeStream`, `dynamodb:ListStreams`).

![Create MatchAnalytic Role](/images/5-Workshop/img_B/image36.png)
![Stream Reading Policy](/images/5-Workshop/img_B/image37.png)
""")

write_page(os.path.join(c561_dir, "_index.vi.md"), "Kích hoạt DynamoDB Streams & IAM Roles", 1, "5.6.1",
"""### Các bước thực hiện

#### Bước 1: Bật DynamoDB Streams
1. Vào **DynamoDB** console -> Chọn bảng `ActiveMatches`.
2. Tại mục **Exports and streams**, bật **DynamoDB stream** (View type: `NEW_AND_OLD_IMAGES`).

![Bật DynamoDB Stream](/images/5-Workshop/img_B/image33.png)

---

#### Bước 2: Tạo IAM Role cho Analytics Lambda
1. Tạo IAM Role `MatchAnalyticRole`.
2. Gắn Policy cho phép đọc dữ liệu từ DynamoDB Streams (`dynamodb:GetRecords`, `dynamodb:GetShardIterator`, `dynamodb:DescribeStream`, `dynamodb:ListStreams`).

![Tạo Role MatchAnalytic](/images/5-Workshop/img_B/image36.png)
![Policy đọc Stream](/images/5-Workshop/img_B/image37.png)
""")

# 5.6.2
c562_dir = os.path.join(c56_dir, "5.6.2-create-analytics-lambda")
os.makedirs(c562_dir, exist_ok=True)
write_page(os.path.join(c562_dir, "_index.md"), "Create MatchAnalytic Lambda & Verify Logs", 2, "5.6.2",
"""### Step-by-Step Implementation

#### Step 1: Create `MatchAnalyticLambda` Function
1. Navigate to **AWS Lambda** -> Click **Create function**.
2. Name: `MatchAnalyticLambda`.
3. Assign `MatchAnalyticRole`.

![Create MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Step 2: Configure Event Source Mapping & Verify Analytics Output
1. Add DynamoDB Stream trigger to `MatchAnalyticLambda`.
2. Test match conclusion: when a match record transitions to finished state, `MatchAnalyticLambda` automatically processes player statistics and writes event logs to the analytics store.

![DynamoDB Stream Event Data](/images/5-Workshop/img_B/image40.png)
""")

write_page(os.path.join(c562_dir, "_index.vi.md"), "Khởi tạo MatchAnalytic Lambda & Kiểm thử Log", 2, "5.6.2",
"""### Các bước thực hiện

#### Bước 1: Tạo `MatchAnalyticLambda` Function
1. Vào **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `MatchAnalyticLambda`.
3. Gắn `MatchAnalyticRole` vừa tạo.

![Tạo MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Bước 2: Cấu hình Event Source Mapping & Kiểm tra Log Phân tích
1. Thêm Trigger DynamoDB Stream cho `MatchAnalyticLambda`.
2. Kiểm thử kết thúc trận đấu: khi bản ghi trận đấu chuyển sang trạng thái hoàn thành (finished), `MatchAnalyticLambda` tự động bắt sự kiện, tính toán chỉ số và ghi log analytics ngầm.

![Dữ liệu Event từ DynamoDB Stream](/images/5-Workshop/img_B/image40.png)
""")


# --- CHAPTER 5.7: RESOURCE CLEANUP ---
c57_dir = os.path.join(workshop_dir, "5.7-Cleanup")
os.makedirs(c57_dir, exist_ok=True)

write_page(os.path.join(c57_dir, "_index.md"), "Resource Cleanup", 7, "5.7",
"""### Overview
In this final chapter, you will clean up the AWS resources created during this workshop to prevent ongoing charges. Follow the step-by-step instructions for each service.

---

### Sub-modules
- [5.7.1 Clean Up Cognito & DynamoDB](5.7.1-cleanup-cognito-dynamodb/)
- [5.7.2 Clean Up Lambda & API Gateway](5.7.2-cleanup-lambda-apigateway/)
- [5.7.3 Clean Up CloudFront & WAF](5.7.3-cleanup-cloudfront-waf/)
""", always_open=True)

write_page(os.path.join(c57_dir, "_index.vi.md"), "Dọn dẹp tài nguyên", 7, "5.7",
"""### Tổng quan
Trong chương cuối cùng này, bạn sẽ tiến hành dọn dẹp các tài nguyên AWS đã khởi tạo trong suốt bài thực hành để tránh phát sinh chi phí không mong muốn. Hãy thực hiện dọn dẹp lần lượt theo từng bước hướng dẫn.

---

### Các bài học nhỏ
- [5.7.1 Dọn dẹp Cognito & DynamoDB](5.7.1-cleanup-cognito-dynamodb/)
- [5.7.2 Dọn dẹp Lambda & API Gateway](5.7.2-cleanup-lambda-apigateway/)
- [5.7.3 Dọn dẹp CloudFront & WAF](5.7.3-cleanup-cloudfront-waf/)
""", always_open=True)

# 5.7.1
c571_dir = os.path.join(c57_dir, "5.7.1-cleanup-cognito-dynamodb")
os.makedirs(c571_dir, exist_ok=True)
write_page(os.path.join(c571_dir, "_index.md"), "Clean Up Cognito & DynamoDB", 1, "5.7.1",
"""### Step-by-Step Implementation

#### Step 1: Delete Cognito User Pool
1. Go to the **Amazon Cognito** console -> **User pools**.
2. Select the User pool you created and click **Delete**.
3. Confirm deletion by typing the pool name.

![Delete Cognito User Pool](/images/5-Workshop/img_C/image1.png)
![Confirm Delete User Pool](/images/5-Workshop/img_C/image2.png)

---

#### Step 2: Delete Cognito Identity Pool
1. Select **Identity pools** from the Cognito dashboard.
2. Select the Identity pool you created and click **Delete**.
3. Confirm the deletion.

![Delete Cognito Identity Pool](/images/5-Workshop/img_C/image3.png)
![Confirm Delete Identity Pool](/images/5-Workshop/img_C/image4.png)

---

#### Step 3: Delete DynamoDB Tables
1. Go to the **Amazon DynamoDB** console -> **Tables**.
2. Select all the tables you created (`MatchmakingQueue`, `ActiveMatches`).
3. Click **Delete** and confirm.

![Delete DynamoDB Tables](/images/5-Workshop/img_C/image5.png)
![Confirm Delete Tables](/images/5-Workshop/img_C/image6.png)
""")

write_page(os.path.join(c571_dir, "_index.vi.md"), "Dọn dẹp Cognito & DynamoDB", 1, "5.7.1",
"""### Các bước thực hiện

#### Bước 1: Xóa Cognito User Pool
1. Truy cập **Amazon Cognito** console -> **User pools**.
2. Chọn User pool đã tạo và click **Delete**.
3. Xác nhận xóa bằng cách nhập tên pool.

![Xóa Cognito User Pool](/images/5-Workshop/img_C/image1.png)
![Xác nhận xóa User Pool](/images/5-Workshop/img_C/image2.png)

---

#### Bước 2: Xóa Cognito Identity Pool
1. Chọn **Identity pools** trên thanh điều hướng Cognito.
2. Chọn Identity pool đã tạo và click **Delete**.
3. Xác nhận hành động xóa.

![Xóa Cognito Identity Pool](/images/5-Workshop/img_C/image3.png)
![Xác nhận xóa Identity Pool](/images/5-Workshop/img_C/image4.png)

---

#### Bước 3: Xóa Bảng DynamoDB
1. Truy cập **Amazon DynamoDB** console -> **Tables**.
2. Chọn tất cả các bảng đã khởi tạo (`MatchmakingQueue`, `ActiveMatches`).
3. Nhấp **Delete** và xác nhận.

![Xóa Bảng DynamoDB](/images/5-Workshop/img_C/image5.png)
![Xác nhận xóa Bảng](/images/5-Workshop/img_C/image6.png)
""")

# 5.7.2
c572_dir = os.path.join(c57_dir, "5.7.2-cleanup-lambda-apigateway")
os.makedirs(c572_dir, exist_ok=True)
write_page(os.path.join(c572_dir, "_index.md"), "Clean Up Lambda & API Gateway", 2, "5.7.2",
"""### Step-by-Step Implementation

#### Step 1: Delete Lambda Functions
1. Go to the **AWS Lambda** console -> **Functions**.
2. Select the Lambda functions you created (`FightingGameMatchmaker`, `MatchAnalyticLambda`).
3. Click **Actions** -> **Delete** and confirm.

![Delete Lambda Functions](/images/5-Workshop/img_C/image7.png)
![Confirm Delete Lambda Functions](/images/5-Workshop/img_C/image8.png)

---

#### Step 2: Delete API Gateway APIs
1. Go to the **Amazon API Gateway** console.
2. Select the API you created (`FightingGameAPI`).
3. Click **Actions** -> **Delete** and confirm.

![Delete API Gateway](/images/5-Workshop/img_C/image9.png)
![Confirm Delete API](/images/5-Workshop/img_C/image10.png)
""")

write_page(os.path.join(c572_dir, "_index.vi.md"), "Dọn dẹp Lambda & API Gateway", 2, "5.7.2",
"""### Các bước thực hiện

#### Bước 1: Xóa các Lambda Function
1. Truy cập **AWS Lambda** console -> **Functions**.
2. Chọn các Function đã khởi tạo (`FightingGameMatchmaker`, `MatchAnalyticLambda`).
3. Chọn **Actions** -> **Delete** và xác nhận xóa.

![Xóa các Lambda Function](/images/5-Workshop/img_C/image7.png)
![Xác nhận xóa Lambda Function](/images/5-Workshop/img_C/image8.png)

---

#### Bước 2: Xóa API Gateway
1. Truy cập **Amazon API Gateway** console.
2. Chọn API đã khởi tạo (`FightingGameAPI`).
3. Chọn **Actions** -> **Delete** và xác nhận.

![Xóa API Gateway](/images/5-Workshop/img_C/image9.png)
![Xác nhận xóa API](/images/5-Workshop/img_C/image10.png)
""")

# 5.7.3
c573_dir = os.path.join(c57_dir, "5.7.3-cleanup-cloudfront-waf")
os.makedirs(c573_dir, exist_ok=True)
write_page(os.path.join(c573_dir, "_index.md"), "Clean Up CloudFront & WAF", 3, "5.7.3",
"""### Step-by-Step Implementation

#### Step 1: Disable and Delete CloudFront Distribution
1. Go to the **Amazon CloudFront** console -> **Distributions**.
2. Select the Distribution you created -> Click **Disable**.
3. Confirm and wait 5-10 minutes for status transition to completed.
4. Select it again and click **Delete**.

![Disable CloudFront Distribution](/images/5-Workshop/img_C/image11.png)
![Confirm Disable Distribution](/images/5-Workshop/img_C/image12.png)
![Delete CloudFront Distribution](/images/5-Workshop/img_C/image13.png)

---

#### Step 2: Disassociate and Delete WAF Web ACL
1. Go to the **AWS WAF & Shield** console -> **Web ACLs**.
2. Select your ACL (e.g. `CreatedByCloudFront-56a8180e`).
3. Go to **Associated AWS resources** and disassociate the CloudFront distribution.
4. Go back to Web ACLs list -> click **Delete**.

![Manage Associated WAF Resources](/images/5-Workshop/img_C/image14.png)
![Disassociate and Delete WAF ACL](/images/5-Workshop/img_C/image15.png)
""")

write_page(os.path.join(c573_dir, "_index.vi.md"), "Dọn dẹp CloudFront & WAF", 3, "5.7.3",
"""### Các bước thực hiện

#### Bước 1: Vô hiệu hóa và Xóa CloudFront Distribution
1. Truy cập **Amazon CloudFront** console -> **Distributions**.
2. Chọn Distribution đã khởi tạo -> Click **Disable**.
3. Xác nhận và đợi 5-10 phút để quá trình vô hiệu hóa hoàn tất.
4. Chọn lại Distribution đó và bấm **Delete** để xóa hẳn.

![Vô hiệu hóa CloudFront Distribution](/images/5-Workshop/img_C/image11.png)
![Xác nhận vô hiệu hóa](/images/5-Workshop/img_C/image12.png)
![Xóa CloudFront Distribution](/images/5-Workshop/img_C/image13.png)

---

#### Bước 2: Gỡ liên kết và Xóa WAF Web ACL
1. Truy cập **AWS WAF & Shield** console -> **Web ACLs**.
2. Chọn Web ACL của bạn (ví dụ: `CreatedByCloudFront-56a8180e`).
3. Chọn tab **Associated AWS resources** và gỡ liên kết (Disassociate) với CloudFront distribution.
4. Quay lại danh sách Web ACLs -> Chọn ACL và bấm **Delete**.

![Quản lý tài nguyên liên kết WAF](/images/5-Workshop/img_C/image14.png)
![Gỡ liên kết và Xóa WAF ACL](/images/5-Workshop/img_C/image15.png)
""")

print("Updated 5.x index files with Demo Web and Source Code links and Chapter 5.7 Cleanup!")

