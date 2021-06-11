import csv
import os
import os.path

SRC_PATH = ""
DST_PATH = SRC_PATH + ".txt"

FILTER_PATH = './filter.csv'
FILTER = None
FILE_SIZE_LIMIT = 200000000

def read_filter_data():
    global FILTER

    with open(FILTER_PATH, newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        FILTER = list(reader)

def remove_useless_word(name):
    for word in FILTER:
        name = name.replace(word[0], "")

    return name

def write_to_file(file_list):
    with open(DST_PATH, 'w', encoding='UTF-8') as f:
        for text in file_list:
            ext = text.split('.')[-1]
            name = text.replace("."+ext, "")
            name = remove_useless_word(name)
            print(name)
            f.write(name+"\n")

def get_useful_file_list(sub_dir, file_list):
    rst_list = []
    for name in file_list:
        ab_path = sub_dir + "/" + name
        if os.path.getsize(ab_path) > FILE_SIZE_LIMIT:
            #print(" - " + ab_path)
            rst_list.append(name)

    return rst_list

def process():
    rst_list = []
    file_list = os.listdir(SRC_PATH)

    for name in file_list:
        ab_path = SRC_PATH + "/" + name
        #print(ab_path)

        if os.path.isdir(ab_path) is True:
            sub_file_list = os.listdir(ab_path)
            sub_list = get_useful_file_list(ab_path, sub_file_list)
            rst_list = rst_list + sub_list

        else:
            if os.path.getsize(ab_path) > FILE_SIZE_LIMIT:
                rst_list.append(name)

    write_to_file(rst_list)
    print("\nTOTAL FILE COUNT : " + str(len(rst_list)))
    print("REMOVED FILTER WORD : ", FILTER)

def main():
    read_filter_data()
    process()

if __name__ == "__main__":
    main()