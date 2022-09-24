import csv


def main():
    with open('main_202209241510.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            dat = row.split(",")
            id = dat[0]
            POS = dat[1]
            led_id = dat[2]
            type = dat[3]
            value = dat[4]
            pcs = dat[5]
            lcsc = dat[6]


if __name__ == '__main__':
    main()

