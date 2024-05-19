#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RMS:
    def __init__(self,resturant_name,resturant_menu):
        self.rest_name=resturant_name
        self.menu=resturant_menu
        self.total_bill=0
        self.user_order=""
    def welcome_user(self):
        print(f'welcome to{self.rest_name}')
    def display_menu(self):
        print("menu: ")
        print('*'*20)
        for i in self.menu:
            print(i.title(),self.menu[i])
        print('*'*20)
    def take_order(self):
        self.user_order=input("please Enter your order here ")
    def preparing_order(self):
        import time
        print(f'preparing your{self.user_order.title()}')
        time.sleep(1)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]

    def serve_order(self):
        print('your order is ready')
        print(f'please Enjoy order{self.user_order.title()}')
    def display_bill(self):
        print("Bill:",self.total_bill)
    def verify_bill(self):
        user_pay=int(input("Enter your bill here"))
        while user_pay<self.total_bill:
            print("payment failed")
            self.total_bill=self.total_bill-user_pay
            print("please pay your pending",self.total_bill)
            user_pay=int(input("Enter your bill here"))
            
        if user_pay>self.total_bill:
            print("payment successful")
            print("here is your change: ",user_pay-self.total_bill)
        else:
            pass
    def ty(self):
        print(f'Thank you visiting{self.rest_name}')
        print(" please visit us again!")
    def order_process(self):
        self.welcome_user()
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu: 
            self.preparing_order()
            order_again=input("Do you want to order again?")
            while order_again.lower()=="yes":
                self.repeat_order()
                order_again=input("Do you want to order again?")
            self.display_bill()
            self.verify_bill()
            self.ty()
        else:
            print("Invalid order")
            print('*'*30)
            self.order_process()
    def repeat_order(self):
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            
        else:
            print("Invalid order")
            self.repeat_order()


# In[ ]:


rn="moonlight cafe"
rm={'pizza': 150,
   'burger': 100,
   'puff'  : 80,
   'soffty': 40,
   'cold coffe': 80 }
mc=(RMS(resturant_name=rn,resturant_menu=rm))
mc.order_process()


# 1
# # rs.

# In[2]:


#m#


# In[ ]:




