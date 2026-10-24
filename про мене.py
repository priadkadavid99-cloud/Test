from tkinter import *

window = Tk()
window.title('знайомство')
window.geometry('480x300+500+0') #ширина, висота, x,y
window.config(bg='#8e3aa1')

clear=PhotoImage(file='rainbow.png').subsample(1)
fon=Label(image=clear)
fon.place(x=0,y=0)

ok1=Button(text='хто я',bg='red',fg='white',font=('Arial',10,'bold'), width=20)
ok1.place(x=10,y=100)
ok2=Button(text='моє хобі',bg='red',fg='white',font=('Arial',10,'bold'), width=20)
ok2.place(x=150,y=100)
ok3=Button(text='цікавий факт',bg='red',fg='white',font=('Arial',10,'bold'), width=20)
ok3.place(x=300,y=100)

mainloop()
