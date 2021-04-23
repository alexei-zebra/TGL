chars = [" ","а","б","в","г","д","е","ж","з","и",
        "й","к","л","м","н","о","п","р","с","т",
        "у","ф","х","ц",'ч','ш','щ','ъ','ы','ь',
        'э','ю','я','А','Б','В','Г','Д','Е','Ж',
        'З','И','Й','К','Л','М','Н','О','П','Р',
        'С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ',
        'Ы','Ь','Э','Ю','Я','a','b','c','d','e',
        'f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y',
        'z','A','B','C','D','E','F','G','H','I',
        'J','K','L','M','N','O','P','Q','R','S',
        'T','U','V','W','X','Y','Z',".",",","!",
        "@","№","#",";","$","%",":","^","?","&",
        "*","(",")","-","_","+","=","~","1","2",
        "3","4","5","6","7","8","9","0"]

    
def write(input_char): #write('=')
    num_char = chars.index(input_char)
    print(num_char)
    with open('font', 'r') as fontbit:
        font = fontbit.readlines()
        for i in range(8):
            print(font[i + (8 * num_char)], end='')

write('t')

class Lable():
    def __init__(self, screen_array):
        self.screen_array = screen_array
    
    def lable(self, text='text', x=0, y=0):
            text = list(text)
            i = 0
            j = 0
            for num_char_text in range(len(text)-1):
                i += 1
                if text[i] == '\n'
                    j += 1
                    i = 0
                self.screen_array[i + x][j + y] = text[num_char_text]
