import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
from sklearn import linear_model as LR

df1 = pd.read_csv('rohit_sharma.csv')
df2 = pd.read_csv('k_l_rahul.csv')
df3 = pd.read_csv('virat_kolhi.csv')
df4 = pd.read_csv('rishabh_pant.csv')
df5 = pd.read_csv('dinesh_karthik.csv')
df6 = pd.read_csv('hardik_pandya.csv')
df7 = pd.read_csv('m_s_dhoni.csv')
df8 = pd.read_csv('sir_ravendra_jadeja.csv')
df9 = pd.read_csv('b_kumar.csv')
df10 = pd.read_csv('y_chahal.csv')
df11 = pd.read_csv('j_bumrah.csv')
length = len(df1)


class players:
    def printDF(self,num):
        if (num == 1):
            print('The Data frame of Rohit sharma is \n', df1)
        elif(num == 2):
            print('The Data frame of K.L.Rahul is \n', df2)
        elif(num == 3):
            print('The Data frame of Virat Kolhi is \n', df3)
        elif(num == 4):
            print('The Data frame of Rishabh Pant is \n', df4)
        elif(num == 5):
            print('The Data frame of Dinesh Karthik is \n', df5)
        elif(num == 6):
            print('The Data frame of Hardik Pandya is \n', df6)
        elif(num == 7):
            print('The Data frame of M.S.Dhoni is \n', df7)
        elif(num == 8):
            print('The Data frame of Sir Ravendra Jadeja is \n', df8)
        elif(num == 9):
            print('The Data frame of Bhuvenshwar Kumar is \n', df9)
        elif(num == 10):
            print('The Data frame of Yuzevendra Chahal is \n', df10)
        elif(num == 11):
            print('The Data frame of Jasprit Bhumrah is \n', df11)
        else:
            print('Enter valid Player ID')


    def getdata(self,num):
        self.num=num
        if (num == 1):
            self.newdf = pd.DataFrame(df1)
            self.name = 'Rohit Sharma'
        elif (num == 2):
            self.newdf = pd.DataFrame(df2)
            self.name = 'K.L.Rahul'
        elif (num == 3):
            self.newdf = pd.DataFrame(df3)
            self.name = 'Virat Kolhi'
        elif (num == 4):
            self.newdf = pd.DataFrame(df4)
            self.name = 'Rishabh Pant'
        elif (num == 5):
            self.newdf = pd.DataFrame(df5)
            self.name = 'Dinesh Karthik'
        elif (num == 6):
            self.newdf = pd.DataFrame(df6)
            self.name = 'Hardik Pandya'
        elif (num == 7):
            self.newdf = pd.DataFrame(df7)
            self.name = 'M.S.Dhoni'
        elif (num == 8):
            self.newdf = pd.DataFrame(df8)
            self.name = 'Sir Ravendra Jadeja'
        elif (num == 9):
            self.newdf = pd.DataFrame(df9)
            self.name = 'Bhuvenshvar Kumar'
        elif (num == 10):
            self.newdf = pd.DataFrame(df10)
            self.name = 'Yuzevendra chahal'
        elif (num == 11):
            self.newdf = pd.DataFrame(df11)
            self.name = 'Jasprit bumrah'
        else:
            return ('SELECT A PLAYER')

        return self.name


    def bestscore(self):
        lists = sorted(self.newdf['runs'], reverse=True)

        for i in range(len(self.newdf)):
            if (self.newdf['runs'][i] == lists[0]):
                break
        self.best = self.newdf['runs'][i]
        m ="The Best Score of",self.name,r"is",self.best,r"in",self.newdf['No. of balls'][i],r'balls in match index',self.newdf['match_id'][i]
        m =str(m)
        return m

    def bestscoreteam(self):
        return self.best

    def strikerate(self):

        stlist = []
        for j in range (len(self.newdf)):
            strikerate = ((self.newdf['runs'][j])*100)/(self.newdf['No. of balls'][j])
            stlist.append(strikerate)

        self.average_sr = int((sum(stlist))/(len(self.newdf+1)))
        m= "The Average strike rate of", self.name, r"is", self.average_sr
        m= str(m)
        return m

    def strikerateteam(self):
        return self.average_sr


    def battingavg(self):
        self.average = (sum(self.newdf['runs']))/(len(self.newdf))
        m="The batting average of", self.name, "is", self.average
        m= str(m)
        return m

    def battingavgteam(self):
        return self.average




    def mostsixes(self):
        lists = sorted(self.newdf['sixes'], reverse=True)
        length = len(self.newdf)

        for i in range(length):
            if (self.newdf['sixes'][i] == lists[0]):
                break
        m= "The most number of sixes hit by", self.name, "is", self.newdf["sixes"][i], "in match index", self.newdf['match_id'][i]
        m= str(m)
        return m

    def mostfours(self):
        lists = sorted(self.newdf['fours'], reverse=True)
        length = len(self.newdf)

        for i in range(length):
            if (self.newdf['fours'][i] == lists[0]):
                break
        m = ("The most number of fours hit by", self.name, "is", self.newdf["fours"][i], "in match index", self.newdf['match_id'][i])
        m = str(m)
        return m

    def form(self):
        last_3_match_runs = []
        last_3_match_balls = []
        for m in range(3):
            last_3_match_runs.append(self.newdf['runs'][length - (m + 1)])
            last_3_match_balls.append(self.newdf['No. of balls'][length - (m + 1)])

        new_strk_rate = sum(last_3_match_runs) / sum(last_3_match_balls)
        batting_avg_last_3 = sum(last_3_match_runs) / 3
        old_strk_rate = sum(self.newdf['runs'][0:length - 2]) / sum(self.newdf['No. of balls'][0:length - 2])
        old_batting_avg = sum(self.newdf['runs'][0:length - 2])/ (length-3)

        if (new_strk_rate > old_strk_rate and batting_avg_last_3 > old_batting_avg):
            return ("IS IN FORM")
        else:
            return ("IS NOT IN FROM")


    def runs_plot(self):
        plt_strk= []
        for m in range(len(self.newdf)):
            plt_strk.append(((self.newdf['runs'][m])*100)/self.newdf['No. of balls'][m])

        plt.figure(figsize=(8, 20))
        plt.plot(self.newdf["match_id"],self.newdf['runs'],color='red',marker='*')
        plt.plot(self.newdf["match_id"],plt_strk,color='blue',marker='.')

        str ='Runs/Strike rate of',self.name
        plt.title(str)
        plt.xlabel('MATCH')
        plt.ylabel('RUNS/STRIKE RATE')
        plt.show()

    def PREDICTOR(self,y):
        self.y =y
        totalruns =[]
        totalballs= []
        for q in range (0,49):
            sumruns = 0
            sumballs = 0
            for w in range (1,11):
                obj.getdata(w)
                sumruns = sumruns + (self.newdf['runs'][q])
                sumballs = sumballs + (self.newdf['No. of balls'][q])

            totalruns.append(sumruns)
            totalballs.append((sumballs))

        dict_pred_df = {'total_runs':totalruns, 'total_balls':totalballs}
        pred_df = pd.DataFrame(dict_pred_df)
        reg_model = LR.LinearRegression()
        reg_model.fit(pred_df[['total_balls']],pred_df[['total_runs']])
        x = (reg_model.predict([[y]]))
        x = int(x)
        m ='PREDICTED SCORE: ',x
        m= str(m)
        return m



obj = players()

class team():

    def best_score(self):
        self.team_best_score_list = []
        self.team_best_score_name_list = []

        for q in range(1,12):
            self.team_best_score_name_list.append(obj.getdata(q))
            obj.bestscore()
            self.team_best_score_list.append(obj.bestscoreteam())

        nmlst = self.team_best_score_name_list
        newlist = self.team_best_score_list
        x = max(newlist)
        for l in range(0,11):
            if (newlist[l] == x):
                break
        return ("The highest score by any individual in the team is",newlist[l],"by",nmlst[l])


    def best_avg_strike_rate(self):
        self.best_strike_list = []
        self.strike_names_list = []


        for q in range(1,12):
            self.strike_names_list.append(obj.getdata(q))
            obj.strikerate()
            self.best_strike_list.append(obj.strikerateteam())

        nmlst = self.strike_names_list
        newlist = self.best_strike_list
        for l in range (0,11):
            if (newlist[l] == max(newlist)):
                break

        return (nmlst[l],"has the best strike rate in the team.\n His strike rate is",newlist[l],'.')

    def best_batting_avg(self):
        self.best_batting_avg_list = []
        self.best_batting_avg_names_list = []
        for t in range(1,12):

            self.best_batting_avg_names_list.append(obj.getdata(t))
            obj.battingavg()
            self.best_batting_avg_list.append(obj.battingavgteam())

        nmlst = self.best_batting_avg_names_list
        newlist = self.best_batting_avg_list

        for l in range (0,11):
            if (newlist[l] == max(newlist)):
                break

        return (nmlst[l],"has the best batting average in the team.\n His average is",newlist[l],'.')


obj2 = team()

#***************************************************************#

class GUI(players,team):
    root = tk.Tk()
    root.title("CRICKET ANALYSIS")
    heading = tk.Label(text="INDIAN CRICKET TEAM")
    heading.pack()

    logo = Image.open("Indian_cricket_team_photo.jpg")
    resize_image = logo.resize((460, 120))
    img = ImageTk.PhotoImage(resize_image)
    logo_label = tk.Label(image=img)
    logo_label.image = img
    logo_label.pack()

    canvas = tk.Canvas(root, height=1500, width=2000, bg='#FFFFFF')
    canvas.pack()
    global frame1
    frame1 = tk.Frame(root, bg='#3399FF')
    frame1.place(relx=0.03, rely=0.2, relheight=0.75, relwidth=0.45)

    global frame2
    frame2 = tk.Frame(root, bg='#3399FF')
    frame2.place(relx=0.53, rely=0.2, relheight=0.75, relwidth=0.45)

    global frame3
    frame3 = tk.Frame(frame1, bg='#000000')
    frame3.place(relx=0.56, rely=0.51, relheight=0.46, relwidth=0.4)

    global list_box
    list_box = tk.Listbox(frame1, relief='groove', )
    list_box.place(relx=0.03, rely=0.02, relheight=0.3, relwidth=0.93, anchor='nw')
    name_list = ['1. ROHIT SHARMA', '2. K.L.RAHUL', '3. VIRAT KOLHI', '4. RISHABH PANT', '5. DINESH KARTHIK',
                 '6. HARDIK PANDYA', '7. M.S.DHONI', '8. SIR RAVENDRA JADEJA', '9. BHUVENSWAR KUMAR',
                 '10. YUZIVENDRA CHAHAL', '11. JASPRIT BUMRAH']

    for name in name_list:
        txt = 50 * ' ' + name
        list_box.insert('end', txt)

    global label1_frame1
    global label2
    global label_form

    def select():
        if (list_box.get('anchor') == 50 * ' ' + '1. ROHIT SHARMA'):
            obj.getdata(1)
            photo = Image.open('Rohit_Sharma_image.png')
            photo = photo.resize((250, 250))
            global img_RS
            img_RS = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_RS, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='ROHIT SHARMA '+x, bg='black',fg='white')



        elif (list_box.get('anchor') == 50 * ' ' + '2. K.L.RAHUL'):
            obj.getdata(2)
            photo = Image.open('KL_Rahul_image.png')
            photo = photo.resize((250, 250))
            global img_KL
            img_KL = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_KL, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='K.L.RAHUL '+x, bg='black',fg='white')


        elif (list_box.get('anchor') == 50 * ' ' + '3. VIRAT KOLHI'):
            obj.getdata(3)
            photo = Image.open('virat_kolhi_image4.png')
            photo = photo.resize((250, 250))
            global img_VK
            img_VK = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_VK, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='VIRAT KOHLI '+x, bg='black',fg='white')


        elif (list_box.get('anchor') == 50 * ' ' + '4. RISHABH PANT'):
            obj.getdata(4)
            photo = Image.open('rishab_pant_image.png')
            photo = photo.resize((250, 250))
            global img_RP
            img_RP = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_RP, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='RISHABH PANT '+x, bg='black',fg='white')


        elif (list_box.get('anchor') == 50 * ' ' + '5. DINESH KARTHIK'):
            obj.getdata(5)
            photo = Image.open('dinesh_karthik_image.png')
            photo = photo.resize((250, 250))
            global img_DK
            img_DK = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_DK, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='DINESH KARTIKH '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '6. HARDIK PANDYA'):
            obj.getdata(6)
            photo = Image.open('pandya_image.png')
            photo = photo.resize((250, 250))
            global img_HP
            img_HP = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_HP, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='HARDIK PANDYA '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '7. M.S.DHONI'):
            obj.getdata(7)
            photo = Image.open('dhoni_image.png')
            photo = photo.resize((250, 250))
            global img_MS
            img_MS = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_MS, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='M.S.DHONI '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '8. SIR RAVENDRA JADEJA'):
            obj.getdata(8)
            photo = Image.open('jadeja_image.png')
            photo = photo.resize((250, 250))
            global img_RJ
            img_RJ = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_RJ, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='RAVINDER JADEJA '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '9. BHUVENSWAR KUMAR'):
            obj.getdata(9)
            photo = Image.open('b_kumar_image.png')
            photo = photo.resize((250, 250))
            global img_BK
            img_BK = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_BK, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='B.KUMAR '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '10. YUZIVENDRA CHAHAL'):
            obj.getdata(10)
            photo = Image.open('y_chahal_image.png')
            photo = photo.resize((250, 250))
            global img_YC
            img_YC = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_YC, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='Y.CHAHAL '+x, bg='black',fg='white')

        elif (list_box.get('anchor') == 50 * ' ' + '11. JASPRIT BUMRAH'):
            obj.getdata(11)
            photo = Image.open('jasprit_bumrah_image.png')
            photo = photo.resize((250, 250))
            global img_JB
            img_JB = ImageTk.PhotoImage(photo)
            label1_frame1 = tk.Label(frame1, image=img_JB, bg='#000000')

            x = obj.form()
            label_form = tk.Label(frame1, text='JASPRIT BUMRAH '+x, bg='black',fg='white')
        else:
            label2.config(text='no')

        label1_frame1.place(relx=0.03, rely=0.51, relheight=0.4, relwidth=0.4)

        label_form.place(relx=0.03, rely=0.93, relheight=0.05, relwidth=0.4)

    def print2():
        obj.getdata(33)
        label2.config(text='cancelled')
        label1_frame1 = tk.Label(frame1, bg='#000000')
        label1_frame1.place(relx=0.03, rely=0.51, relheight=0.4, relwidth=0.4)

    def best_score_G():
        sc = obj.bestscore()
        label2.config(text=sc)

    def best_strike_rate_G():
        sc = obj.strikerate()
        label2.config(text=sc)

    def battingavg_G():
        sc = obj.battingavg()
        label2.config(text=sc)

    def most_sixes_G():
        sc = obj.mostsixes()
        label2.config(text=sc)

    def most_fours_G():
        sc = obj.mostfours()
        label2.config(text=sc)

    def graph_G():
        obj.runs_plot()
        label2.config(text='')

    def teamf_1():
        sc = obj2.best_score()
        label2.config(text=sc)

    def teamf_2():
        sc = obj2.best_batting_avg()
        label2.config(text=sc)

    def teamf_3():
        sc = obj2.best_avg_strike_rate()
        label2.config(text=sc)




    def predict_G():
        x = int(text_pred.get())
        if(x>60 and x<600):
            string = obj.PREDICTOR(x)
            string = str(string)
            label2_frame3.config(text=string)
        elif(x<60):
            label2_frame3.config(text='No. of balls should be \ngreater than 60')
        elif(x>600):
            label2_frame3.config(text='No. of balls should be \nless than 600')

        else:
            label2_frame3.config(text='Enter integer')


    button_select = tk.Button(frame1, text='select', command=select, bg='#4af030')
    button_select.place(relx=0.03, rely=0.34, relheight=0.15, relwidth=0.4)

    button_cancel = tk.Button(frame1, text='cancel', command=print2, bg='#ff3b3b')
    button_cancel.place(relx=0.56, rely=0.34, relheight=0.15, relwidth=0.4)

    button_fn2 = tk.Button(frame2, text='BEST SCORE OF THE PLAYER', command=best_score_G)
    button_fn2.place(relx=0.56, rely=0.2, relheight=0.15, relwidth=0.4)

    button_fn1 = tk.Button(frame2, text='AVERAGE STRIKE RATE OF THE PLAYER', command=best_strike_rate_G)
    button_fn1.place(relx=0.06, rely=0.2, relheight=0.15, relwidth=0.4)

    button_fn6 = tk.Button(frame2, text='BATTING AVERAGE OF THE PLAYER', command=battingavg_G)
    button_fn6.place(relx=0.56, rely=0.56, relheight=0.15, relwidth=0.4)

    button_fn3 = tk.Button(frame2, text='MOST SIXES HIT BY THE PLAYER', command=most_sixes_G)
    button_fn3.place(relx=0.06, rely=0.38, relheight=0.15, relwidth=0.4)

    button_fn4 = tk.Button(frame2, text='MOST FOURS HIT BY THE PLAYER', command=most_fours_G)
    button_fn4.place(relx=0.56, rely=0.38, relheight=0.15, relwidth=0.4)

    button_fn5 = tk.Button(frame2, text='GRAPH OF CAREER STATS', command=graph_G)
    button_fn5.place(relx=0.06, rely=0.56, relheight=0.15, relwidth=0.4)

    button_fn6 = tk.Button(frame2, text='BEST SCORE', command=teamf_1)
    button_fn6.place(relx=0.10, rely=0.75, relheight=0.15, relwidth=0.2)

    button_fn7 = tk.Button(frame2, text='BEST BATTING AVERAGE', command=teamf_2)
    button_fn7.place(relx=0.40, rely=0.75, relheight=0.15, relwidth=0.2)

    button_fn8 = tk.Button(frame2, text='BEST STRIKE RATE', command=teamf_3)
    button_fn8.place(relx=0.70, rely=0.75, relheight=0.15, relwidth=0.2)

    label2 = tk.Label(frame2, text='', )
    label2.place(relx=0.01, rely=0.01, relheight=0.15, relwidth=0.98)
    label2.config(font=('Helvatical bold', 13))

    global label1_frame3
    global label2_frame3
    label1_frame3 = tk.Label(frame3, text="SCORE PREDICTOR \n(TEAM SCORE)", bg="#000000", fg="#FFFFFF")
    label1_frame3.config(font=('Helvatical bold', 13))
    label1_frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.26)

    global text_pred
    text_pred = tk.Entry(frame3)
    text_pred.place(relx=0.02, rely=0.43, relwidth=0.46, relheight=0.25)

    label2_frame3 = tk.Label(frame3, text="", bg="#000000",fg='#FFFFFF')
    label2_frame3.config(font=('Helvatical bold', 12))
    label2_frame3.place(relx=0.01, rely=0.73, relwidth=0.98, relheight=0.25)

    button_predict = tk.Button(frame3, text="PREDICT", command= predict_G)
    button_predict.place(relx=0.52, rely=0.43, relwidth=0.46, relheight=0.25)

    label3_frame3 = tk.Label(frame3, text="ENTER THE NUMBER \n OF BALLS", bg="#000000", fg="#FFFFFF")
    label3_frame3.config(font=('Helvatical bold', 10))
    label3_frame3.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.25)


    root.mainloop()


