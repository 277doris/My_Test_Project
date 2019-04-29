driver.get("https://h5.juxinda360.com/login");
		driver.findElement(By.cssSelector("#tab1 > div > div:nth-child(1) > div.weui-cell__bd > p > input"))
				.sendKeys("17090804521");
		driver.findElement(
				By.cssSelector("#tab1 > div > div:nth-child(2) > div.weui-cell__bd > p > input[type='password']"))
				.sendKeys("abc123");
		driver.findElement(By.xpath("//*[@id='showModel']")).click();
		driver.findElement(By.xpath("//*[@id='app']/div/div/div[2]/div/ul/li[2]/a/span")).click();
		Thread.sleep(5000);
		driver.quit();