R1 Console
interface Loopback 0
ip address 192.168.1.1 255.255.255.0
exit
 
R1 Console
conf t
interface Serial1/0
ip address 10.1.1.1 255.255.255.252
clock rate 128000
no shutdown
exit
R2 Console
interface Serial1/0
ip address 10.1.1.2 255.255.255.252
no shutdown
exit
R2 Console
conf t
interface Serial1/1
ip address 10.2.2.1 255.255.255.252
clock rate 128000
no shutdown
exit
R3 Console
interface Loopback0
ip address 192.168.3.1 255.255.255.0
exit
R3 Console
interface Serial1/1
ip address 10.2.2.2 255.255.255.252
no shutdown
exit
Step 2: Configure static routes.
R1 Console
ip route 0.0.0.0 0.0.0.0 10.1.1.2
R1 Console
R1#tclsh
foreach address {
+>(tcl)#192.168.1.1
+>(tcl)#10.1.1.1
+>(tcl)#10.1.1.2
+>(tcl)#10.2.2.1
+>(tcl)#10.2.2.2
+>(tcl)#192.168.3.1
+>(tcl)#} { ping $address }

R3 Console
ip route 0.0.0.0 0.0.0.0 10.2.2.1	

Step 3: Secure management access.
R1 Console
security passwords min-length 10
enable secret class12345
line console 0
password ciscoconpass
exec-timeout 5 0
login
logging synchronous
exit

line vty 0 4
password ciscovtypass
exec-timeout 5 0
login
exit

line aux 0
no exec 
end

service password-encryption
banner motd $Unauthorized access strictly prohibited!$
exit

R3 Console
security passwords min-length 10
enable secret class12345
line console 0
password ciscoconpass
exec-timeout 5 0
login
logging synchronous
exit

line vty 0 4
password ciscovtypass
exec-timeout 5 0
login
exit

line aux 0
no exec 
end

service password-encryption
banner motd $Unauthorized access strictly prohibited!$
exit

R1 Console
username JR-ADMIN secret class12345
username ADMIN secret class54321
line console 0
login local
exit

line vty 0 4
login local
end

R3 Console
username JR-ADMIN secret class12345
username ADMIN secret class54321
line console 0
login local
exit

line vty 0 4
login local
end

R1 Console
telnet 10.2.2.2
