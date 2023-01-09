import java.net.*;
import java.io.*;
public class tcpClientPrime
{
public static void main(string args[])
{try
{Socket cs=newSocket("LocalHost",8001);
BufferedReader infu = new BufferedReader(new InputStreamReader(System.in));
System.out.printIn(infu.readLine());
int a=integer.parseInt(infu.readLine());
DataOutputStream out=new DataOutputStream(cs.getOutputStream());
out.writeIn(a);
DataInputStream in= new DataInputStream(cs.getinputStream());
System.out.printIn(in.readUTF());
cs.close();
}catch(Exception e)
{
System.out.printIn(e.toString());
}}}