---
title: "Event 2"
date: 2025-06-27
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---
# Báo cáo tổng kết: AWS SageMaker Deep Dive

### Thông tin sự kiện:
* **Tên Sự Kiện:** AWS SageMaker Deep Dive (Công bố các tính năng nổi bật từ AWS re:Invent 2024)
* **Thời gian tổ chức:** Ngày 27-06-2025
* **Địa điểm tổ chức:** Workshop kết hợp trực tiếp & trực tuyến tại Tầng 26 (và tầng 36), Tòa tháp Bitexco Financial Tower, Số 02 Hải Triều, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh
* **Đơn vị tổ chức:** AWS (Amazon Web Services), phát trực tiếp trên kênh YouTube AWS Study Group

---

### Mục đích của sự kiện:
* **Đi sâu vào công nghệ AI/ML:** Khám phá nền tảng hợp nhất SageMaker Unified Studio và các khả năng phát triển AI/học máy mới nhất của hệ sinh thái AWS.
* **Môi trường lập trình hợp nhất:** Giới thiệu một giải pháp tích hợp duy nhất giúp kết hợp các tác vụ: xử lý dữ liệu (data prep), phân tích SQL, huấn luyện mô hình học máy (ML), phát triển AI tạo sinh (GenAI) và quản trị dữ liệu.
* **Hợp tác không biên giới:** Xóa bỏ các rào cản làm việc độc lập (silos) để các kỹ sư dữ liệu (Data Engineers), nhà khoa học dữ liệu (Data Scientists) và nhà phân tích dữ liệu (Data Analysts) có thể hợp tác trực tiếp trong một không gian duy nhất.

---

### Danh sách diễn giả:
* **Anh Trung** – Diễn giả 1
* **Kirara Lador** – Diễn giả 2
* **Isaac** – Diễn giả 3

---

### Nội dung nổi bật:

#### 1. Khó khăn từ việc phân mảnh công cụ dữ liệu cũ
* Trước đây, các công cụ xử lý dữ liệu (EMR, Glue, Athena) và công cụ quản lý ML được tách rời riêng biệt, gây bối rối khi chuyển đổi môi trường làm việc.
* Quy trình chia sẻ dữ liệu nội bộ bị tắc nghẽn do phải chờ đợi bộ phận quản trị viên hoặc IT cấp quyền thủ công.
* Dữ liệu mang tính kỹ thuật thô khó hiểu đối với nhóm người dùng kinh doanh (business users).

#### 2. Giải pháp: SageMaker Unified Studio
* **Unified Studio:** Cung cấp một môi trường hợp nhất, cho phép toàn quyền truy cập an toàn vào kho mã nguồn (code repositories), tài nguyên tính toán (compute nodes), các mô hình AI và catalog dữ liệu dùng chung.

#### 3. Công nghệ và công cụ nổi bật
* **Jupyter Lab IDE:** Hỗ trợ sổ tay đa ngôn ngữ, cho phép chạy song song các cell code Python, Scala và SQL trong cùng một notebook. Hỗ trợ công cụ kéo thả Visual ETL để xây dựng luồng dữ liệu trực quan.
* **Tích hợp trợ lý Amazon Q:** Trợ lý ảo AI đắc lực tích hợp trực tiếp trong IDE giúp viết truy vấn SQL từ ngôn ngữ tự nhiên, giải thích code, gỡ lỗi và tái cấu trúc (refactor) mã nguồn.
* **Các mô hình AI tiên tiến:** Tích hợp với Amazon Bedrock, SageMaker Jumpstart và các mô hình LLM mới như Amazon Nova, Claude 4. Giới thiệu hệ thống SageMaker HyperPod phục vụ huấn luyện mô hình phân tán cực lớn.
* **Quản trị dữ liệu (Data Governance):** Hỗ trợ tính năng Data Catalog, Data Lineage (truy vết nguồn gốc dữ liệu) và đóng gói dữ liệu thành các "Data Products" (Sản phẩm dữ liệu).

#### 4. Demo & Case Study thực tế
* **Demo vai trò phối hợp:** Diễn giả Kirara hóa thân vào 3 vai trò: Data Engineer thiết lập chính sách bảo mật dữ liệu, Data Scientist yêu cầu cấp quyền truy cập để huấn luyện mô hình dự báo nợ xấu (loan default prediction), và Data Analyst tìm kiếm bộ dữ liệu Marketing. Tất cả quy trình gửi yêu cầu và duyệt quyền đều tự động và mượt mà trên giao diện Unified Studio.
* **Tự động sinh Business Metadata:** Dùng GenAI để tự động điền các mô tả bối cảnh kinh doanh cho hàng trăm cột dữ liệu kỹ thuật thô để người làm kinh doanh dễ hiểu.
* **Khái niệm Data Product:** Gom các bảng dữ liệu liên quan thành một sản phẩm dữ liệu duy nhất. Người dùng chỉ cần gửi một yêu cầu cấp quyền duy nhất cho Data Product thay vì xin phép hàng trăm bảng riêng lẻ.

---

### Những gì học được:

#### 1. Tư duy cộng tác dữ liệu (Data Collaboration)
* Chuyển đổi từ mô hình làm việc độc lập sang hợp tác dữ liệu đa chức năng. Quản trị dữ liệu không phải là khóa kín thông tin, mà là làm cho dữ liệu dễ khám phá (discoverable) nhưng vẫn đảm bảo bảo mật nghiêm ngặt.
* **Quản lý thay đổi:** Sử dụng tính năng Data Lineage để xác định những ai đang tiêu thụ dữ liệu của mình (data consumers) trước khi thay đổi cấu trúc bảng, tránh làm hỏng các báo cáo của bộ phận khác.

#### 2. Kiến thức kỹ thuật
* Hiểu cách hệ thống lưu vết sự biến đổi dữ liệu (Data Lineage) để vẽ bản đồ luồng đi của dữ liệu từ nguồn gốc đến bảng đích.
* Thực hiện phân luồng Apache Airflow (MWAA) trực tiếp trên giao diện của Studio.
* **Bảo mật chuyên sâu:** Cấu hình bảo mật cấp độ cột (Column-level security) để che giấu các thông tin nhạy cảm (như thông tin cá nhân PII) trước khi cấp quyền truy cập cho Data Scientist.
* **Tối ưu mã nguồn:** Sử dụng tính năng Refactor của Amazon Q để viết lại code chuẩn hóa, tăng hiệu năng và tối ưu cấu trúc.

---

### Ứng dụng vào công việc:
* **Duyệt quyền tự phục vụ (Self-service):** Áp dụng cơ chế xin quyền qua giao diện UI thay vì viết lệnh SQL GRANT thủ công để loại bỏ điểm nghẽn hành chính.
* **Tự động hóa luồng ETL:** Thử nghiệm dùng Amazon Q để tự động sinh các pipeline Visual ETL từ câu lệnh mô tả ngôn ngữ tự nhiên.
* **Triển khai mô hình nhanh:** Sử dụng SageMaker Jumpstart để deploy nhanh các mô hình mã nguồn mở (như Hugging Face) chỉ với vài dòng code.
* **Chuẩn hóa chia sẻ dữ liệu:** Dừng việc copy file CSV thủ công qua lại trong S3; áp dụng Business Glossary để chuẩn hóa từ vựng doanh nghiệp.

---

### Trải nghiệm trong sự kiện:
* **Tính thực tiễn cao:** Lộ trình bài giảng đi từ lý thuyết tổng quan đến trực quan hóa quy trình phối hợp qua Demo của Kiara và Isaac.
* **Thực hành Hands-on:** Tham gia trực tiếp các buổi lab thực hành xử lý dữ liệu trên môi trường AWS.
* **Giao lưu kết nối:** Diễn giả nhiệt tình hỗ trợ trực tiếp sau sự kiện các thắc mắc chuyên sâu về thiết lập SageMaker Hyperpod.
* **Ấn tượng nhất:** Spark debugging UI được nhúng trực tiếp vào IDE, giúp theo dõi lỗi thực thi mà không cần cấu hình mạng phức tạp.

---

### Bài học rút ra & Định hướng:
* **Sự chuyển mình của SageMaker:** Amazon SageMaker đã chuyển đổi từ công cụ học máy (ML) đơn lẻ thành một nền tảng Học máy và Phân tích (Machine learning and analytics product) toàn diện bao phủ toàn bộ vòng đời dữ liệu.
* **Định hướng tiếp theo:** Tìm hiểu sâu về kiến trúc Data Lakehouse, cách ứng dụng dòng mô hình nhỏ/tốc độ cao Amazon Nova và tích hợp công cụ MLflow để theo dõi lịch sử huấn luyện mô hình.

---

### Hình ảnh trong sự kiện:
![AWS SageMaker Deep Dive Intro Ho Chi Minh City](/images/4-EventParticipated/event2-1.png)

![AWS SageMaker Deep Dive Live Demo Lineage](/images/4-EventParticipated/event2-2.png)

![AWS SageMaker AI Notebook Development](/images/4-EventParticipated/event2-3.png)
