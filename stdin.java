import java.util.Scanner;

class stdin
{
  public static void main(String arg[])
  {
    Scanner in=new Scanner(System.in);
    int n=in.nextInt();
    String s=in.nextLine();
    System.out.println(n*2);
    System.out.println(s);
  }
}
