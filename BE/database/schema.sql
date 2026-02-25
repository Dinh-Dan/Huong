CREATE DATABASE IF NOT EXISTS skillrank;
USE skillrank;

-- Students table
CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  university VARCHAR(150),
  major VARCHAR(100),
  year_of_study INT,
  skills TEXT,
  phone VARCHAR(20),
  cv_path VARCHAR(255),
  portfolio_link VARCHAR(255),
  linkedin VARCHAR(255),
  avatar_path VARCHAR(255),
  total_score DECIMAL(10,2) DEFAULT 0,
  average_score DECIMAL(5,2) DEFAULT 0,
  total_submissions INT DEFAULT 0,
  interested_count INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Companies table
CREATE TABLE IF NOT EXISTS companies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  company_name VARCHAR(150) NOT NULL,
  registration_number VARCHAR(50) UNIQUE,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  industry VARCHAR(100),
  company_size VARCHAR(50),
  website VARCHAR(255),
  address TEXT,
  description TEXT,
  business_license_path VARCHAR(255),
  logo_path VARCHAR(255),
  subscription_plan ENUM('basic','standard','premium') DEFAULT 'basic',
  task_limit INT DEFAULT 2,
  tasks_used INT DEFAULT 0,
  subscription_expiry DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  company_id INT NOT NULL,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  expected_output TEXT,
  estimated_time VARCHAR(50),
  deadline DATE,
  difficulty ENUM('easy','medium','hard') DEFAULT 'medium',
  industry VARCHAR(100),
  max_submissions INT DEFAULT 50,
  current_submissions INT DEFAULT 0,
  status ENUM('active','closed','draft') DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);

-- Submissions table
CREATE TABLE IF NOT EXISTS submissions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  task_id INT NOT NULL,
  student_id INT NOT NULL,
  file_path VARCHAR(255),
  text_answer TEXT,
  portfolio_link VARCHAR(255),
  score DECIMAL(5,2) DEFAULT NULL,
  feedback TEXT,
  status ENUM('pending','reviewed','interested','rejected') DEFAULT 'pending',
  submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  evaluated_at TIMESTAMP NULL,
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  UNIQUE KEY unique_submission (task_id, student_id)
);

-- Subscription Plans reference table
CREATE TABLE IF NOT EXISTS subscription_plans (
  id INT AUTO_INCREMENT PRIMARY KEY,
  plan_name ENUM('basic','standard','premium') UNIQUE,
  task_limit INT,
  has_task_leaderboard BOOLEAN DEFAULT FALSE,
  has_global_leaderboard BOOLEAN DEFAULT FALSE,
  has_advanced_filters BOOLEAN DEFAULT FALSE,
  has_csv_export BOOLEAN DEFAULT FALSE,
  price DECIMAL(10,2),
  description TEXT
);

-- Seed subscription plans
INSERT INTO subscription_plans (plan_name, task_limit, has_task_leaderboard, has_global_leaderboard, has_advanced_filters, has_csv_export, price, description) VALUES
('basic', 2, FALSE, FALSE, FALSE, FALSE, 0, 'Phù hợp startup nhỏ - Tạo tối đa 2 task/tháng'),
('standard', 5, TRUE, FALSE, FALSE, FALSE, 49.99, 'Phù hợp doanh nghiệp vừa - 5 task/tháng + Task Leaderboard'),
('premium', 999, TRUE, TRUE, TRUE, TRUE, 99.99, 'Phù hợp doanh nghiệp lớn - Không giới hạn + Full Leaderboard + CSV Export')
ON DUPLICATE KEY UPDATE plan_name = plan_name;
