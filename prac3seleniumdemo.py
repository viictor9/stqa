Pract 3
St client selenium-java-2.47.1 ADD librarys selenium-java.2.47.1.jar ,
selenium-java.2.47.1-srcs.jar + all librarys in libs folder





code:

package pk3;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
public class p3 {
public static void main(String[] args) {
// TODO Auto-generated method stub
int a = 10, b = 20;
System.out.println("Hi...");
System.out.println(a+b);
System.out.println("Selenium demo ...");
WebDriver driver = new FirefoxDriver();
driver.get("https://www.facebook.com/");
driver.manage().window().maximize();
driver.quit();
}
}
