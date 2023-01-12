chat = open("chat.txt", "r", encoding = "utf8")

def count(name, chat):
    words = chat.read().count(name)

    chat.seek(0)

    return words

data = [["Talat Akbulut", 0], ["Bilal Tonbaz", 0], ["Oğuz Keskin", 0], ["Mert Can Ay", 0], ["Mete Berk Ay", 0], ["Melih Kuas", 0], ["Musa Aydın", 0], ["Alperen Yılmaz", 0], ["Yiğit Tamer Yılmaz", 0], ["Mert Selçuk Tonbaz", 0],
        ["Yakup Baş", 0], ["Ömer Faruk Sağır", 0]]


for a in range (0, 12):

    data[a][1] = count(data[a][0], chat)

    print(data[a][0], "= ", data[a][1])


    




