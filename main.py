o=True
n='title '
m=range
f='space'
e=False
d='cls'
R=str
K=int
C=print
import subprocess as g,requests as L,time as H,os,mss,requests as L,random as S
from colorama import Fore as B,Style as A,init,Back
h='https://zentoxdev.github.io/randomtitle.txt'
i=L.get(h).text
T=i.split()
os.system(n+S.choice(T))
U=g.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
j=L.get('https://zentoxdev.github.io/hwid_auth.txt')
try:
	if U in j.text:0
	else:os.system(d);C(A.BRIGHT+B.RED+'[HATA] Üyeliğin Bulunamadı!');C(A.BRIGHT+B.GREEN+f"Üyelik Kodu: {U}");H.sleep(5);os._exit()
except:os.system(d);os.startfile('https://discord.gg/agjfbsgDtT');C(A.BRIGHT+B.RED+'Üyelik satın almak için yönlendiriliyorsunuz...');H.sleep(3);os._exit()
import keyboard as F,pyautogui as V,time as H,ctypes as W,PIL.ImageGrab,PIL.Image,winsound as D,os
X,Y=PIL.ImageGrab.grab().size
Z,a,c=250,100,250
J=31
G=10
M='ctrl + alt'
N='ctrl + tab'
O='ctrl + up'
P='ctrl + space'
Q='ctrl + down'
k=['YAVAŞ','ORTA','HIZLI']
V.FAILSAFE=e
class b(Exception):0
class l:
	def __init__(A):A.toggled=e;A._bunny=e;A.mode=1;A.last_reac=0
	def toggle(A):A.toggled=not A.toggled
	def bunnyy(A):A._bunny=not A._bunny
	def switch(A):
		if A.mode!=2:A.mode+=1
		else:A.mode=0
		if A.mode==0:D.Beep(200,200)
		if A.mode==1:D.Beep(200,200),D.Beep(200,200)
		if A.mode==2:D.Beep(200,200),D.Beep(200,200),D.Beep(200,200)
	def click(A):W.windll.user32.mouse_event(2,0,0,0,0);W.windll.user32.mouse_event(4,0,0,0,0)
	def approx(A,r,g,b):return Z-J<r<Z+J and a-J<g<a+J and c-J<b<c+J
	def grab(D):
		with mss.mss()as B:C=K(X/2-G),K(Y/2-G),K(X/2+G),K(Y/2+G);A=B.grab(C);return PIL.Image.frombytes('RGB',A.size,A.bgra,'raw','BGRX')
	def scan(A):
		B=H.time();C=A.grab()
		try:
			for D in m(0,G*2):
				for E in m(0,G*2):
					F,J,L=C.getpixel((D,E))
					if A.approx(F,J,L):raise b
		except b:
			A.last_reac=K((H.time()-B)*1000);A.click()
			if A.mode==0:H.sleep(0.5)
			if A.mode==1:H.sleep(0.25)
			if A.mode==2:H.sleep(0.2)
			I(A)
	def bunny(A):
		while o:
			if F.is_pressed(f):V.press(f)
			else:break
def I(bot):I='Kapalı';H='Açık';F='================== V ==================';E='';D=bot;os.system(n+S.choice(T));os.system(d);C(E);C(B.RED+'   ██╗   ██╗ █████╗ ██╗      ██████╗ ██╗  ██╗'+A.RESET_ALL);C(B.RED+'   ██║   ██║██╔══██╗██║     ██╔═══██╗╚██╗██╔╝'+A.RESET_ALL);C(B.RED+'   ██║   ██║███████║██║     ██║   ██║ ╚███╔╝ '+A.RESET_ALL);C(B.RED+'   ╚██╗ ██╔╝██╔══██║██║     ██║   ██║ ██╔██╗ '+A.RESET_ALL);C(B.RED+'    ╚████╔╝ ██║  ██║███████╗╚██████╔╝██╔╝ ██╗'+A.RESET_ALL);C(B.RED+'     ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝'+A.RESET_ALL);C(E);C(A.BRIGHT+B.GREEN+'Üyelik Süresi = '+B.YELLOW+'[Sınırsız]'+A.RESET_ALL);C(E);C(A.BRIGHT+B.YELLOW+'============ Website ============');C(A.BRIGHT+B.MAGENTA+'      zentoxdev.github.io');C(A.BRIGHT+B.YELLOW+'=============== V ===============');C(E);C(A.BRIGHT+B.RED+'============= Kontroller =============='+A.RESET_ALL);C(A.BRIGHT+B.BLUE+'|         Aktifleştirme Tuşu           |:',B.YELLOW+M+A.RESET_ALL);C(A.BRIGHT+B.BLUE+'|        Mod Değiştirme Tuşu           |:',B.YELLOW+N+A.RESET_ALL);C(A.BRIGHT+B.BLUE+'|          Bunny Hop Tuşu              |:',B.YELLOW+P+A.RESET_ALL);C(A.BRIGHT+B.BLUE+'|         Yakalama Alanı Ayar          |:',B.YELLOW+O+'/'+Q+A.RESET_ALL);C(A.BRIGHT+B.RED+F+A.RESET_ALL);C(E);C(A.BRIGHT+B.BLUE+'============ Bilgilendirme ============'+A.RESET_ALL);C(A.BRIGHT+B.RED+'|                 Mod                  |:',B.CYAN+k[D.mode]+A.RESET_ALL);C(A.BRIGHT+B.RED+'|            Yakalama Alanı            |:',B.CYAN+R(G)+'x'+R(G)+A.RESET_ALL);C(A.BRIGHT+B.RED+'|            Trigger Durumu            |:',(B.GREEN if D.toggled else B.RED)+(H if D.toggled else I)+A.RESET_ALL);C(A.BRIGHT+B.RED+'|             Bunny Durumu             |:',(B.GREEN if D._bunny else B.RED)+(H if D._bunny else I)+A.RESET_ALL);C(A.BRIGHT+B.RED+'|         Son Reaksiyon Süresi         |:',B.CYAN+R(D.last_reac)+A.RESET_ALL+' ms ('+R(D.last_reac/(G*G))+'ms/pix)');C(A.BRIGHT+B.BLUE+F+A.RESET_ALL)
if __name__=='__main__':
	E=l();I(E)
	while o:
		if F.is_pressed(N):
			E.switch();I(E)
			while F.is_pressed(N):0
		if F.is_pressed(O):
			G+=5;I(E);D.Beep(400,200)
			while F.is_pressed(O):0
		if F.is_pressed(Q):
			G-=5;I(E);D.Beep(300,200)
			while F.is_pressed(Q):0
		if F.is_pressed(M):
			E.toggle();I(E)
			if E.toggled:D.Beep(440,75),D.Beep(700,100)
			else:D.Beep(440,75),D.Beep(200,100)
			while F.is_pressed(M):0
		if F.is_pressed(P):
			E.bunnyy();I(E)
			if E._bunny:D.Beep(440,75),D.Beep(700,100)
			else:D.Beep(440,75),D.Beep(200,100)
			while F.is_pressed(P):0
		if E.toggled:E.scan()
		if E._bunny:
			if F.is_pressed(f):E.bunny()