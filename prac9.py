package pk9;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
public class c9 {
/**
* @param args
*/
public static void main(String[] args) {
// TODO Auto-generated method stub
WebDriver driver=new FirefoxDriver();
driver.get("C:\\st\\Combo.html");
int radiochk=0,checkboxchk=0;
int radiounchk=0,checkboxunchk=0;
java.util.List <WebElement>
els=driver.findElements(By.xpath("//input[@type='radio']"));
for(WebElement el:els)
{
if(el.isSelected())
{
radiochk++;
}
else
{
radiounchk++;
}
}
System.out.println("Radio Buttons");
System.out.println("Total Checked items"+ radiochk);
System.out.println("Total unChecked items"+ radiounchk);
java.util.List<WebElement>ebox=driver.findElements(By.xpath("//input[@type='c
heckbox']"));
for(WebElement el:ebox)
{
if(el.isSelected())
{
checkboxchk++;
}
else
{
checkboxunchk++;
}
}
System.out.println("Checkboxes");
System.out.println("Total Checked items"+ checkboxchk);
System.out.println("Total unChecked items"+ checkboxunchk);
}
}
Combo.html
<!DOCTYPE html>
<html>
<body>
<form>
<h2>Text Input</h2>
First Name:</br>
<input type="text" name="Firstname">
</br>
Last Name:</br>
<input type="text" name="lastname">
</br>
<h2>Select Gender</h2>
<input type="radio" name="gender" value="male" checked>Male</br>
<input type="radio" name="gender" value="female">Female</br>
<input type="radio" name="gender" value="others">Others</br>
<h2>Select Languages Known</h2>
<input type="checkbox" name="lang" value="Java" checked="checked">Java</br>
<input type="checkbox" name="lang" value="Php">Php</br>
<input type="checkbox" name="lang" value="ASP.net">.Net</br>
<input type="checkbox" name="lang" value="Python" checked="checked">Python</br>
<input type="submit" value="submit"></br>
</form>
</body>
</html>