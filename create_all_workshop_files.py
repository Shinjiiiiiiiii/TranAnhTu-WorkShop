import os

base_dir = r"c:\Study\TranAnhTu-workshop-main"
workshop_dir = os.path.join(base_dir, "content", "5-Workshop")

def write_subfolder(folder, title_en, title_vi, weight, content_en, content_vi):
    target_path = os.path.join(workshop_dir, folder)
    os.makedirs(target_path, exist_ok=True)
    
    header_en = f"""---
title: "{title_en}"
date: 2026-07-21
weight: {weight}
chapter: false
pre: " <b> 5.{weight}. </b> "
---

"""
    header_vi = f"""---
title: "{title_vi}"
date: 2026-07-21
weight: {weight}
chapter: false
pre: " <b> 5.{weight}. </b> "
---

"""
    with open(os.path.join(target_path, "_index.md"), "w", encoding="utf-8") as f:
        f.write(header_en + content_en)
        
    with open(os.path.join(target_path, "_index.vi.md"), "w", encoding="utf-8") as f:
        f.write(header_vi + content_vi)

# Main index EN
main_index_en = """---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Live-Service Game Backend Architecture on AWS
### Step-by-Step Hands-On Implementation Guide

### Overview
This workshop provides a complete, step-by-step hands-on implementation guide for building a serverless and Spot Instance backend architecture for live-service multiplayer games on AWS.

You will learn how to configure authentication with Amazon Cognito, build a serverless matchmaking queue with DynamoDB and AWS Lambda, expose REST APIs using Amazon API Gateway, manage an EC2 Spot fleet for live game servers, automate deployments with GitHub Actions and AWS CodeDeploy, and process post-match analytics asynchronously with DynamoDB Streams.

### Table of Contents

1. [User Authentication with Amazon Cognito](5.1-Cognito/)
2. [Database Setup: DynamoDB Matchmaking Queue & Active Matches](5.2-DynamoDB/)
3. [Matchmaker Lambda & API Gateway REST API](5.3-Lambda-API/)
4. [EC2 Game Server & Auto Scaling Group Warm Pool](5.4-EC2-ASG/)
5. [GitOps CI/CD Pipeline & AWS CodeDeploy](5.5-GitOps-CodeDeploy/)
6. [Asynchronous Post-Match Processing with DynamoDB Streams](5.6-Analytics-Stream/)
"""

# Main index VI
main_index_vi = """---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Xây dựng Kiến trúc Backend Game Live-Service trên AWS
### Hướng dẫn Triển khai Chi tiết từng bước (Hands-On Lab)

### Tổng quan
Bài lab thực hành (Workshop) này hướng dẫn chi tiết từng bước cách thiết lập và triển khai hệ thống Backend cho Game Live-Service trên đám mây AWS kết hợp kiến trúc Serverless và cụm máy chủ EC2 Spot Instance.

Bạn sẽ thực hành cấu hình xác thực người chơi với Amazon Cognito, xây dựng hàng đợi ghép trận với DynamoDB và AWS Lambda, công khai REST API qua Amazon API Gateway, quản lý cụm máy chủ EC2 Spot cho các phiên chơi game, tự động hóa quy trình CI/CD qua GitHub Actions & AWS CodeDeploy, và xử lý dữ liệu sau trận đấu bất đồng bộ với DynamoDB Streams.

### Nội dung bài Lab

1. [Xác thực người dùng với Amazon Cognito](5.1-Cognito/)
2. [Khởi tạo Cơ sở dữ liệu DynamoDB: MatchmakingQueue & ActiveMatches](5.2-DynamoDB/)
3. [Xây dựng Matchmaker Lambda & API Gateway REST API](5.3-Lambda-API/)
4. [Cấu hình EC2 Game Server & Auto Scaling Group Warm Pool](5.4-EC2-ASG/)
5. [Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy](5.5-GitOps-CodeDeploy/)
6. [Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams](5.6-Analytics-Stream/)
"""

with open(os.path.join(workshop_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write(main_index_en)

with open(os.path.join(workshop_dir, "_index.vi.md"), "w", encoding="utf-8") as f:
    f.write(main_index_vi)

# Chapter 5.1 - Cognito
c1_en = """### Overview
In this module, you will configure **Amazon Cognito User Pools** and **Cognito Identity Pools** to handle user sign-up, sign-in, and temporary IAM credential generation for downloading game assets.

---

### Step-by-Step Implementation

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

---

#### Step 3: Configure App Client
1. Navigate to **Applications** -> **App clients**.
2. Select `FightingGame` app client.
3. Under **Authentication flows**, enable `ALLOW_USER_PASSWORD_AUTH`.
4. Save changes.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![App Client Settings](/images/5-Workshop/img_A/image12.png)
![Authentication Flow](/images/5-Workshop/img_A/image14.png)

---

#### Step 4: Create Cognito Identity Pool
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

---

#### Step 5: Verify User Registration UI
1. Open the game client frontend.
2. Test user registration and authentication flow.

![User Registration UI](/images/5-Workshop/img_A/image99.png)
"""

c1_vi = """### Tổng quan
Trong phần này, bạn sẽ thực hành cấu hình **Amazon Cognito User Pools** và **Cognito Identity Pools** để xử lý đăng ký, đăng nhập và cấp quyền IAM ngắn hạn cho client tải tài nguyên game.

---

### Các bước thực hiện

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

---

#### Bước 3: Cấu hình App Client
1. Vào mục **Applications** -> **App clients**.
2. Chọn client `FightingGame` và bấm Edit.
3. Tại **Authentication flows**, tích chọn `ALLOW_USER_PASSWORD_AUTH`.
4. Bấm **Save changes**.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![Cấu hình App Client](/images/5-Workshop/img_A/image12.png)
![Cho phép Password Auth](/images/5-Workshop/img_A/image14.png)

---

#### Bước 4: Tạo Cognito Identity Pool
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

---

#### Bước 5: Kiểm tra giao diện đăng ký/đăng nhập người chơi
1. Mở giao diện frontend ứng dụng game.
2. Đăng ký tài khoản người chơi thử nghiệm.

![Giao diện Đăng ký người dùng](/images/5-Workshop/img_A/image99.png)
"""

write_subfolder("5.1-Cognito", "User Authentication with Amazon Cognito", "Xác thực người dùng với Amazon Cognito", 1, c1_en, c1_vi)

# Chapter 5.2 - DynamoDB
c2_en = """### Overview
In this module, you will create two core **Amazon DynamoDB** tables: `MatchmakingQueue` (for pending players) and `ActiveMatches` (for active match sessions).

---

### Step-by-Step Implementation

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

---

#### Step 3: Create Table `ActiveMatches`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create ActiveMatches Table](/images/5-Workshop/img_A/image28.png)

---

#### Step 4: Verify Tables Status
1. Check the table list to ensure both `MatchmakingQueue` and `ActiveMatches` have reached `Active` status.

![Active DynamoDB Tables](/images/5-Workshop/img_A/image29.png)
"""

c2_vi = """### Tổng quan
Trong phần này, bạn sẽ tiến hành khởi tạo hai bảng **Amazon DynamoDB** cốt lõi: `MatchmakingQueue` (hàng chờ người chơi) và `ActiveMatches` (lưu phiên trận đấu đang diễn ra).

---

### Các bước thực hiện

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

---

#### Bước 3: Tạo Bảng `ActiveMatches`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng ActiveMatches](/images/5-Workshop/img_A/image28.png)

---

#### Bước 4: Kiểm tra trạng thái Bảng
1. Kiểm tra danh sách bảng đảm bảo cả `MatchmakingQueue` và `ActiveMatches` đều ở trạng thái `Active`.

![Bảng DynamoDB ở trạng thái Active](/images/5-Workshop/img_A/image29.png)
"""

write_subfolder("5.2-DynamoDB", "Database Setup: DynamoDB Matchmaking Queue & Active Matches", "Cơ sở dữ liệu DynamoDB: MatchmakingQueue & ActiveMatches", 2, c2_en, c2_vi)

# Chapter 5.3 - Lambda-API
c3_en = """### Overview
In this module, you will build the **FightingGameMatchmaker** AWS Lambda function to process player queueing (`POST /join`) and match checks (`GET /check`), and expose these endpoints via **Amazon API Gateway** secured by Cognito Authorizer.

---

### Step-by-Step Implementation

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

---

#### Step 4: Create Amazon API Gateway REST API
1. Navigate to **API Gateway** console -> Click **Create API**.
2. Select **REST API** -> Build.
3. API Name: `FightingGameAPI`.

![API Gateway Console](/images/5-Workshop/img_A/image56.png)

---

#### Step 5: Create Resources `/join` & `/check`
1. Click **Create resource**:
   - Resource Name: `join` -> Create method `POST` -> Link to `FightingGameMatchmaker` Lambda.
2. Click **Create resource**:
   - Resource Name: `check` -> Create method `GET` -> Link to `FightingGameMatchmaker` Lambda.

![Create Resource Join](/images/5-Workshop/img_A/image61.png)
![Create Resource Check](/images/5-Workshop/img_A/image68.png)

---

#### Step 6: Configure Cognito Authorizer & CORS
1. Under **Authorizers**, click **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Attach `FightinggameCognitoAuthorizer` to `/join` (POST) and `/check` (GET) method request settings.
3. Enable **CORS** for both `/join` and `/check` endpoints.

![Create Cognito Authorizer](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Step 7: Deploy API Gateway
1. Select `/` root resource -> Click **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API](/images/5-Workshop/img_A/image84.png)
"""

c3_vi = """### Tổng quan
Trong phần này, bạn sẽ triển khai hàm AWS Lambda **FightingGameMatchmaker** để xử lý yêu cầu tham gia hàng chờ (`POST /join`) và kiểm tra trạng thái trận đấu (`GET /check`), sau đó công khai dịch vụ qua **Amazon API Gateway** tích hợp bảo mật Cognito Authorizer.

---

### Các bước thực hiện

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

---

#### Bước 4: Tạo Amazon API Gateway REST API
1. Mở console **API Gateway** -> Chọn **Create API**.
2. Chọn **REST API** -> Bấm Build.
3. Đặt tên API: `FightingGameAPI`.

![Tạo REST API](/images/5-Workshop/img_A/image56.png)

---

#### Bước 5: Khởi tạo Resource `/join` & `/check`
1. Bấm **Create resource**:
   - Resource Name: `join` -> Tạo method `POST` -> Kết nối với `FightingGameMatchmaker` Lambda.
2. Bấm **Create resource**:
   - Resource Name: `check` -> Tạo method `GET` -> Kết nối với `FightingGameMatchmaker` Lambda.

![Tạo Resource /join](/images/5-Workshop/img_A/image61.png)
![Tạo Resource /check](/images/5-Workshop/img_A/image68.png)

---

#### Bước 6: Thêm Cognito Authorizer & Cấu hình CORS
1. Vào mục **Authorizers** -> Bấm **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Gắn `FightinggameCognitoAuthorizer` vào Method Request của `/join` (POST) và `/check` (GET).
3. Bật **Enable CORS** cho cả hai resource `/join` và `/check`.

![Tạo Authorizer Cognito](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Bước 7: Deploy API Gateway
1. Chọn gốc `/` -> Bấm **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API thành công](/images/5-Workshop/img_A/image84.png)
"""

write_subfolder("5.3-Lambda-API", "Matchmaker Lambda & API Gateway REST API", "Matchmaker Lambda & API Gateway REST API", 3, c3_en, c3_vi)

# Chapter 5.4 - EC2-ASG
c4_en = """### Overview
In this module, you will launch the baseline **EC2 Game Server**, bake a customized **AMI**, create a **Launch Template**, configure an **Auto Scaling Group (ASG) Warm Pool**, and set up the **Amazon S3 Asset Bucket**.

---

### Step-by-Step Implementation

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

---

#### Step 3: Bake Custom AMI & Create Launch Template
1. Tag the running server instance.
2. Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Create AMI](/images/5-Workshop/img_B/image5.png)

3. Navigate to **Launch Templates** -> Click **Create launch template**:
   - Select `FightingGameServer-AMI`.
   - Set Purchasing Option: **Spot Instances**.

![Create Launch Template](/images/5-Workshop/img_B/image6.png)

---

#### Step 4: Configure Auto Scaling Group (ASG) Warm Pool
1. Create Auto Scaling Group: `FightingGameServerASG`.
2. Attach Launch Template.
3. Configure **Warm Pool** settings to maintain pre-initialized warm instances ready for instant match assignment.

![Configure ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Step 5: Create Amazon S3 Asset Bucket
1. Create S3 Bucket for client builds, patches, and game server bundles.
2. Configure **Public Read Bucket Policy** and **CORS** rules.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Step 6: Assign IAM Instance Profile
1. Create `FightingGameServerInstanceRole` with S3 read permissions.
2. Attach IAM Instance Profile to EC2 Launch Template.

![Attach Instance Role](/images/5-Workshop/img_B/image18.png)
"""

c4_vi = """### Tổng quan
Trong phần này, bạn sẽ khởi tạo máy chủ game mẫu trên **Amazon EC2**, đóng gói **AMI**, thiết lập **Launch Template**, cấu hình **Auto Scaling Group (ASG) Warm Pool** và khởi tạo **S3 Asset Bucket**.

---

### Các bước thực hiện

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

---

#### Bước 3: Gán Tag, Đóng gói AMI & Tạo Launch Template
1. Gán Tag định danh cho game server.
2. Chọn Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Tạo AMI](/images/5-Workshop/img_B/image5.png)

3. Vào mục **Launch Templates** -> Bấm **Create launch template**:
   - Chọn AMI vừa tạo (`FightingGameServer-AMI`).
   - Cấu hình tùy chọn mua tài nguyên: **Spot Instances**.

![Tạo Launch Template Spot](/images/5-Workshop/img_B/image6.png)

---

#### Bước 4: Cấu hình Auto Scaling Group (ASG) Warm Pool
1. Tạo Auto Scaling Group: `FightingGameServerASG`.
2. Gắn Launch Template vừa tạo.
3. Cấu hình **Warm Pool** để duy trì các instance khởi động sẵn (warm), đáp ứng việc gán phòng tức thì khi có trận đấu mới.

![Cấu hình ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Bước 5: Tạo Amazon S3 Asset Bucket
1. Tạo S3 Bucket lưu trữ các bản build client, patch và server binary.
2. Cấu hình **Bucket Policy** và quy tắc **CORS**.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Bước 6: Cấu hình IAM Instance Profile
1. Tạo IAM Role `FightingGameServerInstanceRole` cấp quyền truy cập S3.
2. Gắn IAM Instance Profile vào EC2 Launch Template.

![Gắn IAM Role cho EC2](/images/5-Workshop/img_B/image18.png)
"""

write_subfolder("5.4-EC2-ASG", "EC2 Game Server & Auto Scaling Group Warm Pool", "Cấu hình EC2 Game Server & ASG Warm Pool", 4, c4_en, c4_vi)

# Chapter 5.5 - GitOps-CodeDeploy
c5_en = """### Overview
In this module, you will integrate **GitHub Actions OIDC** for passwordless authentication, install and patch the **AWS CodeDeploy Agent** on Ubuntu 24.04 LTS, configure CodeDeploy applications, and execute automated zero-downtime deployments.

---

### Step-by-Step Implementation

#### Step 1: Configure GitHub OIDC Provider in AWS IAM
1. Navigate to **IAM** -> **Identity providers** -> Add **GitHub OIDC Provider**.
2. Create an IAM Role for GitHub Actions with trust policy restricted to `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Add GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![GitHub Role Trust Policy](/images/5-Workshop/img_B/image14.png)

---

#### Step 2: Install & Patch AWS CodeDeploy Agent on Ubuntu 24.04 LTS
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

---

#### Step 3: Create AWS CodeDeploy Application & Deployment Group
1. Create CodeDeploy Role for EC2 and Lambda deployments.
2. Create CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Create Deployment Group targeting EC2 Spot instances and Lambda alias traffic shifting.

![CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Deployment Group Config](/images/5-Workshop/img_B/image30.png)

---

#### Step 4: Execute Automated Deployment & Verify Logs
1. Trigger GitHub Actions workflow execution.
2. Monitor CodeDeploy job execution progress and verify deployment history.

![Successful CodeDeploy Job](/images/5-Workshop/img_B/image31.png)
"""

c5_vi = """### Tổng quan
Trong phần này, bạn sẽ cấu hình **GitHub Actions OIDC** để xác thực không dùng access key tĩnh, cài đặt và patch **AWS CodeDeploy Agent** trên Ubuntu 24.04 LTS, cấu hình CodeDeploy Application và thực thi quy trình triển khai tự động không gây gián đoạn.

---

### Các bước thực hiện

#### Bước 1: Cấu hình GitHub OIDC Provider trong AWS IAM
1. Vào **IAM** -> **Identity providers** -> Thêm **GitHub OIDC Provider**.
2. Tạo IAM Role dành cho GitHub Actions với Trust Policy giới hạn quyền cho repository `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Thêm GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![Cấu hình Trust Policy](/images/5-Workshop/img_B/image14.png)

---

#### Bước 2: Cài đặt & Patch CodeDeploy Agent trên Ubuntu 24.04 LTS
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

---

#### Bước 3: Tạo AWS CodeDeploy Application & Deployment Group
1. Tạo IAM Role cho CodeDeploy.
2. Tạo CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Tạo Deployment Group cho cụm EC2 và Lambda.

![Tạo CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Cấu hình Deployment Group](/images/5-Workshop/img_B/image30.png)

---

#### Bước 4: Thực thi Triển khai Tự động & Kiểm tra Lịch sử
1. Chạy GitHub Actions workflow để tự động deploy code mới.
2. Theo dõi tiến độ triển khai và xác nhận trạng thái thành công trong CodeDeploy Deployment History.

![Triển khai CodeDeploy thành công](/images/5-Workshop/img_B/image31.png)
"""

write_subfolder("5.5-GitOps-CodeDeploy", "GitOps CI/CD Pipeline & AWS CodeDeploy", "Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy", 5, c5_en, c5_vi)

# Chapter 5.6 - Analytics-Stream
c6_en = """### Overview
In this module, you will enable **DynamoDB Streams** on the `ActiveMatches` table, create the **MatchAnalyticLambda** function, and capture post-match events asynchronously to log analytics without affecting matchmaking latency.

---

### Step-by-Step Implementation

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

---

#### Step 3: Create `MatchAnalyticLambda` Function
1. Navigate to **AWS Lambda** -> Click **Create function**.
2. Name: `MatchAnalyticLambda`.
3. Assign `MatchAnalyticRole`.

![Create MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Step 4: Configure Event Source Mapping & Verify Analytics Output
1. Add DynamoDB Stream trigger to `MatchAnalyticLambda`.
2. Test match conclusion: when a match record transitions to finished state, `MatchAnalyticLambda` automatically processes player statistics and writes event logs to the analytics store.

![DynamoDB Stream Event Data](/images/5-Workshop/img_B/image40.png)
"""

c6_vi = """### Tổng quan
Trong phần này, bạn sẽ bật **DynamoDB Streams** trên bảng `ActiveMatches`, khởi tạo hàm **MatchAnalyticLambda** và thu thập sự kiện kết thúc trận đấu bất đồng bộ để ghi log phân tích mà không gây ảnh hưởng tới độ trễ của hệ thống matchmaking.

---

### Các bước thực hiện

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

---

#### Bước 3: Tạo `MatchAnalyticLambda` Function
1. Vào **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `MatchAnalyticLambda`.
3. Gắn `MatchAnalyticRole` vừa tạo.

![Tạo MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Bước 4: Cấu hình Event Source Mapping & Kiểm tra Log Phân tích
1. Thêm Trigger DynamoDB Stream cho `MatchAnalyticLambda`.
2. Kiểm thử kết thúc trận đấu: khi bản ghi trận đấu chuyển sang trạng thái hoàn thành (finished), `MatchAnalyticLambda` tự động bắt sự kiện, tính toán chỉ số và ghi log analytics ngầm.

![Dữ liệu Event từ DynamoDB Stream](/images/5-Workshop/img_B/image40.png)
"""

write_subfolder("5.6-Analytics-Stream", "Asynchronous Post-Match Processing with DynamoDB Streams", "Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams", 6, c6_en, c6_vi)

print("Updated create_all_workshop_files.py and generated clean files without duplicate H1 headers!")
