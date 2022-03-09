import random

def database():                                             # 這個才有title
    fon = open("eat.txt", "w")
    title=["店名", "種類", "價錢", "距離(分鐘)"]
    fon.write("\t".join(title) + "\n")
    fon.close()
    keyin()


def check():                                                # 檢查是否已經存在eat.txt之中
    A = []
    fin = open("eat.txt")
    line = fin.readline().rstrip()
    while(line):
        l = line.split()
        A.append(l[0])
        line = fin.readline().rstrip()
    return A
    fin.close()


def keyin():
    c = check()
    fon = open("eat.txt", "a")                              # 續寫之前檔案

    while(1):
        print("任何時間想離開時，請輸入(E)xit")
    
        name = input("請輸入店名 :")
        if(name=="E"):
            print("歡迎下次使用~~~~")
            break
        while(name):                                        
            if(name in c):
                print("已經輸入過了喔！")
                name = input("請再次輸入店名 :")
                if(name=="E"):
                    print("歡迎下次使用~~~~")
                    return
            else:        
                break
            
    
        print("種類如下：麵, 飯, 咖哩, 水餃, 義大利麵, 沙拉, 小吃(肚子不太餓的食物), 壽司, 速食, 鍋, pizza, 雜...")
        what = input("請輸入種類(ex:麵) :")
        if(what=="E"):
            print("歡迎下次使用~~~~")
            break
        
        print("價錢為大略值, 請想想在這家店大概都吃多少錢")
        money = input("請輸入價錢(ex:100) :")
        if(money=="E"):
            print("歡迎下次使用~~~~")
            break
        while(money):                                           # 判斷是不是數字                                        
            if(money.isdigit()==False):
                print("請輸入數字喔！")
                money = input("請再次輸入價錢(ex:100) :")
                if(money=="E"):
                    print("歡迎下次使用~~~~")
                    return
            else:        
                break
    
        print("自行判斷此店家與你家所需的時間(單位：分鐘)")
        dis = input("請輸入到這家所花的時間(ex:5) :")
        if(dis=="E"):
            print("歡迎下次使用~~~~")
            break
        while(dis):                                           # 判斷是不是數字                                        
            if(dis.isdigit()==False):
                print("請輸入數字喔！")
                dis = input("請再次輸入到這家所花的時間(ex:5) :")
                if(dis=="E"):
                    print("歡迎下次使用~~~~")
                    return
            else:        
                break

        a = [name, what, money, dis]
        fon.write("\t".join(a) + "\n")
        
    fon.close()

def Eat():
# ---輸入條件---
    whati = input("種類(ex.麵、飯、水餃、咖哩、壽司、義大利麵、沙拉、小吃、速食、鍋、pizza、雜..., 都可以則輸入\"無\")：")            
    moneyi = input("價錢(可接受最高價，請輸入整數,都可以則輸入0)：")
    while(moneyi):                                                                                   
            if(moneyi.isdigit()==False):
                print("請輸入數字喔！")
                moneyi = input("請再次輸入價錢(可接受最高價，請輸入整數,都可以則輸入0)：")
            else:        
                break
    disi = input("距離(可接受最久分鐘數，請輸入整數,都可以則輸入0)：")
    while(disi):                                                                                   
            if(disi.isdigit()==False):
                print("請輸入數字喔！")
                disi = input("請再次輸入距離(可接受最久分鐘數，請輸入整數,都可以則輸入0)：")
            else:        
                break
    disi = int(disi)
    moneyi = int(moneyi)
# ---從資料庫中篩選條件---
    dis = []                         
    money = []
    what = []
    fin = open("eat.txt")
    line = fin.readline().rstrip()
    line = fin.readline().rstrip()
    while(line):
        l = line.split("\t")
        if(whati == "無"):            # 種類都可
            what.append(l[0])
        if(l[1] == whati):            # 種類符合
            what.append(l[0])
        if(moneyi == 0):              # 價錢都可
            money.append(l[0])
        if(int(l[2]) <= moneyi):      # 價錢符合
            money.append(l[0])
        if(disi == 0):                # 距離都可
            dis.append(l[0])
        if(int(l[3]) <= disi):        # 距離符合
            dis.append(l[0]) 
        line = fin.readline().rstrip()
    fin.close()
   
# ---符合全部條件的店家---
    pool = set(what) & set(money) & set(dis)
    pool = list(pool)
    
# ---隨機抽取---
    if(len(pool) == 0):
        print("抱歉沒有符合的選項")
    else:
        print(random.choice(pool))



def intro():
    print("若沒有\"eat.txt\"，請輸入：database()；"+ "\n" + "若已經有\"eat.txt\"，請輸入keyin()；" + "\n" + "若想要隨機抽樣，請輸入Eat()。")



intro()











