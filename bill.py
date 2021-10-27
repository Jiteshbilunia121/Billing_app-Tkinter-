from tkinter import*
import math,random
from tkinter import messagebox
class Bill_App:

    def __init__(self,root):

        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Bill App")
        bg_color="#4efee5"
        title=Label(self.root, text="Billing software", bd=12, relief=GROOVE,bg=bg_color,fg="#000000" ,font=("times new roman",30,"bold"), pady=2).pack(fill=X)
        #vars for info

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        self.coke=IntVar()
        self.sprite=IntVar()
        self.redbull=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()


        self.c_name=StringVar()
        self.c_phon=StringVar()
        x = random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        # customer detail
        F1 = LabelFrame(self.root, bd=10,text="Cutomer Details", font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)


        #customer label
        cname_lbl=Label(F1, text="Customer Name", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5) 
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=1, pady=5,padx=10)

        cphn_lbl=Label(F1, text="Phone .no", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5) 
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=3, pady=5,padx=10)

        c_bill_lbl=Label(F1, text="Bill number", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5) 
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=5, pady=5,padx=10)
        
        bill_btn=Button(F1, text="search",width=10,bd=6,font=("arial 12 bold")).grid(row=0,column=6,padx=10,pady=6)

        #Costmetic frame
        F2 = LabelFrame(self.root, bd=10,text="Costmetics", font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)

        bath_lbl=Label(F2, text="Bath Soap", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2, text="Face Creams", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2, text="Face Wash", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
 
        Hair_s_lbl=Label(F2, text="Hair serums", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2, text="Hair gels", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2, text="Body lotions", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.lotion, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #grocery frame

        F3 = LabelFrame(self.root, bd=10,text="Grocery products", font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F3.place(x=340,y=170,width=325,height=380)
        
        g1_lbl=Label(F3, text="Rice", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3, text="wheat", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.wheat, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_w_lbl=Label(F3, text="Food oil", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_w_txt=Entry(F3,width=10, textvariable=self.food_oil, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3, text="Pulses", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10, textvariable=self.daal, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
   
        g5_lbl=Label(F3, text="Sugar", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3, text="Tea", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Drinks frame

        F4 = LabelFrame(self.root, bd=10,text="drink items", font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F4.place(x=680,y=170,width=325,height=380)

        c1_lbl=Label(F4, text="Coke", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.coke, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4, text="sprite", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.sprite, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4, text="Red Bull", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.redbull, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4, text="Frooti", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.frooti, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4, text="Thumbs Up", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.thumbsup, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4, text="Limca", font=("times new roman",16,"bold"),fg="red", bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.limca, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
          
        #=Bill portion
        F5 = Frame(self.root, bd=10,relief=GROOVE)
        F5.place(x=1010,y=170,width=380,height=380)
        bill_title=Label(F5,text="Bill details",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(orient=VERTICAL) 
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
 
        F6 = LabelFrame(self.root, bd=10,text="Menu",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=150)
        m1_lbl=Label(F6,text="Total Cosmetic price",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_txt=Entry(F6,textvariable=self.cosmetic_price, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=2,pady=1)
  
        m2_lbl=Label(F6,text="Total Grocery price",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=2,sticky="w")
        m2_txt=Entry(F6,textvariable=self.grocery_price, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=2,pady=1)

        m3_lbl=Label(F6,text="Total Drinks price",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=2,sticky="w")
        m3_txt=Entry(F6,textvariable=self.cold_drink_price, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=2,pady=1)

        c1_lbl=Label(F6,text=" Cosmetic tax",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=2,sticky="w")
        c1_txt=Entry(F6,textvariable=self.cosmetic_tax, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=2,pady=1)
  
        c2_lbl=Label(F6,text="Grocery tax",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=2,sticky="w")
        c2_txt=Entry(F6,textvariable=self.grocery_tax, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=2,pady=1)

        c3_lbl=Label(F6,text="Drinks tax",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=2,sticky="w")
        c3_txt=Entry(F6,textvariable=self.cold_drink_tax, font=("Times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=2,pady=1)
        
        btn_F=Frame(F6, bd = 7, relief=GROOVE) 

        btn_F.place(x=800,width=550,height=105)
        total_btn=Button(btn_F, command=self.total,text="Total",bg="cadetblue",fg="white",width="10", font=("arial",12,"bold"),pady=10).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F, command=self.bill_area, text="Generate bill",bg="cadetblue",fg="white",width="10",font=("arial",12,"bold"),pady=10).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F, text="Clear",bg="cadetblue",fg="white",width="10", font=("arial",12,"bold"),pady=10).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,  text="Exit",bg="cadetblue",fg="white",width="10", font=("arial",12,"bold"),pady=10).grid(row=0,column=3,padx=5,pady=5)
        
        self.welcome()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*40
        self.c_fw_p=self.face_wash.get()*40
        self.c_hs_p=self.spray.get()*40
        self.c_hg_p=self.gell.get()*40
        self.c_bl_p=self.lotion.get()*40

        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                
                                    )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=self.total_cosmetic_price*0.05
        self.cosmetic_tax.set(str(self.c_tax))


        self.g_r_p=self.rice.get()*40
        self.g_w_p=self.wheat.get()*40
        self.g_d_p=self.daal.get()*40
        self.g_f_p=self.food_oil.get()*40
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*40


        self.total_grocery_price=float(
                                      self.g_r_p+
                                      self.g_w_p+
                                      self.g_d_p+
                                      self.g_f_p+
                                      self.g_s_p+
                                      self.g_t_p
            
                                    )
        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=self.total_grocery_price*0.05
        self.grocery_tax.set(str(self.g_tax))

        self.d_c_p=self.coke.get()*40
        self.d_s_p=self.sprite.get()*40
        self.d_t_p=self.thumbsup.get()*40
        self.d_f_p=self.frooti.get()*40
        self.d_r_p=self.redbull.get()*40
        self.d_l_p=self.limca.get()*40

        self.total_cold_drink_price=float(
                                    self.d_c_p+
                                    self.d_s_p+
                                    self.d_t_p+
                                    self.d_f_p+
                                    self.d_r_p+
                                    self.d_l_p
                                
                                    )
                                    
        self.cold_drink_price.set(str(self.total_cold_drink_price))
        self.d_tax=self.total_cold_drink_price*0.05
        self.cold_drink_tax.set(str(self.d_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.g_tax+
                              self.c_tax+
                              self.d_tax
                            )

    def welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\twelcome to our bill service\n")
        self.textarea.insert(END, f"\n Bill number :{self.bill_no.get()}")
        self.textarea.insert(END, f"\nCustomer name:{self.c_name.get()}")
        self.textarea.insert(END, f"\nwelcome here:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n***************************************")
        self.textarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.textarea.insert(END,f"\n***************************************")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome()
            #==Cosmetics
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:     
                self.textarea.insert(END,f"\n Face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Body lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")
            
            #==Grocery
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Basmati rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n mustard oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get()!=0:     
                self.textarea.insert(END,f"\n Pulses\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n flour\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Red label\t\t{self.tea.get()}\t\t{self.g_t_p}")

            #Cold Drinks
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.coke.get()}\t\t{self.c_s_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Face cream\t\t{self.sprite.get()}\t\t{self.c_fc_p}")
            if self.thumbsup.get()!=0:     
                self.textarea.insert(END,f"\n Face wash\t\t{self.thumbsup.get()}\t\t{self.c_fw_p}")
            if self.redbull.get()!=0:
                self.textarea.insert(END,f"\n Hair spray\t\t{self.redbull.get()}\t\t{self.c_hs_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Hair gell\t\t{self.frooti.get()}\t\t{self.c_hg_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Body lotion\t\t{self.limca.get()}\t\t{self.c_bl_p}")


            self.textarea.insert(END,f"\n***************************************")
            if self.cosmetic_tax.get()!="0.0":
                self.textarea.insert(END,f"\n Costmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="0.0":
                self.textarea.insert(END,f"\n Costmetic Tax\t\t\t\t{self.grocery_tax.get()}")
            
            if self.cold_drink_tax.get()!="0.0":
                self.textarea.insert(END,f"\n Costmetic Tax\t\t\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END,f"\n Total Bill\t\t\t\t{self.Total_bill}")
            self.textarea.insert(END,f"\n***************************************")


        pass    

root = Tk()
obj = Bill_App(root)  
root.mainloop()


