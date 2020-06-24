#VERSON 1.1.0
#BY C. FERRAZ
#https://github.com/c-ferraz

import requests
import os,sys
import re
import getpass
import easygui
import shutil
from datetime import datetime

url_soft = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%200-SOFT.filter"
url_regular = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%201-REGULAR.filter"
url_semi_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%202-SEMI-STRICT.filter"
url_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%203-STRICT.filter"
url_very_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%204-VERY-STRICT.filter"
url_uber_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%205-UBER-STRICT.filter"
url_uber_plus_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%206-UBER-PLUS-STRICT.filter"
needs_backup = True

def get_filter_folder(): 
    filter_folder = 'C:\\Users\\'+os.getlogin()+'\\Documents\\My Games\\Path of Exile'
    if not os.path.exists(filter_folder):
        print('The default folder for filters: '+filter_folder+'\nWas not found.')
        print('You can choose any folder if you wish only to download a filter.')
        while True:
            print('Please choose the folder where filters are located.')
            filter_folder = easygui.diropenbox()
            answer = ''
            while not (answer == 'Y'):
                print('You have choosen the folder '+filter_folder+' Is this correct? (Y/N)')
                answer = input().upper()
                if (answer == 'Y'):
                    return filter_folder
                if (answer == 'N'):
                    print('Do you wish to choose another folder? (Y/N)')
                    answer = input().upper()
                    while not (answer == 'Y'):
                        if (answer == 'Y'):
                            pass
                        elif (answer == 'N'):
                            print('Exiting the program.')
                            end_execution()
                        else:
                            print('Please enter only Y or N.')
                            answer = input().upper()
                else:
                    print('Please enter only Y or N.')
                    answer = input().upper()
    else:
        return filter_folder
    print('ERROR: @get_filter_folder(). This should not happen.')
    print('Default folder found? '+os.path.exists(filter_folder))
    print('Folder used: '+filter_folder)
    print('Please send this to me.')
    end_execution()


def find_filter_type(filter_folder):
    current_filters = []
    for files in os.listdir(filter_folder):
        if '.filter' in files:
            filter_type = re.search(r'(-|_)(.*)\.filter', files)
            current_filters.append(filter_type.group(2).upper().replace('_','-').strip())
    print(current_filters)
    if len(current_filters) == 0:
        print('No NeverSkin filter found, do you wish to download one? (Y/N)')
        answer = input().upper()
        while True:
            if (answer.upper() == 'Y' or answer.upper() == 'N'):
                break
            else:
                print('Please enter only Y or N.')
                answer = input().upper()
        if (answer.upper() == 'Y'):
            global needs_backup 
            needs_backup = False
            print('Choose filter type:')
            print('0-SOFT\n1-REGULAR\n2-SEMI-STRICT\n3-STRICT\n4-VERY-STRICT\n5-UBER-STRICT\n6-UBER-PLUS-STRICT')
            answer = input().upper()
            while True:
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
                    print('Invalid choice, choose again.')
                    answer = input().upper()
        elif (answer.upper() == 'N'):
            end_execution()
    else:
        return current_filters

    print('ERROR: @find_filter_type(). This should not happen.')
    print('Folder used: '+folder)
    print('Filters found: '+current_filters)
    print('Please send this to me.')
    end_execution()


def get_filter_version(): #TODO: Find updated and current filter version and compare both
    pass


def backup_old_filters(folder):
    filter_list = []
    for items in os.listdir(folder):
        if (".filter" in items):
            filter_list.append(items)
    current_date = datetime.now()
    current_date = current_date.strftime("%y-%m-%d-%H%M%S")
    os.makedirs(folder+"\\filterBackup"+current_date, exist_ok = True)
    for items in filter_list:
        src = os.path.join(folder, items)
        dest = os.path.join(folder, "filterBackup"+current_date)
        shutil.copy(src, dest)
        if (os.path.exists(os.path.join(dest, items))):
            os.remove(src)
        else:
            print('ERROR failed to backup file:' + items)
    print('Old filters have been backed-up to '+str(os.path.join(folder,"filterBackup"+current_date)))


def install_my_custom(): #TODO: If yes, download STRICT filter and add my custom changes to it, also copy .mp3 files into filters folder
    print('Do you wish to install my custom NeverSink STRICT filter? (Y/N)')
    answer = input()
    pass


def end_execution():
    getpass.getpass('Press ENTER to exit...')
    sys.exit()


def update_filter(filters, folder):
    updated_at_least_one = False
    for filter_type in filters:    
        filename = os.path.join(folder,"NeverSink's filter - "+filter_type+".filter")
        if (filter_type == '0-SOFT'):
            git_file = requests.get(url_soft)
            updated_at_least_one = True
        elif (filter_type == '1-REGULAR'):
            git_file = requests.get(url_regular)
            updated_at_least_one = True
        elif (filter_type == '2-SEMI-STRICT'):
            git_file = requests.get(url_semi_strict)
            updated_at_least_one = True
        elif (filter_type == '3-STRICT'):
            git_file = requests.get(url_strict)
            updated_at_least_one = True
        elif (filter_type == '4-VERY-STRICT'):
            git_file = requests.get(url_very_strict)
            updated_at_least_one = True
        elif (filter_type == '5-UBER-STRICT'):
            git_file = requests.get(url_uber_strict)
            updated_at_least_one = True
        elif (filter_type == '6-UBER-PLUS-STRICT'):
            git_file = requests.get(url_uber_plus_strict)
            updated_at_least_one = True
        else:
            pass
        try:
            filter_file = open(filename,'wb')
            filter_file.write(git_file.content)
        except:
            print('Error updating filter %s' %filter_type)
        
        print('%s has been sucesfully updated' %filter_type)

    if not (updated_at_least_one):
        print('ERROR: git_file failed to find correct filter_type. No filters where updated.')
        print('This might happen if your filters are named differently from the default or if they are not a NeveSink filter.')
        end_execution()

        







#METHOD CALLS=================================================
folder = get_filter_folder()
filters = find_filter_type(folder)

print('Using folder: ' + folder)
print('For filter selection...')
print('The following Filters will be updated:')
for filter in filters:
    print(filter)
print('Do you wish to continue with update? (Y/N)')
answer = input().upper()
while True:
    if (answer == 'Y'):
        break
    if (answer == 'N'):
        end_execution()
    print('Please enter only Y or N.')
    answer = input().upper()

backup_old_filters(folder)

update_filter(filters, folder)

print('\n\n\nUpdate complete.')
end_execution()
