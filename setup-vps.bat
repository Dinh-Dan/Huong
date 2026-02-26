@echo off
echo ============================================
echo    SETUP APACHE CHO VPS - SKILLRANK
echo    IP: 163.223.12.120
echo ============================================
echo.

:: Kiem tra XAMPP
if not exist "C:\xampp\apache\conf\httpd.conf" (
    echo [LOI] Khong tim thay XAMPP tai C:\xampp
    pause
    exit /b 1
)

echo [1/6] Copy frontend vao htdocs...
if exist "C:\xampp\htdocs\skillrank" (
    rmdir /s /q "C:\xampp\htdocs\skillrank"
)
xcopy "%~dp0FE" "C:\xampp\htdocs\skillrank\" /E /I /Q /Y
echo      OK - Da copy FE vao C:\xampp\htdocs\skillrank

echo.
echo [2/6] Bat module proxy trong httpd.conf...
powershell -Command "$f='C:\xampp\apache\conf\httpd.conf'; $c=Get-Content $f; $c=$c -replace '^#LoadModule proxy_module modules/mod_proxy.so','LoadModule proxy_module modules/mod_proxy.so'; $c=$c -replace '^#LoadModule proxy_http_module modules/mod_proxy_http.so','LoadModule proxy_http_module modules/mod_proxy_http.so'; $c=$c -replace '^#LoadModule rewrite_module modules/mod_rewrite.so','LoadModule rewrite_module modules/mod_rewrite.so'; $c | Set-Content $f"
echo      OK - Da bat mod_proxy, mod_proxy_http, mod_rewrite

echo.
echo [3/6] Doi DocumentRoot sang skillrank...
powershell -Command "(Get-Content 'C:\xampp\apache\conf\httpd.conf') -replace 'DocumentRoot \"C:/xampp/htdocs\"','DocumentRoot \"C:/xampp/htdocs/skillrank\"' -replace '<Directory \"C:/xampp/htdocs\">','<Directory \"C:/xampp/htdocs/skillrank\">' | Set-Content 'C:\xampp\apache\conf\httpd.conf'"
echo      OK - DocumentRoot da tro ve skillrank

echo.
echo [4/6] Them VirtualHost config...
powershell -Command "$vhostFile = 'C:\xampp\apache\conf\extra\httpd-vhosts.conf'; $content = Get-Content $vhostFile -Raw; if ($content -notmatch 'SKILLRANK') { $vhost = @\"`n# ===== SKILLRANK =====`n<VirtualHost *:80>`n    ServerName 163.223.12.120`n`n    DocumentRoot \"\"C:/xampp/htdocs/skillrank\"\"`n`n    <Directory \"\"C:/xampp/htdocs/skillrank\"\">`n        Options FollowSymLinks`n        AllowOverride All`n        Require all granted`n    </Directory>`n`n    ProxyPreserveHost On`n    ProxyPass /api http://localhost:5000/api`n    ProxyPassReverse /api http://localhost:5000/api`n`n    ProxyPass /uploads http://localhost:5000/uploads`n    ProxyPassReverse /uploads http://localhost:5000/uploads`n</VirtualHost>`n\"@; Add-Content $vhostFile $vhost; Write-Host '      OK - Da them VirtualHost' } else { Write-Host '      OK - VirtualHost da ton tai, bo qua' }"

echo.
echo [5/6] Mo port 80 tren Windows Firewall...
netsh advfirewall firewall add rule name="HTTP Port 80" dir=in action=allow protocol=TCP localport=80 >nul 2>&1
netsh advfirewall firewall add rule name="Flask Port 5000" dir=in action=allow protocol=TCP localport=5000 >nul 2>&1
echo      OK - Da mo port 80 va 5000

echo.
echo [6/6] Restart Apache...
net stop Apache2.4 >nul 2>&1
"C:\xampp\apache\bin\httpd.exe" -k restart >nul 2>&1
echo      OK - Apache da restart

echo.
echo ============================================
echo    HOAN THANH!
echo ============================================
echo.
echo Tiep theo:
echo   1. Start Apache va MySQL trong XAMPP
echo   2. Chay Flask:
echo      cd %~dp0BE-Python
echo      venv\Scripts\activate
echo      py app.py
echo.
echo   TRANG WEB:    http://163.223.12.120
echo   ADMIN PANEL:  http://163.223.12.120/admin-huong
echo   Dang nhap:    admin / admin123
echo.
pause
