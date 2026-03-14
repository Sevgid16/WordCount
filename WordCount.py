text = input("Metni girin: ")
word_count = {}# sözlük oluşturduk.
for word in text.split():#girilen metni split() fonksiyonuyla ayırarak for döngüsüne koyduk.
    word_count[word] = word_count.get(word, 0) + 1 # Kelimenin sözlükte kaç kez geçtiğini bulmak için get fonksiyonunu kullandık.
print(word_count) #Sözlüğü yazdırdık.
