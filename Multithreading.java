/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package multithreading;
import java.lang.Thread;
/**
 *
 * @author Administrator
 */
class A extends Thread
{
    public void run()
    {
        for(int i = 1;i<=5;i++)
        {
            System.out.println("From Thread A : i = "+i);
        }
        System.out.println("Exit from A");
    }
}
class B extends Thread
{
    public void run()
    {
        for(int j = 1;j<=5;j++)
        {
            System.out.println("From Thread B : j = "+j);
        }
        System.out.println("Exit from B");
    }
}
class C extends Thread
{
    public void run()
    {
        for(int k = 1;k<=5;k++)
        {
            System.out.println("From Thread B : k = "+k);
        }
        System.out.println("Exit from C");
    }
}

public class Multithreading {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        new A().start();
        new B().start();
        new C().start();
    }
    
}
