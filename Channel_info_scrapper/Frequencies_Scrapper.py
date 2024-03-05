import requests
from bs4 import BeautifulSoup
import csv
channel_name=input("Please enter a channel name: ")
formatted_name=channel_name.replace(" ","+")
page=requests.get(f"https://en.kingofsat.net/find.php?question={formatted_name}")
def main(page):
    src=page.content #content in byte code.
    soup=BeautifulSoup(src,"lxml") #convert byte code to the original code in the web page.
    frequencies=soup.find_all("table",{'class':'frq'}) #find_all is to get descendants of a tag
    number_of_frequencies=len(frequencies)
    frequencies_list=[]

    def get_frequencies_info(frequencies):
      for i in range (1,number_of_frequencies):
         info=frequencies[i].find_all("td",{'class':'bld'})
         info1=frequencies[i].find_all("a",{'class':'bld'})
         satellite_name=info1[0].text.strip()
         frequency=info[0].text.strip()
         polarization=info[1].text.strip()
         symbol_rate=info1[3].text + " " + info1[4].text # for ex: 27500 3/4
         frequencies_list.append({"Satellite":satellite_name, "Frequency":frequency, "Polarization":polarization,"Symbol rate":symbol_rate})
    get_frequencies_info(frequencies)
    with open("C:\\Scrapped_Frequencies.csv", 'w', newline='') as csvfile:
    # Create a CSV writer object
     csv_writer = csv.writer(csvfile)
     keys = frequencies_list[0].keys()
     csv_writer.writerow(keys)
     for i in frequencies_list:
        csv_writer.writerow(i.values())

main(page)