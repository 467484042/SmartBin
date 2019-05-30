import tkinter as Tk
import serial
import pyautogui
from PIL import Image, ImageTk
import threading

import time #Required to use delay functions



    


class SmartBin(Tk.Frame):
    '''
    Dislay an image on Tkinter.Canvas and delete it on button click
    '''
    def __init__(self, parent):
        '''
        Inititialize the GUI with a button and a Canvas objects
        '''
        Tk.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()
        '''
        self.ArduinoSerial = serial.Serial("COM7",115200) #Create Serial port object called arduinoSerialData
        time.sleep(1)
        self.student_IDs=['UID Value:  0x4D 0xBC 0x6 0xD9','UID Value:  0x4D 0xBC 0x6 0xD9']
        '''
    def initialize_user_interface(self):
        """
        Draw the GUI
        """
        self.parent.title("Smart Bin")
        self.w = 1070
        self.h = 1838
        self.canvas = Tk.Canvas(self.parent, width=self.w,height=self.h,bg='black')
        self.canvas.pack()
        self.draw_create_account_student()

     
        
        

        
    

    def home_page(self):
        #self.draw_background("homepage.png")
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="bgHomeScreen.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        tutorialBtn=Tk.Button(self.parent,width=237,height=108,highlightthickness = 0, bd = 0)
        tutorialBtn.image = Tk.PhotoImage(file="tutoralbutton.png")
        tutorialBtn['image'] = tutorialBtn.image
        tutorialBtn.pack()
        self.canvas.create_window(117,56, width=235, height=106,window=tutorialBtn)


        self.draw_tutorial_button()
        self.draw_navigation_button()
        self.draw_language_button()

        '''
        languageBtn=Tk.Button(self.parent,width=237,height=108,highlightthickness = 0, bd = 0)
        languageBtn.image = Tk.PhotoImage(file="languagebutton.png")
        languageBtn['image'] = languageBtn.image
        languageBtn.pack()
        self.canvas.create_window(955,56, width=237, height=106,window=languageBtn)


        databaseBtn=Tk.Button(self.parent,width=994,height=326,highlightthickness = 0, bd = 0)
        databaseBtn.image = Tk.PhotoImage(file="databasesearch.png")
        databaseBtn['image'] = databaseBtn.image
        databaseBtn.pack()
        self.canvas.create_window(550,750, width=992, height=324,window=databaseBtn)


        keepuoBtn=Tk.Button(self.parent,width=464,height=627,highlightthickness = 0, bd = 0)
        keepuoBtn.image = Tk.PhotoImage(file="keepuptodate.png")
        keepuoBtn['image'] = keepuoBtn.image
        keepuoBtn.pack()
        self.canvas.create_window(310,1490, width=462, height=625,window=keepuoBtn)


        learnmoreBtn=Tk.Button(self.parent,width=464,height=627,highlightthickness = 0, bd = 0)
        learnmoreBtn.image = Tk.PhotoImage(file="learnaboutrecycling.png")
        learnmoreBtn['image'] = learnmoreBtn.image
        learnmoreBtn.pack()
        self.canvas.create_window(810,1490, width=462, height=625,window=learnmoreBtn)
        '''

    def draw_tutorial_button(self):
        tutorialBtn=Tk.Button(self.parent,width=237,height=108,highlightthickness = 0, bd = 0)
        tutorialBtn.image = Tk.PhotoImage(file="tutoralbutton.png")
        tutorialBtn['image'] = tutorialBtn.image
        tutorialBtn.pack()
        self.canvas.create_window(117,56, width=235, height=106,window=tutorialBtn)

    def draw_navigation_button(self):
        navigationBtn=Tk.Button(self.parent,width=159,height=115,highlightthickness = 0, bd = 0)
        navigationBtn.image = Tk.PhotoImage(file="mapbutton.png")
        navigationBtn['image'] = navigationBtn.image
        navigationBtn.pack()
        self.canvas.create_window(757,57, width=157, height=113,window=navigationBtn)


    def draw_language_button(self):
        languageBtn=Tk.Button(self.parent,width=237,height=108,highlightthickness = 0, bd = 0)
        languageBtn.image = Tk.PhotoImage(file="languagebutton.png")
        languageBtn['image'] = languageBtn.image
        languageBtn.pack()
        self.canvas.create_window(955,56, width=237, height=106,window=languageBtn)


    def draw_current_Events_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="currentEvents.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    '''
    def draw_current_Events_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="currentEvents.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()
    '''


    def draw_coffe_cup_info_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="coffeecupinfo.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_coffe_cup_info2_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="coffeecupinfo1.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def draw_coffe_cup_info2_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="coffeecupinfo2.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def draw_coffe_cup_info3_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="coffeecupinfo3.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def draw_coffe_cup_info4_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="coffeecupinfo4.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_create_account_not_student(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="createAccountNonStudent.png")
        bg['image'] = bg.image
        bg.pack()
        
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()
        large_font = ('Verdana',30)
        entry1Var = Tk.StringVar(value='input your name')
        self.name=Tk.Entry(self.parent,width=700,textvariable=entry1Var,font=large_font,highlightthickness = 0, bd = 0)
        self.name.pack()
        self.canvas.create_window(440,780, width=700, height=100,window=self.name)


        entry2Var = Tk.StringVar(value='input your email')
        self.email=Tk.Entry(self.parent,width=700,textvariable=entry2Var,font=large_font,highlightthickness = 0, bd = 0)
        self.email.pack()
        self.canvas.create_window(440,1080, width=700, height=100,window=self.email)

        submitBtn=Tk.Button(self.parent,width=414,height=163,highlightthickness = 0, bd = 0)
        submitBtn.image = Tk.PhotoImage(file="submit.png")
        submitBtn['image'] = submitBtn.image
        submitBtn.pack()
        self.canvas.create_window(820,1310, width=412, height=161,window=submitBtn)





    def draw_create_account_student(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="createCardAccount.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()
        createBtn=Tk.Button(self.parent,width=688,height=192,highlightthickness = 0, bd = 0)
        createBtn.image = Tk.PhotoImage(file="createaccount.png")
        createBtn['image'] = createBtn.image
        createBtn.pack()
        self.canvas.create_window(530,950, width=686, height=190,window=createBtn)


    
    def draw_create_account_form(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="createNewAccount.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def student_jason(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="jackson1.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def account_update_success():
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="loadingNewAccountScreen.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def new_account_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="newAccountAccount.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def recycable_bin_full(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="recyclingBin.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def reward_question_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="rewardsQuestion.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def scan_card_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="scanIDCard.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()



    def draw_screen_saver_page(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="screenSaver.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_box_page(slef):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="singleRecyclingItem.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def draw_pencil_box_page(slef):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="singleWasteItem.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_special_item(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="specialItem.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_coffe(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="splitItemRecycling.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def draw_talk_to_new_account(self):
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="takingtonewAccount1.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()


    def throw_away_page():
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="throwAway.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    def waste_bin_full():
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="wastebinfullnot.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

    
    def waste_bin_full_screen_saver():
        self.canvas.delete("all")
        bg=Tk.Label(self.parent,width=1080,height=1838,highlightthickness = 0, bd = 0)
        bg.image = Tk.PhotoImage(file="wasteBinFullScreenSaver.png")
        bg['image'] = bg.image
        bg.pack()
        self.canvas.create_window((self.w/2)-1,(self.h/2)+40, width=1080, height=1920,window=bg)
        self.draw_tutorial_button()
        self.draw_language_button()
        self.draw_navigation_button()

        '''
        #self.draw_title()
        self.draw_fixBtn()
        self.draw_navigationBtn()
        
        

        
        guidanceBtn=Tk.Button(self.parent,width=1077,height=241,highlightthickness = 0, bd = 0,command = self.guidance_page)
        guidanceBtn.image = Tk.PhotoImage(file="guidance.png")
        guidanceBtn['image'] = guidanceBtn.image
        guidanceBtn.pack()
        self.canvas.create_window(536,538, width=1075, height=239,window=guidanceBtn)


        searchBtn=Tk.Button(self.parent,width=1077,height=241,highlightthickness = 0, bd = 0,command = self.search_page)
        searchBtn.image = Tk.PhotoImage(file="search.png")
        searchBtn['image'] = searchBtn.image
        searchBtn.pack()
        self.canvas.create_window(536,810, width=1075, height=239,window=searchBtn)


        exploreBtn=Tk.Button(self.parent,width=1077,height=240,highlightthickness = 0, bd = 0,command=self.explore_page)
        exploreBtn.image = Tk.PhotoImage(file="explore.png")
        exploreBtn['image'] = exploreBtn.image
        exploreBtn.pack()
        self.canvas.create_window(536,1080, width=1075, height=238,window=exploreBtn)

        languageBtn=Tk.Button(self.parent,width=157,height=158,highlightthickness = 0, bd = 0,command = self.language_page)
        languageBtn.image = Tk.PhotoImage(file="language.png")
        languageBtn['image'] = languageBtn.image
        languageBtn.pack()
        self.canvas.create_window(90,1740, width=154, height=156,window=languageBtn)
        self.jump_to_split_page_thread=threading.Timer(1,self.color_sensor_det)
        self.jump_to_split_page_thread.start()
        '''


    '''
    def distent_sensor_det(self):
        self.distance_value=-1
        self.info
        while 1:
            incoming = str(self.ArduinoSerial.readline())
            rawStr=incoming.split("\\")
            newLineRemoved=rawStr[0:len(rawStr)-2]
           
            self.info=newLineRemoved[0].split("'")[1]
            a=self.info.split(" ")
            if len(a)==3 and a[0]=='distance':
                self.distance_value=int(a[2])                
            if self.distance_value >0 and self.distance_value<=30:
                self.distance_det_thread=threading.Timer(0,self.reward_page)
                self.distance_det_thread.start()
                return



    def color_sensor_det(self):
        while 1:
            incoming = str(self.ArduinoSerial.readline())
            rawStr=incoming.split("\\")
            newLineRemoved=rawStr[0:len(rawStr)-2]
            info=newLineRemoved[0].split("'")[1]
            print(info)
            if info=="white":
                self.color_thread=threading.Timer(0,self.split_page)
                self.color_thread.start()
                return
            elif info=="light blue":
                self.color_thread=threading.Timer(0,self.split_page)
                self.color_thread.start()
                return
            elif info=="blue":
                self.color_thread=threading.Timer(0,self.split_page)
                self.color_thread.start()
                return
        self.color_thread._delete()
          

    '''
    def card_sensor_det(self):
        time.sleep(4)
         #wait for 2 seconds for the communication to get established


        while 1:
            incoming = str(self.ArduinoSerial.readline())
            rawStr=incoming.split("\\")
            newLineRemoved=rawStr[0:len(rawStr)-2]
            info=newLineRemoved[0].split("'")[1]
            print(info)
            if info=="t find":
                self.time2=threading.Timer(0,self.home_page)
                self.time2.start()
                return
            elif info=="UID Value:  0x4D 0xBC 0x6 0xD9":
                self.time2=threading.Timer(0,self.reward_no_page)
                self.time2.start()
                return
            elif info=="UID Value:  0x4D 0x8 0x82 0x7C":
                self.time2=threading.Timer(0,self.not_student_page)
                self.time2.start()
                return
        self.time2._delete()
           
        
    



        


    

# Main method
def main():
    root=Tk.Tk()
    sb=SmartBin(root)
    root.mainloop()

# Main program       
if __name__=="__main__":
    main()
