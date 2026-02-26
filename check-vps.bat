@echo off
echo ============================================
echo    CHECK VPS SKILLRANK
echo ============================================
echo.

echo [1] Kiem tra Apache dang chay...
tasklist /FI "IMAGENAME eq httpd.exe" 2>nul | find /I "httpd.exe" >nul
if %errorlevel%==0 (echo      OK - Apache dang chay) else (echo      LOI - Apache CHUA chay! Start trong XAMPP)

echo.
echo [2] Kiem tra Flask dang chay tren port 5000...
netstat -an | find "5000" | find "LISTENING" >nul
if %errorlevel%==0 (echo      OK - Port 5000 dang LISTENING) else (echo      LOI - Flask CHUA chay! Chay: py app.py)

echo.
echo [3] Kiem tra port 80...
netstat -an | find ":80 " | find "LISTENING" >nul
if %errorlevel%==0 (echo      OK - Port 80 dang LISTENING) else (echo      LOI - Port 80 CHUA mo!)

echo.
echo [4] Test Flask truc tiep...
curl -s -o nul -w "      Flask API: HTTP %%{http_code}" http://localhost:5000/api/health
echo.

echo.
echo [5] Test Apache proxy /api...
curl -s -o nul -w "      Apache proxy: HTTP %%{http_code}" http://localhost/api/health
echo.

echo.
echo [6] Kiem tra module proxy trong httpd.conf...
find /C "LoadModule proxy_module" "C:\xampp\apache\conf\httpd.conf" >nul 2>&1
findstr /R "^LoadModule proxy_module" "C:\xampp\apache\conf\httpd.conf" >nul 2>&1
if %errorlevel%==0 (echo      OK - mod_proxy da bat) else (echo      LOI - mod_proxy CHUA bat! Bo dau # trong httpd.conf)

findstr /R "^LoadModule proxy_http_module" "C:\xampp\apache\conf\httpd.conf" >nul 2>&1
if %errorlevel%==0 (echo      OK - mod_proxy_http da bat) else (echo      LOI - mod_proxy_http CHUA bat! Bo dau # trong httpd.conf)

echo.
echo [7] Kiem tra VirtualHost co ProxyPass...
findstr /C "ProxyPass /api" "C:\xampp\apache\conf\extra\httpd-vhosts.conf" >nul 2>&1
if %errorlevel%==0 (echo      OK - ProxyPass /api da co trong vhosts) else (echo      LOI - ProxyPass CHUA co! Chay lai setup-vps.bat)

echo.
echo [8] Kiem tra Firewall port 80...
netsh advfirewall firewall show rule name="HTTP Port 80" >nul 2>&1
if %errorlevel%==0 (echo      OK - Firewall cho phep port 80) else (echo      LOI - Firewall CHUA mo port 80!)

echo.
echo [9] Hien thi noi dung httpd-vhosts.conf...
echo      ------------------------------------------
type "C:\xampp\apache\conf\extra\httpd-vhosts.conf"
echo.
echo      ------------------------------------------

echo.
echo [10] Test tu ben ngoai...
curl -s -o nul -w "      External: HTTP %%{http_code}" http://163.223.12.120/api/health
echo.

echo.
echo ============================================
echo    Xem ket qua o tren de biet loi o dau
echo ============================================
pause
