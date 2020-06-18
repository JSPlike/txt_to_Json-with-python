import json
from collections import OrderedDict

file_data = OrderedDict()

# buildYear,dealYear,dealMonth,dealDay,dong,dealAmount,AptName,area,code,floor,jibun
## 파일 읽기 and 쓰기
with open('input.txt', 'r') as file:
    for content in file:
        con = str(content)
        con = con.split(',')
        #
        con1 = con[0]
        con2 = con[1]
        con3 = con[2]
        con4 = con[3]

        con5 = con[4]
        con5 = con5[1:]

        tmp_str1 = con[5]
        tmp_str1 = tmp_str1[4:]

        tmp_str2 = con[6]
        tmp_str2 = tmp_str2[:3]
        new_str = tmp_str1 + "," + tmp_str2
        con6 = new_str

        con7 = con[7]
        con8 = con[8]
        con9 = con[9]
        con10 = con[10]
        con11 = con[11]

        # 데이터 가공
        file_data["buildYear"] = con1
        file_data["dealYear"] = con2
        file_data["dealMonth"] = con3
        file_data["dealDay"] = con4
        file_data["dong"] = con5
        file_data["dealAmount"] = con6
        file_data["aptName"] = con7
        file_data["area"] = con8
        file_data["code"] = con9
        file_data["floor"] = con10
        file_data["jibun"] = con11
        # output to JSON

        tmp = json.dumps(file_data, ensure_ascii=False, indent="\t")
        print(tmp)
        result = ""
        result += (tmp + "," + "\t")

        #print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    print("result: ")
    print(result)

    # with open('output.json', 'w', encoding="utf-8") as make_file:
    #     json.dump(tmp, make_file, ensure_ascii=False, indent="\t")


