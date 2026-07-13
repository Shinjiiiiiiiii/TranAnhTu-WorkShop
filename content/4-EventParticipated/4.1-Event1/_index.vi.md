---
title: "Event 1"
date: 2026-05-23
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---
# Báo cáo tổng kết: FCAJ Community Day

### Thông tin sự kiện:
* **Tên Sự Kiện:** FCAJ Community Day
* **Thời gian tổ chức:** Buổi sáng cuối tuần, ngày 23-05-2026
* **Địa điểm tổ chức:** Tầng 26 (và tầng 36), Tòa tháp Bitexco Financial Tower, Số 02 Hải Triều, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh
* **Đơn vị tổ chức:** Tập thể AWS Study Group (FCAJ Community)

---

### Mục đích của sự kiện:
* **Kết nối & Truyền cảm hứng:** Không chỉ đơn thuần là nghe hội thảo kỹ thuật mà còn tạo ra không gian cởi mở để người tham dự chủ động kết nối, chia sẻ ý tưởng, tìm kiếm bạn bè và đối tác mới.
* **Cập nhật công nghệ:** Đi qua 6 phiên chia sẻ thú vị xoay quanh các chủ đề từ AI, Điện toán đám mây đến các câu chuyện ứng dụng thực tế từ các chuyên gia.
* **Thiết kế hệ thống chuẩn Doanh nghiệp:** Bàn luận chuyên sâu về cách thiết kế hệ thống đáp ứng tốt nghiệp vụ thực tế của doanh nghiệp (enterprise grade).
* **Định hướng nhân sự trẻ:** Giúp người tham gia (đặc biệt là sinh viên và kỹ sư trẻ) hiểu rõ thực tế thị trường lao động trong kỷ nguyên AI, hướng tới việc trang bị kiến thức kỹ thuật thực tế để xây dựng "Sản phẩm thật" thay vì chỉ làm demo.

---

### Danh sách diễn giả:
* **Quỳnh Mai** – MC dẫn dắt chương trình
* **Nguyễn Gia Hưng** – Head of Solution Architect tại AWS Việt Nam, Người sáng lập FCAJ
* **Anh Tịnh** – Platform Engineer tại Gotam X
* **Chị Hải Anh** – Kỹ sư hệ thống tại Pacific Việt Nam
* **Anh Thịnh** – DevOps Engineer
* **Nhóm UTM** – Đội thi tham gia giải Hackathon
* **Chị Vi** – Chuyên gia xây dựng hệ thống tại VBBank

---

### Nội dung nổi bật:

#### 1. Sự dịch chuyển của thị trường công nghệ
* Khi AI giúp chi phí phát triển phần mềm rẻ đi, nhu cầu xây dựng phần mềm thực tế sẽ tăng trưởng mạnh mẽ, kéo theo sự xuất hiện của các vị trí việc làm mới như kỹ sư sửa lỗi code AI (fix bug) hoặc platform engineering.
* **Sử dụng AI thiếu ngữ cảnh:** AI thường trả lời chung chung hoặc lan man do người dùng không cung cấp đầy đủ bối cảnh (context) nghiệp vụ riêng biệt.

#### 2. Tính ngẫu nhiên của LLM trên đám mây
* Ngay cả khi cài đặt tham số `temperature = 0`, các mô hình ngôn ngữ lớn (LLM) host trên cloud vẫn có thể trả về kết quả khác nhau do các thuật toán tối ưu hóa suy luận (inference optimization) từ nhà cung cấp dịch vụ đám mây.

#### 3. Bài toán đánh giá tín dụng Startup
* Đánh giá mức độ tín nhiệm của các Startup là bài toán phức tạp do họ không có tài sản thế chấp truyền thống hay báo cáo tài chính 3 năm liên tiếp.

#### 4. Giải pháp giới thiệu
* **Amazon CloudFront Flat-rate Pricing:** Giải pháp tính phí cố định mới của CloudFront giúp doanh nghiệp tránh rủi ro phát sinh chi phí đột biến (bill spike) khi sử dụng CDN.
* **Hệ thống đa tác nhân (Multi-agent System):** Phân chia vai trò rõ ràng cho nhiều AI Agent (ví dụ: Agent phân tích tài chính, Agent nghiên cứu thị trường) phối hợp giải quyết bài toán phức tạp của doanh nghiệp.
* **Công nghệ/Dịch vụ sử dụng:** Amazon Bedrock Agent Core, Amazon Q (Tạo Agent nội bộ), Amazon S3, Terraform, AWS CloudFront.

#### 5. Demo & Case Study thực tế
* **Phân tích với Amazon Q:** Demo sử dụng Amazon Q để tự động phân tích dữ liệu từ file Excel doanh thu và tạo dashboard trực quan.
* **Ứng dụng UTM Morpho:** Demo ứng dụng AI tự động chuyển đổi bản vẽ wireframe thô thành code HTML/CSS hoàn chỉnh và cho phép kéo thả chỉnh sửa trực tiếp.
* **Thử nghiệm so sánh LLM:** Case study so sánh kết quả sinh text của LLM khi host trên Amazon Bedrock và host ở Local với `temperature = 0`.
* **An toàn thông tin doanh nghiệp:** Việc đưa AI vào vận hành thực tế tại doanh nghiệp yêu cầu quy trình bảo mật cực kỳ khắt khe (Security, Guardrails, chống Prompt Injection, Audit Trail).

---

### Những gì học được:

#### 1. Tư duy thiết kế hệ thống
* Khi xây dựng giải pháp công nghệ, hãy bắt đầu bằng câu hỏi nghiệp vụ lõi: *"Ai xài, xài cái gì, tại sao họ phải xài, khi nào là lúc thích hợp?"*
* **Kinh nghiệm thi Hackathon:** Không nên tham lam nhồi nhét quá nhiều tính năng (tránh overthinking/overload), hãy tập trung giải quyết triệt để 1 tính năng cốt lõi (core feature) tốt nhất.

#### 2. Kiến thức kỹ thuật
* Hiểu sâu hơn về kiến trúc CloudFront (VPC Origin, mTLS).
* Nắm vững nguyên lý hoạt động chọn từ ngữ tiếp theo (logit/probability) của các mô hình LLM.
* **Best Practices:** Cần thực hiện kiểm thử (testing) diện rộng với nhiều trường hợp để kiểm soát output của AI, tránh tình trạng sinh chữ dư thừa (over-generation).

---

### Ứng dụng vào công việc:
* **Cấu hình ngữ cảnh prompt:** Thiết lập vai trò và bối cảnh nghiệp vụ rõ ràng cho các công cụ AI trước khi prompt hỗ trợ viết mã nguồn.
* **Thử nghiệm công nghệ:** Thử nghiệm Bedrock Agent Core để xây dựng hệ thống đa tác nhân và Terraform để quản lý cơ sở hạ tầng tự động (IaC).
* **Quy tắc an toàn (Guardrails):** Cấu hình các bộ lọc an toàn và cơ chế ghi vết (Audit Trail) để đánh giá các quyết định của AI trước khi đưa vào môi trường Production thực tế.

---

### Trải nghiệm trong sự kiện:
* **Góc nhìn từ diễn giả:** Nhận được các bài học quý giá, từ việc khắc phục khó khăn khi không có bằng đại học đến các kinh nghiệm thực chiến khi phát triển AI trong lĩnh vực tài chính ngân hàng.
* **Trực quan sinh động:** Được theo dõi trực tiếp luồng stream UI tự động tạo code từ wireframe và các dashboard tự sinh bởi Amazon Q.
* **Giao lưu kết nối:** Cơ hội tốt để gặp gỡ các kỹ sư, lập trình viên trong ngành để hỏi han ý tưởng và trao đổi kinh nghiệm kiến trúc hệ thống.
* **Bài học cảnh tỉnh:** Câu chuyện một nhân viên vô tình copy code lỗi từ ChatGPT đẩy lên hệ thống Production của ngân hàng, dẫn đến việc phải rà soát mã nguồn toàn hệ thống.

---

### Bài học rút ra & Định hướng:
* **Chuẩn Enterprise:** Việc xây dựng hệ thống AI thực tế cho doanh nghiệp hoàn toàn khác biệt với làm POC hay đồ án sinh viên; nó đòi hỏi các quy chuẩn khắt khe về bảo mật, tuân thủ (compliance) và kỹ thuật phần mềm lõi.
* **Lợi thế cạnh tranh:** Các yếu tố như kiến thức thực tế doanh nghiệp, kỹ năng tạo ra sản phẩm hoàn chỉnh, tiếng Anh, kỹ năng mềm và bằng đại học vẫn luôn là lợi thế lớn.
* **Định hướng tiếp theo:** Tìm hiểu sâu về "AI Adoption" và củng cố vững chắc nền tảng kỹ thuật phần mềm, lập trình Backend thay vì chỉ chạy theo các công cụ AI bề nổi.

---

### Hình ảnh trong sự kiện:

![FCAJ Community Day Presentation](/images/4-EventParticipated/event1-1.jpg)

![FCAJ Community Day Group Photo](/images/4-EventParticipated/event1-2.jpg)

![FCAJ Community Day Opening Session](/images/4-EventParticipated/event1-3.jpg)

![FCAJ Community Day Keynote](/images/4-EventParticipated/event1-4.jpg)
