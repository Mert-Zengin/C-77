from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time

global starttime

class ZeroScann():

    def __init__(self):
        self.scan()
        
    def scan(self):
        # argument parser like shit
        parser = argparse.ArgumentParser(prog="wordlist.txt", description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[36musage: scan -u example.com -w wordlist.txt")
        if not args.wordlist:
            sys.exit("\033[36musage: scan -u example.com -w wordlist.txt")
            
        # handle url website format
        site = args.domain
        print("\033[32;1m   _______ __                            __        _______ _______      ")
        print("\033[32;1m   |   _   |  |--.-----.--------.-----.--|  |______|   _   |   _   |")
        print("\033[32;1m   |.  1___|     |  -__|        |  _  |  _  |______|___|   |___|   |")
        print("\033[32;1m   |.  |___|__|__|_____|__|__|__|_____|_____|         /   /   /   /")
        print("\033[32;1m   |:  1   |                                         |   |   |   |")
        print("\033[32;1m   |::.. . |          \033[96m   Shell-Finder  \033[32;1m              |   |   |   |")
        print("\033[32;1m   `-------'                                         `---'   `---'","\n")
        
        
       
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("  \033[91mUpss, Wordlist tidak di temukan!\033[0m")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("  \033[91mWordlist Tidak Di Temukan!\033[0m")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("\033[96m------------\033[33;1m> \033[92mfound:","\033[0m/"+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("\033[96m------------\033[33;1m> \033[91merror:","\033[0m/"+psx)
                    else:
                        print("\033[96m------------\033[33;1m> \033[92minfo :","\033[33m/"+psx,"\033[92mstatus:\033[33m",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("\033[31m Upss, Domain yg anda masukan eror！")
                except Exception as er:
                    print("\n\033[96m----> \033[0mKoneksi Internet Anda Buruk!")
                    print("\n\033[96m----> \033[0mExit Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("\n\033[96m----> \033[0mAnda Menekan Tombol CTRL+C")
                print("\n\033[96m----> \033[0mAnda Akan Keluar Dari Program")
                time.sleep(2)
                exit()
        
        if found:
            print("\n\033[96m----> \033[0mFiles Yg Di Temukan\033[92m")
            print("\n".join(found))
            print("\033[96m----> \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("\n\033[96m----> \033[0mTidak Di Temukan Files Apapun!")
            print("\n\033[96m----> \033[0mSepertinya Wordlist Anda Kurang Detail")
                
    def banner():
        # just the screen display like this
        info = """\033[33m
	
	
	
              """
        return info
    print(banner())
                
if __name__ == '__main__':
    ZeroScann()
