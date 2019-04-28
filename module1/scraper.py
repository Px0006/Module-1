import urllib.request as request
from bs4 import BeautifulSoup
import string, re, pprint, unicodedata
import csv, os, datetime

class SecFilings():
    def __init__(self,stock_symbol,start_row=1, end_row=10,sort=('date_filed','ascending'), url_root="http://secfilings.nasdaq.com/"):
        self.url_root = url_root
        self._get = self.parser(stock_symbol,start_row,end_row,sort)
        self.export = self.export()

    def __getitem__(self,filing_id):
        return self._get[filing_id]
    
    def __str__(self):
        return str(self.pretty_print(self._get))
    
    def __repr__(self):
        return str(self._get)
    
    def pretty_print(self, x):
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pprint(x)
    
    def build_query(self, stock_symbol, start_row, end_row, sort=('date_filed', 'descending')):
        #Process the inputted arguments used for our query url
        asc_desc = {'ascending':'A', 'descending':'D'}
        sort_ids = {'form_type':'104', 'date_filed':'101', 'period':'105'}
        sort_by = sort_ids[str(sort[0])]
        sort_direction = asc_desc[str(sort[1])]

        #build minimal query to get get total number of records
        url_template = str("{ur}filingsCompany.asp?SortBy={sb}&{sd}=D&StartRow={sr}&EndRow={er}&selected={ss}&SchValue=0000320193")
        url = url_template.format(ss=stock_symbol, ur=self.url_root, sr=1, er=1, sb=sort_by, sd=sort_direction)
        pre_results = request.urlopen(url)

        #Display the url for our query just so we can make sure everything is on track.
        print('Accessing url: ' + url + '...')
        print('Stock symbol: ' + stock_symbol)
        
        #Download the results for the first stage of the query
        print('Searching...')

        #Make soup, and parse outter table
        soup = BeautifulSoup(pre_results.read(), from_encoding="iso-8859-1")
        meta_table = soup.find_all("table",attrs={"class":"body1"})[2] #This outter level of the table contains the "Records X - Y of Z" statement, which is useful data to our parser function.

        meta_row = meta_table.find_all("tr")
        #print(meta_row)
        
        for record in meta_row:
            meta_statement = record.find("td", attrs={"align":"center"}).text
            count = re.search(r"(\bRecords )(\d+)( - )(\d+)( of )(\d+)", str(meta_statement)).group(6) #Parse "Records X - Y of Z"
            self.count = int(count)
            print(str(count) + " records found.")

        query = url_template.format(ss=stock_symbol, ur=self.url_root, sr=start_row, er=self.count, sb=sort_by, sd=sort_direction)
        self.query = query
        return query

    def parser(self,stock_symbol,start_row,end_row,sort):
        url = self.build_query(stock_symbol,start_row,end_row,sort)
        print('Downloading...')
        results = request.urlopen(url)
        soup = BeautifulSoup(results.read(), from_encoding="iso-8859-1")

        print('Parsing...')
        #Find the table
        table = soup.find_all("table",attrs={"class":"body1"})[3] #Tables appear to be nested for formatting purposes on this page. [3] selects the 3rd level of nested table, which contains our data.

        #Returns a list of rows in our main table
        rows = table.find_all("tr")

        #rows[0] contains some directions that aren't useful to us. row[1] contains headings. All other rows[2:] contain the actual data you want to parse.
        data_rows = BeautifulSoup(str(rows[2:])).find_all('tr')
        heading_row = BeautifulSoup(str(rows[1])).find_all('td')
           
        #Add two list comprehensions together to create list of headers. Two are needed due to different formatting on headers.
        headings = [heading.find('b').text for heading in heading_row if heading.find('b') and not heading.find('a')] + [heading.find('a').text for heading in heading_row if heading.find('a')]
        headings.append('Owner/Filer')  #additional heading
        headings.append('Filing Id')    #another additional heading!
        self.headings = headings

        row_list = list()
        self.list = row_list

        row_dict = dict()
        self.dict = row_dict

        #Open a for loop that will take us down to the individual-record level.
        for record in data_rows:
            row = dict()

            #Start parsing the html tags and adding them to row{} dict. 
            company_name = record.find('b')
            if company_name:
                company_name = unicodedata.normalize("NFKD", company_name.text).strip()
                row[headings[0]] = str(company_name)   #Should be 'Company Name'

                form_type = record.find('a')
                if form_type:
                    form_type = unicodedata.normalize("NFKD", form_type.text).strip()
                    row[headings[2]] = str(form_type)   #Should be 'Form Type'

                period = record.find('td', attrs={"class":"secperiod"})
                if period:
                    period = unicodedata.normalize("NFKD", period.text).strip()
                    row[headings[4]] = str(period)

                filed = record.find('td', attrs={"class":"secreceived"})
                if filed:
                    filed = unicodedata.normalize("NFKD", filed.text).strip()
                    row[headings[3]] = str(filed)

                #Parse the filer name. Tricker 
                filer = record.find('font', attrs={"class":"smallText"})
                if filer:
                    filer = unicodedata.normalize("NFKD", filer.text)
                    if 'Reporting' in filer:
                        filer = filer.replace('Reporting Owner: ','')
                    elif 'Filed' in filer:
                        filer = filer.replace('Filed As: ','')
                    elif 'Filer' in filer:
                        filer = filer.replace('Filer: ','')
                    
                    row['Owner/Filer'] =  re.sub(r'[\t\n\r]', '', filer)


                #Parse the list of urls from the href tags.
                url_list = [link.get('href') for link in record.find_all('a', href=True)]
                url_dict = dict()
                #remove duplciates by using set() as an intermediary type
                url_list = list(set(url_list))

                #append root directory for any urls that were parsed as a relative path
                for n,url in enumerate(url_list):                
                    if self.url_root not in url:
                        url_list[n] = str(self.url_root) + str(url)

                #build dictionary of urls based on file type
                if url_list:
                    for url in url_list:
                        if 'html' in url:
                            url_dict['html'] = url
                        if 'pdf' in url:
                            url_dict['pdf'] = url
                        if 'xls' in url:
                            url_dict['xls'] = url
                        if 'orig' in url:
                            url_dict['original'] = url
                        if 'rtf' in url:
                            url_dict['rtf'] = url
    
                    row[headings[1]] = url_dict
    
                #Parse the filing_id from the first url available using regex. Not available in any other location.
                filing_id = re.search(r"(FilingID=)(\d+)", url_list[0]).group(2)
                row['Filing Id'] = filing_id
    
                #Add our newly created row to our list-of-dicts, aka row_list[]
                row_list.append(row)
    
        for row in row_list:
            row_dict[row['Filing Id']] = row
        print('Parsing completed.')

        if self.export == True:
            export(self.list)

        return row_dict

    def export(self,directory="~"):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename=str('\SEC_Filings({now}).csv').format(now=now)
        location = str(directory + filename)
        print(location)

        with open(str(filename), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headings)

            writer.writeheader()
            for record in self.list:
                writer.writerow(record)
