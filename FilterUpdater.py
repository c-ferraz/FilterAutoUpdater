#VERSON 0.9.2
#BY C. FERRAZ
#https://github.com/c-ferraz

import requests
import os,sys
import re
import getpass

url_soft = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%200-SOFT.filter"
url_regular = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%201-REGULAR.filter"
url_semi_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%202-SEMI-STRICT.filter"
url_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%203-STRICT.filter"
url_very_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%204-VERY-STRICT.filter"
url_uber_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%205-UBER-STRICT.filter"
url_uber_plus_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%206-UBER-PLUS-STRICT.filter"

def find_filter_type():
    current_filters = []
    filter_folder = 'C:\\Users\\'+os.getlogin()+'\\Documents\\My Games\\Path of Exile'
    if not os.path.exists(filter_folder):
        print('The default folder for filters: '+filter_folder+'\nWas not found.')
        quit()
        #TODO: chose new folder or create a folder to save those files

    for files in os.listdir(filter_folder):
        if 'NeverSink' in files:
            filter_type = re.search(r'(\d-.*)\.filter', files)
            current_filters.append(filter_type.group(1))
    if len(current_filters) == 0:
        answer = input('No NeverSkin filter found, do you wish to download one? (Y/N)')
        while True:
            if (answer.upper() == 'Y' or answer.upper() == 'N'):
                break
            else:
                answer = input('Choose Y or N.')
        if (answer.upper() == 'Y'):
            print('Choose filter type:')
            print('0-SOFT\n1-REGULAR\n2-SEMI-STRICT\n3-STRICT\n4-VERY-STRICT\n5-UBER-STRICT\n6-UBER-PLUS-STRICT')
            answer = input()
            while True:
                answer = answer.upper()
                if answer == '0' or answer == 'SOFT' or answer == '0-SOFT':
                    return ['0-SOFT']
                elif answer == '1' or answer == 'REGULAR' or answer == '1-REGULAR':
                    return ['1-REGULAR']
                elif answer == '2' or answer == 'SEMI-STRICT' or answer == 'SEMI STRICT' or answer == '2-SEMI-STRICT' or answer == '2-SEMI STRICT':
                    return ['2-SEMI-STRICT']
                elif answer == '3' or answer == 'STRICT' or answer == '1-STRICT':
                    return ['3-STRICT']
                elif answer == '4' or answer == 'VERY-STRICT' or answer == 'VERY STRICT' or answer == '4-VERY-STRICT' or answer == '4-VERY STRICT':
                    return ['4-VERY-STRICT']
                elif answer == '5' or answer == 'UBER-STRICT' or answer == 'UBER STRICT' or answer == '5-UBER-STRICT' or answer == '5-UBER STRICT':
                    return ['5-UBER-STRICT']
                elif answer == '6' or answer == 'UBER-PLUS-STRICT' or answer == 'UBER PLUS STRICT' or answer == '6-UBER-PLUS-STRICT' or answer == '6-UBER PLUS STRICT':
                    return ['6-UBER-PLUS-STRICT']
                else:
                    answer = input('Invalid choice, choose again.')
        elif (answer.upper() == 'N'):
            quit()
    else:
        return current_filters

    raise Exception("ERROR: find_filter_type. TBF I don't even know if this can happen.")


def get_filter_folder(): #TODO: Change folder selection to this method from find_filter_type
    pass

def get_filter_version(): #TODO: Find most current filter version and compare both
    pass



def update_filter(filters):
    for filter_type in filters:    
        filename = os.path.join('C:\\Users\\'+os.getlogin()+'\\Documents\\My Games\\Path of Exile',"NeverSink's filter - "+filter_type+".filter") #TODO: change to poe filter folder after testing
        if (filter_type == '0-SOFT'):
            git_file = requests.get(url_soft)
        elif (filter_type == '1-REGULAR'):
            git_file = requests.get(url_regular)
        elif (filter_type == '2-SEMI-STRICT'):
            git_file = requests.get(url_semi_strict)
        elif (filter_type == '3-STRICT'):
            git_file = requests.get(url_strict)
        elif (filter_type == '4-VERY-STRICT'):
            git_file = requests.get(url_very_strict)
        elif (filter_type == '5-UBER-STRICT'):
            git_file = requests.get(url_uber_strict)
        elif (filter_type == '6-UBER-PLUS-STRICT'):
            git_file = requests.get(url_uber_plus_strict)
        else:
            raise Exception('ERROR: git_file failed to find correct filter_type')

        filter_file = open(filename,'wb')
        filter_file.write(git_file.content)


filter_list = find_filter_type()
update_filter(filter_list)
getpass.getpass('\n\n\nPress ENTER to exit...')
