import re

#Kullanacagimiz text dosyasini projemize okutarak bir degiskene aktardik.
#"r" parametresi ile sadece okuma islemi yapacagimizi belirttik.
tweetsData = open("tweets.txt","r")

#Daha sonra yazdirma islemi icin Kullanacagimiz text dosyasini tanittik
#"w" parametresi ile sadece yazdirma islemi yapacagimizi belirttik.
newData = open("newRegularTweets.txt","w")

#Daha sonra 5 harfli kelimeleri, icinde z gecen kelimeleri ve sayilari yazdiracagimiz text dosyasini tanittik
#"w" parametresi ile sadece yazdirma islemi yapacagimizi belirttik.
excText = open("ozelKelimeler.txt","w")


kontrol = 0                                   #12. tweeti bulabilmek icin bir kontrol degiskeni tanimladik

def duzenliIfadelerFonk(line):
        line = re.sub('@','',line)            #mentionlari temizliyoruz.
        line = re.sub('#','',line)            #hashtag  temizliyoruz.
        line = re.sub('_',' ',line)           #alt tireleri temizliyoruz.
        line = re.sub('[^\w\s]','',line)      #noktalama isaretlerini temizliyoruz.
        line = line.lower()                   #tum harfleri kuculterek buyuk harflerden kurtuluyoruz.
        line = re.sub('  +',' ',line)         #iki kelime arasindaki fazla bosluklari temizliyoruz.
        newData.write(line)                   #islemlerimizi yaptiktan sonra yeni text dosyamiza kaydediyoruz
        pass


def tirnakBul(line):
    regex = r"\".+\""                         #Tirnak icindeki ifadeyi bulacak duzenli ifade

    eslesenIfade = re.finditer(regex, line, re.MULTILINE)

    #Bir for dongusu ile tirnakin basindan sonuna kadar tarayarak ekrana yazdiriyoruz.
    for index, karakter in enumerate(eslesenIfade, start=1):
        print ("Tirnak icindeki ifade : {match}".format(matchNum = index, start = karakter.start(), end = karakter.end(), match = karakter.group()))
        pass
    pass


def ozelKelimelerFonk(line):
    # 5 harfli kelimeleri, icinde z gecen kelimeleri ve sayilari bulan duzenli ifade.
    line = re.findall(r'\b\w{5}\b|[0-9]+|[a-zA-Z]*[zZ][a-zA-Z]*',line)

    #satir satir for dongusune gonderdigimiz line icinde de for dongusu kullanarak kelime kelime inceliyoruz.
    for word in line:
        excText.write(word + "\n")
        pass
    pass

def repeatLetter(line):
    line = re.sub(r'(.+?)\1+', r'\1', line)                 #kelimenin icinde tekrar eden harfleri silen duzenli ifade
    print("Tekrar eden harfler duzeltildi : "+line)         #ve o satiri bastan yazdirdik


for line in tweetsData:
    kontrol += 1                              #12. satirdaki ifadeyi yakalayabilmek icin kontrol degiskenimizi artiriyoruz
    ozelKelimelerFonk(line)

    #3. satirdaki birlesik kelimeleri ayiracagiz
    if kontrol == 3 or kontrol == 13:
        line =re.sub('([A-Z][a-z]+)', r' \1',re.sub('([A-Z]+)',r'\1',line)) #birlesik kelimeleri ayirdigimiz duzenli ifade.
        line = re.sub(' +',' ',line)                                        #iki kelime arasindaki fazla bosluklari temizliyoruz.
        print("Birlesik kelimeler ayrildi :" + line)                        #ayrica gorelim diye ekrana bastirdik

    #12. satirdaki tirnakli ifadeye ulasmak icin bir if
    if kontrol == 12:
        tirnakBul(line)
        pass
    if kontrol == 6 or kontrol == 17 or kontrol == 15 or kontrol == 13:
        repeatLetter(line)
        pass

    #her dongunun sonunda satirimizi duzenli ifadelere gonderip oradaki islemleri uygulatip yeni dosyamiza yazdiriyoruz.
    duzenliIfadelerFonk(line)
