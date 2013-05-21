import csv
import string

alphabet = string.uppercase[0:26]
with open("D:/MSIA/Courses/Spring13/MSIA 431/Lab/Lab6/NASDAQ/nasdaq.csv", "w") as outfile:
    for i in range(26):
        write = csv.writer(outfile)
        with open('D:/MSIA/Courses/Spring13/MSIA 431/Lab/Lab6/NASDAQ/NASDAQ_daily_prices_'+alphabet[i]+'.csv') as infile:
            read = csv.reader(infile)
            title = read.next()
            for row in read:
                write.writerow(row)