import colorama
from colorama import Fore
colorama.init(autoreset=True)
from stdiomask import getpass
import os
import time
clear = lambda: os.system('cls')


def forgot_password():
    clear()
    print(Fore.BLUE+"||--------------------------------\\\_________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Forgot Password  \\\ New Tab (+)\\\                                                                 ||")
    print(Fore.BLUE+"||----------------------------------\\\------------\\\________________________________________________________________||")
    print(Fore.LIGHTRED_EX+"""
                            ███████╗ ██████╗ ██████╗  ██████╗  ██████╗ ████████╗               
                            ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔═══██╗╚══██╔══╝               
                            █████╗  ██║   ██║██████╔╝██║  ███╗██║   ██║   ██║                  
                            ██╔══╝  ██║   ██║██╔══██╗██║   ██║██║   ██║   ██║                  
                            ██║     ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝   ██║                  
                            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                  
                                                                   
                ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗   ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗  ╚════██╗
                ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ▄███╔╝
                ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ▀▀══╝ 
                ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██╗   
                ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝   
                                                                            
        
    
    
    
    
    """)
    username = input(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\tUsername: ")
    with open("database.txt") as file:

        if username in file.read():
            clear()
            print(Fore.BLUE+"||--------------------------------\\\_________________________________________________________________________________")
            print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Forgot Password  \\\ New Tab (+)\\\                                                                 ||")
            print(Fore.BLUE+"||----------------------------------\\\------------\\\________________________________________________________________||")
            print(Fore.LIGHTRED_EX+"""
                                        ███████╗ ██████╗ ██████╗  ██████╗  ██████╗ ████████╗               
                                        ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔═══██╗╚══██╔══╝               
                                        █████╗  ██║   ██║██████╔╝██║  ███╗██║   ██║   ██║                  
                                        ██╔══╝  ██║   ██║██╔══██╗██║   ██║██║   ██║   ██║                  
                                        ██║     ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝   ██║                  
                                        ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                  

                            ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗   ██████╗ 
                            ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗  ╚════██╗
                            ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ▄███╔╝
                            ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ▀▀══╝ 
                            ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██╗   
                            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝ 
                """)
            print(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\t\t\t\tWelcome back!"+ username +"\n\n\n\n\n\n")
            print(Fore.MAGENTA+"\t\t\t\t\tFor Identification!")
            fullname = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tCurrent Fullname: ")
            email = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tCurrent Email Address: ")
            phone_number = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tCurrent Phone Number: ")
            password = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tNew Password: ")
            password2 = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tConfirm Password: ")



    if len(password) <= 6:
        clear()
        print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
        print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
        print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
        print(Fore.RED+"""
                                                    ███████╗ █████╗ ██╗██╗     ███████╗██████╗ ██╗
                                                    ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗██║
                                                    █████╗  ███████║██║██║     █████╗  ██║  ██║██║
                                                    ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║╚═╝
                                                    ██║     ██║  ██║██║███████╗███████╗██████╔╝██╗
                                                    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝

                        """)
        print(Fore.RED+"\n\n\t\t\t\t\t\tPassword is too short!, Please try Again!\n\n\n\n\n")
        time.sleep(3)
        forgot_password()
    elif password != password2:
        clear()
        print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
        print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
        print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
        print(Fore.RED+"""
                                                    ███████╗ █████╗ ██╗██╗     ███████╗██████╗ ██╗
                                                    ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗██║
                                                    █████╗  ███████║██║██║     █████╗  ██║  ██║██║
                                                    ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║╚═╝
                                                    ██║     ██║  ██║██║███████╗███████╗██████╔╝██╗
                                                    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝

                """)
        print(Fore.RED+"\n\n\t\t\t\t\t\tPassword didn't matched!, Please try Again!\n\n\n\n\n")
    else:
        clear()
        database = open("database.txt", "a+")
        db = ("Fullname: " + fullname + "\nUsername: " + username + "\nEmail Address: " + email + "\nPhone Number: " + phone_number + "\nPassword: " + password2 + "\n\n")
        database.write(str(db))


        def ques():
            clear()
            print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
            print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
            print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
            print(Fore.LIGHTGREEN_EX+"""
                                    ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗██╗
                                    ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║
                                    ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗██║
                                    ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║╚═╝
                                    ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██╗
                                    ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝

                    """)
        login1 = input(Fore.MAGENTA+"\n\n\t\t\t\t\t\tYour Account was successfully created! Do you want to login?(Yes/No):")
        if login1 == "yes" or login1 == "YES" or login1 == "Yes":
            login()

        elif login1 == "no" or login1 == "NO" or login1 == "No":
            home()
        else:
            ques()





def menu():
    items = []
    price = []
    quantitys = []
    total = 0

    clear()
    print(Fore.BLUE+"||------------------------\\\_________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen\\\ New Tab (+)\\\                                                                         ||")
    print(Fore.BLUE+"||--------------------------\\\------------\\\________________________________________________________________________||")
    print(Fore.YELLOW+"|___________|======|____________________________________|====|___________________________________|======|_____________|")
    print(Fore.LIGHTYELLOW_EX+"|-----------|DRINKS|------------------------------------|MEAL|-----------------------------------|SNACKS|-------------|")
    print(Fore.YELLOW+"|-----------|======|------------------------------------|====|-----------------------------------|======|-------------|")
    print(Fore.YELLOW+"|_____________________________________________________________________________________________________________________|")
    print(Fore.LIGHTYELLOW_EX+"|__||______________________||__||_______BREAKFAST_______||__||_________LUNCH__________||__________________________||__|")
    print(Fore.LIGHTYELLOW_EX+"|--||Water.........Php 7.00||--||Scrambled Egg..Php12.00||--||Fried Chicken...Php25.00||--||Kikiam........Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coca-cola.....Php12.00||--||Fried Rice.....Php10.00||--||Chicken Curry...Php25.00||--||Fishball......Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Pepsi.........Php12.00||--||Hotdog.........Php 8.00||--||Pork Menudo.....Php20.00||--||Bananaque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Mountain Dew..Php15.00||--||Ham............Php12.00||--||Beef Steak......Php20.00||--||Camoteque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Sprite........Php10.00||--||Tocino.........Php15.00||--||Caldereta.......Php20.00||--||Hotcake.......Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Milk..........Php15.00||--||                       ||--||                        ||--||Hamburger.....Php30.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coffee........Php14.00||--||                       ||--||                        ||--||Cheeseburger..Php35.00||--|")
    print(Fore.YELLOW+"|--||**********************||--||***********************||--||************************||--||**********************||--|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    wallet = float(input(Fore.LIGHTMAGENTA_EX+"Enter your wallet:"))
    clear()
    print(Fore.BLUE+"||------------------------\\\_________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen\\\ New Tab (+)\\\                                                                         ||")
    print(Fore.BLUE+"||--------------------------\\\------------\\\________________________________________________________________________||")
    print(Fore.YELLOW+"|___________|======|____________________________________|====|___________________________________|======|_____________|")
    print(Fore.LIGHTYELLOW_EX+"|-----------|DRINKS|------------------------------------|MEAL|-----------------------------------|SNACKS|-------------|")
    print(Fore.YELLOW+"|-----------|======|------------------------------------|====|-----------------------------------|======|-------------|")
    print(Fore.YELLOW+"|_____________________________________________________________________________________________________________________|")
    print(Fore.LIGHTYELLOW_EX+"|__||______________________||__||_______BREAKFAST_______||__||_________LUNCH__________||__________________________||__|")
    print(Fore.LIGHTYELLOW_EX+"|--||Water.........Php 7.00||--||Scrambled Egg..Php12.00||--||Fried Chicken...Php25.00||--||Kikiam........Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coca-cola.....Php12.00||--||Fried Rice.....Php10.00||--||Chicken Curry...Php25.00||--||Fishball......Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Pepsi.........Php12.00||--||Hotdog.........Php 8.00||--||Pork Menudo.....Php20.00||--||Bananaque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Mountain Dew..Php15.00||--||Ham............Php12.00||--||Beef Steak......Php20.00||--||Camoteque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Sprite........Php10.00||--||Tocino.........Php15.00||--||Caldereta.......Php20.00||--||Hotcake.......Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Milk..........Php15.00||--||                       ||--||                        ||--||Hamburger.....Php30.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coffee........Php14.00||--||                       ||--||                        ||--||Cheeseburger..Php35.00||--|")
    print(Fore.YELLOW+"|--||**********************||--||***********************||--||************************||--||**********************||--|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.LIGHTYELLOW_EX+"|---------------------------------------------||Your Wallet:Php"+str(wallet)+"0 ||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    numOf_Orders = int(input(Fore.LIGHTMAGENTA_EX+"Number of orders: "))


    clear()
    print(Fore.BLUE+"||------------------------\\\_________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen\\\ New Tab (+)\\\                                                                         ||")
    print(Fore.BLUE+"||--------------------------\\\------------\\\________________________________________________________________________||")
    print(Fore.YELLOW+"|___________|======|____________________________________|====|___________________________________|======|_____________|")
    print(Fore.LIGHTYELLOW_EX+"|-----------|DRINKS|------------------------------------|MEAL|-----------------------------------|SNACKS|-------------|")
    print(Fore.YELLOW+"|-----------|======|------------------------------------|====|-----------------------------------|======|-------------|")
    print(Fore.YELLOW+"|_____________________________________________________________________________________________________________________|")
    print(Fore.LIGHTYELLOW_EX+"|__||______________________||__||_______BREAKFAST_______||__||_________LUNCH__________||__________________________||__|")
    print(Fore.LIGHTYELLOW_EX+"|--||Water.........Php 7.00||--||Scrambled Egg..Php12.00||--||Fried Chicken...Php25.00||--||Kikiam........Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coca-cola.....Php12.00||--||Fried Rice.....Php10.00||--||Chicken Curry...Php25.00||--||Fishball......Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Pepsi.........Php12.00||--||Hotdog.........Php 8.00||--||Pork Menudo.....Php20.00||--||Bananaque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Mountain Dew..Php15.00||--||Ham............Php12.00||--||Beef Steak......Php20.00||--||Camoteque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Sprite........Php10.00||--||Tocino.........Php15.00||--||Caldereta.......Php20.00||--||Hotcake.......Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Milk..........Php15.00||--||                       ||--||                        ||--||Hamburger.....Php30.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coffee........Php14.00||--||                       ||--||                        ||--||Cheeseburger..Php35.00||--|")
    print(Fore.YELLOW+"|--||**********************||--||***********************||--||************************||--||**********************||--|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.LIGHTYELLOW_EX+"|---------------------------------------------||Your Wallet:Php"+str(wallet)+"0 ||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.MAGENTA+"Type your orders: ")
    for i in range(numOf_Orders):
        order = str(input(Fore.LIGHTMAGENTA_EX+"Order: "))

        try:


 #       <-------------------------V------DRINKS SECTION---------V---------------------------//


            if order == "Water" or order == "water" or order == "WATER":
                items.append("Water")
                price.append(7)

            elif order == "Coca-cola" or order == "coca-cola" or order =="COCA-COLA":
                items.append("Coca-cola")
                price.append(12)

            elif order == "Pepsi" or order == "pepsi" or order == "PEPSI":
                items.append("Pepsi")
                price.append(12)

            elif order == "Mountain Dew" or order == "mountain dew" or order == "MOUNTAIN DEW":
                items.append("Mountain Dew")
                price.append(15)

            elif order == "Sprite" or order == "sprite" or order == "SPRITE":
                items.append("Sprite")
                price.append(10)

            elif order == "Milk" or order == "milk" or order == "MILK":
                items.append("Milk")
                price.append(15)

            elif order == "Coffee" or order == "coffee" or order == "COFFEE":
                items.append("Coffee")
                price.append(14)


#<-----------------------V-------BREAKFAST & LUNCH SECTION------V--------------------------->


            elif order == "Scrambled Egg" or order == "scrambled egg" or order == "SCRAMBLED EGG":
                items.append("Scrambled Egg")
                price.append(12)

            elif order == "Fried Rice" or order == "fried rice" or order == "FRIED RICE":
                items.append("Fried Rice")
                price.append(10)

            elif order == "Hotdog" or order == "hotdog" or order == "HOTDOG":
                items.append("Hotdog")
                price.append(8)

            elif order == "Ham" or order == "ham" or order == "HAM":
                items.append("Ham")
                price.append(12)

            elif order == "Tocino" or order == "tocino" or order == "TOCINO":
                items.append("Tocino")
                price.append(15)

            elif order == "Fried Chicken" or order == "fried chicken" or order == "FRIED CHICKEN":
                items.append("Fried Chicken")
                price.append(25)

            elif order == "Chicken Curry" or order == "chicken curry" or order == "CHICKEN CURRY":
                items.append("Chicken Curry")
                price.append(25)

            elif order == "Pork Menudo" or order == "pork menudo" or order == "PORK MENUDO":
                items.append("Por Menudo")
                price.append(20)

            elif order == "Beef Steak" or order == "beef steak" or order == "BEEF STEAK":
                items.append("Beef Steak")
                price.append(20)

            elif order == "Caldereta" or order == "caldereta" or order == "CALDERETA":
                items.append("Caldereta")
                price.append(20)


#   <---------------------V------------SNACKS SECTION----------V----------------------->


            elif order == "Kikiam" or order == "kikiam" or order == "KIKIAM":
                items.append("Kikiam")
                price.append(10)

            elif order == "Fishball" or order == "fishball" or order == "FISHBALL":
                items.append("Fishball")
                price.append(10)

            elif order == "Bananaque" or order == "bananaque" or order == "BANANAQUE":
                items.append("Bananaque")
                price.append(5)

            elif order == "Camoteque" or order == "camoteque" or order == "CAMOTEQUE":
                items.append("Camoteque")
                price.append(5)

            elif order == "Hocake"  or order == "hotcake" or order == "HOTCAKE":
                items.append("Hotcake")
                price.append(5)

            elif order == "Hamburger" or order == "hamburger" or order == "HAMBURGER":
                items.append("Hamburger")
                price.append(30)

            elif order == "Cheeseburger" or order == "cheeseburger" or order == "CHEESEBURGER":
                items.append("Cheeseburger")
                price.append(35)

            else:
                print(Fore.LIGHTMAGENTA_EX+"Please reselect type the correct value!")
                menu()

        except:
            print(Fore.LIGHTMAGENTA_EX+"Please type the given correct order!")
            menu()


    clear()
    print(Fore.BLUE+"||------------------------\\\_________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen\\\ New Tab (+)\\\                                                                         ||")
    print(Fore.BLUE+"||--------------------------\\\------------\\\________________________________________________________________________||")
    print(Fore.YELLOW+"|___________|======|____________________________________|====|___________________________________|======|_____________|")
    print(Fore.LIGHTYELLOW_EX+"|-----------|DRINKS|------------------------------------|MEAL|-----------------------------------|SNACKS|-------------|")
    print(Fore.YELLOW+"|-----------|======|------------------------------------|====|-----------------------------------|======|-------------|")
    print(Fore.YELLOW+"|_____________________________________________________________________________________________________________________|")
    print(Fore.LIGHTYELLOW_EX+"|__||______________________||__||_______BREAKFAST_______||__||_________LUNCH__________||__________________________||__|")
    print(Fore.LIGHTYELLOW_EX+"|--||Water.........Php 7.00||--||Scrambled Egg..Php12.00||--||Fried Chicken...Php25.00||--||Kikiam........Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coca-cola.....Php12.00||--||Fried Rice.....Php10.00||--||Chicken Curry...Php25.00||--||Fishball......Php10.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Pepsi.........Php12.00||--||Hotdog.........Php 8.00||--||Pork Menudo.....Php20.00||--||Bananaque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Mountain Dew..Php15.00||--||Ham............Php12.00||--||Beef Steak......Php20.00||--||Camoteque.....Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Sprite........Php10.00||--||Tocino.........Php15.00||--||Caldereta.......Php20.00||--||Hotcake.......Php 5.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Milk..........Php15.00||--||                       ||--||                        ||--||Hamburger.....Php30.00||--|")
    print(Fore.LIGHTYELLOW_EX+"|--||Coffee........Php14.00||--||                       ||--||                        ||--||Cheeseburger..Php35.00||--|")
    print(Fore.YELLOW+"|--||**********************||--||***********************||--||************************||--||**********************||--|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.LIGHTYELLOW_EX+"|---------------------------------------------||Your Wallet:Php"+str(wallet)+"0 ||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------||=======================||---------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.YELLOW+"|---------------------------------------------------------------------------------------------------------------------|")
    print(Fore.MAGENTA+"Quantity:")

    for i in range(0, numOf_Orders):
        quantity = int(input(items[i]+": "))
        quantitys.append(quantity)
        total += quantitys[i] * price[i]
        i += 1
    clear()

    print(Fore.BLUE+"||--------------------------------\\\_________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen/receipt\\\ New Tab (+)\\\                                                                 ||")
    print(Fore.BLUE+"||----------------------------------\\\------------\\\________________________________________________________________||")
    print(Fore.LIGHTYELLOW_EX+"""                                                                                                                                     
                                                                                                                  
                                                                                                                  
                                                                                                                                                                                                                            
                                ██████╗ ███████╗ ██████╗███████╗██╗██████╗ ████████╗                                   
                                ██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔══██╗╚══██╔══╝                                   
                                ██████╔╝█████╗  ██║     █████╗  ██║██████╔╝   ██║                                      
                                ██╔══██╗██╔══╝  ██║     ██╔══╝  ██║██╔═══╝    ██║                                      
                                ██║  ██║███████╗╚██████╗███████╗██║██║        ██║                                      
                                ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝╚═╝        ╚═╝                                      
                                                                                                                  
    """)
    print("             ITEM                            QUANTITY                        PRICE                                     ")
    for i in range(numOf_Orders):
        print("            ",items[i],"                             x",quantitys[i],"                        Php",price[i]         )
    print("             Wallet:                                                         "+str(wallet)+"                           ")
    print("             Total:                                                          "+str(total)+"                            ")
    print("             Change:                                                         "+str(wallet - total)+"                   ")
    print("                                    WAIT FOR 10 SECONDS!!                                                               ")
    time.sleep(10)
    clear()
    print(Fore.BLUE+"||--------------------------------\\\_________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen/receipt\\\ New Tab (+)\\\                                                                 ||")
    print(Fore.BLUE+"||----------------------------------\\\------------\\\________________________________________________________________||")
    print(Fore.LIGHTGREEN_EX+"""
                             ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗██╗   ██╗ ██████╗ ██╗   ██╗
                             ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝╚██╗ ██╔╝██╔═══██╗██║   ██║
                                ██║   ███████║███████║██╔██╗ ██║█████╔╝  ╚████╔╝ ██║   ██║██║   ██║
                                ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗   ╚██╔╝  ██║   ██║██║   ██║
                                ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗   ██║   ╚██████╔╝╚██████╔╝
                                ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ 
                                                                      
                                                 ███████╗ ██████╗ ██████╗                          
                                                 ██╔════╝██╔═══██╗██╔══██╗                         
                                                 █████╗  ██║   ██║██████╔╝                         
                                                 ██╔══╝  ██║   ██║██╔══██╗                         
                                                 ██║     ╚██████╔╝██║  ██║                         
                                                 ╚═╝      ╚═════╝ ╚═╝  ╚═╝                         
                                                                      
                                ██████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗███╗   ██╗ ██████╗    
                                ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║████╗  ██║██╔════╝    
                                ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗   
                                ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║   
                                ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║██║██║ ╚████║╚██████╔╝   
                                 ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    
    """)
    input(Fore.LIGHTMAGENTA_EX+"Press any key to logout!: ")
    home()















def signup():
    clear()
    print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
    print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
    print(Fore.LIGHTYELLOW_EX+"""
                                    ███████╗██╗ ██████╗ ███╗   ██╗██╗   ██╗██████╗ 
                                    ██╔════╝██║██╔════╝ ████╗  ██║██║   ██║██╔══██╗
                                    ███████╗██║██║  ███╗██╔██╗ ██║██║   ██║██████╔╝
                                    ╚════██║██║██║   ██║██║╚██╗██║██║   ██║██╔═══╝ 
                                    ███████║██║╚██████╔╝██║ ╚████║╚██████╔╝██║     
                                    ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     
    """)

    fullname = input(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\t\tFullname: ")
    username = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tUsername: ")
    try:
        with open("database.txt") as file:
            if username in file.read():
                print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
                print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
                print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
                print(Fore.LIGHTYELLOW_EX+"""
                                                    ███████╗██╗ ██████╗ ███╗   ██╗██╗   ██╗██████╗ 
                                                    ██╔════╝██║██╔════╝ ████╗  ██║██║   ██║██╔══██╗
                                                    ███████╗██║██║  ███╗██╔██╗ ██║██║   ██║██████╔╝
                                                    ╚════██║██║██║   ██║██║╚██╗██║██║   ██║██╔═══╝ 
                                                    ███████║██║╚██████╔╝██║ ╚████║╚██████╔╝██║     
                                                    ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     
                    """)
                print(Fore.RED+"\n\n\t\t\t\t\t\tThis username is already exist!\n\n\n\n\n")
                time.sleep(3)
                signup()
            else:
                email = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tEmail Address: ")
                phone_number = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tPhone Number: ")
                password = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tPassword: ")
                password2 = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tConfirm Password: ")
    except:
        print(Fore.RED+"Input a valid Value!")
        signup()

    if len(password)<=6:
        clear()
        print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
        print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
        print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
        print(Fore.RED+"""
                                            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ ██╗
                                            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗██║
                                            █████╗  ███████║██║██║     █████╗  ██║  ██║██║
                                            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║╚═╝
                                            ██║     ██║  ██║██║███████╗███████╗██████╔╝██╗
                                            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝

                """)
        print(Fore.RED+"\n\n\t\t\t\t\t\tPassword is too short!, Please try Again!\n\n\n\n\n")
        time.sleep(3)
        signup()
    elif password != password2:
        clear()
        print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
        print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
        print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
        print(Fore.RED+"""
                                            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ ██╗
                                            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗██║
                                            █████╗  ███████║██║██║     █████╗  ██║  ██║██║
                                            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║╚═╝
                                            ██║     ██║  ██║██║███████╗███████╗██████╔╝██╗
                                            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝
                                                                                                     
        """)
        print(Fore.RED+"\n\n\t\t\t\t\t\tPassword didn't matched!, Please try Again!\n\n\n\n\n")
    else:
        clear()
        database = open("database.txt", "a+")
        db = ("Fullname: " + fullname +"\nUsername: "+username+"\nEmail Address: "+email+"\nPhone Number: "+phone_number+"\nPassword: "+password2+"\n\n")
        database.write(str(db))

        def ques():
            clear()
            print(Fore.BLUE+"||-----------------------\\\__________________________________________________________________________________________")
            print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Signup  \\\ New Tab (+)\\\                                                                          ||")
            print(Fore.BLUE+"||-------------------------\\\------------\\\_________________________________________________________________________||")
            print(Fore.LIGHTGREEN_EX+"""
                                                ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗██╗
                                                ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║
                                                ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗██║
                                                ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║╚═╝
                                                ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██╗
                                                ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝
                                                              
            """)
            login1 = input(Fore.RED+"\n\n\t\t\t\t\t\tYour Account was successfully created! Do you want to login?(Yes/No):")
            if login1 == "yes" or login1 == "YES" or login1 == "Yes":
                login()

            elif login1 == "no" or login1 == "NO" or login1 == "No":
                home()
            else:
                ques()

def login():
    clear()
    print(Fore.BLUE+"||----------------------\\\___________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/Login  \\\ New Tab (+)\\\                                                                           ||")
    print(Fore.BLUE+"||------------------------\\\------------\\\__________________________________________________________________________||")
    print(Fore.LIGHTYELLOW_EX+"""
                                           ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
                                           ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
                                           ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
                                           ██║     ██║   ██║██║   ██║██║██║╚██╗██║
                                           ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
                                           ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝       
    """)





    username = input(Fore.LIGHTMAGENTA_EX+"\n\n\n\n\t\t\t\t\tUsername: ")
    password = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\tPassword: ")

    with open("database.txt") as file:
        if username and password in file.read():
            clear()
            print(Fore.BLUE+"||------------------------\\\_________________________________________________________________________________________")
            print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph/E-Canteen\\\ New Tab (+)\\\                                                                         ||")
            print(Fore.BLUE+"||--------------------------\\\------------\\\________________________________________________________________________||")
            print(Fore.LIGHTYELLOW_EX+"""
                            ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗
                            ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║
                            ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║
                            ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
                            ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗
                             ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝

                             """)
            print(Fore.MAGENTA+"\n\n\t\t\t\t\t\t\t"+ username +"\n\n\n\n\n\n")
            time.sleep(3)
            clear()
            menu()







        else:
            print(Fore.RED+"wrong name or password")




def home():
    clear()
    print(Fore.BLUE+"||----------------\\\_________________________________________________________________________________________________")
    print(Fore.LIGHTCYAN_EX+"||Foodweb.evsu.ph  \\\ New Tab (+)\\\                                                                                 ||")
    print(Fore.BLUE+"||------------------\\\------------\\\________________________________________________________________________________||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTGREEN_EX+"||                                                 1. Signup                                                        ||")
    print(Fore.LIGHTGREEN_EX+"||                                                 2. Login                                                         ||")
    print(Fore.LIGHTGREEN_EX+"||                                                 3. Forgot Password                                               ||")
    print(Fore.LIGHTGREEN_EX+"||                                                 0. Exit                                                          ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||                                                                                                                  ||")
    print(Fore.LIGHTYELLOW_EX+"||__________________________________________________________________________________________________________________||")
    choice = int(input(Fore.LIGHTMAGENTA_EX+"\nRoot@Type: "))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        forgot_password()
    elif choice == 0:
        return 0
    else:
        clear()
        print(Fore.RED+"Please input the valid value: ")
        home()

home()
