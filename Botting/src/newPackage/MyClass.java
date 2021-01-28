package newPackage;


import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Cookie;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;

public class MyClass {

	public static void main(String[] args) throws InterruptedException {
		
		String UID = "116345439", password = "Al3xisGr3@t1";
		
		System.setProperty("webdriver.chrome.driver", "chromedriver");
		
		WebDriver driver = new ChromeDriver();
		//driver.manage().window().maximize();
		//driver.manage().deleteAllCookies();
		
		driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS);
		
		//loads url
		driver.get("https://www.imleagues.com/spa/fitness/4395e0c781af4905a4088a9561509399/home");
		
		Set<Cookie> cookies = driver.manage().getCookies();

		//click login button
		driver.findElement(By.cssSelector("#imlFloatBar > div > div > div > ul.list-unstyled.iml-nav.iml-m-0.iml-nav-right.pull-right > li > div > a.btn.iml-btn-warning-outline.btn-sm")).click();
		
		//proceed to SSO
		driver.findElement(By.cssSelector("#ssoDirect")).click();

		//enter username
		driver.findElement(By.id("username")).sendKeys(UID);
		
		//enter password NEEDS ENCRYPTION READ PASSWORD FROM ENCRYPTED TEXT FILE
		driver.findElement(By.id("password")).sendKeys(password);

		//click Log in
		driver.findElement(By.name("_eventId_proceed")).click();
		
		
		
		driver.findElement(By.cssSelector("#imlDefaultMenu > div.btn-group.iml-head-main-title-btn-group.schoolMainNavigBack > a:nth-child(2)")).click();

//		//give page time to load?
//		Thread.sleep(1000);
//		
//		//navigates to next day
//		driver.findElement(By.cssSelector("#imlBodyMain > div > div:nth-child(1) > div.animate-show.animate-fade-in > div:nth-child(1) > div > div:nth-child(5) > week-calendar > div:nth-child(1) > div.iml-panel-head.bottom-line > table > tbody > tr > td.left-td > table > tbody > tr > td:nth-child(1) > div > button:nth-child(2)")).click();
//
//		
//		//Opens drop down lists of activities
//		driver.findElement(By.cssSelector("#imlBodyMain > div > div:nth-child(1) > div.animate-show.animate-fade-in > div:nth-child(1) > div > div:nth-child(5) > week-calendar > div.iml-panel.iml-panel-1.event-calendar > div.iml-panel-head.bottom-line > div > button")).click();
//		
//		//selects Ritchie individual workout
//		driver.findElement(By.cssSelector("#imlBodyMain > div > div:nth-child(1) > div.animate-show.animate-fade-in > div:nth-child(1) > div > div:nth-child(5) > week-calendar > div.iml-panel.iml-panel-1.event-calendar > div.iml-panel-head.bottom-line > div > ul > li:nth-child(50) > a > label > input[type=checkbox]")).click();
//		

		
		//driver.quit();
		
		System.out.println("Automation Exited Successfully!");

	}
}

