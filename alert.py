import sys
import os
import requests



colorcode = {

    'ITALIC':'\033[3m', 'YELLOW':'\033[1;33m',
    'GREEN':'\033[0;32m', 'BLINK':'\033[5m',
    'RESET':'\033[0m', 'RED':'\033[0;31m',
    'BROWN':'\033[0;33m', 'PURPLE':'\033[0;35m'

}

class disclaimer():
    print('\n{3}Hey Friend !! before starting using this program, Dont forget \
    \n{0}{3}Hacking{2}{3} with out authorization is illegal, Dont use this program to attack\
        \n{3}networks with out legal permissions, {1}{3}AuxGrep{2}{3} is not responsible with \
            \n{3}any {0}{3}malicious activities{2}'.format(colorcode['RED'], \
            colorcode['YELLOW'], colorcode['RESET'], colorcode['ITALIC']))
    print('')
    oky = str(input('{0}I Agree(yes/no):{1} '.format(colorcode['GREEN'], colorcode['RESET'])))
    if oky == str('yes'):
        try:
            print('')
            ex = os.uname()[1]
            site = requests.get('https://checkip.amazonaws.com')
            ext_ip = site.text
            with open(f'/opt/{ex}.txt', mode='w') as f:
                f.write(ext_ip)
        except OSError:
            os.system('clear')
            print('{0}Your a dumbest {1}{2}hacker{1}{0} run this as root{1}'.format(colorcode['RED'], \
                colorcode['RESET'], colorcode['YELLOW']))
    else:
        os.system('clear')
        sys.exit('{0}Stupid dumbest KID!! Exiting....!!!{1}'.format(colorcode['RED'], \
            colorcode['RESET']))
