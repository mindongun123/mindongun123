# 🎮 Plan: GitHub Profile "siêu xịn" cho Game Developer — mindongun123

## 1. Mục tiêu
- Profile README nhìn vào là biết ngay: **Casual & Hyper-casual Game Developer (Unity / C#)**, có sản phẩm thật, chơi được.
- Phong cách: **casual / hyper-casual mobile** — tươi sáng, bo tròn, màu kẹo ngọt, chuyển động mượt kiểu "juicy" (bounce, pop, squash & stretch). **Không dùng pixel art / retro.** Hỗ trợ cả dark & light mode.
- Kèm **portfolio web** (GitHub Pages) để showcase game chi tiết hơn, có thể chơi thử WebGL.
- Tự động cập nhật bằng **GitHub Actions** (snake, stats, bài viết, thời tiết...).

## 2. Hiện trạng (README cũ)
| Vấn đề | Hướng xử lý |
|---|---|
| README dài, lẫn nhiều nội dung cá nhân (bài hát, ca sĩ, diễn viên) | Gom vào 1 mục "Fun facts" thu gọn hoặc bỏ |
| Thời tiết là bảng tĩnh từ 2023 | Thay bằng Action tự cập nhật hoặc bỏ |
| Lỗi HTML (`</details` thiếu `>`, `""` thừa, ngày `16/09/2023/2023`, `show_owner=flase`) | Sửa hết |
| Ảnh ở root lộn xộn | Chuyển vào `assets/` |
| Mô tả game bằng tiếng Việt, ngày sai | Viết lại song ngữ, chuẩn hóa |
| Thiếu "điểm nhấn" thị giác | Thêm banner, typing SVG, snake, card game |

## 3. Cấu trúc README mới (từ trên xuống)
1. **Header banner** — capsule-render (sóng/gradient) + tên "MJ Game" + slogan.
2. **Typing animation** (readme-typing-svg): "Casual & Hyper-casual Game Developer", "Unity + C#", "Easy to play, hard to put down 🎮".
3. **"Player Card"** — giới thiệu kiểu nhân vật game:
   ```
   🧙 Class: Casual / Hyper-casual Dev  ⚔️ Level: 2003 born   🗺️ Region: Thanh Hóa, VN
   🎯 Quest: ...              🛡️ Main weapon: Unity + C#
   ```
4. **Tech Stack / Inventory** — skill-icons (Unity, C#, .NET, Git, Firebase, AdMob/IronSource/AppLovin MAX, Unity Analytics, DOTween...).
5. **🕹️ Game Showcase** — lưới card 2–3 cột: GIF gameplay ngắn (5–10s, đúng chất hyper-casual), tên, thể loại (Match-3, Merge, Puzzle, Music/Tap, Idle...), nền tảng, nút "Download APK" / "Play WebGL".
6. **📊 Stats "Boss fight"** — github-readme-stats + streak + top languages + activity graph (theme đồng bộ, dark/light qua `<picture>`).
7. **🏆 Achievements** — trophy (github-profile-trophy).
8. **🐍 Contribution Snake / Pac-Man** — sinh bằng Action (Platane/snk).
9. **📝 Blog / Devlog mới nhất** — tự động (blog-post-workflow) nếu có blog/YouTube.
10. **🎵 Fun facts** (thu gọn trong `<details>`) — bài hát yêu thích, idol...
11. **📫 Connect** — badge Facebook, Discord, Instagram, Email, itch.io / Google Play.
12. **Footer** — capsule-render sóng ngược + visitor counter.

## 4. Portfolio Web (GitHub Pages) — phong cách "game studio" chuyên nghiệp
> README = trang show GitHub (stats, repo, hoạt động). Web = portfolio chính, **hiện đại, tươi trẻ, năng động, kiểu công ty** (như website một indie studio: "MJ Game Studio").

- Repo: `mindongun123.github.io` (hoặc `/docs` trong repo này).
- Công nghệ: HTML/CSS/JS thuần (nhẹ, không cần build), animation bằng GSAP/CSS.
- **Nhận diện thương hiệu**
  - Tên: **MJ Game Studio** + logo "MJ" (đã lưu tại `assets/brand/logo.png`).
  - Màu (lấy theo logo): gradient **xanh ngọc `#2DD4BF` → xanh dương `#0EA5E9` → xanh biển `#2563EB`**, điểm nhấn **nâu nhạt / be `#D6B48C`** (ấm, trẻ trung); nền sáng trắng ngà `#FAF7F2`, dark mode nền xanh than `#0B1220`.
  - **Nút chuyển Sáng / Tối** và **nút chuyển ngôn ngữ EN / VI** trên navbar (lưu lựa chọn vào localStorage, mặc định theo hệ thống/trình duyệt).
  - Toàn bộ chữ trên web lấy từ file `i18n` (`en.json` / `vi.json`) để dễ sửa.
  - Font: *Plus Jakarta Sans* / *Outfit* (hiện đại, bo tròn), bo góc lớn, glassmorphism nhẹ, blob gradient chuyển động.
- **Các section (giống website công ty)**
  1. **Navbar** dính trên cùng: Home · Games · Services · About · Contact + nút CTA "Hire me".
  2. **Hero**: slogan lớn ("We craft games people love"), mô tả ngắn, 2 nút (Xem game / Liên hệ), mockup điện thoại chạy GIF game, blob màu chuyển động.
  3. **Số liệu nổi bật** (counter chạy số): số game đã làm, số prototype, năm kinh nghiệm, lượt tải.
  4. **Games / Portfolio**: lưới card có filter (Match-3, Merge, Puzzle, Music/Tap, Hyper-casual…), hover hiện GIF, mở modal chi tiết + nút Download APK / Play WebGL.
  5. **Services**: Prototype hyper-casual nhanh (test CPI) · Game casual mobile Unity · Game feel / juicy UI · Tích hợp Ads & IAP, Analytics · Tối ưu & publish lên store.
  6. **Tech stack**: dải logo chạy ngang (marquee).
  7. **Quy trình làm việc**: Ý tưởng → Prototype → Phát triển → Test → Phát hành (timeline).
  8. **About / Founder**: ảnh, giới thiệu, hành trình (timeline năm).
  9. **Contact**: form (Formspree), email, mạng xã hội.
  10. **Footer** chuyên nghiệp: logo, link nhanh, © MJ Game Studio.
- Hiệu ứng: scroll reveal, hover nghiêng card (tilt), cursor glow, chuyển dark/light, responsive mobile.
- README link sang web bằng nút lớn "🌐 Visit MJ Game Studio".

## 5. GitHub Actions
- `snake.yml` — snake/pac-man từ contribution graph (chạy hằng ngày).
- `blog.yml` — cập nhật devlog/YouTube (nếu có).
- (tuỳ chọn) `weather.yml` — thời tiết Thanh Hóa thực tế.
- `pages.yml` — deploy portfolio web.

## 6. Cấu trúc thư mục dự kiến
```
mindongun123/
├── README.md
├── plan.md
├── assets/
│   ├── games/        (thumbnail, gif các game)
│   ├── icons/        (discord, facebook, instagram...)
│   └── banner/
├── .github/workflows/
│   ├── snake.yml
│   └── blog.yml
└── docs/  (hoặc repo riêng mindongun123.github.io)
    ├── index.html
    ├── css/  js/  games/
```

## 7. Các bước thực hiện
1. [ ] Bạn trả lời các câu hỏi ở mục 8.
2. [x] Dọn ảnh vào `assets/`, sửa lỗi README cũ.
3. [x] Viết README mới (header → showcase → stats → footer).
4. [x] Thêm workflow snake + kiểm tra chạy.
5. [x] Xây portfolio web + deploy GitHub Pages.
6. [ ] Kiểm tra dark/light mode, mobile, link hỏng.
7. [x] Commit & push.

## 8. ❓ Câu hỏi cần bạn trả lời
1. ~~Ngôn ngữ README~~ → **Đã chốt**: README chỉ 1 ngôn ngữ (đề xuất **tiếng Anh** cho nhà tuyển dụng); song ngữ EN/VI + sáng/tối nằm ở web.
2. **Nội dung cá nhân** (bài hát, BABYMONSTER, diễn viên, địa chỉ chi tiết, bản đồ): giữ, thu gọn, hay bỏ? *(Khuyến nghị: thu gọn, bỏ địa chỉ chi tiết vì lý do riêng tư.)*
3. **Danh sách game** casual/hyper-casual muốn showcase (Match Kit, Block, Emoji, TapMusic, MergeRestaurant... — có bỏ Mario không?): game nào, link tải mới nhất (APK / Google Play / itch.io), có bản WebGL không?
4. **Skill** ngoài Unity/C#/.NET: ad mediation (AdMob, IronSource, MAX), IAP, Firebase, Analytics/AB test, DOTween, SDK publisher (Voodoo, Homa, Rollic...)?
5. **Hiện tại** bạn đang làm ở đâu / tìm việc / freelance? Có muốn ghi "Open to work"?
6. **Link mạng xã hội** cập nhật: Facebook, Discord, Instagram, LinkedIn, YouTube, itch.io, email nào dùng công khai?
7. ~~Phong cách~~ → **Đã chốt**: hiện đại, tươi trẻ, kiểu công ty. Logo đã có, màu chủ đạo xanh ngọc/xanh dương + nâu nhạt. Tên "MJ Game Studio" được không?
8. **Portfolio web**: đặt ở repo riêng `mindongun123.github.io` hay thư mục `docs/` trong repo này?
9. Có blog / kênh YouTube devlog để tự động lấy bài mới không?
