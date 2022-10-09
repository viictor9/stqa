Test NG 


import java.io.FileInputStream;
import java.io.FileOutputStream;
import jxl.Sheet;
import jxl.Workbook;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
public class c5 {
@BeforeClass
public void f1()
{}
@Test
public void testImportexport1() throws Exception {
FileInputStream fi = new
FileInputStream("C:\\st\\sampledata.xls");
Workbook w = Workbook.getWorkbook(fi);
Sheet s = w.getSheet(0);
String a[][] = new String[s.getRows()][s.getColumns()];
FileOutputStream fo = new
FileOutputStream("C:\\st\\result.xls");
WritableWorkbook wwb = Workbook.createWorkbook(fo);
WritableSheet ws = wwb.createSheet("result1", 0);
for (int i = 0; i<s.getRows(); i++)
{
for (int j = 0; j <s.getColumns(); j++)
{
a[i][j]=s.getCell(j,i).getContents();
Label l2=new Label(j,i,a[i][j]);
ws.addCell(l2);
Label l1=new Label(6,0,"Results");
ws.addCell(l1);
}
}
for (int i = 1; i<s.getRows(); i++)
{
for (int j = 2; j <s.getColumns(); j++)
{
a[i][j]=s.getCell(j,i).getContents();
int x=Integer.parseInt(a[i][j]);
if(x>35)
{
Label l1=new Label(6,i,"Pass");
ws.addCell(l1);
}
else
{
Label l1= new Label(6,i,"Fail");
ws.addCell(l1);
break;
}
}
}
wwb.write();
wwb.close();
}
}