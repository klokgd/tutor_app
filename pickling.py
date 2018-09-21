# имя файла, в котором мы сохраним объект
shoplistfile ='shoplist.txt'
# список покупок
shoplist = input('Введи текст: ') # Запись в файл

f=open(shoplistfile,'a')

f.write(shoplist)

# помещаем объект в файл
f.close()
