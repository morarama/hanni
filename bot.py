# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,datetime,subprocess,urllib3,os,requests,urllib,goslate,pyown
from bs4 import BeautifulSoup
from threading import Thread
from pyowm import OWM

cl = LINETCR.LINE()
cl.login(token="Em1MLKWf2rYhXqF6Izb8.t0uzqyjD9cgRN/IdWhSi2a.MJJqIhbXAZuk9CL7DbotNLpfdAAXj5daZgF5RNGTLu4=")
cl.loginResult()

kk = LINETCR.LINE()
kk.login(token="EmqyfGRzG8shyaxxyxva.h3KqNoP0JeN8FrJP6uiJoG.65n8x0QhvQulMeOArHx3qyz52in9QZbKWiCG2tE+Tvk=")
kk.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmcdGcr39siPjyfjUHU8.DTbDh/XY1svG6guOLGgrEa.J9aK10nBHHPamoTrpNycY3jwIpaokHSUe4DKrMyCblM=")
ki.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmKkIYjfelsmgNiXTIh2.KpKWyorTPY1wwWUHFd03OG.yUrwPRkpJqbiZ1tohkh7+SpX1TWpUP+/RVUdTkhEgAg=")
kc.loginResult()

print "Login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 􀜁􀅹Salute􏿿 | Keyboard Member | 􀜁􀅹Salute􏿿

[􀜁􀅹Salute􏿿] Hi  (yah begitulah)
[􀜁􀅹Salute􏿿] Creator ( Creator / Admin )
[􀜁􀅹Salute􏿿] Me ( Info Contact )
[􀜁􀅹Salute􏿿] Gift ( Gift Thema )
[􀜁􀅹Salute􏿿] Ginfo ( Group info )
[􀜁􀅹Salute􏿿] Welcome ( yah begitulah )
[􀜁􀅹Salute􏿿] Cancel ( Cancel member pending )
[􀜁􀅹Salute􏿿] Tagall ( Tagall member group )
[􀜁􀅹Salute􏿿] pp @tag ( PP yang di tag )
[􀜁􀅹Salute􏿿] cover @tag ( Cover yang di tag )
[􀜁􀅹Salute􏿿] Kedapkedip ( Teks kekinian 􀜁􀅔Har Har􏿿 , Contoh : Kedapkedip  )
[􀜁􀅹Salute􏿿] /apakah ( Kerang ajaib )
[􀜁􀅹Salute􏿿] /translate-en ( Translate Indo - EN , Contoh : /translate-en Grup ) 
[􀜁􀅹Salute􏿿] /set ( Set point )
[􀜁􀅹Salute􏿿] /check ( Check sider )
[􀜁􀅹Salute􏿿] /lagu ( Cari lagu , Contoh : /lagu iwan fals ibu )
[􀜁􀅹Salute􏿿] /lirik ( Cari Lirik , Contoh : /lirik Payung teduh Akad )
[􀜁􀅹Salute􏿿] /ig ( Cek profile Instagram , Contoh : /ig instagram )
[􀜁􀅹Salute􏿿] /youtube ( Scrap link youtube , Contoh : /youtube young dumb & broke )

􀜁􀅹Salute􏿿 | Keyboard (Admin) | 􀜁􀅹Salute􏿿

[􀜁􀅹Salute􏿿] bye # Mengusir Bot (Di Aktifin Admin)
[􀜁􀅹Salute􏿿] /unban > Tidak Di Banned
[􀜁􀅹Salute􏿿] /ban > Target Di Banned
[􀜁􀅹Salute􏿿] join > Membawa Pasukan (4 Bot)
[􀜁􀅹Salute􏿿] ourl > Open Link Grup *Tanpa Staaff/Admin
[􀜁􀅹Salute􏿿] curl > Menutup Link Grup *Tanpa Staff/Admin
[􀜁􀅹Salute􏿿] /spam (Jumlah) (Kata) > Menyempam Kata

[􀜁􀅹Salute􏿿] /nk @tag -> Mengkick Target
[􀜁􀅹Salute􏿿] /bcgc -> Untuk Broadcast Group
[􀜁􀅹Salute􏿿] /bc -> Untuk Broadcast Melalui Pc
[􀜁􀅹Salute􏿿] /grup id -> Mengentahui Grup List
[􀜁􀅹Salute􏿿] /bio -> Mengedit Bio
[􀜁􀅹Salute􏿿] /gn -> Mengganti Nama Grup
[􀜁􀅹Salute􏿿] /cn -> Mengganti Nama Bot 1,2,3,4
[􀜁􀅹Salute􏿿] /removechat -> remove chat
[􀜁􀅹Salute􏿿] kill -> kick yang ban

[􀜁􀅹Salute􏿿] contact on/off
[􀜁􀅹Salute􏿿] join on/off
[􀜁􀅹Salute􏿿] Gcancel on/off
[􀜁􀅹Salute􏿿] leave on/off
[􀜁􀅹Salute􏿿] protect on/off
[􀜁􀅹Salute􏿿] qr on/off
[􀜁􀅹Salute􏿿] invite on/off
[􀜁􀅹Salute􏿿] cancel on/off

[􀜁􀅹Salute􏿿] Mulai -> Meratakan  [􀜁􀅹Salute􏿿]"""

KAC=[cl,ki,kk,kc]
dmid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots = [dmid,Amid,Bmid,Cmid]
admin = ["u4f451941825df421ab9fe883c07b08d8"]
staff = ["u4f451941825df421ab9fe883c07b08d8"]
adminMID = "u4f451941825df421ab9fe883c07b08d8"
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    "lang":"JP",
    "comment":"Like Back",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":False,
    "protect":False,
    "cancelprotect":True,
    "inviteprotect":False,
    "linkprotect":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += '\n ☞ ' + Name
                    wait2['ROM'][op.param1][op.param2] = '☞ ' + Name
            else:
                pass

        if op.type == 13:
                if op.param3 in dmid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in dmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
                if dmid in op.param3:
                    if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                        print "Bot 1 Join"
                        cl.sendText(op.param1,'Hallo Generasi, Hormat 􀜁􀅹Salute􏿿')
                        cl.sendText(op.param1,'Daftar Command? Ketik /help')
                    else:
                        print "Error"
                if Amid in op.param3:
                    if wait["autoJoin"] == True:
                        ki.acceptGroupInvitation(op.param1)
                        print "Bot 2 Join"
                        ki.sendText(op.param1,'welcome')
                    else:
                        print "Error"
                if Bmid in op.param3:
                    if wait["autoJoin"] == True:
                        kk.acceptGroupInvitation(op.param1)
                        print "Bot 3 Join"
                        kk.sendText(op.param1,'apa kabar generasi jaman now')
                    else:
                        print "Error"
                if Cmid in op.param3:
                    if wait["autoJoin"] == True:
                        kc.acceptGroupInvitation(op.param1)
                        print "Bot 4 Join"
                        kc.sendText(op.param1,'dasar generasi micin')
                    else:
                        print "Error"

        if op.type == 19:
                    if op.param3 in Bots:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[Bots])

        if op.type == 19:
                if dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                        kc.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                        kk.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                        kk.inviteIntoGroup(op.param1,[op.param1,[op.param3]])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if dmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(G)
#           random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
#               random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            elif wait["inviteprotect"] == True:
                cl.cancelGroupInvitation(op.param1,[op.param3])
#                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 not in Bots:
                    if op.param2 in Bots:
                        pass
                    elif wait["cancelprotect"] == True:
                        cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            elif wait["linkprotect"] == True:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
#                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                cl.sendText(op.param1,"")

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ub95ceaf08031da4a7478016ac1ed1f3dd":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 0:
                    if msg.to in wait2['readPoint']:
                        if msg.from_ in wait2["ROM"][msg.to]:
                            del wait2["ROM"][msg.to][msg.from_]
                    else:
                        pass
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"added")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + msg.contentMetadata["displayName"] + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + contact.displayName + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#----------------------------------------------------------------------------
#---------------------------- HELP COMMAND ----------------------------------
            elif msg.text.lower() in ["key","help","/help","/key"]:
                cl.sendText(msg.to,helpMessage)
#----------------------------------------------------------------------------
#---------------------------- SPAM CHAT -------------------------------------
            elif "/spam " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace("/spam " + str(jmlh) + " ","")
                    if jmlh <= 999:
                        for x in range(jmlh):
                            cl.sendText(msg.to,teks)
#----------------------------------------------------------------------------
#---------------------------- CHANGE GROUP NAME -----------------------------
            elif "/gn " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("/gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
#----------------------------------------------------------------------------
#-------------------------------- MID ---------------------------------------
            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------- CREATOR ------------------------------------
            elif msg.text.lower() in ["creator","admin"]:
                msg.contentType = 13
                adm = 'ube187443474747c3ec352e7efeb48c1b'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Instagram : @dekaprabowoo\nNama : Aked\nZodiak : Taurus")
#----------------------------------------------------------------------------
#--------------------------------- GIFT -------------------------------------
            elif msg.text.lower() in ["gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------ CANCEL PENDING ------------------------------
            elif msg.text.lower() in ["cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ OPEN URL ------------------------------------
            elif msg.text.lower() in ["ourl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tolong Tutup")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ CLOSE URL -----------------------------------
            elif msg.text.lower() in ["curl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Bagus Sudah Tutup")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GET GROUP LINK ------------------------------
            elif  msg.text.lower() in ["gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,x.name + " : line://ti/g/" + gurl)
                    print "[Command] Get Grup Link"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GROUP INFO ----------------------------------
            elif msg.text.lower() in ["ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"􀜁􀅹Salute􏿿 Grup Name 􀜁􀅹Salute􏿿 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n􀜁􀅹Salute􏿿 Grup Creator 􀜁􀅹Salute􏿿 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nTotal Anggota : " + str(len(ginfo.members)) + " Orang\nPending : " + sinvitee + " Orang")#URL : " + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"􀜁􀅹Salute􏿿 Grup Name 􀜁􀅹Salute􏿿 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n􀜁􀅹Salute􏿿 Grup Creator 􀜁􀅹Salute􏿿 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Grup Only Boy")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#---------------------------------- MID -------------------------------------
            elif msg.text.lower() in ["mid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)
#----------------------------------------------------------------------------
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Bacod"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Ngakak"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Payah"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Siapa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Lah"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Anjir"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Sedih"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
#------------------------------ CHANGE NAME ---------------------------------
            elif "/cn " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/cn ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------
#------------------------------ CHANGE BIO ----------------------------------
            elif "/bio " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------                    
            elif msg.text.lower() in ["contact on"]:
                if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")

            elif msg.text.lower() in ["contact off"]:
                if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")

            elif msg.text.lower() in ["join on"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")

            elif msg.text.lower() in ["join off"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")

            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text.lower() in ["leave on"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")

            elif msg.text.lower() in ["leave off"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")

            elif msg.text.lower() in ["protect on"]:
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")

            elif msg.text.lower() in ["protect off"]:
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")

            elif msg.text.lower() in ["qr on"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")

            elif msg.text.lower() in ["qr off"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")

            elif msg.text.lower() in ["invite on"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")

            elif msg.text.lower() in ["invite off"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")

            elif msg.text.lower() in ["cancel on"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")

            elif msg.text.lower() in ["cancel off"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
#------------------------------ STATUS BOT ----------------------------------
            elif "/status" in msg.text.lower():
                md = ""
                if wait["contact"] == True: md+="[*] Contact : on\n"
                else: md+="[*] Contact : off\n"
                if wait["autoJoin"] == True: md+="[*] Auto join : on\n"
                else: md +="[*] Auto join : off\n"
                if wait["leaveRoom"] == True: md+="[*] Auto leave : on\n"
                else: md+="[*] Auto leave : off\n"
                if wait["autoAdd"] == True: md+="[*] Auto add : on\n"
                else:md+="[*] Auto add : off\n"
                if wait["protect"] == True: md+="[*] Protect : on\n"
                else:md+="[*] Protect : off\n"
                if wait["linkprotect"] == True: md+="[*] Link Protect : on\n"
                else:md+="[*] Link Protect : off\n"
                if wait["inviteprotect"] == True: md+="[*] Invite Protect : on\n"
                else:md+="[*] Invite Protect : off\n"
                if wait["cancelprotect"] == True: md+="[*] Cancel Protect : on"
                else:md+="[*] Cancel Protect : off"
                cl.sendText(msg.to,md)
#----------------------------------------------------------------------------
#---------------------------- GROUP ID / LIST--------------------------------
            elif msg.text.lower() in ["/grup id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)

            elif msg.text.lower() in ["/list grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s \n" % (cl.getGroup(i).name + " : " + str(len(cl.getGroup(i).members)) + " Members")
                    cl.sendText(msg.to,"「List Group」\n" + h + "Total Group : " + str(len(gid)))
#----------------------------------------------------------------------------
#------------------------------ CANCEL GROUP --------------------------------
            elif msg.text.lower() in ["cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Done")
                else:
                    cl.sendText(msg.to,"Nothing invite.")
#----------------------------------------------------------------------------
#------------------------------- JOIN GROUP ---------------------------------
            elif msg.text.lower() in ["join"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "[Command] Join"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#----------------------------------------------------------------------------
#-------------------------------- OUT GROUP ---------------------------------
            elif msg.text.lower() in ["bye"]:
                if msg.toType == 2:
                  if msg.from_ in admin:
                    print "[Command] Bye"
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------------------------------------
#------------------------------ BROADCAST PC --------------------------------
            elif "/bc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bc ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"
#----------------------------------------------------------------------------
#----------------------------- BROADCAST Group ------------------------------
            elif "/bcgc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bcgc ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"
#----------------------------------------------------------------------------
#-------------------------------- WELCOME -----------------------------------
            if msg.text.lower() in ["wc","welcome"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di " + str(ginfo.name))
#----------------------------------------------------------------------------
#------------------------------- KICK BY TAG --------------------------------
            elif "nk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                      print "[Command] Kick"
                   except:
                      pass
#----------------------------------------------------------------------------
#------------------------------ BAN BY TAG ----------------------------------
            elif "/ban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "/unban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#----------------------------- TAG ALL MEMBER -------------------------------
            if msg.text.lower() in ["tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#----------------------------------------------------------------------------
#------------------------------- CHECK SIDER --------------------------------
            if msg.text.lower() in ["/set"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "Sini Muncul")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Set"

            if msg.text.lower() in ["/check"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ Read : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] Set"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik /set untuk membuat Read point.")
#----------------------------------------------------------------------------
#------------------------------- COVER BY TAG -------------------------------
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
#--------------------------------- HI / HAI ---------------------------------
            elif msg.text.lower() in ["hi","hai","apa"]:
                if msg.from_ in admin:
                    beb = "Hi sayang " + cl.getContact(msg.from_).displayName #+ " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,beb)
                else:
                    hi = "Hi " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
#----------------------------------------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#----------------------------------------------------------------------------
#--------------------------------- Remove Chat ------------------------------
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#----------------------------------------------------------------------------
#------------------------------- Kerang Ajaib -------------------------------
            elif "/apakah " in msg.text.lower():
                apk = msg.text.replace("/apakah ","")
                rnd = ['Ya','Tidak']
                p = random.choice(rnd)
                cl.sendText(msg.to,p)
                print "[Command] Kerang Ajaib"
#----------------------------------------------------------------------------
#---------------------------------- SONG ------------------------------------
            elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif "/lagu " in msg.text.lower():
                songname = msg.text.replace("/lagu ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])
                    print "[Command] Lagu"
#----------------------------------------------------------------------------
#--------------------------------- INSTAGRAM --------------------------------
            elif "/ig " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig hairu.ones")
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#----------------------------------------------------------------------------
#--------------------------------- ABSEN ------------------------------------
            elif msg.text.lower() in ["absen"]:
                cl.sendText(msg.to,"Hadir Bosku ????Salute??")
                ki.sendText(msg.to,"Hadir  ????Salute??")
                kk.sendText(msg.to,"Selalu Hadir ????Salute??")
                kc.sendText(msg.to,"Come Back ????Salute??")
#----------------------------------------------------------------------------
#------------------------------ RESPON SPEED --------------------------------
            elif msg.text.lower() in ["respon"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Respon : %s Seconds" % (elapsed_time))
#----------------------------------------------------------------------------
#---------------------------- CEK BAN LIST ----------------------------------
            elif msg.text.lower() in ["banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "[*] " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#----------------------------------------------------------------------------
#------------------------- CEK BAN LIST ( MID ) -----------------------------
            elif msg.text.lower() in ["banlist mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
#----------------------------------------------------------------------------
#-------------------------------- KILL BAN ----------------------------------
            elif msg.text.lower() in ["kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        pass
#----------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        pass


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
