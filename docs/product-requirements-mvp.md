# ============================================================
# SKILLRANK - PRODUCT REQUIREMENTS DOCUMENT (MVP)
# Nen tang ket noi sinh vien voi doanh nghiep qua thu thach thuc te
# ============================================================


# ============================================================
# PHAN 1: TONG QUAN SAN PHAM (Product Overview)
# ============================================================

## 1.1. Boi canh thi truong

### Thuc trang tuyen dung tai Viet Nam:
- 70% doanh nghiep cho rang CV khong phan anh dung nang luc thuc te cua ung vien
- Trung binh mot doanh nghiep mat 23 ngay de tuyen 1 vi tri, chi phi tuyen dung len toi 30-50 trieu/vi tri
- 65% sinh vien ra truong khong tim duoc viec lam dung nganh trong 6 thang dau
- 83% nha tuyen dung muon danh gia ung vien qua bai test thuc te thay vi chi phong van

### Gap giua nha truong va doanh nghiep:
- Chuong trinh dao tao thieu thuc hanh, sinh vien thieu kinh nghiem thuc te
- Doanh nghiep phai dao tao lai nhan vien moi tu 3-6 thang
- Khong co nen tang nao giup doanh nghiep "test thu" ung vien truoc khi tuyen

### Co hoi:
- Thi truong EdTech + HRTech Viet Nam du kien dat 3.5 ty USD vao 2027
- Xu huong "skill-based hiring" dang tang manh toan cau (LinkedIn, Google da bo yeu cau bang cap)
- Chua co doi thu truc tiep tai Viet Nam ket hop EdTech + Recruitment qua task thuc te

---

## 1.2. Van de can giai quyet

### Phia doanh nghiep (Pain Points):

| Van de | Hau qua | Muc do nghiem trong |
|--------|---------|---------------------|
| CV khong phan anh thuc te | Tuyen nham nguoi, mat thoi gian dao tao | Cao |
| Phong van ton thoi gian | Mat 2-4 tuan cho 1 vong tuyen dung | Cao |
| Kho tim ung vien co ky nang cu the | Phai dang tuyen nhieu kenh, chi phi cao | Trung binh |
| Khong so sanh duoc ung vien khach quan | Quyet dinh tuyen dung chu quan, thieu data | Trung binh |

### Phia sinh vien (Pain Points):

| Van de | Hau qua | Muc do nghiem trong |
|--------|---------|---------------------|
| Bang cap khong du de xin viec | Bi tu choi vi "thieu kinh nghiem" | Cao |
| Khong biet doanh nghiep can ky nang gi | Hoc sai huong, lang phi thoi gian | Cao |
| It co hoi thuc hanh thuc te | Ky nang ly thuyet, khong ap dung duoc | Trung binh |
| Kho tiep can doanh nghiep tot | Chi biet den cong ty qua quang cao | Trung binh |

---

## 1.3. Giai phap: SkillRank

### Tam nhin (Vision):
> "Moi sinh vien deu co co hoi chung minh nang luc thuc te va duoc doanh nghiep cong nhan, bat ke ho hoc truong nao."

### Su menh (Mission):
Xay dung nen tang ket noi truc tiep sinh vien voi doanh nghiep thong qua cac thu thach (task) thuc te, noi nang luc duoc danh gia bang ket qua, khong phai bang cap.

### Mo hinh hoat dong chi tiet:

```
+------------------+         +------------------+         +------------------+
|   DOANH NGHIEP   |         |     SKILLRANK    |         |    SINH VIEN     |
+------------------+         +------------------+         +------------------+
|                   |         |                  |         |                  |
| 1. Dang ky        |-------->| Xac minh DN      |         |                  |
| 2. Chon goi       |-------->| Kich hoat goi    |         |                  |
| 3. Tao task       |-------->| Hien thi task    |-------->| 4. Duyet task    |
|                   |         |                  |         | 5. Nop bai giai  |
|                   |         | Luu tru bai nop  |<--------|                  |
| 6. Cham diem      |<--------|                  |         |                  |
| 7. Chon ung vien  |-------->| Cap nhat ranking |-------->| 8. Nhan ket qua  |
| 9. Lien he tuyen  |         |                  |         |                  |
+------------------+         +------------------+         +------------------+
```

### Gia tri cot loi:

**Cho doanh nghiep:**
- Tiet kiem 60% thoi gian tuyen dung so voi phuong phap truyen thong
- Danh gia ung vien bang data cu the (diem so, xep hang), khong chu quan
- Chi phi thap hon headhunter (tu $49.99/thang so voi $500-2000/ung vien)
- Tiep can pool sinh vien tai nang tu nhieu truong dai hoc

**Cho sinh vien:**
- Mien phi 100% - khong mat bat ky chi phi nao
- Duoc doanh nghiep danh gia truc tiep bang ky nang thuc te
- Xay dung portfolio tu cac bai giai thuc te
- Co hoi duoc tuyen dung truc tiep tu doanh nghiep

---

## 1.4. Doi tuong su dung chi tiet (User Personas)

### Persona 1: Sinh vien - "Minh" (22 tuoi)
- **Hoc van:** Sinh vien nam 4 nganh CNTT, Dai hoc Bach Khoa Ha Noi
- **Muc tieu:** Tim thuc tap/viec lam tai cong ty cong nghe
- **Van de:** Co kien thuc ly thuyet nhung chua co du an thuc te de show nha tuyen dung
- **Hanh vi:** Thuong xuyen lam side project, tham gia hackathon, muon duoc nhan xet tu chuyen gia
- **Ky vong voi SkillRank:** Lam cac task thuc te tu doanh nghiep, duoc cham diem va co co hoi tuyen dung

### Persona 2: Doanh nghiep - "CEO Startup TechViet" (30 nhan vien)
- **Nganh:** Cong nghe phan mem
- **Muc tieu:** Tuyen 5 developer junior trong 2 thang
- **Van de:** Nhan 200+ CV nhung khong biet ai code duoc thuc su
- **Hanh vi:** Da dung LinkedIn, TopCV nhung chat luong ung vien khong on dinh
- **Ky vong voi SkillRank:** Dang bai test coding, sinh vien nop bai, cham va chon top nguoi gioi nhat

### Persona 3: Admin - "Huong" (Quan tri he thong)
- **Vai tro:** Quan ly toan bo nen tang SkillRank
- **Muc tieu:** Dam bao he thong van hanh on dinh, duyet thanh toan chinh xac
- **Hanh vi:** Kiem tra dashboard hang ngay, xu ly yeu cau nang cap goi, ho tro nguoi dung
- **Ky vong:** Giao dien quan tri de su dung, thong ke truc quan, duyet nhanh

---

## 1.5. USP & Loi the canh tranh

| Tieu chi | SkillRank | TopCV | LinkedIn | Freelancer.vn |
|----------|-----------|-------|----------|---------------|
| Danh gia bang task thuc te | CO | Khong | Khong | 1 phan |
| Leaderboard xep hang | CO | Khong | Khong | Khong |
| Mien phi cho sinh vien | CO | CO | CO | Khong |
| Doanh nghiep tu thiet ke bai test | CO | Khong | Khong | Khong |
| Cham diem & feedback truc tiep | CO | Khong | Khong | 1 phan |
| Loc ung vien theo ky nang thuc te | CO | Theo CV | Theo CV | Theo review |
| Thanh toan QR noi dia | CO | CO | Khong | Khong |

### Competitive Moat (Rao can canh tranh):
1. **Data network effect**: Cang nhieu sinh vien lam task -> cang nhieu data xep hang -> cang hap dan doanh nghiep -> cang nhieu task -> thu hut them sinh vien
2. **Task library**: Kho task thuc te tich luy theo thoi gian, khong doi thu nao co
3. **Skill graph**: Du lieu ky nang thuc te cua sinh vien, chinh xac hon CV tu khai

---

## 1.6. Mo hinh kinh doanh (Business Model)

### Nguon doanh thu:

| Nguon | Mo ta | Gia |
|-------|-------|-----|
| **Goi Standard** | 5 task/thang + Task Leaderboard | $49.99/thang (~1.2 trieu VND) |
| **Goi Premium** | Unlimited + Global Leaderboard + CSV + Advanced Filters | $99.99/thang (~2.4 trieu VND) |
| **Goi Basic** | Mien phi, 2 task/thang (de thu nghiem va chuyen doi) | Mien phi |

### Du phong doanh thu (nam 1):

| Chi so | Gia tri |
|--------|---------|
| Muc tieu doanh nghiep dang ky | 200 DN |
| Ty le chuyen doi Standard | 15% (30 DN x $49.99) |
| Ty le chuyen doi Premium | 5% (10 DN x $99.99) |
| Doanh thu hang thang | ~$2,500/thang |
| Doanh thu nam 1 | ~$30,000/nam (~720 trieu VND) |

### Chi phi van hanh:
| Hang muc | Chi phi/thang |
|----------|---------------|
| VPS Server | $20-50 |
| Ten mien + SSL | $10 |
| Marketing | $100-200 |
| **Tong** | **~$200/thang** |

**=> Loi nhuan rong du kien: ~$2,300/thang tu thang 6 tro di**


# ============================================================
# PHAN 2: YEU CAU CHUC NANG CHI TIET (Functional Requirements)
# ============================================================

## 2.1. He thong xac thuc & phan quyen

### 2.1.1. Dang ky Sinh vien

**URL:** /register-student

| Truong | Kieu | Bat buoc | Validation |
|--------|------|----------|------------|
| Ho va ten | Text | Co | Khong duoc de trong |
| Email | Email | Co | Dinh dang email, unique trong DB |
| Mat khau | Password | Co | Toi thieu 6 ky tu |
| So dien thoai | Text | Co | Khong duoc de trong |
| Truong dai hoc | Text | Co | Khong duoc de trong |
| Chuyen nganh | Text | Co | Khong duoc de trong |
| Nam hoc | Number | Khong | 1-6 |
| Ky nang | Text | Khong | Phan cach boi dau phay |
| Link portfolio | URL | Khong | Dinh dang URL |
| LinkedIn | URL | Khong | Dinh dang URL |
| CV | File | Co | PDF, toi da 20MB |

**Luong xu ly:**
1. Nguoi dung nhap thong tin va upload CV
2. He thong kiem tra email da ton tai chua (real-time, goi API /check-email)
3. Validate tat ca truong bat buoc
4. Hash password bang Bcrypt (salt rounds)
5. Luu file CV vao /uploads/cv/ voi ten [timestamp]-[ten_goc]
6. Tao record trong bang students
7. Tao JWT token (7 ngay), tra ve token + user info
8. Frontend luu token vao localStorage, redirect den dashboard

### 2.1.2. Dang ky Doanh nghiep

**URL:** /register-company

| Truong | Kieu | Bat buoc | Validation |
|--------|------|----------|------------|
| Ten cong ty | Text | Co | Khong duoc de trong |
| Ma so dang ky kinh doanh | Text | Co | Unique trong DB |
| Email | Email | Co | Dinh dang email, unique trong DB |
| Mat khau | Password | Co | Toi thieu 6 ky tu |
| Nganh nghe | Dropdown | Co | 6 lua chon: Technology, Finance, Marketing, Healthcare, Education, E-commerce |
| Quy mo | Dropdown | Khong | 1-10, 11-50, 51-200, 200+ |
| Website | URL | Khong | Dinh dang URL |
| Dia chi | Text | Khong | - |
| Mo ta cong ty | Textarea | Khong | - |
| Giay phep kinh doanh | File | Khong | PDF/JPG/PNG |
| Logo cong ty | File | Khong | Image (JPG/PNG) |

**Sau dang ky:**
- Tu dong gan goi Basic (mien phi, 2 task/thang)
- task_limit = 2, tasks_used = 0
- subscription_plan = 'basic'

### 2.1.3. Dang nhap

**URL:** /login

**Luong:**
1. Chon tab: Student hoac Company
2. Nhap email + password
3. API POST /api/auth/login voi body: { email, password, role }
4. Backend kiem tra email trong bang tuong ung (students hoac companies)
5. So sanh password hash bang bcrypt.checkpw()
6. Tao JWT token chua: { id, role, email, exp }
7. Tra ve: { token, user: { id, name, email, role } }
8. Frontend luu token + user vao localStorage
9. Redirect: student -> /student/dashboard, company -> /company/dashboard

### 2.1.4. Dang nhap Admin

**URL:** /admin-huong/login

**Luong:**
1. Nhap username + password
2. API POST /api/admin/login
3. Kiem tra trong bang admins
4. Tra ve JWT token voi role = 'admin'
5. Luu vao localStorage rieng (admin_token, admin_user)
6. Redirect den /admin-huong/

**Tai khoan mac dinh:** admin / admin123

### 2.1.5. Phan quyen chi tiet

```
+------------------+-----------------------------------+
|     Role         |     Quyen truy cap                |
+------------------+-----------------------------------+
| Chua dang nhap   | Trang chu, Pricing, Browse Tasks  |
|                  | Dang ky, Dang nhap                |
+------------------+-----------------------------------+
| Student          | Dashboard, Browse Tasks           |
|                  | Task Detail, Submit Work          |
|                  | My Submissions, Profile           |
|                  | Thong bao danh gia                |
+------------------+-----------------------------------+
| Company (Basic)  | Dashboard, Create Task (2/thang)  |
|                  | Applicants, Evaluate              |
|                  | Subscription, Profile             |
+------------------+-----------------------------------+
| Company (Std)    | Tat ca Basic +                    |
|                  | Task Leaderboard (5 task/thang)   |
+------------------+-----------------------------------+
| Company (Premium)| Tat ca Standard +                 |
|                  | Global Leaderboard                |
|                  | Advanced Filters                  |
|                  | CSV Export (unlimited task)        |
+------------------+-----------------------------------+
| Admin            | Dashboard tong quan               |
|                  | CRUD Companies, Students          |
|                  | Duyet/Tu choi Upgrade Requests    |
+------------------+-----------------------------------+
```

---

## 2.2. Chuc nang Sinh vien (7 man hinh)

### 2.2.1. Student Dashboard (/student/dashboard)

**Layout:**
- Header: Loi chao "Welcome back, [ten]!"
- 3 stat cards hien thi nhanh
- Danh sach 5 bai nop gan nhat
- He thong thong bao

**Thong ke hien thi:**
| Stat | Mo ta | Cach tinh |
|------|-------|-----------|
| Total Submissions | Tong so bai da nop | COUNT tu submissions WHERE student_id = ? |
| Pending | So bai dang cho danh gia | COUNT WHERE status = 'pending' |
| Accepted | So bai duoc chap nhan | COUNT WHERE status = 'interested' |

**He thong thong bao:**
- Khi doanh nghiep danh gia bai nop, sinh vien nhan thong bao
- Hien thi modal voi: icon trang thai, ten cong ty, ten task, diem, feedback
- Mau sac theo trang thai:
  - Xanh la (interested): "Chuc mung! [Company] da chap nhan bai cua ban"
  - Xanh duong (reviewed): "[Company] da danh gia bai cua ban"
  - Do (rejected): "[Company] da tu choi bai cua ban"
- Luu thoi gian kiem tra cuoi cung vao localStorage

### 2.2.2. Duyet Task (/browse-tasks)

**Tinh nang tim kiem & loc:**
| Bo loc | Kieu | Gia tri |
|--------|------|---------|
| Search | Text input | Tim trong title va description |
| Industry | Dropdown | Technology, Finance, Marketing, Healthcare, Education, E-commerce |
| Difficulty | Dropdown | Easy, Medium, Hard |

**Hien thi:**
- Grid layout 3 cot (responsive 1-2 cot tren mobile)
- 12 task/trang voi phan trang
- Moi card hien thi:
  - Logo cong ty (hoac initial letter)
  - Tieu de task
  - Mo ta (cat ngan 100 ky tu)
  - Badge do kho (xanh la/vang/do)
  - Thoi gian uoc tinh
  - Deadline
  - So luong da nop / gioi han

### 2.2.3. Chi tiet Task (/student/task-detail?id=X)

**Thong tin hien thi:**
- **Header:** Tieu de task + badge trang thai + badge do kho
- **Cong ty:** Logo, ten, link website
- **3 cot thong ke:** Deadline | So bai nop (X/max) | Do kho
- **Noi dung:** Mo ta chi tiet + Ket qua mong doi
- **Nut hanh dong:** "Submit Your Work" (an neu da qua deadline hoac da nop)

### 2.2.4. Nop bai (/student/submit-work?taskId=X)

**Form nop bai:**
| Truong | Kieu | Mo ta |
|--------|------|-------|
| File | Upload | PDF/ZIP, toi da 20MB |
| Text Answer | Textarea | Tra loi bang van ban (tuy chon) |
| Portfolio Link | URL | Link den project (tuy chon) |
| Confirmation | Checkbox | "Toi xac nhan day la bai lam cua toi" |

**Kiem tra truoc khi nop:**
1. Sinh vien da dang nhap chua
2. Task con active khong
3. Chua qua deadline
4. Chua dat gioi han max_submissions
5. Sinh vien chua nop bai cho task nay (unique constraint)

**Sau khi nop thanh cong:**
- Tang current_submissions cua task len 1
- Tang total_submissions cua student len 1
- Hien thi man hinh thanh cong voi animation
- Tu dong redirect ve My Submissions sau 2 giay

### 2.2.5. Bai nop cua toi (/student/my-submissions)

**Bang hien thi:**
| Cot | Mo ta |
|-----|-------|
| Task Name | Ten task (link den chi tiet) |
| Company | Ten cong ty |
| Date | Ngay nop |
| Status | Badge: Pending (vang) / Reviewed (xanh) / Accepted (xanh la) / Rejected (do) |
| Score | Thanh diem (0-100) hoac "-" neu chua cham |
| Feedback | Nhan xet cua doanh nghiep |

### 2.2.6. Ho so ca nhan (/student/profile)

**Che do xem:**
- Avatar (chu cai dau ten), ten, email
- Truong, chuyen nganh, nam hoc
- Ky nang (hien thi dang tag)
- SDT, portfolio, LinkedIn
- Link tai CV
- Thong ke: Tong bai nop | Diem trung binh | Tong diem | So lan duoc chap nhan

**Che do sua:**
- Tat ca truong deu co the sua tru email
- Upload CV moi (thay the cu)
- Validate va luu

### 2.2.7. Thong bao danh gia

**Co che hoat dong:**
1. Khi vao dashboard, goi API GET /api/submissions/mine
2. Loc cac bai co evaluated_at > last_notification_check (luu trong localStorage)
3. Neu co bai moi duoc danh gia -> hien modal thong bao
4. Cap nhat last_notification_check = now()

---

## 2.3. Chuc nang Doanh nghiep (8 man hinh)

### 2.3.1. Company Dashboard (/company/dashboard)

**Layout:**
- Header: "Welcome back, [ten cong ty]!" + nut "Create Task"
- 4 stat cards
- Danh sach Recent Tasks

**Thong ke:**
| Stat | Cach tinh |
|------|-----------|
| Total Tasks | COUNT tasks WHERE company_id = ? |
| Total Submissions | COUNT submissions cua cac task cua company |
| Accepted Candidates | COUNT submissions WHERE status = 'interested' |
| Task Usage | tasks_used / task_limit (hien thi theo goi) |

### 2.3.2. Tao Task (/company/create-task)

**Form:**
| Truong | Kieu | Bat buoc | Validation |
|--------|------|----------|------------|
| Title | Text | Co | Max 200 ky tu |
| Description | Textarea | Co | Mo ta chi tiet nhiem vu |
| Expected Output | Textarea | Khong | Ket qua mong doi |
| Estimated Time | Text | Khong | VD: "2-3 gio", "1 tuan" |
| Deadline | Date | Co | Phai > ngay hien tai |
| Difficulty | Select | Co | Easy / Medium / Hard |
| Industry | Select | Khong | 6 nganh nghe |
| Max Submissions | Number | Co | Mac dinh 50 |

**Kiem tra truoc khi tao:**
- tasks_used < task_limit (theo goi dang ki)
- Neu vuot gioi han -> thong bao "Ban da het luot tao task thang nay. Nang cap goi de tao them."

**Sau khi tao:**
- Tang tasks_used len 1
- Task co status = 'active' mac dinh
- Hien thi tren trang Browse Tasks cho sinh vien

### 2.3.3. Quan ly Ung vien (/company/applicants)

**Tinh nang:**
- Dropdown chon task (tu dong chon tu URL param ?taskId=X)
- Bang hien thi tat ca bai nop cua task:

| Cot | Mo ta |
|-----|-------|
| Student Name | Ten sinh vien |
| Email | Email lien he |
| University | Truong dai hoc |
| Skills | Danh sach ky nang |
| Portfolio | Link (clickable) |
| CV | Link download |
| Date | Ngay nop |
| Status | Badge trang thai |
| Score | Diem hien tai |
| Actions | Nut "Evaluate" |

### 2.3.4. Danh gia bai nop (/company/evaluate?id=X)

**Giao dien:**
- **Panel trai:** Thong tin sinh vien (ten, email, truong, SDT, ky nang, CV, portfolio)
- **Panel phai:** Bai nop (file download, text answer, portfolio link)
- **Form danh gia:**

| Truong | Kieu | Mo ta |
|--------|------|-------|
| Score | Number (0-100) | Diem danh gia |
| Status | Select | Reviewed / Interested (Accepted) / Rejected |
| Feedback | Textarea | Nhan xet chi tiet |

**Logic sau khi danh gia:**
1. Cap nhat submission: score, feedback, status, evaluated_at = NOW()
2. Tinh lai diem sinh vien:
   - total_score += score (moi)
   - Tinh lai average_score = tong diem / so bai da cham
3. Neu status = 'interested': tang interested_count cua student len 1
4. Sinh vien se nhan thong bao o lan vao dashboard tiep theo

### 2.3.5. Task Leaderboard (/company/task-ranking)

**Yeu cau:** Goi Standard tro len

**Tinh nang:**
- Dropdown chon task
- Sap xep theo: Diem cao nhat | Nop som nhat | Nhieu task nhat
- Bang xep hang:

| Cot | Mo ta |
|-----|-------|
| Rank | Thu hang (1, 2, 3...) |
| Student | Ten sinh vien |
| University | Truong dai hoc |
| Score | Diem so |
| Status | Trang thai danh gia |

### 2.3.6. Global Leaderboard (/company/global-leaderboard)

**Yeu cau:** Goi Premium

**Bo loc nang cao:**
| Bo loc | Kieu | Mo ta |
|--------|------|-------|
| University | Text | Loc theo truong |
| Skill | Text | Loc theo ky nang |
| Year of Study | Dropdown | Nam 1-5 |
| Min Score | Number | Diem toi thieu |
| Max Score | Number | Diem toi da |

**Bang xep hang:**
| Cot | Mo ta |
|-----|-------|
| Rank | Thu hang toan he thong |
| Name | Ten sinh vien |
| University | Truong |
| Avg Score | Diem trung binh |
| Tasks Completed | So task da lam |
| Accepted Count | So lan duoc chap nhan |

**Xuat CSV:** Download file Excel chua toan bo thong tin sinh vien (ten, email, truong, chuyen nganh, ky nang, diem, SDT, portfolio, LinkedIn)

### 2.3.7. Quan ly Subscription (/company/subscription)

**Hien thi goi hien tai:**
- Ten goi (Basic/Standard/Premium)
- Task usage: X / Y (thanh progress bar)
- Ngay het han (neu co)

**3 the goi:**
| Goi | Gia | Tinh nang chinh | Nut |
|-----|-----|-----------------|-----|
| Basic | Free | 2 task/thang, xem bai nop, cham diem | "Current Plan" (disabled) |
| Standard | $49.99/mo | 5 task/thang + Task Leaderboard | "Upgrade" |
| Premium | $99.99/mo | Unlimited + Global Leaderboard + CSV | "Upgrade" |

**Luong thanh toan:**
1. Bam "Upgrade" -> Mo modal QR Code
2. Modal hien thi: Ten goi, gia, anh QR chuyen khoan
3. Nguoi dung quet QR va chuyen khoan
4. Bam "Xac nhan da thanh toan"
5. He thong tao upgrade_request (status = 'pending')
6. Hien thi thong bao: "Yeu cau da gui. Vui long cho admin duyet."
7. **Doanh nghiep KHONG duoc tu nang cap** - phai cho admin xac nhan

### 2.3.8. Ho so Cong ty (/company/profile)

- Xem/sua: Ten cong ty, email, nganh nghe, quy mo, website, dia chi, mo ta
- Upload logo moi
- Hien thi goi hien tai va task usage

---

## 2.4. Chuc nang Admin (4 tab trong 1 trang)

### 2.4.1. Admin Dashboard (Tab mac dinh)

**6 stat cards:**
| Stat | Icon | Mau | Cach tinh |
|------|------|-----|-----------|
| Total Students | User icon | Xanh duong | COUNT students |
| Total Companies | Building icon | Xanh la | COUNT companies |
| Total Tasks | Clipboard icon | Tim | COUNT tasks |
| Total Submissions | Upload icon | Cam | COUNT submissions |
| Pending Requests | Clock icon | Vang | COUNT upgrade_requests WHERE status='pending' |
| Monthly Revenue | Dollar icon | Xanh ngoc | SUM(Standard*49.99 + Premium*99.99) WHERE expiry >= today |

**Bieu do phan bo goi:**
- Thanh ngang (bar chart CSS) hien thi so cong ty theo tung goi
- VD: Basic: 150 (75%) | Standard: 30 (15%) | Premium: 10 (5%)

**Hoat dong gan day:**
- 2 cot: Recent Companies (5 moi nhat) | Recent Students (5 moi nhat)
- Hien thi: ten, email, ngay tao, goi (cho company)

### 2.4.2. Quan ly Doanh nghiep (Tab Companies)

**Tinh nang:**
- Thanh tim kiem theo ten hoac email
- Phan trang (15 dong/trang)
- Bang:

| Cot | Mo ta |
|-----|-------|
| ID | Ma dinh danh |
| Company | Ten cong ty |
| Email | Email dang ky |
| Industry | Nganh nghe |
| Plan | Badge goi (xanh la/xanh duong/tim) |
| Tasks | tasks_used / task_limit |
| Created | Ngay dang ky |
| Actions | Nut "Delete" (do) |

**Xoa doanh nghiep:**
- Hien modal xac nhan: "Ban co chac muon xoa [ten]? Hanh dong nay khong the hoan tac."
- Xoa company -> CASCADE xoa tasks + submissions lien quan

### 2.4.3. Quan ly Sinh vien (Tab Students)

**Tuong tu tab Companies:**
- Tim kiem theo ten/email
- Phan trang 15 dong/trang

| Cot | Mo ta |
|-----|-------|
| ID | Ma dinh danh |
| Name | Ho ten |
| Email | Email |
| University | Truong |
| Avg Score | Diem trung binh |
| Submissions | Tong so bai nop |
| Created | Ngay dang ky |
| Actions | Nut "Delete" |

### 2.4.4. Duyet thanh toan (Tab Payment Requests)

**Bo loc trang thai:**
- 4 nut: All | Pending | Approved | Rejected
- Nut dang chon duoc highlight xanh

**Bang:**
| Cot | Mo ta |
|-----|-------|
| ID | Ma yeu cau |
| Company | Ten cong ty |
| Email | Email cong ty |
| Current Plan | Goi hien tai (badge) |
| Requested Plan | Goi muon nang cap (badge) |
| Status | Trang thai (badge vang/xanh/do) |
| Date | Ngay gui yeu cau |
| Actions | Nut Approve (xanh) + Reject (do) hoac ngay xu ly |

**Luong duyet:**
1. Admin bam "Approve" hoac "Reject"
2. Mo modal xac nhan voi truong ghi chu (tuy chon)
3. Neu Approve:
   - Cap nhat upgrade_request: status='approved', processed_at=NOW()
   - Cap nhat company: subscription_plan, task_limit, subscription_expiry = +30 ngay
4. Neu Reject:
   - Cap nhat upgrade_request: status='rejected', admin_note, processed_at=NOW()
   - Cong ty KHONG duoc nang cap

**Badge pending hien thi tren sidebar:**
- So luong yeu cau dang cho hien thi tren icon Payment Requests
- Tu dong cap nhat khi load dashboard

---

## 2.5. He thong Subscription chi tiet

### 2.5.1. Bang so sanh goi

| Tinh nang | Basic (Free) | Standard ($49.99) | Premium ($99.99) |
|-----------|-------------|-------------------|------------------|
| Task/thang | 2 | 5 | Khong gioi han (999) |
| Xem bai nop | Co | Co | Co |
| Cham diem & feedback | Co | Co | Co |
| Task Leaderboard | Khong | Co | Co |
| Global Leaderboard | Khong | Khong | Co |
| Loc nang cao | Khong | Khong | Co |
| Xuat CSV | Khong | Khong | Co |
| Gia | $0 | $49.99/thang | $99.99/thang |

### 2.5.2. Quy trinh nang cap day du

```
BUOC 1: Doanh nghiep vao /company/subscription
    |
BUOC 2: Bam "Upgrade" tren goi mong muon
    |
BUOC 3: Modal QR hien thi -> Quet QR -> Chuyen khoan
    |
BUOC 4: Bam "Xac nhan da thanh toan"
    |
BUOC 5: API PUT /api/subscription/upgrade
    |-- Kiem tra: goi moi != goi hien tai
    |-- Kiem tra: khong co request pending trung
    |-- Tao record upgrade_requests (status='pending')
    |-- Tra ve: "Yeu cau da gui, cho admin duyet"
    |
BUOC 6: Admin vao /admin-huong -> Tab Payment Requests
    |
BUOC 7: Admin bam "Approve"
    |-- Cap nhat upgrade_request status = 'approved'
    |-- Cap nhat company:
    |   - subscription_plan = goi moi
    |   - task_limit = limit cua goi moi
    |   - subscription_expiry = NOW() + 30 ngay
    |
BUOC 8: Doanh nghiep reload trang -> thay goi moi da active
```

### 2.5.3. Rang buoc quan trong
- Doanh nghiep **BAT BUOC** phai qua admin de nang cap
- Khong the tu nang cap bang cach goi API truc tiep (backend da block)
- Moi yeu cau pending chi duoc xu ly 1 lan (khong duyet lai)
- Khong co yeu cau pending trung (cung goi) cho 1 cong ty


# ============================================================
# PHAN 3: YEU CAU KY THUAT & KIEN TRUC (Technical Architecture)
# ============================================================

## 3.1. Kien truc he thong

```
+-------------------------------------------------------------------+
|                        INTERNET                                    |
+-------------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------------+
|                    APACHE WEB SERVER (:80)                         |
|                                                                    |
|   +---------------------------+  +-----------------------------+  |
|   |   Static Files            |  |   Reverse Proxy             |  |
|   |   /FE/* -> htdocs/        |  |   /api/* -> localhost:5000  |  |
|   |   HTML, CSS, JS, Images   |  |   /uploads/* -> :5000       |  |
|   +---------------------------+  +-----------------------------+  |
+-------------------------------------------------------------------+
                                              |
                                              v
+-------------------------------------------------------------------+
|                    FLASK BACKEND (:5000)                            |
|                                                                    |
|   +-------------+  +---------------+  +------------------------+  |
|   | Routes      |  | Controllers   |  | Middleware              |  |
|   | 9 Blueprints|  | Business Logic|  | auth.py (JWT validate)  |  |
|   | 37 endpoints|  | DB queries    |  | role.py (RBAC + Plan)   |  |
|   +-------------+  +---------------+  +------------------------+  |
|                              |                                     |
+-------------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------------+
|                    MYSQL DATABASE (skillrank)                       |
|                                                                    |
|   +----------+ +----------+ +-------+ +-----------+ +----------+ |
|   | students | | companies| | tasks | |submissions| | admins   | |
|   +----------+ +----------+ +-------+ +-----------+ +----------+ |
|   +-------------------+ +------------------+                      |
|   | subscription_plans| | upgrade_requests |                      |
|   +-------------------+ +------------------+                      |
+-------------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------------+
|                    FILE STORAGE (Local)                             |
|   /uploads/cv/          - CV sinh vien (PDF)                       |
|   /uploads/submissions/ - Bai nop (PDF/ZIP)                        |
|   /uploads/licenses/    - Giay phep kinh doanh                     |
|   /uploads/logos/        - Logo cong ty                             |
+-------------------------------------------------------------------+
```

## 3.2. Cong nghe su dung chi tiet

| Tang | Cong nghe | Phien ban | Ly do chon |
|------|-----------|-----------|------------|
| **Frontend** | HTML5 + Vanilla JS | - | Don gian, khong can build, load nhanh |
| **CSS Framework** | Tailwind CSS (CDN) | 3.x | Utility-first, responsive san, khong can file CSS lon |
| **Font** | Google Fonts (Inter) | - | Font hien dai, de doc |
| **Backend** | Python Flask | 2.2.5 | Lightweight, de hoc, phu hop MVP |
| **CORS** | Flask-CORS | 4.0.0 | Xu ly cross-origin requests |
| **Database Driver** | PyMySQL | 1.1.0 | Pure Python MySQL client |
| **Auth** | PyJWT | 2.8.0 | JSON Web Token |
| **Password** | Bcrypt | 4.1.2 | Hash password an toan |
| **Config** | python-dotenv | 1.0.0 | Quan ly bien moi truong |
| **Web Server** | Apache (XAMPP) | 2.4.58 | Pho bien, ho tro mod_proxy |
| **Database** | MySQL/MariaDB | 10.4.32 | Quan he, ACID, pho bien |

## 3.3. Co so du lieu chi tiet

### 3.3.1. Bang students (Sinh vien)

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma sinh vien |
| full_name | VARCHAR(100) | NOT NULL | Ho va ten |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Email dang ky |
| password | VARCHAR(255) | NOT NULL | Mat khau (bcrypt hash) |
| university | VARCHAR(150) | - | Truong dai hoc |
| major | VARCHAR(100) | - | Chuyen nganh |
| year_of_study | INT | - | Nam hoc (1-6) |
| skills | TEXT | - | Danh sach ky nang |
| phone | VARCHAR(20) | - | So dien thoai |
| cv_path | VARCHAR(255) | - | Duong dan file CV |
| portfolio_link | VARCHAR(255) | - | Link portfolio |
| linkedin | VARCHAR(255) | - | Link LinkedIn |
| avatar_path | VARCHAR(255) | - | Duong dan avatar |
| total_score | DECIMAL(10,2) | DEFAULT 0 | Tong diem |
| average_score | DECIMAL(5,2) | DEFAULT 0 | Diem trung binh |
| total_submissions | INT | DEFAULT 0 | Tong bai nop |
| interested_count | INT | DEFAULT 0 | So lan duoc chap nhan |
| created_at | TIMESTAMP | DEFAULT NOW() | Ngay tao |

### 3.3.2. Bang companies (Doanh nghiep)

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma cong ty |
| company_name | VARCHAR(150) | NOT NULL | Ten cong ty |
| registration_number | VARCHAR(50) | UNIQUE | Ma dang ky kinh doanh |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Email |
| password | VARCHAR(255) | NOT NULL | Mat khau (bcrypt hash) |
| industry | VARCHAR(100) | - | Nganh nghe |
| company_size | VARCHAR(50) | - | Quy mo |
| website | VARCHAR(255) | - | Website |
| address | TEXT | - | Dia chi |
| description | TEXT | - | Mo ta |
| business_license_path | VARCHAR(255) | - | Duong dan giay phep |
| logo_path | VARCHAR(255) | - | Duong dan logo |
| subscription_plan | ENUM('basic','standard','premium') | DEFAULT 'basic' | Goi hien tai |
| task_limit | INT | DEFAULT 2 | Gioi han task/thang |
| tasks_used | INT | DEFAULT 0 | So task da dung |
| subscription_expiry | DATE | - | Ngay het han goi |
| created_at | TIMESTAMP | DEFAULT NOW() | Ngay tao |

### 3.3.3. Bang tasks (Thu thach)

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma task |
| company_id | INT | FK -> companies(id) CASCADE | Cong ty tao |
| title | VARCHAR(200) | NOT NULL | Tieu de |
| description | TEXT | - | Mo ta chi tiet |
| expected_output | TEXT | - | Ket qua mong doi |
| estimated_time | VARCHAR(50) | - | Thoi gian uoc tinh |
| deadline | DATE | - | Han nop |
| difficulty | ENUM('easy','medium','hard') | DEFAULT 'medium' | Do kho |
| industry | VARCHAR(100) | - | Nganh nghe |
| max_submissions | INT | DEFAULT 50 | Gioi han bai nop |
| current_submissions | INT | DEFAULT 0 | So bai da nop |
| status | ENUM('active','closed','draft') | DEFAULT 'active' | Trang thai |
| created_at | TIMESTAMP | DEFAULT NOW() | Ngay tao |

### 3.3.4. Bang submissions (Bai nop)

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma bai nop |
| task_id | INT | FK -> tasks(id) CASCADE | Task tuong ung |
| student_id | INT | FK -> students(id) CASCADE | Sinh vien nop |
| file_path | VARCHAR(255) | - | Duong dan file |
| text_answer | TEXT | - | Tra loi text |
| portfolio_link | VARCHAR(255) | - | Link portfolio |
| score | DECIMAL(5,2) | DEFAULT NULL | Diem (0-100) |
| feedback | TEXT | - | Nhan xet |
| status | ENUM('pending','reviewed','interested','rejected') | DEFAULT 'pending' | Trang thai |
| submitted_at | TIMESTAMP | DEFAULT NOW() | Ngay nop |
| evaluated_at | TIMESTAMP | NULL | Ngay danh gia |
| | | UNIQUE(task_id, student_id) | Chong nop trung |

### 3.3.5. Bang admins

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma admin |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Ten dang nhap |
| password | VARCHAR(255) | NOT NULL | Mat khau (bcrypt) |
| full_name | VARCHAR(100) | - | Ho ten |
| created_at | TIMESTAMP | DEFAULT NOW() | Ngay tao |

### 3.3.6. Bang subscription_plans

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma goi |
| plan_name | ENUM('basic','standard','premium') | UNIQUE | Ten goi |
| task_limit | INT | - | Gioi han task |
| has_task_leaderboard | BOOLEAN | DEFAULT FALSE | Co task leaderboard |
| has_global_leaderboard | BOOLEAN | DEFAULT FALSE | Co global leaderboard |
| has_advanced_filters | BOOLEAN | DEFAULT FALSE | Co loc nang cao |
| has_csv_export | BOOLEAN | DEFAULT FALSE | Co xuat CSV |
| price | DECIMAL(10,2) | - | Gia |
| description | TEXT | - | Mo ta |

### 3.3.7. Bang upgrade_requests

| Cot | Kieu | Rang buoc | Mo ta |
|-----|------|-----------|-------|
| id | INT | PK, AUTO_INCREMENT | Ma yeu cau |
| company_id | INT | FK -> companies(id) CASCADE | Cong ty yeu cau |
| current_plan | ENUM | NOT NULL | Goi hien tai |
| requested_plan | ENUM | NOT NULL | Goi muon nang cap |
| status | ENUM('pending','approved','rejected') | DEFAULT 'pending' | Trang thai |
| admin_note | TEXT | - | Ghi chu cua admin |
| created_at | TIMESTAMP | DEFAULT NOW() | Ngay gui |
| processed_at | TIMESTAMP | NULL | Ngay xu ly |

### 3.3.8. So do quan he (ERD)

```
students ----< submissions >---- tasks ----| companies
                                             |
                               upgrade_requests
                                             |
                               subscription_plans

admins (doc lap)

Quan he:
- companies 1-N tasks (ON DELETE CASCADE)
- tasks 1-N submissions (ON DELETE CASCADE)
- students 1-N submissions (ON DELETE CASCADE)
- companies 1-N upgrade_requests (ON DELETE CASCADE)
- submissions: UNIQUE(task_id, student_id) - moi SV chi nop 1 lan/task
```

---

## 3.4. API Endpoints chi tiet (37 endpoints)

### 3.4.1. Authentication (/api/auth) - 5 endpoints

| Method | Path | Auth | Mo ta | Request | Response |
|--------|------|------|-------|---------|----------|
| POST | /register/student | No | Dang ky SV | FormData (multipart) | { token, user } |
| POST | /register/company | No | Dang ky DN | FormData (multipart) | { token, user } |
| POST | /login | No | Dang nhap | { email, password, role } | { token, user } |
| GET | /me | Yes | Lay thong tin user | Bearer token | { user object } |
| GET | /check-email | No | Kiem tra email | ?email=&role= | { available: bool } |

### 3.4.2. Tasks (/api/tasks) - 5 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| GET | / | Optional | All | Duyet task (search, filter, pagination) |
| GET | /company/mine | Yes | Company | Lay task cua cong ty |
| GET | /:id | Optional | All | Chi tiet 1 task |
| POST | / | Yes | Company | Tao task moi |
| DELETE | /:id | Yes | Company (owner) | Xoa task |

### 3.4.3. Submissions (/api/submissions) - 5 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| POST | /:task_id | Yes | Student | Nop bai (file + text + link) |
| GET | /mine | Yes | Student | Lay tat ca bai nop cua SV |
| GET | /company/all | Yes | Company | Lay bai nop cho tat ca task |
| GET | /task/:task_id | Yes | Company | Lay bai nop theo task |
| GET | /:id | Yes | Company/Student | Chi tiet 1 bai nop |

### 3.4.4. Evaluation (/api/evaluation) - 1 endpoint

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| PUT | /:submission_id | Yes | Company | Cham diem (score, feedback, status) |

### 3.4.5. Student (/api/student) - 3 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| GET | /profile | Yes | Student | Lay profile |
| PUT | /profile | Yes | Student | Cap nhat profile |
| GET | /dashboard | Yes | Student | Lay thong ke dashboard |

### 3.4.6. Company (/api/company) - 3 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| GET | /profile | Yes | Company | Lay profile |
| PUT | /profile | Yes | Company | Cap nhat profile |
| GET | /dashboard | Yes | Company | Lay thong ke dashboard |

### 3.4.7. Subscription (/api/subscription) - 3 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| GET | /plans | No | All | Lay danh sach goi |
| GET | /current | Yes | Company | Lay goi hien tai |
| PUT | /upgrade | Yes | Company | Gui yeu cau nang cap (tao pending request) |

### 3.4.8. Leaderboard (/api/leaderboard) - 3 endpoints

| Method | Path | Auth | Role + Plan | Mo ta |
|--------|------|------|-------------|-------|
| GET | /task/:task_id | Yes | Company (Standard+) | Xep hang theo task |
| GET | /global | Yes | Company (Premium) | Xep hang toan he thong |
| GET | /export-csv | Yes | Company (Premium) | Xuat CSV |

### 3.4.9. Admin (/api/admin) - 9 endpoints

| Method | Path | Auth | Role | Mo ta |
|--------|------|------|------|-------|
| POST | /login | No | - | Dang nhap admin |
| POST | /create | No | - | Tao tai khoan admin |
| GET | /dashboard | Yes | Admin | Thong ke tong quan |
| GET | /companies | Yes | Admin | Danh sach DN (search, pagination) |
| GET | /students | Yes | Admin | Danh sach SV (search, pagination) |
| DELETE | /companies/:id | Yes | Admin | Xoa DN |
| DELETE | /students/:id | Yes | Admin | Xoa SV |
| GET | /upgrade-requests | Yes | Admin | Danh sach yeu cau nang cap |
| PUT | /upgrade-requests/:id | Yes | Admin | Duyet/Tu choi yeu cau |

---

## 3.5. Bao mat chi tiet

### 3.5.1. Xac thuc (Authentication)
- **Mat khau:** Hash bang bcrypt voi salt tu dong, khong luu plaintext
- **JWT Token:** Thoi han 7 ngay, ky bang HS256, secret key luu trong .env
- **Token payload:** { id, role, email, exp } - khong chua mat khau hay thong tin nhay cam
- **Auto-redirect:** Khi token het han (401), tu dong xoa token va redirect ve /login

### 3.5.2. Phan quyen (Authorization)
- **Middleware authenticate_token:** Kiem tra Bearer token truoc moi request can auth
- **Middleware require_role:** Kiem tra role (student/company/admin)
- **Middleware require_plan:** Kiem tra goi dich vu theo hierarchy (basic < standard < premium)
- **Owner verification:** Company chi danh gia duoc submissions cua task minh tao

### 3.5.3. Bao ve du lieu
- **CORS:** Chi cho phep request tu domain duoc khai bao (localhost, IP VPS)
- **UNIQUE constraint:** email, registration_number khong trung
- **SQL injection:** Su dung parameterized queries (%s placeholder), khong noi chuoi SQL
- **File upload:** Gioi han 20MB, dat ten bang timestamp tranh trung
- **Cascade delete:** Xoa company -> tu dong xoa tasks + submissions lien quan

---

## 3.6. Cau truc thu muc du an

```
Huong/
├── BE-Python/                    # Backend Flask
│   ├── app.py                    # Entry point, CORS, blueprints
│   ├── requirements.txt          # Dependencies
│   ├── .env                      # Bien moi truong (DB, JWT secret)
│   ├── controllers/              # Business logic
│   │   ├── auth_controller.py    # Dang ky, dang nhap
│   │   ├── task_controller.py    # CRUD tasks
│   │   ├── submission_controller.py # Nop bai, xem bai
│   │   ├── evaluation_controller.py # Cham diem
│   │   ├── student_controller.py    # Profile, dashboard SV
│   │   ├── company_controller.py    # Profile, dashboard DN
│   │   ├── subscription_controller.py # Goi dich vu
│   │   ├── leaderboard_controller.py  # Xep hang
│   │   └── admin_controller.py       # Quan tri admin
│   ├── routes/                   # URL routing (9 blueprints)
│   │   ├── auth_routes.py
│   │   ├── task_routes.py
│   │   ├── submission_routes.py
│   │   ├── evaluation_routes.py
│   │   ├── student_routes.py
│   │   ├── company_routes.py
│   │   ├── subscription_routes.py
│   │   ├── leaderboard_routes.py
│   │   └── admin_routes.py
│   ├── middleware/                # Middleware
│   │   ├── auth.py               # JWT validation
│   │   └── role.py               # RBAC + Plan check
│   ├── database/
│   │   └── db.py                 # MySQL connection (query, execute)
│   └── uploads/                  # File storage
│       ├── cv/
│       ├── submissions/
│       ├── licenses/
│       └── logos/
│
├── FE/                           # Frontend (Static HTML)
│   ├── index.html                # Trang chu
│   ├── login.html                # Dang nhap
│   ├── register-student.html     # Dang ky SV
│   ├── register-company.html     # Dang ky DN
│   ├── browse-tasks.html         # Duyet task
│   ├── pricing.html              # Bang gia
│   ├── student/                  # Trang sinh vien
│   │   ├── dashboard.html
│   │   ├── task-detail.html
│   │   ├── submit-work.html
│   │   ├── my-submissions.html
│   │   └── profile.html
│   ├── company/                  # Trang doanh nghiep
│   │   ├── dashboard.html
│   │   ├── create-task.html
│   │   ├── applicants.html
│   │   ├── evaluate.html
│   │   ├── task-ranking.html
│   │   ├── global-leaderboard.html
│   │   ├── subscription.html
│   │   └── profile.html
│   ├── admin-huong/              # Trang admin
│   │   ├── login.html
│   │   └── index.html
│   └── assets/
│       ├── css/style.css         # Custom CSS
│       ├── js/
│       │   ├── api.js            # API helpers (fetch, token)
│       │   ├── navbar.js         # Navigation bar
│       │   └── utils.js          # Toast, badge, format
│       └── image/
│           └── image.png         # QR code chuyen khoan
│
├── BE/database/
│   └── schema.sql                # SQL schema + seed data
├── skillrank.sql                 # Full database export (import len VPS)
├── setup-apache.bat              # Setup local (XAMPP)
├── setup-vps.bat                 # Setup VPS
├── fix-vhost.bat                 # Fix Apache VirtualHost
├── check-vps.bat                 # Kiem tra VPS
└── docs/
    └── product-requirements-mvp.md  # Tai lieu nay
```

---

## 3.7. Trien khai (Deployment Guide)

### 3.7.1. Yeu cau he thong

| Thanh phan | Yeu cau toi thieu |
|------------|-------------------|
| OS | Windows Server 2012+ hoac Linux |
| Python | 3.8+ |
| MySQL/MariaDB | 10.4+ |
| Apache | 2.4+ voi mod_proxy |
| RAM | 2GB+ |
| Disk | 10GB+ |

### 3.7.2. Cac buoc trien khai

```
BUOC 1: Cai dat XAMPP (Apache + MySQL)
    |
BUOC 2: Import skillrank.sql vao MySQL
    |    mysql -u root -p < skillrank.sql
    |
BUOC 3: Copy FE/ vao C:\xampp\htdocs\skillrank\
    |
BUOC 4: Cai dat Python dependencies
    |    cd BE-Python
    |    py -m venv venv
    |    venv\Scripts\activate
    |    pip install -r requirements.txt
    |
BUOC 5: Cau hinh .env (DB password, JWT secret)
    |
BUOC 6: Chay setup-vps.bat (cau hinh Apache + Firewall)
    |
BUOC 7: Start Apache + MySQL trong XAMPP
    |
BUOC 8: Chay Flask: py app.py
    |
BUOC 9: Truy cap http://[IP_VPS]
```

---

## 3.8. Roadmap phat trien

### Phase 1: MVP (Hien tai - Da hoan thanh)
- [x] He thong 3 role: Student, Company, Admin
- [x] Dang ky, dang nhap voi JWT
- [x] Tao task, nop bai, danh gia
- [x] 3 goi subscription (Basic/Standard/Premium)
- [x] Task Leaderboard + Global Leaderboard
- [x] Admin Dashboard + Duyet thanh toan
- [x] Thanh toan QR Code + Admin duyet thu cong
- [x] Deploy tren VPS Windows

### Phase 2: V1.1 (Thang 4-5/2026)
- [ ] Tich hop VNPay/MoMo thanh toan tu dong
- [ ] Email thong bao (dang ky, danh gia, nang cap goi)
- [ ] Lich su thanh toan
- [ ] Dashboard doanh thu chi tiet cho admin
- [ ] Tu dong reset tasks_used moi thang

### Phase 3: V1.2 (Thang 6-7/2026)
- [ ] Chat truc tiep giua DN va SV
- [ ] Thong bao real-time (WebSocket)
- [ ] Company verified badge
- [ ] Student portfolio page (public URL)
- [ ] Multi-language (Viet/Anh)

### Phase 4: V2.0 (Thang 9-12/2026)
- [ ] AI auto-scoring cho bai nop code
- [ ] Goi y task theo ky nang sinh vien
- [ ] Mobile app (React Native)
- [ ] Analytics dashboard nang cao
- [ ] API cho doi tac tich hop


# ============================================================
# THONG TIN DU AN
# ============================================================

- **Ten du an:** SkillRank
- **Mo ta:** Nen tang ket noi sinh vien voi doanh nghiep qua thu thach thuc te
- **Loai:** Web Application (MVP)
- **URL Production:** http://163.223.12.120
- **Admin Panel:** http://163.223.12.120/admin-huong
- **Admin Login:** admin / admin123
- **Tech Stack:** Flask + MySQL + Tailwind CSS + Apache
- **Trang thai:** Da trien khai tren VPS
- **So man hinh:** 21 trang (6 public + 7 student + 8 company + 2 admin)
- **So API:** 37 endpoints
- **So bang DB:** 7 bang
