from tkinter import*

window = Tk()
window.title('веселка')
window.geometry('300x500+500+50') #ширина, висота, x,y

clear=PhotoImage(file='rainbow.png').subsample(4)
fon=Label(image=clear)
fon.pack()


txt=Label(text='назва укр кольорів',font=('Arial', 14,'bold'))#текст
txt.pack() #показати у вікні/розмістити
ans=Entry(width=25,font=('Arial', 12,'italic')) #однорядкове поле
ans.pack()
b1=Button(bg='red',width=32)
b1.pack()
b2=Button(bg='orange',width=32)
b2.pack()
b3=Button(bg='yellow',width=32)
b3.pack()
b4=Button(bg='green',width=32)
b4.pack()
b5=Button(bg='blue',width=32)
b5.pack()
b6=Button(bg='darkblue',width=32)
b6.pack()
b1=Button(bg='purple',width=32)
b1.pack()

mainloop()
