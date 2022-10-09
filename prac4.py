rac 4
St junit junit-4.10.jar→ junit-4.10
TestJUnit.java


package p4;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class TestJUnit {
@Test
public void testSetup(){
String str = "I am Done with Junit Setup";
assertEquals("I am Done with Junit Setup",str);
}
}



TestRunner.java
package p4;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import p4.TestJUnit;
public class TestRunner {
public static void main(String[] args) {
// TODO Auto-generated method stub
Result result = JUnitCore.runClasses(TestJUnit.class);
for(Failure failure:result.getFailures()){
System.out.println(failure.toString());
}
System.out.println("Result=="+result.wasSuccessful());
}
}
