o
    ?.b	?  ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dl
mZ d dlmZmZmZ d dl	mZmZmZmZ d dlmZ d dlmZmZmZmZmZmZmZ d dlmZmZm Z m!Z!m"Z"m#Z#m$Z$m%Z%m&Z& d dl'm(Z(m)Z) d d	l*m+Z+ d d
l,m-Z-m.Z. d dl/m0Z0m1Z1m2Z2 d dl3m4Z4 d dl5m6Z6m7Z7m8Z8m9Z9m:Z:m;Z;m<Z<m=Z= d dl>m?Z? dZ@dZAdZdZBdZCdZDejE?Fd?s?e?Gd? ejE?Fd?s?eHdd? dd? ZIdd? ZJdd? ZKdd? ZLd d!? ZMd"d#? ZNd$d%? ZOd&d'? ZPd(d)? ZQejRZSejTZUejVZWejXZYejZZCej[Z\ej]ZBeUeWeYeCe\eBgZ^d*d+? Z_d,d-? Z`d.d/? Zad0d1? Zbd2d3? Zcd4d5? Zdd6d7? Zed8d9? Zfd:d;? Zgeg?  dS )<?    N)?reader)?MINYEAR?datetime?	timedelta)?Fore?Back?Style?init)?TelegramClient)?	functions?typesr
   ?
connection?sync?utils?errors)	?InputPeerEmpty?UserStatusOffline?UserStatusRecently?UserStatusLastMonth?UserStatusLastWeek?PeerUser?PeerChannel?InputPeerChannel?InputPeerUser)?GetContactsRequest?DeleteContactsRequest)?DeletePhotosRequest)?GetDialogsRequest?ImportChatInviteRequest)?GetFullChannelRequest?JoinChannelRequest?InviteToChannelRequest)?SessionPasswordNeededError)?UsernameInvalidError?ChannelInvalidError?PhoneNumberBannedError?YouBlockedUserError?PeerFloodError?UserPrivacyRestrictedError?ChatWriteForbiddenError?UserAlreadyParticipantError)?StringSessioni?$ Z 7e14b38d250953c8c1e94fd7b2d63550z[1;31mz[1;32mz[1;36mz[1,35mz
./sessions?	phone.csv?wc                  C   s?   t ?  tdd??F} dd? t?| ?D ?}d}|D ]-}t?|?}|d7 }ttjt	j
 d|? ? ? td|? ?tt?}|?|? |??  t?  qd	}W d   ? n1 sQw   Y  t|ratjt	j d
 nd? ttjt	j d ? t?  d S )Nr,   ?rc                 S   ?   g | ]}|d  ?qS ?r   ? ??.0?rowr1   r1   ?/storage/emulated/0/k/rex.py?
<listcomp>'   ?    zlogin.<locals>.<listcomp>r   ?   ?Login ?	sessions/TzAll Number Login Done !?Error!zPress Enter to back)?banner?open?csvr   r   ?parse_phone?printr   ?BRIGHTr   ?GREENr
   ?API_ID?HashID?start?
disconnect?RESET?YELLOW?input)?f?str_list?po?pphone?phone?client?doner1   r1   r5   ?login!   s"   

?
rQ   c               
   C   s?  t t?} tt?}g }d}tdd???}dd? t?|?D ?}d}|D ]T}|d7 }t?|?}t	d|? ?? t
d	|? ?| |?}	|	??  |	?? sqzt	d
? t|?}
t|?}|?|? W q  typ   t	d? t|?}
t|?}|?|? Y q w t	?  q d}t	d? t	|ddi? t	d? tdddd??}tj|ddd?}|?|? W d   ? n1 s?w   Y  W d   ? n1 s?w   Y  dd? }dd? }|?  |?  t|r?d? d S d? d S )NFr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   >   r7   zBanFilter.<locals>.<listcomp>r   r8   r9   r:   zThis Phone Has Been RevokedZBanTzList Of Banned Numbers?sep?
zSaved In BanNumers.csv?BanNumbers.csvr-   ?UTF-8??encoding?,?Z	delimiter?lineterminatorc               	   S   s^  g } g }g }g }g }t dd??}|D ]}| ?|? qW d   ? n1 s$w   Y  | D ]}t|??dd?}|?|? q+t d??+}t dd??}	|D ]}|	?|?dd?? qHW d   ? n1 s^w   Y  W d   ? n1 smw   Y  t dd??}	|	D ]}
|?|
? qzW d   ? n1 s?w   Y  |D ]}t|??dd?}|?|? q?t|?}t|?}|?|?}|D ]}||vr?|?|? q?t d	dd
d??}tj|dd?}|?	|? W d   ? n1 s?w   Y  t d	??0}t dd??}|D ]}t|??dd?}|?|? q?W d   ? n	1 ?s	w   Y  W d   ? n	1 ?sw   Y  t
?d? t
?d	d? td? d S )Nr,   r.   rS   ? rT   zoutfile.csvr-   rX   ?	unban.csvrU   rV   )rZ   z(Done,All Banned Number Have Been Removed)r=   ?append?str?replace?write?set?intersectionr>   ?writer?	writerows?os?remove?renamer@   )Z
collectionZncZcollection1Znc1Zmaind?infile?line?xZmod_x?outfileZline1?iZmod_i?uniqueZunique1Zitd?	writeFilerc   Zlast?finalZline3r1   r1   r5   ?
autoremovef   sd   ????? ??

????? 
zBanFilter.<locals>.autoremovec               	   S   s?   dd l } dd l}td??+}tdd??}|D ]}|?|?dd?? qW d   ? n1 s+w   Y  W d   ? n1 s:w   Y  |?d? |?dd? td? d S )Nr   r,   r\   r-   rX   r[   Zcomplete)r>   re   r=   r`   r_   rf   rg   r@   )r>   re   rh   rk   ri   r1   r1   r5   ?dellst?   s   ??? 
zBanFilter.<locals>.dellst?Done!r;   )?intrC   r^   rD   r=   r>   r   r   r?   r@   r
   ?connect?is_user_authorizedr]   r%   rc   rd   rI   )?api_id?api_hashZMadeByHackingZonerP   rJ   rK   rL   Zunparsed_phonerN   rO   ?HackingZoneZNero_oprn   rc   rp   rq   r1   r1   r5   ?	BanFilter6   sV   


?	???)4ry   c               
   C   sV  t ?  d} d}d}d}d}tdd??}}dd	? t?|?D ?}d}|D ]f}t?|?}	|d
7 }ttjt	j
 dtj? dtjt	j ? d|	? ? ? td|	? ?tt?}
|
?|	? |
tjjdd?? |
?| d? t?d
? t|
?| ??}||v rzt|? |d
7 }ntd? |
??  t?  d}q!W d   ? n1 s?w   Y  t|? d?? t|r?d? d S d? d S )NZSpamBotuT   Good news, no limits are currently applied to your account. You’re free as a bird!Zbirdr   Fr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   ?   r7   z"SpamBotChecker.<locals>.<listcomp>r8   r9   ? r:   z@SpamBot??idz/startzyou are limitedTz - Accounts Are Usablerr   r;   )r<   r=   r>   r   r   r?   r@   r   rA   r   rB   ?	RESET_ALLrG   r
   rC   rD   rE   r   ?contactsZUnblockRequestZsend_message?time?sleepr^   Zget_messagesrF   rI   )Zbot?mrx   r.   rP   rJ   rK   rL   rM   rN   rO   ?msgr1   r1   r5   ?SpamBotChecker?   s<   
0


??r?   c                  C   s?  t ?? } | ?d? | d d ?? }|?d?}| d d ?? }tjtjd? tt	j
tj d|? ? ? ?ztd|? ?tt?}|??  |?? ?r5tt	j
tj d	 ? d
}t?? }|tdd? }|tdd? }tdddd?}	tj|	ddd?}
|
?g d?? z?|D ]?}z|t|?? W n ty? } zW Y d }~nd }~ww tt	j
tj d|? d? ? g }z	|j|dd?}W n ty? } zW Y d }~nd }~ww |D ]L}|jr?|j}nd}|jr?|j}nd}t |j!t"?r?|}nt |j!t#?r?|}t |j!t$?r?|}t |j!t%?r?|j!j&}|?'d?}|
?|||j(|||g? |d
 }q?q}W n t?y* } zW Y d }~nd }~ww |	?)?  td|? ntt	j
tj* d|? ? ? W n t?y` } ztt	j
tj* d ? W Y d }~nd }~ww t+? }dd? }d d!? }|?  |?  td"d#dd??U}t?,|?}tdddd??8}	tj|	ddd?}
|
?g d?? d$}|D ]}|d
7 }|
?||d
 |d% |d& |d' |d( f? ?q?W d   ? n	1 ?s?w   Y  W d   ? n	1 ?s?w   Y  t-?.d)? t-?.d"? tt	j
tj d* ? tt	j
tj d+ ? t/?  d S ),N?
config.inirx   ?	FromGrouprX   ?PhoneNumber??level?
Logging For r:   ?
login Doner8   ??????Zdays??????data.csvr-   rU   rV   rS   rY   ?zsr. no.?usernamezuser id?name?groupZStatuszScrabing Members from ? group.....T?Z
aggressiver[   ?%Y%m%dzCount : ?login fail z
login failc                  S   ??   t ? } tdddd??%}t?|?}|D ]}| ?|? |D ]}|dkr&| ?|? qqW d   ? n1 s2w   Y  tdddd??}tj|dd	d
?}|?| ? W d   ? d S 1 sWw   Y  d S ?Nr?   r.   rU   rV   r[   ?1.csvr-   rX   rS   rY   ??listr=   r>   r   r]   rf   rc   rd   ??linesZreadFiler   r4   Zfieldrn   rc   r1   r1   r5   ?main  ?    


????"?zScraper.<locals>.mainc                  S   r?   ?Nr?   r.   rU   rV   r?   ?2.csvr-   rX   rS   rY   r?   r?   r1   r1   r5   ?main1#  ?    


????"?zScraper.<locals>.main1r?   r.   r   ?   ?   ?   ?   r?   zTask completed?Enter any key to exit)0?configparser?ConfigParser?read?strip?split?logging?basicConfig?WARNINGr@   r   rA   r   rG   r
   rC   rD   rt   ru   rB   r   ?nowr   r=   r>   rc   ?writerowr    ?	ExceptionrH   ?iter_participantsr?   ?
first_name?
isinstance?statusr   r   r   r   ?
was_online?strftimer|   ?close?REDr?   r   re   rf   rI   )?configZlink1?linksrN   rO   ?count?today?	last_week?
last_monthrJ   rc   ?link?e?all_participants?userr?   r?   ?date_online?date_online_strr?   r?   r?   ?source?rdrrl   r4   r1   r1   r5   ?Scraper?   s?   


????

??!??? ??
.????


r?   c                  C   s?  t jdd? ttjtj d ? dd? } ttjtj d ? tt	? ?}|}t
?? t| d? ?d?}g }t?? }|?d	? |d
 d ?? }|?d?}|d
 d ?? }tjtjd? ttjtj d|? ? ? z1td|? ?tt?}|??  |?? r?ttjtj d ? | |||?}	nttjtj |? d? ? W n  ty? }
 zt|
? ttjtj d ? W Y d }
~
nd }
~
ww t? }dd? }dd? }|?  |?  tdddd??T}t ?!|?}tdddd??7}t j"|ddd?}|?#g d ?? d!}|D ]}|d"7 }|?#||d" |d# |d$ |d% |d& f? q?W d   ? n	1 ?sw   Y  W d   ? n	1 ?s(w   Y  t$?%d'? t$?%d? ttjtj d( ? ttjtj d) ? t	?  d S )*NT?Z	autoresetzWelcome To HackingZone Program
c                 S   ??  t ?? }|tdd? }|tdd? }|?d?}g d?g}d}| ?? }|D ]?}	ttjtj	 d|	? d? ? | ?
|	?}
z
| j|
jd	d
?}W n tyU } zW Y d }~q$d }~ww |D ]c}|jd kr?zVt|jt?ri|}nt|jt?rq|}t|jt?ry|}t|jt?r?|jj}|?d?}t|?t|?kr?|t|j?t|j?t|jd |j ?t|
j?t|?g}|?|? |d7 }W qX   Y qXqXq$|r?tddddd??}t?|?}|?|? W d   ? n1 s?w   Y  td|? | ??  t?  d S )Nr?   r?   r?   r?   r?   r8   ?Filter Members from r?   Tr?   rz   r?   r-   ?utf-8r[   ?rW   ?newlinez
Members : ? r   r?   r   r?   Zget_dialogsr@   r   rA   r   rG   ?
get_entityr?   r|   r?   r?   r?   r?   r   r   r   r   r?   r^   r?   ?	last_name?titler]   r=   r>   rc   rd   rF   ?rO   r?   ?last_dayr?   r?   r?   ?ar?   Zdialogsrl   r?   r?   r?   r?   r?   r?   ?brJ   r`   r1   r1   r5   ?nfilterQ  ?^   


??

$?
???
?

zDailyFilter.<locals>.nfilterz
Enter the day for filter :r?   r?   r?   rx   r?   rX   r?   r?   r?   r:   r?   z login failzPlease Enter Vailed Groupc                  S   r?   r?   r?   r?   r1   r1   r5   r?   ?  r?   zDailyFilter.<locals>.mainc                  S   r?   r?   r?   r?   r1   r1   r5   r?   ?  r?   zDailyFilter.<locals>.main1r?   r.   rU   rV   r?   r-   rS   rY   r?   r   r8   r?   r?   r?   r?   r?   ?Filter completedr?   )&?coloramar	   r@   r   rA   r   rG   rH   rs   rI   r   r?   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   r
   rC   rD   rt   ru   rB   r?   r?   r?   r=   r>   r   rc   r?   re   rf   ?r?   ?nr?   Zdeler?   r?   r?   rN   rO   r?   r?   r?   r?   r?   r?   r?   rJ   rc   rl   r4   r1   r1   r5   ?DailyFilterL  sf   ,


? ??
,????


r?   c                  C   s?  dd? } t tjtj d ? tt? ?}|d }t?? t	| d? ?
d?}g }t?? }|?d? |d d	 ?? }|?d
?}|d d ?? }tjtjd? t tjtj d|? ? ? z1td|? ?tt?}|??  |?? r{t tjtj d ? | |||?}	nt tjtj d|? ? ? W n  ty? }
 zt |
? t tjtj d ? W Y d }
~
nd }
~
ww t? }dd? }dd? }|?  |?  tdddd??T}t?|?}tdddd??7}tj |d
dd?}|?!g d?? d}|D ]}|d 7 }|?!||d  |d! |d" |d# |d$ f? q?W d   ? n	1 ?s
w   Y  W d   ? n	1 ?sw   Y  t"?#d%? t"?#d? t tjtj d& ? t tjtj d' ? t?  d S )(Nc                 S   r?   )Nr?   r?   r?   r?   r?   r8   r?   r?   Tr?   rz   r?   r-   r?   r[   r?   zcounting : r?   r?   r1   r1   r5   r?   ?  r?   zWeeklyFilter.<locals>.nfilterz
Enter the week for filter :?   r?   r?   r?   rx   r?   rX   r?   r?   r?   r:   z
Login Doner?   zPlease Enter A Vailed Groupc                  S   r?   r?   r?   r?   r1   r1   r5   r?   %  r?   zWeeklyFilter.<locals>.mainc                  S   r?   r?   r?   r?   r1   r1   r5   r?   9  r?   zWeeklyFilter.<locals>.main1r?   r.   rU   rV   r?   r-   rS   rY   r?   r   r8   r?   r?   r?   r?   r?   r?   r?   )$r@   r   rA   r   rH   rs   rI   r   r?   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   rG   r
   rC   rD   rt   ru   rB   r?   r?   r?   r=   r>   r   rc   r?   re   rf   r?   r1   r1   r5   ?WeeklyFilter?  sb   ,


? ??
,????


r?   c                  C   s?  t jt jd? t?? } | ?d? | d d ?? }| d d ?? }tdddd	??}t?	|?}d
d? |D ?}W d   ? n1 s>w   Y  tdddd	??}t?	|?}dd? |D ?}W d   ? n1 saw   Y  t
d|? ?tt?}|??  |?? s?td|? d?? n?g }d }	d}
g }d}|dk?rVz?|?|?}|jdk?rt|j?}|j|dd?}g }g }d}g }|D ]}zt|j?|v r?|?|?t|j??? W q?   td? Y q?|??  |??  |jdd? |D ]}||= q?tddddd??}t?|?}|?|? W d   ? n	1 ?sw   Y  d}n
ttjtj d ? d}W n7 t j!j"j#?y-   |t$|?? Y n% t%?yB   ttjtj& d ? d}Y n   ttjtj d ? d}Y |dks?t'? }dd? }dd ? }|?  |?  td!dd"d	??U}t?	|?}tddd"d	??8}tj|d#d$d%?}|?(g d&?? d}|D ]}|d'7 }|?(||d' |d( |d) |d* |d+ f? ?q?W d   ? n	1 ?s?w   Y  W d   ? n	1 ?s?w   Y  t)?*d,? t)?*d!? ttjtj+ d- ? ttjtj& d. ? ttjtj, d/ ? t-?  d S )0Nr?   r?   rx   ?ToGroupr?   r?   r.   r?   rV   c                 S   ?   g | ]}|?qS r1   r1   ?r3   rl   r1   r1   r5   r6   r  ?    z(DeleteALreadyMembers.<locals>.<listcomp>c                 S   s   g | ]}t |d  ??qS )r?   )r^   r?   r1   r1   r5   r6   v  s    r:   z
Login fail, for number z need Login first
??   r   ?????Tr?   zError get user)?reverser-   r[   r?   z
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
c                  S   r?   r?   r?   r?   r1   r1   r5   r?   ?  r?   z"DeleteALreadyMembers.<locals>.mainc                  S   r?   r?   r?   r?   r1   r1   r5   r?   ?  r?   z#DeleteALreadyMembers.<locals>.main1r?   rU   rX   rS   rY   r?   r8   r?   r?   r?   r?   r?   zAlready Member Deleted Done !zTask CompletedzPress Enter to exit).r?   r?   r?   r?   r?   r?   r?   r=   r>   r   r
   rC   rD   rt   ru   r@   r?   Z	megagroupr^   r|   r?   r]   ?indexr?   rF   ?sortrc   rd   r   rA   r   r?   ?telethonr   Zrpcerrorlistr)   r    ?
ValueErrorrB   r?   r?   re   rf   rG   rH   rI   )r?   r?   rN   rJ   Zusers1?usersZuserlistrO   ZchatsZ	last_dateZ
chunk_size?groupsr?   r?   Zgroup_idr?   ?resultsZresults1r?   Zindex1r?   rl   r`   r?   r?   r?   r?   r?   rc   r4   r1   r1   r5   ?DeleteALreadyMembersb  s?   

?
?


?
??%
.????


r?   c                  C   s?   d} t dd??O}dd? t?|?D ?}d}|D ]8}t?|?}|d7 }ttjtj	 d|? ? ? t
d	|? ?tt?}|?|? |tjj|?d
?d??}td? d} qW d   ? n1 sYw   Y  t| rfd? d S d? d S )NFr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   ?  r7   zSetProfile.<locals>.<listcomp>r   r8   zChanging in r:   zset.jpg)?filez"done! profile pic has been changedTrr   r;   )r=   r>   r   r   r?   r@   r   rA   r   rB   r
   rC   rD   rE   r   ZphotosZUploadProfilePhotoRequestZupload_filerI   )rP   rJ   rK   rL   rM   rN   rO   ?resultr1   r1   r5   ?
SetProfile?  s$   

???r?   c                  C   s?   d} t dd??R}dd? t?|?D ?}d}|D ];}t?|?}|d7 }ttjtj	 d|? ? ? t
d	|? ?tt?}|?|? |t|?d
??? ttjtj d ? d} qW d   ? n1 s\w   Y  t| rid? d S d? d S )NFr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6     r7   z!DeleteProfile.<locals>.<listcomp>r   r8   zDeleting in r:   ?mezProfile Pic DeletedTrr   r;   )r=   r>   r   r   r?   r@   r   rA   r   r?   r
   rC   rD   rE   r   Zget_profile_photosrB   rI   )rP   rJ   rK   rL   rM   rN   rO   r1   r1   r5   ?DeleteProfile?  s    

??r?   c                  C   sx   dd l } t?d? g d?}|D ]}t| ?t?? |? t? ?? qtt? dt? ?? tt? dt? ?? tt	? dt	? ?? d S )Nr   ?clear)uJ    ██████╗░███████╗██╗░░██╗ uJ    ██╔══██╗██╔════╝╚██╗██╔╝ uJ    ██████╔╝█████╗░░░╚███╔╝░ uJ    ██╔══██╗██╔══╝░░░██╔██╗░ uJ    ██║░░██║███████╗██╔╝╚██╗ uJ    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ z Channel: @The_Hacking_Zonez  Group : @The_Hacking_Zone_Grouprz   )
?randomre   ?systemr@   ?choice?colorsr?   ?lg?yer.   )r?   r?   ?charr1   r1   r5   r<     s   
r<   c               	      s?   t ?  tj?tj} tj?tj?tj?t?  g }g }g }tdd??}t	|?}t
|?}|D ]}|?t|d ?? q+W d   ? n1 sAw   Y  |?t| ? d?? d?? tt|??? ?? ?? ? ?????fdd?????fdd	?? ??  d S )
Nr,   r.   r   ?Total account: rz   c                      s6  t t?? d?? ???d } t t?? d?? ???}t t?? d?? ???}t t?? d?? ???}tdddd	??}tj|d
dd?}|?||| g? W d   ? n1 sQw   Y  d}d}?| |? D ?]?}|d7 }td|? ?? t?|?}	tt	j
tj dt	j? dt	j
tj ? d|	? ? ? td|	? ?tt?}
|
??  |
?? s?t?? d?? ?? |
?|	? |
?|	td?? d}g }t|dd	??;}tj|d
dd?}t|d ? |D ]#}i }|d |d< |d |d< t |d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?s&w   Y  t |?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sZw   Y  t |?}|| }tdddd	??}tj|d
dd?}|?||g? W d   ? n	1 ?s?w   Y  d}|D ]y}t |?t |d ?k?r
t |d ?t |?k?r
z1|d7 }|d dk?r?t?? d?? ?? W ?q?|
tjj|d |d td?dd d!?? |? d"?}W n* tj?y? } z
|j j!}W Y d }~nd }~w   t"?#?  t?? d#?? ?? Y ?q?t|? ?q?|d7 }q`t$?%d? ? ?  d S )$N?From Account No : r8   ?Upto Account No : zFrom where you want to start : z3How many contacts you want to add in one Account : ?
memory.csvr-   rU   rV   rX   rS   rY   r   ?Index : r9   rz   r:   ?some thing has changed?Enter the code: r?   ?srnor?   r?   r|   r?   r?   r.   r[   ?no username, moving to nextrx   ZgdfT)r|   r?   r?   rN   Zadd_phone_privacy_exception? - done?Unexpected Error)&rs   rI   r=   r>   rc   r?   r@   r   r?   r   rA   r   rB   r}   rG   r
   rC   rD   rt   ru   ?send_code_request?sign_inr   ?nextr]   r?   r   r~   ZAddContactRequestr^   r   ?RPCError?	__class__?__name__?	traceback?	print_excre   rf   ) ?From?Upto?rex?hacksr?   rc   r?   ?indexx?xdrN   rO   ?
input_filer?   rJ   ?rowsr4   r?   ?hash_obj?
csv_reader?list_of_rows?
row_number?
col_number?numnext?	startfrom?	nextstart?numend?endto?nextend?df?itr?   r?   )?again?blr?   rM   r.   r?   r1   r5   ?autosF  s?   ?
0

???	??,???


z"AutoaddContactPhone.<locals>.autosc                     s.   t ?? d?? ??} | dkr? ?  d S t?  d S )NzRDone!
Choose From Below:

1 - Repeat The Script
OR Just Hit Enter To Quit

Enter: ?1)rI   ?quit)?stat)r(  r?   r.   r1   r5   r&  ?  s   

z"AutoaddContactPhone.<locals>.again)r	   r   ?LIGHTRED_EXrB   rG   ?BLUErH   r<   r=   r   ?tupler]   rs   r@   r^   ?len)?grrv   rw   rN   ?	delta_objr  ?list_of_phone?phone_r1   )r&  r(  r'  r?   rM   r.   r?   r5   ?AutoaddContactPhone+  s,   ??(i
r4  c                  C   s?  t jdd? ttjtj d ? t? } t| ? d?d??}dd? t	?
|?D ?aW d   ? n1 s0w   Y  tdttt?? ? ttd	??d
 }ttd??}d}dat||? D ]y}|d
7 }td|? ?? t?|?}td|? ?? td|? ?tt?}|?|? |tdd??}d}	|jD ]E}
|	d
7 }	z|t|
gd?? ttjtj |	? d|
j? d? ? W q? tjy? } z|jj}t|	? d|
j? d|? ?? W Y d }~q?d }~ww qWd S )NTr?   zEnter Accounts List : z.csvr.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   ?  r7   z!DeleteContact.<locals>.<listcomp>r?   r?   r8   r   r   r  r9   r:   ??hashr{   ? - z	 - DELETE)r?   r	   r@   r   rA   r   rB   rI   r=   r>   r   ?phlistr^   r/  rs   ?HackingZonepror   r?   r
   rC   rD   rE   r   r?   r   r|   r   r  r  r  )ZphonecsvrJ   ? HackingZone_ne_script_banaya_hai?5telegram_script_banyane_ke_liye_HackingZone_ko_dm_kror  ZHackingZoneonytrN   rO   r~   ZrexaddZrexopr?   ?error1   r1   r5   ?DeleteContact?  sB   ?


&????r=  c                   C   s?  t ?? } | ?d? | d d }| d d }| d d }| d d }| d d }tdd	??}d
d? t?|?D ?}W d   ? n1 sAw   Y  tdtt|?? ? tt	j
tj d ? t? }tt	j
tj d ? tt? ?}	tt	j
tj d ? tt? ?}
|dkr?t|?}|}n
|dkr?t|?}|}t|?}t|?d }t|?}d}da|||? D ?]}|d7 }t?|?}td|? ?? td|? ?tt?}|?|? td|? ?? z	|?t|??}W n3 t?y   |dkr?|t|?? |?t|??}n|dk?r
|t|?? t?d? |?t|??}Y nw |t|d??}t|jj ?atdt? ?? t|k?r4td|? d?? t?  t!?  |t"dd??}|j#}t|?}td|? ?? d}d}||k ?r?dd? |d |	? D ?}zDt?|
? |t$j%j&||d?? ||	7 }t'dd ?D ]}z||= W ?qv t(?y? } zW Y d }~?qvd }~ww tt	j
tj d!|? ? ? W n t)j*?y? } z|j+j,}tt|?? W Y d }~?q?d }~ww ||k ?sRq?d S )"Nr?   rx   r?   ?GroupID?	EnterStop?StartingAccount?
EndAccountr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   ?  r7   zBulkAdder.<locals>.<listcomp>r?   ?1Enter Y if group has private link else N (Y/N) : z.In A Batch How many Members You Want To Add : ?*Enter Delay Time Per Request 0 For None : ?Y?Nr8   r   r9   r:   r  r?   ??channel?	Members: ?The Goal Of ? Has Been Completedr5  zTotal : c                 S   r?   r1   r1   )r3   Zdeltar1   r1   r5   r6   $  r?   ?rG  r?   ?
   zBATCH: )-r?   r?   r?   r=   r>   r   r@   r^   r/  r   rA   r   rB   rI   rs   Z HackingZonedev_is_main_developerr   r?   r
   rC   rD   rE   r?   r   r?   r   ?get_input_entityr    r   r?   r   ?	full_chat?participants_countr*  r   r?   r   ?channelsr!   ?ranger?   r   r  r  r  ) r?   ?	grouplink?groupid?stopnum?stacno?endacnorJ   r8  ?prchkZHackingZonedevismain?HackingZone_devr|   ?prlink?stopZ
start_fromZuptor  ZpythondeveloperrN   rO   rG  ?channelinfo?membersZuser_to_addZcountconZ
batchcountZlolZsemenrl   ?Dr?   r<  r1   r1   r5   ?	BulkAdder?  s?   
?





??	


?????
???r^  c                  C   s  t ?? } | ?d? | d d }| d d }| d d }| d d }| d d }tdd	??}d
d? t?|?D ?}W d   ? n1 sAw   Y  tdtt|?? ? tt	j
tj d ? t? }tt	j
tj d ? tt? ?}	|dkrwt|?}
|}n
|dkr?t|?}
|}t|?}t|?d }t|?}d}da|||? D ]?}|d7 }td|? ?? t?|?}td|? ?? td|? ?tt?}|?|? z	|?t|
??}W n1 ty?   |dkr?|t|?? |?t|
??}n|dkr?|t|?? t?d? |?t|
??}Y nw |t|d??}t|jj ?atdt? ?? t|k?r"td|? d?? t?  t!?  |t"dd??}d}|j#D ]T}|d7 }z"|t$|
|gd?? tt	j
tj |? d|j%? d? ? t?|	? W ?q. t&j'?y? } z|j(j)}tt	j
tj* |? d|j%? d|? ? ? W Y d }~?q.d }~ww q?d S )Nr?   rx   r?   r>  r?  r@  rA  r,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   E  r7   zSingleAdder.<locals>.<listcomp>r?   rB  rC  rD  rE  r8   r   r  r9   r:   r?   rF  rH  rI  rJ  r5  rK  r7  z - DONE)+r?   r?   r?   r=   r>   r   r@   r^   r/  r   rA   r   rB   rI   rs   r9  r   r?   r
   rC   rD   rE   r?   r   r?   r   rM  r    r   r?   r   rN  rO  r*  r   r?   r!   r|   r   r  r  r  r?   )r?   rR  rS  rT  rU  rV  rJ   r8  rW  rX  r|   rY  rZ  r:  r;  r  ZdeltaxdrN   rO   rG  r[  r~   ZdeltaaddZdeltaopr?   r<  r1   r1   r5   ?SingleAdder9  s?   
?



??	

"&????r_  c            	         s?   t tjtj d ? tt? ?} tdd??}t|?}t	|?}| }d}||d  |d  }W d   ? n1 s5w   Y  t
?t? |?t?? }|?d? |d d ?? ???fdd	?}|?  d S )
Nz'Which Account You Want To Use?

Enter: r,   r.   r8   r?   rx   r?   c                     s?  ?} t ???}td|? ??? ?}|??  |?? sHz|?|? |?|td?? td? |?|? W n t	yG   td?}td? |j|d? Y nw d}g }t
|dd??;}tj|d	d
d?}t|d ? |D ]#}i }	|d |	d< |d |	d< t|d ?|	d< |d |	d< |?|	? qbW d   ? n1 s?w   Y  ttd??}
ttd??}|D ?]*}	t|
?t|	d ?k?r?t|	d ?t|?k?r?z1d}|	d dkr?td? W q?|t| |	d g?? tjtj d }ttjtj d ? t?d? W n? t?y   tjtj d }t?d? Y n? t?y   d}Y nx t?y2 } zd}ttjtj d ? t?d? W Y d }~nYd }~w t?yO } z|t| ?? t?d? W Y d }~q?d }~w tj?yf } z
|j j!}W Y d }~n%d }~w t"?yz } z|}W Y d }~nd }~w   t#?$?  td? Y q?|?%| ?}|t&|d ??}t|j'j(?}ttjtj) d!|? tj*? d"tjtj+ ? d#|	d ? d$|? ?	 ? q?t|	d ?t|?k?r?td%? t?  t,?  q?d S )&Nr:   zEnter code: r[   zEnter password: )?passwordr?   rU   rV   rX   rS   rY   r   r  r8   r?   r?   r|   r?   r?   zStart From = z	End To = rX  r  ZDONEzMoving To NextZPrivacyRestrictedErrorZALREADYr'   z(Script Are In Progress So Please Wait...r?   r  rF  zGroup Members rz   z>> z >> zMembers Added Successfully!)-r   r?   r
   rt   ru   r	  r
  rI   r@   r"   r=   r>   r   r  rs   r]   r!   r   rA   r   rB   rH   r   r?   r(   r?   r*   r'   r)   r    r   r  r  r  r?   r  r  r?   r   rN  rO  rG   r}   ?CYAN?exit)Zchannel_usernamerN   rO   r`  r  r?   rJ   r  r4   r?   r  r"  r?   ?g?cwfer?   ?dZchannel_connectZchannel_full_infoZcountt?rw   rv   rM   Zto_groupr1   r5   r(  ?  s?   

?
??
,?
???
@??zAdder.<locals>.autos)r@   r   rA   r   rH   rs   rI   r=   r   r?   rC   rD   r?   r?   r?   )	ZHackingZone_devinputZread_objr  r  r  r  ?valuer?   r(  r1   rf  r5   ?Adder  s"   
?

Yrh  c               	      sn  t ?  tj?tj} tj?tj}tj?t?? }|?	d? |d d ?|d d ?|d d ?|d d ?|d d ? g }t
dd	??}t|?}t|?}|D ]}|?t|d
 ?? qKW d   ? n1 saw   Y  |?t| ? d?? d?? tt|??? ?? ?? ? ????????f	dd?}? ????????f	dd?}	tt|? d?? ???}
|
dkr?|	?  d S |
dkr?|?  d S d S )Nr?   rx   r?   r>  r?  r@  rA  r,   r.   r   r?   rz   c            )         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]?}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??;}t	j|d	d
d?}t|d ? |D ]#}i }|d |d< |d |d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sw   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sLw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s{w   Y  |t|?? t?d? |?t|??}"|t|"d??}#t|#jj ?}$t d|$? ?? |$|k?r?t d|? d?? t?  t!?  d}%|D ]?}t|?t|d ?k?rZt|d ?t|?k?rZz2|%d7 }%|d dk?r?t ?? d?? ?? W ?q?|t"j#?$||d g?? t |%? d ?? t?| ? W ?q? t%?y& }& z|t|?? t?d? W Y d }&~&?q?d }&~&w t&j'?yG }' z|'j(j)}(t |%? d!|(? ?? W Y d }'~'?q?d }'~'w   t*?+?  t ?? d"?? ?? Y ?q??q?|d7 }qct,?-d? d S ?#NrC  r?   r8   ?2   r  r-   rU   rV   rX   rS   rY   r   r  r9   r:   r  r  r  r?   r?   r|   r?   r?   r.   r?   rF  rH  rI  rJ  r[   r  r  r7  r  ).r@   r   rA   r   rB   rs   rI   r^   r=   r>   rc   r?   r   r?   r
   rC   rD   rt   ru   r	  r
  r   r  r]   r?   r    r   r?   rM  r   r   rN  rO  r*  r   rP  r!   r)   r   r  r  r  r  r  re   rf   ?)rX  rx   Zrexlinkr|   r  r  r  r  rZ  r?   rc   r?   r  r  rN   rO   r  r?   rJ   r  r4   r?   r  r  r  r  r  r  r  r   r!  r"  r#  r$  rG  r[  Zrexprodeltanoobr%  rd  r?   r?   ?	rV  rS  rR  r?   rM   r.   rU  rT  r?   r1   r5   r(    s?   
?


???	??

,
? ??
zAdderForPhone.<locals>.autosc            )         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??;}t	j|d	d
d?}t|d ? |D ]#}i }|d |d< |d |d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sw   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sLw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s{w   Y  |t|?? t?d? |?t|??}"|t|"d??}#t|#jj ?}$t d|$? ?? |$|k?r?t d|? d?? t?  t!?  d}%|D ]?}t|?t|d ?k?rat|d ?t|?k?rat d|$? ?? z2|%d7 }%|d dk?r?t ?? d?? ?? W ?q?|t"j#?$||d g?? t |%? d ?? t?| ? W ?q? t%?y- }& z|t|?? t?d? W Y d }&~&?q?d }&~&w t&j'?yN }' z|'j(j)}(t |%? d!|(? ?? W Y d }'~'?q?d }'~'w   t*?+?  t ?? d"?? ?? Y ?q??q?|d7 }qct,?-d? d S ri  ).r@   r   rA   r   rB   rs   rI   r^   r=   r>   rc   r?   r   r?   r
   rC   rD   rt   ru   r	  r
  r   r  r]   r?   r   r   r?   rM  r   r   rN  rO  r*  r   rP  r!   r)   r   r  r  r  r  r  re   rf   rk  rl  r1   r5   ?private?  s?   
?


???	??

,
? ??
zAdderForPhone.<locals>.privatez%Press Y if group is private else N : rD  rE  )r	   r   r,  rB   rG   r-  rH   r?   r?   r?   r=   r   r.  r]   rs   r@   r^   r/  rI   )r0  r'  r?   rN   r1  r  r2  r3  r(  rm  Z	rexchooser1   rl  r5   ?AdderForPhone?  s>   
??(yy

?rn  c                  C   s?   t dddd??} tj| ddd?}|?g d?? W d   ? n1 s!w   Y  ttd	??d
 }d}||krItjdtjd? |d
 }t	?
d? ||ks4t	?
d? t?d? d S )Nr  r-   rU   rV   rX   rS   rY   )r8   r8   rj  z*How many accounts do you want to run ? => r8   r   zpython v1-1.py)Zcreationflagsr?   rL  )r=   r>   rc   r?   rs   rI   ?
subprocess?PopenZCREATE_NEW_CONSOLEr   r?   re   rf   )r?   rc   r?   rj   r1   r1   r5   ?MultipleAdder  s   ?
?
rq  c                  C   s  t ?  tttd t d t d ??} | dkrbt ?  tttd t d t d ??}|dkr3t?  d S |dkr<t?  d S |dkrEt?  d S |dkrNt	?  d S |d	krWt
?  d S |d
kr`t?  d S d S | dkr?t ?  tttd t d t d ??}|dkr?t?  d S |dkr?t?  d S |dkr?t?  d S |dkr?t?  d S |d	kr?t?  d S |d
kr?t?  d S |dkr?t?  d S d S | dk?r	t ?  tttd t d t d ??}|dkr?t?  d S |dkr?t?  d S |dkr?t?  d S |dkr?t?  d S |d	kr?t?  d S |d
k?rt?  d S d S d S )NzChoose Option from Following:zO
       [1]. Accounts 
       [2]. Scraper 
       [3]. Adder 
       [4]. Exitz	 
 Enter:r8   z?
       [1]. Login 
       [2]. Ban Filter 
       [3]. AccStats 
       [4]. Change Profile 
       [5]. Clear Profile 
       [6]. Backr?   r?   r?   r?   ?   z?
       [1]. Normal Scraper 
       [2]. Daily Filter 
       [3]. Weekly Filter 
       [4]. Delete ALready Members 
       [5]. Auto Add Contact Phone 
       [6]. Delete Contact 
       [7]. Backr?   z?
       [1]. Adder 
       [2]. Bulk Adder Phone 
       [3]. Bulk Adder Pc 
       [4]. Contact Adder 
       [5]. Multiple Contact Adder 
       [6]. Back)r<   rs   rI   ?re?cyr0  rQ   ry   r?   r?   r?   ?	main_menur?   r?   r?   r?   r4  r=  rh  rn  rq  r_  r^  )r?   r?   r1   r1   r5   ru    sj     





? 






?
 






?ru  )hro  Zrequestsr   re   rs  r  r?   r?   r?   r?   r>   Zjsonr?   r   r   r   r   r   r   r   r	   Ztelethon.syncr
   r   r   r   r   r   r   Ztelethon.tl.typesr   r   r   r   r   r   r   r   r   Ztelethon.tl.functions.contactsr   r   Ztelethon.tl.functions.photosr   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.functions.channelsr   r    r!   Ztelethon.errorsr"   Ztelethon.errors.rpcerrorlistr#   r$   r%   r&   r'   r(   r)   r*   Ztelethon.sessionsr+   rC   rD   r0  rt  Zwi?path?exists?mkdirr=   rQ   ry   r?   r?   r?   r?   r?   r?   r?   rG   r?   r-  r?   r?   r.   ZWHITEr-   ra  rH   r?   rB   r?   r<   r4  r=  r^  r_  rh  rn  rq  ru  r1   r1   r1   r5   ?<module>   st   h $,(

v   
  (YFo  
2