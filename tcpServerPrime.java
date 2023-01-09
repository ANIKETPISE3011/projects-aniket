import java.net.*;
import java.io.*;
class tcpServerPrime
{
public static void main(String args[])
{try
{
ServerSocket ss=new ServerSocket(8001);
System.out.printin("Server Started.....");
socket s=ss.accept();
DataInputStream in =new DataInputStream(s.getInputStream());
int x=in.readint();
DataOutputStream otc= new DataOutputStream(s.getOutputStream());
int y=x/2;
if(x==1|x==2|x==3)
{otc.writeUTF(x+"isprime");
{ if(x%i!=0)
{otc.writeUTF(x+"is prime");
}else
{
otc.writeUTF(x+"is not prime")
}}}
{
System.out.printin(e.tostring());
}}}
