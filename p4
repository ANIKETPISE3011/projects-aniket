R1 (hostname ISP)
conf t
hostname ISP

R2 (hostname SanJose1)
conf t
hostname SanJose1
R3(hostname SanJose2)
conf t
hostname SanJose2

Run the following in all the router consoles:

no ip domain-lookup
line con 0
logging synchronous
exec-timeout 0 0

R1(hostname ISP)
conf t
hostname ISP
interface Loopback0 
ip address 192.168.100.1 255.255.255.0 
exit 
interface S1/0 
ip address 192.168.1.5 255.255.255.252 
clock rate 128000 
no shutdown 
exit 
interface S1/1 
ip address 192.168.1.1 255.255.255.252 
no shutdown
end 

R2 (hostname SanJose1)
conf t
hostname SanJose1
interface Loopback0 
ip address 192.168.100.1 255.255.255.0 
exit 
interface S1/0
ip address 192.168.1.5 255.255.255.252 
clock rate 128000 
no shutdown 
exit 
interface S1/1 
ip address 192.168.1.1 255.255.255.252 
no shutdown 
End

R2(hostname SanJose1)
router bgp 64512
neighbor 172.16.32.1 remote-as 64512
neighbor 172.16.32.1 update-source lo0
b. Complete the IBGP configuration on SanJose2 using the following commands.
R3(hostname SanJose2)
router bgp 64512
neighbor 172.16.64.1 remote-as 64512
neighbor 172.16.64.1 update-source lo0
exit
exit
SanJose2# show ip bgp neighbors

R1(hostname ISP)
ISP(config)# router bgp 200
ISP(config-router)# neighbor 192.168.1.6 remote-as 64512
ISP(config-router)# neighbor 192.168.1.2 remote-as 64512
ISP(config-router)# network 192.168.100.0


R2(hostname SanJose1)
exit
SanJose1(config)# ip route 172.16.0.0 255.255.0.0 null0

R2(hostname SanJose1)
SanJose1(config)# router bgp 64512
SanJose1(config-router)# neighbor 192.168.1.5 remote-as 200
SanJose1(config-router)# network 172.16.0.0

R2(hostname SanJose1)
SanJose1# show ip bgp neighbors
