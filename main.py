try:
    import time
    import os
    from pystyle import *

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    clear()
    condition = '''

    ╔════════════════════════════════════════════════════════════════════════╗
    ║                            TERMS OF SERVICE                            ║
    ╠════════════════════════════════════════════════════════════════════════╣
    ║ FROM ADMINISTRATION:                                                   ║
    ║ We are not responsible!!                                               ║
    ║ Before using this tool, you must accept our conditions, to confirm     ║
    ║ and undertake that we will not be responsible for any damage you have  ║         
    ║ caused to the damaged website.                                         ║
    ╚════════════════════════════════════════════════════════════════════════╝'''

    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_red)), Center.XCenter(condition)))
    tos = input("Input (Y/N): ")

    def attack():
        clear()
        banner1 = '''
     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
    ███████║   ██║      ██║   ███████║██║     █████╔╝ 
    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
           ╚══════╦═══════════════════╦══════╝             
    ╔═════════════╩═══════════════════╩═════════════╗
    ║  ╔═╗╔╗ ╔═╗  ╔╦╗╔╦╗╔═╗╔═╗         Method       ║
    ║  ╠═╣╠╩╗║     ║║ ║║║ ║╚═╗   [1] GET  [2] POST  ║
    ║  ╩ ╩╚═╝╚═╝  ═╩╝═╩╝╚═╝╚═╝    [#] QuangHuwngg   ║
    ╚═══════════════════════════════════════════════╝'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_red)), Center.XCenter(banner1)))
        target = input("├───┐\n│   ├───TARGET: ")
        method = input("│   └───METHOD: ")

        if method in ["1", "get", "GET"]:
            method = "get"
        elif method in ["2", "post", "POST"]:
            method = "post"
        else:
            method = "get"

        os.system(f"go run resources/main.go -site {target} -data {method}")

    def update():
        clear()
        banner2 = '''
    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
     ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
            ╚══════╦═══════════════════╦══════╝             
     ╔═════════════╩═══════════════════╩═════════════╗
     ║  ╔═╗╔╗ ╔═╗  ╔╦╗╔╦╗╔═╗╔═╗  Update new version  ║
     ║  ╠═╣╠╩╗║     ║║ ║║║ ║╚═╗          [+]         ║
     ║  ╩ ╩╚═╝╚═╝  ═╩╝═╩╝╚═╝╚═╝   [#] QuangHuwngg    ║
     ╚═══════════════════════════════════════════════╝'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_red)), Center.XCenter(banner2)))
        time.sleep(1)
        print("Installing new version")
        os.system("git pull")
        time.sleep(2)
        home()

    def home():
        clear()
        banner = '''
         █████╗ ██████╗  ██████╗    ██████╗ ██████╗  ██████╗ ███████╗
        ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
        ███████║██████╔╝██║         ██║  ██║██║  ██║██║   ██║███████╗
        ██╔══██║██╔══██╗██║         ██║  ██║██║  ██║██║   ██║╚════██║
        ██║  ██║██████╔╝╚██████╗    ██████╔╝██████╔╝╚██████╔╝███████║
        ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                    ╚══════╦═══════════════════╦══════╝               
             ╔═════════════╩═══════════════════╩═════════════╗
             ║  ╔═╗╔╗ ╔═╗  ╔╦╗╔╦╗╔═╗╔═╗   [1] Create Attack  ║
             ║  ╠═╣╠╩╗║     ║║ ║║║ ║╚═╗   [2] Update Version ║
             ║  ╩ ╩╚═╝╚═╝  ═╩╝═╩╝╚═╝╚═╝   [#] QuangHuwngg    ║
             ╚═══════════════════════════════════════════════╝'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))
        while True:
            player = input("Input ~> ")
            if player in "1":
                time.sleep(1)
                attack()
            elif player in "2":
                time.sleep(1)
                update()
            elif player in "exit":
                exit("GOODBYE")
            else:
                print(f"Command: [ {player} ] Not Found!")

    if tos in ["y", "Y"]:
        time.sleep(1)
        home()
    elif tos in ["n", "n"]:
        exit("GOODBYE")
    else:
        exit("GOODBYE")
except:
    os.system("pip install pystyle")
    os.system("pip install pyarmor")