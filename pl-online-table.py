import requests
import re
import datetime
import csv

print('connecting...')

try:
    r=requests.get('https://www.premierleague.com/tables?co=1&se=274&ha=-1')
    f=open('last','w')
    teamlist = re.findall(r'<span class="long">(.+)</span>',r.text)
    teamlist = teamlist[:20]
    teampts = re.findall(r'<td class="points">(\d+)</td>',r.text)
    teampts = teampts[:20]

    teamstate = re.findall(r'<td>(\d+)</td>\n        <td>(\d+)</td>\n        <td>(\d+)</td>\n        <td>(\d+)</td>\n        <td class="hideSmall">(\d+)</td>\n        <td class="hideSmall">(\d+)</td>\n        <td> \n        (.+)\n\n </td>',r.text)
    teamstate = teamstate[:20]

    print('connected!')
    print('///////////////////////////////////////////////////////////////////////////')
    print('//                                                                       //')             
    print('//  N               teams        played wons drawns lost GF  GA  GD  pts //')

    for i in range(1,21):
        teamstatei = teamstate[i-1]
        played=teamstatei[0]
        win =teamstatei[1]
        drawn=teamstatei[2]
        lost=teamstatei[3]
        gf=teamstatei[4]
        ga=teamstatei[5]
        gd=teamstatei[6]
        
        a='// %2i - %25s  %2s    %2s    %2s    %2s %3s %3s %3s  %3s // '% (i,teamlist[i-1],played,win,drawn,lost,gf,ga,gd,teampts[i-1])
        print('// %2i - %25s  %2s    %2s    %2s    %2s %3s %3s %3s  %3s // '% (i,teamlist[i-1],played,win,drawn,lost,gf,ga,gd,teampts[i-1]))
        f.writelines(a+'\n')
    print('//                                                                       //')           
    print('///////////////////////////////////////////////////////////////////////////')
    x= str(datetime.datetime.now())
    x=x[:-10]

    f.writelines(f'premier league table at ({x})')
    f.close()

except:
    print('connection error!')
    k=input('do you whant to see last table? y/n : ')
    if k.startswith('y') or k.startswith('Y'):
        try:
            with open('last') as f:
                f= csv.reader(f)
                print('///////////////////////////////////////////////////////////////////////////')            
                print('//  N               teams        played wons drawns lost GF  GA  GD  pts //')             
                for i in f:
                    i=i[0]
                    if i.startswith('p'):
                        break
                    print(f'{i}')             
                print('//                                                                       //')              
                print('///////////////////////////////////////////////////////////////////////////')            
                print(f'//               {i}              //')
                print('//                                                                       //')
                print('///////////////////////////////////////////////////////////////////////////')              
        except:
            print('in first time you must be online')
    


input('\n')

