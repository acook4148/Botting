package newPackage;


import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;

public class MyClass {

	public static void main(String[] args) {

		System.out.println("EdgeDriver execution on macOS!!");
		
		System.setProperty("webdriver.edge.driver", "edgedriver_mac64/msedgedriver");
		
		WebDriver driver = new EdgeDriver();
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		
		driver.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		
		//loads url
		driver.get("https://www.google.com/");

		//enters search query in google search bar
		driver.findElement(By.name("q")).sendKeys("BrowserStack Guide");
		
		//finds and clicks search button
		WebElement searchIcon = driver.findElement(By.name("btnK"));
		searchIcon.click();
		
		driver.quit();
		
		System.out.println("Execution complete on macOS");

	}

}

