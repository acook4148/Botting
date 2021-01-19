#! python3
#Written by: --Khephren Andrews
import os
import time
import shutil
import tkinter
import os.path
from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import tkinter as tk

#creating the color gradient
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f1 = GradientFrame(self, borderwidth=1, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="#E0FFFF", color2="#40E0D0", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

def theRun(entered_text):
    if len(entered_text) > 0:
        main(entered_text)
    else:
        print("Invalid Input")

def quitter(br):
    if br==1:
        quit()

def addBR(br):
    br = 1
    quitter(br)

def click():
    entered_text = textentry.get()
    entered_text.replace("\\", "/")
    theRun(entered_text)
def click2():
    br = 0
    addBR(br)
    root.destroy()

#creating the window
root = tk.Tk()
color = Example(root).pack(fill="both", expand=True)
#modify window
root.title("Start Screen")
root.geometry("800x500")
#Content
#top icon
logo = PhotoImage(file = "/Users/khephren/Desktop/Projects/WebScrape_Package/Source_Code/dcg.png") 
logoPic = Label(root, image=logo, bg = "black")
logoPic.place(anchor = NW, relheight = 0.33, relwidth = 1)
#text entry
textentry = Entry(root, width=100, bg="white")
textentry.place(relx = 0.1, rely = 0.76)
#text
instr = "Welcome to the American FactFinder Web Scraper. This application will automatically open, scan, and download all ACS 5-year estimate data in the CSV and SAS formats. Documentation/screenshots on the program functionality and installation can be found in the word document in the “Installation Instructions” folder. This program cannot run without the chrome web driver (see documentation). Additionally, this program needs the path of this program file folder in order to run. To correctly copy the path, open your PC’s file explorer and find the location of this “WebScrape_Package” folder. Double click on the folder to see the program files. Next, double click on the “ACS Data” folder. Finally, locate the file path bar at the top and click in the box to the right of the file icons. You can now copy the highlighted file path into the text box below. For detailed instructions with screenshots, see documentation."
Label(root, text = "Path:", font = ("Courier 15 bold"), bg = "#E0FFFF").place(relx = 0.01, rely = 0.75)
Label(root, text = instr, font = ("Georgia 11"), bg = "#AFEEEE", wraplength = 750, fg = "black").place(relx = 0.03, rely = 0.37)
#submit
Button(root, text = "RUN", width = 6, command=click, activebackground = "black", activeforeground = "white").place(relx = 0.41, rely = 0.85)
#cancel
Button(root, text = "QUIT", width = 6, command=click2, activebackground = "black", activeforeground = "white").place(relx = 0.53, rely = 0.85)
#footer
Label(root, text = "DOH | OHE | 2019").pack()
#closing code
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        quit()

root.protocol("WM_DELETE_WINDOW", on_closing)

def main(entered_text):
    def filter1(element):
        wait = WebDriverWait(driver, 20)
        el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="resulttable"]/table/tbody[2]/tr['+ str(element) +']/td[3]/div')))
        name = el.text
        value = name.find("PUMS")
        return value

    def filter2(element):
        wait = WebDriverWait(driver, 20)
        el2=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="resulttable"]/table/tbody[2]/tr['+ str(element) +']/td[4]/div')))
        name2 = el2.text
        value2 = name2.find("5-year")
        return value2
        
    def filter3(element):
        wait = WebDriverWait(driver, 20)
        el2=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="resulttable"]/table/tbody[2]/tr['+ str(element) +']/td[4]/div')))
        name2 = el2.text
        x_count = 9
        value3 = name2.find("2011")
        if value3 == -1:
            value3 = name2.find("2010")
        for element in range(0,10):
            if value3 == -1 :
                value3 = name2.find("200" + str(x_count))
            x_count = x_count-1
        return value3

    chrome_options = webdriver.ChromeOptions() 
    prefs = {'download.default_directory' : entered_text}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml")
    driver.find_element_by_xpath('//a[contains(text(), "Download Center")]').click()

    wait = WebDriverWait(driver, 20)
    el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="1"]')))
    el.click()

    wait = WebDriverWait(driver, 20)
    el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="nextButton"]')))
    el.click()

    wait = WebDriverWait(driver, 20)
    el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="controls_container"]/div/div[3]/div[1]/div/div/div/div/div[1]')))
    el.click()

    wait = WebDriverWait(driver, 20)
    el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="controls_container"]/div/div[3]/div[1]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr/td[3]/span/span')))
    el.click()

    wait = WebDriverWait(driver, 20)
    el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="nextButton"]')))
    el.click()

    file_tit = entered_text + '/FilesDownloaded.txt'
    saveFile = open(file_tit, "w")
    list_count = 0

        
    def findFile(type1_1, type1_2, theOneToUse, counter, x1, x2, x3, element, error_count, list_count):
        if type1_1 != -1:
            if os.path.exists(entered_text + "/" + theOneToUse + ".zip") == True and os.path.exists(entered_text + "/csv_pdc.zip") == True:
                print("here 1")
                os.remove(entered_text + "/" + theOneToUse + ".zip")
                os.rename(entered_text + "/csv_pdc.zip", entered_text + "/" + theOneToUse + ".zip")
            elif os.path.exists(entered_text + "/csv_pdc.zip") == True:
                os.rename(entered_text + "/csv_pdc.zip", entered_text + "/" + theOneToUse + ".zip")
                print("yay")
            elif counter > 20:
                print("Error File Not Found")
                error_count += 1
                print("here 3")
                print(error_count)
                if error_count==3:
                    print("exiting")
                    saveFile.write("  --This file did not download due to either this PC's browser permissions or internet connection. Either re-run the application or download manually." + "\n")
                else:
                    print("going again")
                    checker(x1, x2, x3, element, error_count, list_count)
            else:
                time.sleep(1)
                counter += 1
                print("here 2")
                print(counter)
                findFile(type1_1, type1_2, theOneToUse, counter, x1, x2, x3, element, error_count, list_count)
        elif type1_2 != -1:
            if os.path.exists(entered_text + "/" + theOneToUse + ".zip") == True and os.path.exists(entered_text + "/unix_pdc.zip") == True:
                print("here 1")
                os.remove(entered_text + "/" + theOneToUse + ".zip")
                os.rename(entered_text + "/unix_pdc.zip", entered_text + "/" + theOneToUse + ".zip")
            elif os.path.exists(entered_text + "/unix_pdc.zip") == True:
                os.rename(entered_text + "/unix_pdc.zip", entered_text + "/" + theOneToUse + ".zip")
                print("yay")
            elif counter > 20:
                print("Error File Not Found")
                error_count += 1
                print("here 3")
                print(error_count)
                if error_count==3:
                    print("exiting")
                    saveFile.write("  --This file did not download due to either this PC's browser permissions or internet connection. Either re-run the application or download manually." + "\n")
                else:
                    print("going again")
                    checker(x1, x2, x3, element, error_count, list_count)
            else:
                time.sleep(1)
                counter += 1
                print("here 2")
                print(counter)
                findFile(type1_1, type1_2, theOneToUse, counter, x1, x2, x3, element, error_count, list_count)


    def finish():
        saveFile.close()
        driver.close()
        exit()

    def next(list_count):
        try:
            el=driver.find_element_by_xpath('//*[@id="controls_container"]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]//*[@id="yui-pg0-0-next-link"]')
            el.click()
            collect(list_count)
        except NoSuchElementException:
            print("Complete")
            finish()

    def collect(list_count):
        for element in range(1, 100):  
            print(list_count)
            time.sleep(1.5)
            try:
                elem = driver.find_element_by_xpath('//*[@id="resulttable"]/table/tbody[2]/tr['+ str(element) +']/td[2]/div/a')
            except NoSuchElementException:
                next(list_count)
            x1 = filter1(element)
            x2 = filter2(element)
            x3 = filter3(element)
            error_count = 0
            checker(x1, x2, x3, element, error_count, list_count)
            
    def checker(x1, x2, x3, element, error_count, list_count):
        if x1 != -1 and x2 != -1 and x3 == -1:
            wait = WebDriverWait(driver, 20)
            el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="resulttable"]/table/tbody[2]/tr['+ str(element) +']/td[2]/div/a')))
            theOneToUse = el.text
            if error_count == 0:
                saveFile.write(str(list_count + 1) + ". " + str(el.text) + "\n")
                list_count += 1
                print(list_count)
            el.click()
            print(list_count)
            if os.path.exists(entered_text + "/csv_pdc.zip") == True:
                os.remove(entered_text + "/csv_pdc.zip")
            elif os.path.exists(entered_text + "/unix_pdc.zip") == True:
                os.remove(entered_text + "/unix_pdc.zip")
            wait = WebDriverWait(driver, 20)
            el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="documentDisplay"]/div/table/tbody/tr[10]/td[1]/a')))
            el.click()
            wait = WebDriverWait(driver, 20)
            el=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="steps"]/div[3]')))
            el.click()
            time.sleep(2)
            type1_1 = theOneToUse.find("CSV")
            type1_2 = theOneToUse.find("SAS")
            findFile(type1_1, type1_2, theOneToUse, 0, x1, x2, x3, element, error_count, list_count)

    collect(list_count)

