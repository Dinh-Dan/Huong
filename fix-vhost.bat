@echo off
echo Dang them VirtualHost vao httpd-vhosts.conf...

>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo.
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo # ===== SKILLRANK =====
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo ^<VirtualHost *:80^>
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ServerName 163.223.12.120
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo.
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     DocumentRoot "C:/xampp/htdocs/skillrank"
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo.
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ^<Directory "C:/xampp/htdocs/skillrank"^>
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo         Options FollowSymLinks
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo         AllowOverride All
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo         Require all granted
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ^</Directory^>
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo.
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ProxyPreserveHost On
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ProxyPass /api http://localhost:5000/api
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ProxyPassReverse /api http://localhost:5000/api
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo.
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ProxyPass /uploads http://localhost:5000/uploads
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo     ProxyPassReverse /uploads http://localhost:5000/uploads
>> "C:\xampp\apache\conf\extra\httpd-vhosts.conf" echo ^</VirtualHost^>

echo OK - Da them VirtualHost!
echo.
echo Bay gio RESTART Apache trong XAMPP Control Panel
echo Roi truy cap http://163.223.12.120
pause
