
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;

public class TestBot {

	public static void main(String[] args) throws InterruptedException{
		
		System.out.println("EdgeDriver execution on macOS!!");
        WebDriver driver = new EdgeDriver();
        driver.get("https://demoqa.com");
        Thread.sleep(3000);
        driver.quit();
        System.out.println("Execution complete on macOS");
		
	}
	
}
