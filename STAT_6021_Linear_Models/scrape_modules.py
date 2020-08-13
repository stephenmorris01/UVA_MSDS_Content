from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, InvalidCookieDomainException
from Screenshot import Screenshot_Clipping
from bs4 import BeautifulSoup
import unittest, time, re
import itertools
import pickle
import os 
import pprint as pp
import csv
import json
from PIL import Image
#import glob
#import pdfkit
#bulk of example code produced automatically by Katalon add-on for Chrome

# def pdf_generator(filename_ext):
#     render_test = render_template(filename_ext)
#     config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
#     options = {'enable-local-file-access': None}

#     pdf_test = pdfkit.from_string(render_test, False, configuration=config, options=options)

#     response_test = make_response(pdf_test)
#     response_test.headers['Content-Type'] = 'application/pdf'
#     response_test.headers['content-Disposition'] = 'attachment; filename=' + filename_ext

#     return response_test

class scrape_uva_collab():

    def __init__(self, like="",save_pdf_to=""):
        self.cookiedir = r"C:\Users\kipmc\anaconda3\cookie.pickle"

        if like=="headless":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif save_pdf_to:
        #src: https://chromedriver.chromium.org/getting-started
            settings = {
                "recentDestinations": [{
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": "",
                    }],
                "selectedDestinationId": "Save as PDF",
                "version": 2
                }
            prefs = {"printing.print_preview_sticky_settings.appState": json.dumps(settings), \
                "download.default_directory": save_pdf_to, \
                "download.prompt_for_download": False, \
                "download.directory_upgrade": True, \
                "safebrowsing.enabled": True} ##savefile.
            # options = Options()
            # options.add_experimental_option("prefs", {
            #     "download.default_directory": save_pdf_to,
            #     "download.prompt_for_download": False,
            #     "download.directory_upgrade": True,
            #     "safebrowsing.enabled": True
            #     })
            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_experimental_option('prefs', prefs)
            #chrome_options.add_argument('--kiosk-printing')
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        self.base_url = "https://collab.its.virginia.edu/portal/site/~cam7cu"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.soup = None

    def driver_to_beautifulsoup(self):
        """Transform current driver page source into beautiful soup
        object. Any any time transform this soup into xpath using
        xpath_soup(). """
        source = self.driver.page_source
        #driver.quit()  # remove this line to leave the browser open
        self.soup = BeautifulSoup(source, "html.parser")

    def xpath_soup(self):
        """Transform current self.soup into a functional xpath 
        for selenium to identify and use. """
        #https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf
        #pass in soup object produced by BeautifulSoup

        # example:
            # buttons = driver.find_elements_by_xpath('//button[@data-test-id="seemoretoggle"]');
            # for btn in buttons:
            #     btn.click()
            # html = driver.page_source
            # soup = BS(html, 'html.parser')
            # elem = soup.find(string=re.compile('Tiny House interior'))
            # print(elem)
            # xpath_soup(elem)
            # print(xpath_soup(elem))

        element = self.soup
        components = [] 
        child = element if element.name else element.parent
        for parent in child.parents:
            siblings = parent.find_all(child.name, recursive=False)
            components.append(
                child.name
                if siblings == [child] else
                '%s[%d]' % (child.name, 1 + siblings.index(child))
                )
            child = parent
        components.reverse()
        #returns functional xpath
        return '/%s' % '/'.join(components)

    def save_cookie(self):
        with open(self.cookiedir, 'w') as filehandler:
            #pickle.dump(self.driver.get_cookies(), filehandler)
            filehandler.writelines([self.driver.command_executor._url,"\n"+self.driver.session_id])

    def load_cookie(self):
        if os.path.exists(self.cookiedir):
            #try: 
            with open(self.cookiedir, 'r') as cookiesfile:
                rl = cookiesfile.readlines()
                rl = [x.replace("\n", "") for x in rl]
                self.driver = webdriver.Remote(command_executor=rl[0],desired_capabilities={})
                self.driver.close()
                self.driver.session_id = rl[1]
                # cookies = pickle.load(cookiesfile)
                # for cookie in cookies:
                #     self.driver.add_cookie(cookie)
            #except: # InvalidCookieDomainException:
            #    "Invalid Cookie Domain Exception, must save new one. "
        else:
            f"No cookie at {self.cookiedir}"

    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException: 
            return False
        return True

    def is_alert_present(self):
        try: 
            self.driver.switch_to_alert()
        except NoAlertPresentException: 
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()

    def open_collab_pass_creds(self):
        driver = self.driver
        driver.get("https://collab.its.virginia.edu/portal/site/294dab0f-ccd3-431d-940c-ff9e44bd497c/tool/1ae5d634-ca62-4e94-aeed-cace1fedf87e/ShowPage?returnView=&studentItemId=0&backPath=push&errorMessage=&clearAttr=&source=&title=&sendingPage=213916&newTopLevel=false&postedComment=false&addBefore=&itemId=1591904&path=next&addTool=-1&recheck=&id=")
        input("press enter once creds process complete")

    def extract_sidebar_pagelinks(self,outdir):
        sucsoup = self.soup

        #works to get module header pages
        mod_head_regex = re.compile(r"(Week|Module)\s*(\d+)\:\s*([\w\-\/\d ]*)")
        module_headers = sucsoup.findAll("a", class_="lessons-goto-top-page", text=mod_head_regex)
        final_list = []
        for modhead in module_headers:
            regres = mod_head_regex.findall(modhead.text)[0]
            r1 = str(regres[1].zfill(2))
            r2 = re.sub(r"[\- ]", "_", regres[2])
            r2 = re.sub(r"[^\w\d\_]", "", r2.replace("__", "_"))
            final_list.append([f"{r1}.00_{r2}", modhead['href']])

        sub_head_regex = re.compile(r"^([\d\.]{3,})\:\s*([\w\-\/\d ]*)")
        sub_headers = sucsoup.findAll("a", text=sub_head_regex)
        for subhead in sub_headers:
            regres = sub_head_regex.findall(subhead.text)
            if regres:
                regres = regres[0]
                r1 = regres[0].split(".")
                r1 = ".".join([x.zfill(2) for x in r1])
                #r1 = str(regres[1])
                r2 = re.sub(r"[\- ]", "_", regres[1])
                r2 = re.sub(r"[^\w\d\_]", "", r2.replace("__", "_"))
                final_list.append([f"{r1}_{r2}", "https://collab.its.virginia.edu" +subhead['href']])
        
        with open(outdir, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(final_list)


    def print_single_pages(self, page_url_src, print_to_dir):
        src_urls = []

        with open(page_url_src, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj)
            # Pass reader object to list() to get a list of lists
            src_urls = list(csv_reader)[1:]
        #print(src_urls)
        for pg in src_urls:
            self.driver.get(pg[1])
            filename_base = print_to_dir + "\\" + pg[0]
            ob=Screenshot_Clipping.Screenshot()
            ob.full_Screenshot(self.driver, save_path=print_to_dir, image_name=f"{pg[0]}.png")
            image1 = Image.open(f"{filename_base}.png")
            width, height = image1.size
            cropped = image1.crop((220, 104, width, height-42))
            im1 = cropped.convert('RGB')
            im1.save(f"{filename_base}.pdf")
            os.remove(f"{filename_base}.png")
            ##ATTEMPT #3 - did not actually resize screen
            # #the element with longest height on page
            # ele = self.driver.find_element("xpath", '//div[@class="Mrphs-portalWrapper"]')
            # total_height = ele.size["height"]+1000

            # self.driver.set_window_size(1920, total_height)      #the trick
            # time.sleep(1)
            # self.driver.save_screenshot(f"{filename_base}.png")


            ##ATTEMPT #2, PRODUCES GARBAGE PDFs
            # self.driver.find_element_by_id("print-view").click()
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            # #driver = webdriver.PhantomJS()
            # lessonpage_path = print_to_dir + "\\" + "Lesson Page.html"
            # 
            # with open(lessonpage_path, "w", encoding="utf-8") as f:
            #     f.write(self.driver.page_source)
            # options = {'enable-local-file-access': None}
            # try:
            #     pdfkit.from_file(lessonpage_path, filename_base + ".pdf", options=options)
            # except: 
            #     pass



            ##ATTEMPT 1, would not print to PDF
            #self.driver.title = pg[0]
            #self.driver.execute_script('window.print();')
            #self.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'w')
            #LatestFile = max(glob.glob(print_to_dir + "*"),key=os.path.getctime)
            #os.rename(LatestFile, pg[0] + ".pdf")
            #self.driver.close()


if __name__ == "__main__":
    #unittest.main(
    save_pdfs = r"D:\\Git\\UVA_MSDS_Content\\STAT_6021_Linear_Models\\PDFs"
    suc = scrape_uva_collab(like="headless")
    suc.load_cookie()
    #suc.open_collab_pass_creds()
    #suc.save_cookie()
    #suc.driver_to_beautifulsoup()
    outdir = r"D:\Git\UVA_MSDS_Content\STAT_6021_Linear_Models\statpages.csv"
    #suc.extract_sidebar_pagelinks(outdir)
    suc.print_single_pages(outdir,save_pdfs)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# cookiedir = r"C:\Users\kipmc\anaconda3\cookie.pickle"
# driver.get(r'https://collab.its.virginia.edu/portal/site/294dab0f-ccd3-431d-940c-ff9e44bd497c/')
# load_cookie(driver, cookiedir)
# out = input("have you entered your creds yet?")
# #time.sleep(5) # Let the user actually see something!
# # search_box = driver.find_element_by_name('q')
# # search_box.send_keys('ChromeDriver')
# # search_box.submit()
# # time.sleep(5) # Let the user actually see something!

# #individual module buttons
# # //*[@id="toolMenu"]/ul/li[10]/a
# # //*[@id="toolMenu"]/ul/li[12]/a
# # //*[@id="toolMenu"]/ul/li[14]/a
# # //*[@id="toolMenu"]/ul/li[12]/span/a[2]
# # <a class="Mrphs-toolsNav__menuitem--link " href="javascript:void(0);" title="Expand to show subpages" aria-controls="lessonsSubMenu_79431c75-5c2f-4124-8b4a-32cc855a24df" aria-expanded="false" aria-hidden="false">
# # driver.find_elements(By.XPATH, '//*[@id="toolMenu"]/ul/li[]')
# # title="Click to open top-level page" class="lessons-goto-top-page"
# top_pages = driver.find_elements_by_class_name("lessons-goto-top-page")
# print(top_pages)

# text_out = []

# for module in top_pages:
#     module.click
#     page_content = driver.find_elements_by_class_name("uva-lessons-container")
#     text_out.append(page_content.text)
#     module_links = []
#     page_links = module.find_elements_by_class_name("itemlink")
#     for l in page_links:
#         module_links.append(l.get_attribute('href'))
#         print(module_links)


# save_cookie(driver, cookiedir)
# driver.quit()
