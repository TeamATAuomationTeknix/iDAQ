public class Test
{
public static void main(String args[])
{
Calculator d = new Calculator();
int s = d.add(3,5);
System.out.println("Addition "+s);

int t = d.sub(3,5);
System.out.println("Substraction "+t);

int u = d.mult(3,5);
System.out.println("Multiplication "+u);

int v = d.div(3,5);
System.out.println("Division "+v);

int w = d.sqr(3);
System.out.println("Square "+w);
}
}