@echo off
echo ============================================
echo    SETUP APACHE CHO SKILLRANK
echo ============================================
echo.

:: Kiem tra XAMPP
if not exist "C:\xampp\apache\conf\httpd.conf" (
    echo [LOI] Khong tim thay XAMPP tai C:\xampp
    echo Hay cai XAMPP truoc roi chay lai file nay.
    pause
    exit /b 1
)

echo [1/4] Copy frontend vao htdocs...
if exist "C:\xampp\htdocs\skillrank" (
    rmdir /s /q "C:\xampp\htdocs\skillrank"
)
xcopy "%~dp0FE" "C:\xampp\htdocs\skillrank\" /E /I /Q /Y
echo      OK - Da copy FE vao C:\xampp\htdocs\skillrank

echo.
echo [2/4] Bat module proxy_http trong httpd.conf...
powershell -Command "(Get-Content 'C:\xampp\apache\conf\httpd.conf') -replace '^#LoadModule proxy_http_module modules/mod_proxy_http.so','LoadModule proxy_http_module modules/mod_proxy_http.so' | Set-Content 'C:\xampp\apache\conf\httpd.conf'"
echo      OK - Da bat mod_proxy_http

echo.
echo [3/4] Doi DocumentRoot sang skillrank...
powershell -Command "(Get-Content 'C:\xampp\apache\conf\httpd.conf') -replace 'DocumentRoot \"C:/xampp/htdocs\"','DocumentRoot \"C:/xampp/htdocs/skillrank\"' -replace '<Directory \"C:/xampp/htdocs\">','<Directory \"C:/xampp/htdocs/skillrank\">' | Set-Content 'C:\xampp\apache\conf\httpd.conf'"
echo      OK - DocumentRoot da tro ve skillrank

echo.
echo [4/4] Them VirtualHost config...
powershell -Command "$vhostFile = 'C:\xampp\apache\conf\extra\httpd-vhosts.conf'; $content = Get-Content $vhostFile -Raw; if ($content -notmatch 'SKILLRANK') { $vhost = @\"`n# ===== SKILLRANK =====`n<VirtualHost *:80>`n    ServerName localhost`n`n    DocumentRoot \"\"C:/xampp/htdocs/skillrank\"\"`n`n    <Directory \"\"C:/xampp/htdocs/skillrank\"\">`n        Options FollowSymLinks`n        AllowOverride All`n        Require all granted`n    </Directory>`n`n    ProxyPreserveHost On`n    ProxyPass /api http://localhost:5000/api`n    ProxyPassReverse /api http://localhost:5000/api`n`n    ProxyPass /uploads http://localhost:5000/uploads`n    ProxyPassReverse /uploads http://localhost:5000/uploads`n</VirtualHost>`n\"@; Add-Content $vhostFile $vhost; Write-Host '      OK - Da them VirtualHost' } else { Write-Host '      OK - VirtualHost da ton tai, bo qua' }"

echo.
echo [5/5] Tao tai khoan Admin...
timeout /t 3 /nobreak >nul
curl -s -X POST http://localhost:5000/api/admin/create -H "Content-Type: application/json" -d "{\"username\":\"admin\",\"password\":\"admin123\",\"full_name\":\"Admin Huong\"}" >nul 2>&1
echo      OK - Admin account: admin / admin123

echo.
echo ============================================
echo    HOAN THANH!
echo ============================================
echo.
echo Buoc tiep theo:
echo   1. Mo XAMPP Control Panel
echo   2. Start Apache va MySQL
echo   3. Chay Flask: cd BE-Python ^& python app.py
echo   4. Truy cap: http://localhost
echo.
echo   ADMIN PANEL: http://localhost/admin-huong
echo   Dang nhap:   admin / admin123
echo.
echo Neu co ten mien, sua ServerName trong file:
echo   C:\xampp\apache\conf\extra\httpd-vhosts.conf
echo   Doi "ServerName localhost" thanh "ServerName tenmiencuaban.com"
echo.
pause
