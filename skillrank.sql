-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th2 26, 2026 lúc 03:33 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `skillrank`
--
CREATE DATABASE IF NOT EXISTS `skillrank` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `skillrank`;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `admins`
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `admins`
--

INSERT INTO `admins` (`id`, `username`, `password`, `full_name`, `created_at`) VALUES
(1, 'admin', '$2b$12$wcVU2xOonh2REDljMDNwi.GBJ7ebYpEP1nz74b/NIMkN0Q/Yo4eqe', 'Admin Huong', '2026-02-26 02:17:31');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `companies`
--

DROP TABLE IF EXISTS `companies`;
CREATE TABLE `companies` (
  `id` int(11) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `registration_number` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `industry` varchar(100) DEFAULT NULL,
  `company_size` varchar(50) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `business_license_path` varchar(255) DEFAULT NULL,
  `logo_path` varchar(255) DEFAULT NULL,
  `subscription_plan` enum('basic','standard','premium') DEFAULT 'basic',
  `task_limit` int(11) DEFAULT 2,
  `tasks_used` int(11) DEFAULT 0,
  `subscription_expiry` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `companies`
--

INSERT INTO `companies` (`id`, `company_name`, `registration_number`, `email`, `password`, `industry`, `company_size`, `website`, `address`, `description`, `business_license_path`, `logo_path`, `subscription_plan`, `task_limit`, `tasks_used`, `subscription_expiry`, `created_at`) VALUES
(1, 'công ti ', '1234789753', 'wleanhducw2005@gmail.com', '$2a$10$p6bg8AW4pN2I5.BxvQIPlertVOwxfe6LbaPlgvfHxFvGc51Rgaq.i', 'Technology', '1-10', 'http://127.0.0.1:5500/FE/register-company.html', 'chung cư hh2 linh đàm', '12qửetdrftjgmn', NULL, '1772005560131-12.png', 'premium', 999, 7, '2026-03-27', '2026-02-25 07:46:00'),
(2, 'công ti nghèo', '23453425', 'dinhdannguyen2003@gmail.com', '$2b$12$fpVF5ZKP9ZPGlRxnGE7Kh.trUnH3coshLw/oYv8mka/uaV5hIZ58G', 'Marketing', '11-50', '', 'chung cư hh2 linh đàm', 'ềwfè', '1772016931669-2073.png', '1772016931670-2077.png', 'basic', 2, 1, NULL, '2026-02-25 10:55:31');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `university` varchar(150) DEFAULT NULL,
  `major` varchar(100) DEFAULT NULL,
  `year_of_study` int(11) DEFAULT NULL,
  `skills` text DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `cv_path` varchar(255) DEFAULT NULL,
  `portfolio_link` varchar(255) DEFAULT NULL,
  `linkedin` varchar(255) DEFAULT NULL,
  `avatar_path` varchar(255) DEFAULT NULL,
  `total_score` decimal(10,2) DEFAULT 0.00,
  `average_score` decimal(5,2) DEFAULT 0.00,
  `total_submissions` int(11) DEFAULT 0,
  `interested_count` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `students`
--

INSERT INTO `students` (`id`, `full_name`, `email`, `password`, `university`, `major`, `year_of_study`, `skills`, `phone`, `cv_path`, `portfolio_link`, `linkedin`, `avatar_path`, `total_score`, `average_score`, `total_submissions`, `interested_count`, `created_at`) VALUES
(1, 'ĐÌNH DÂN', 'dinhdannguyen2003@gmail.com', '$2a$10$XdVVkZ3rqmo0HHABKlzJIeJaI6mY.UY9EAzpXL7TQYdF1dFyZ0A/.', 'XÚC HỒ V2', 'HACKER', 1, 'TRỘM CẮP VẶT', '0362469321', '1772008565793-TIN314___Final_Project (1).pdf', 'http://127.0.0.1:5500/FE/register-student.html', 'http://127.0.0.1:5500/FE/register-student.html', NULL, 189.00, 63.00, 9, 2, '2026-02-25 07:33:51');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `submissions`
--

DROP TABLE IF EXISTS `submissions`;
CREATE TABLE `submissions` (
  `id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `text_answer` text DEFAULT NULL,
  `portfolio_link` varchar(255) DEFAULT NULL,
  `score` decimal(5,2) DEFAULT NULL,
  `feedback` text DEFAULT NULL,
  `status` enum('pending','reviewed','interested','rejected') DEFAULT 'pending',
  `submitted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `evaluated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `submissions`
--

INSERT INTO `submissions` (`id`, `task_id`, `student_id`, `file_path`, `text_answer`, `portfolio_link`, `score`, `feedback`, `status`, `submitted_at`, `evaluated_at`) VALUES
(1, 1, 1, '1772005735903-TIN314___Final_Project (1).pdf', 'tôi đã làm xong', 'http://127.0.0.1:5500/FE/register-student.html', 100.00, 'ngu', 'interested', '2026-02-25 07:48:55', '2026-02-25 07:49:51'),
(2, 5, 1, NULL, NULL, NULL, 77.00, 'wleanhducw2005@gmail.comwleanhducw2005@gmail.com', 'interested', '2026-02-25 09:04:42', '2026-02-25 09:06:24'),
(9, 7, 1, '1772015323472-TIN314___Final_Project (1).pdf', 'afwdưq', 'https://www.facebook.com/dinhdannguyen2003', NULL, NULL, 'pending', '2026-02-25 10:28:43', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `subscription_plans`
--

DROP TABLE IF EXISTS `subscription_plans`;
CREATE TABLE `subscription_plans` (
  `id` int(11) NOT NULL,
  `plan_name` enum('basic','standard','premium') DEFAULT NULL,
  `task_limit` int(11) DEFAULT NULL,
  `has_task_leaderboard` tinyint(1) DEFAULT 0,
  `has_global_leaderboard` tinyint(1) DEFAULT 0,
  `has_advanced_filters` tinyint(1) DEFAULT 0,
  `has_csv_export` tinyint(1) DEFAULT 0,
  `price` decimal(10,2) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `subscription_plans`
--

INSERT INTO `subscription_plans` (`id`, `plan_name`, `task_limit`, `has_task_leaderboard`, `has_global_leaderboard`, `has_advanced_filters`, `has_csv_export`, `price`, `description`) VALUES
(1, 'basic', 2, 0, 0, 0, 0, 0.00, 'Phù hợp startup nhỏ - Tạo tối đa 2 task/tháng'),
(2, 'standard', 5, 1, 0, 0, 0, 49.99, 'Phù hợp doanh nghiệp vừa - 5 task/tháng + Task Leaderboard'),
(3, 'premium', 999, 1, 1, 1, 1, 99.99, 'Phù hợp doanh nghiệp lớn - Không giới hạn + Full Leaderboard + CSV Export');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tasks`
--

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text DEFAULT NULL,
  `expected_output` text DEFAULT NULL,
  `estimated_time` varchar(50) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `difficulty` enum('easy','medium','hard') DEFAULT 'medium',
  `industry` varchar(100) DEFAULT NULL,
  `max_submissions` int(11) DEFAULT 50,
  `current_submissions` int(11) DEFAULT 0,
  `status` enum('active','closed','draft') DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tasks`
--

INSERT INTO `tasks` (`id`, `company_id`, `title`, `description`, `expected_output`, `estimated_time`, `deadline`, `difficulty`, `industry`, `max_submissions`, `current_submissions`, `status`, `created_at`) VALUES
(1, 1, 'tên nhiệm vụ ', 'hãy làm 1 nhiệm vụ ', 'nộp bằng file js ', '30 năm', '2026-02-26', 'hard', 'Education', 50, 1, 'active', '2026-02-25 07:47:19'),
(2, 1, 'task2', 'task2', 'task2', '30 năm', '2026-03-01', 'hard', 'Technology', 50, 1, 'active', '2026-02-25 08:48:48'),
(3, 1, 'task223', 'task2214', '13123', '30 năm', '2026-02-14', 'medium', 'Marketing', 50, 0, 'active', '2026-02-25 08:49:07'),
(4, 1, 'task2', 'e2qdaw', 'qdưaqđe', 'qeqe', '2026-02-13', 'easy', 'Marketing', 50, 0, 'active', '2026-02-25 08:49:38'),
(5, 1, 'taswleanhducw2005@gmail.com', 'wleanhducw2005@gmail.comwleanhducw2005@gmail.comwleanhducw2005@gmail.comwleanhducw2005@gmail.com', 'wleanhducw2005@gmail.comwleanhducw2005@gmail.comwleanhducw2005@gmail.comwleanhducw2005@gmail.com', 'wleanhducw2005@gmail.comwleanhducw2005@gmail.com', '2026-02-28', 'hard', 'Marketing', 50, 1, 'active', '2026-02-25 09:04:07'),
(6, 1, 'https://www.facebook.com/dinhdannguyen2003', 'https://www.facebook.com/dinhdannguyen2003', 'https://www.facebook.com/dinhdannguyen2003', 'wleanhducw2005@gmail.comwleanhducw2005@gmail.com', '2026-02-28', 'easy', 'Finance', 50, 1, 'active', '2026-02-25 09:14:11'),
(7, 1, 'ầcfa', 'aềâf', 'qwqfw', 'wleanhducw2005@gmail.comwleanhducw2005@gmail.com', '2026-02-28', 'medium', '', 50, 5, 'active', '2026-02-25 09:19:17'),
(8, 2, 'task công ti nghèo', 'task công ti nghèo', 'task công ti nghèo', 'task công ti nghèo', '2026-02-28', 'medium', '', 50, 0, 'active', '2026-02-25 10:56:14');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `upgrade_requests`
--

DROP TABLE IF EXISTS `upgrade_requests`;
CREATE TABLE `upgrade_requests` (
  `id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `current_plan` enum('basic','standard','premium') NOT NULL,
  `requested_plan` enum('basic','standard','premium') NOT NULL,
  `status` enum('pending','approved','rejected') DEFAULT 'pending',
  `admin_note` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `processed_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `upgrade_requests`
--

INSERT INTO `upgrade_requests` (`id`, `company_id`, `current_plan`, `requested_plan`, `status`, `admin_note`, `created_at`, `processed_at`) VALUES
(1, 2, 'basic', 'standard', 'rejected', '', '2026-02-26 02:28:48', '2026-02-26 02:30:13');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Chỉ mục cho bảng `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `registration_number` (`registration_number`);

--
-- Chỉ mục cho bảng `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Chỉ mục cho bảng `submissions`
--
ALTER TABLE `submissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_submission` (`task_id`,`student_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Chỉ mục cho bảng `subscription_plans`
--
ALTER TABLE `subscription_plans`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `plan_name` (`plan_name`);

--
-- Chỉ mục cho bảng `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_id` (`company_id`);

--
-- Chỉ mục cho bảng `upgrade_requests`
--
ALTER TABLE `upgrade_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_id` (`company_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `companies`
--
ALTER TABLE `companies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `submissions`
--
ALTER TABLE `submissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `subscription_plans`
--
ALTER TABLE `subscription_plans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `tasks`
--
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `upgrade_requests`
--
ALTER TABLE `upgrade_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `submissions`
--
ALTER TABLE `submissions`
  ADD CONSTRAINT `submissions_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `submissions_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `upgrade_requests`
--
ALTER TABLE `upgrade_requests`
  ADD CONSTRAINT `upgrade_requests_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
