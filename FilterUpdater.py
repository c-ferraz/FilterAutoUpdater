# VERSiON 1.1.1
# BY C. FERRAZ
# https://github.com/c-ferraz

import getpass
import os
import re
import shutil
import sys
from datetime import datetime

import easygui
import requests

url_soft = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%200-SOFT" \
           r".filter "
url_regular = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%201" \
              r"-REGULAR.filter "
url_semi_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20" \
                  r"-%202-SEMI-STRICT.filter "
url_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20-%203" \
             r"-STRICT.filter "
url_very_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20" \
                  r"-%204-VERY-STRICT.filter "
url_uber_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter%20" \
                  r"-%205-UBER-STRICT.filter "
url_uber_plus_strict = r"https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter/master/NeverSink's%20filter" \
                       r"%20-%206-UBER-PLUS-STRICT.filter "
needs_backup = True


def get_filter_folder():
    filter_folder = 'C:\\Users\\' + os.getlogin() + '\\Documents\\My Games\\Path of Exile'
    if not os.path.exists(filter_folder):
        print('The default folder for filters: ' + filter_folder + '\nWas not found.')
        print('You can choose any folder if you wish only to download a filter.')
        while True:
            print('Please choose the folder where filters are located.')
            filter_folder = easygui.diropenbox()
            user_answer = ''
            while not (user_answer == 'Y'):
                print('You have chosen the folder ' + filter_folder + ' Is this correct? (Y/N)')
                user_answer = input().upper()
                if user_answer == 'Y':
                    return filter_folder
                if user_answer == 'N':
                    print('Do you wish to choose another folder? (Y/N)')
                    user_answer = input().upper()
                    while not (user_answer == 'Y'):
                        if user_answer == 'Y':
                            pass
                        elif user_answer == 'N':
                            print('Exiting the program.')
                            end_execution()
                        else:
                            print('Please enter only Y or N.')
                            user_answer = input().upper()
                else:
                    print('Please enter only Y or N.')
                    user_answer = input().upper()
    else:
        return filter_folder


def find_filter_type(filter_folder):
    current_filters = []
    for files in os.listdir(filter_folder):
        if '.filter' in files:
            filter_type = re.search(r'(-|_)(.*)\.filter', files)
            current_filters.append(filter_type.group(2).upper().replace('_', '-').strip())
    print(current_filters)
    if len(current_filters) == 0:
        print('No NeverSkin filter found, do you wish to download one? (Y/N)')
        user_answer = input().upper()
        while True:
            if user_answer == 'Y' or user_answer.upper() == 'N':
                break
            else:
                print('Please enter only Y or N.')
                user_answer = input().upper()
        if user_answer == 'Y':
            global needs_backup
            needs_backup = False
            print('Choose filter type:')
            print('0-SOFT\n1-REGULAR\n2-SEMI-STRICT\n3-STRICT\n4-VERY-STRICT\n5-UBER-STRICT\n6-UBER-PLUS-STRICT')
            user_answer = input().upper()
            while True:
                if user_answer == '0' or user_answer == 'SOFT' or user_answer == '0-SOFT':
                    return ['0-SOFT']
                elif user_answer == '1' or user_answer == 'REGULAR' or user_answer == '1-REGULAR':
                    return ['1-REGULAR']
                elif user_answer == '2' or user_answer == 'SEMI-STRICT' or user_answer == 'SEMI STRICT' \
                        or user_answer == '2-SEMI-STRICT' or user_answer == '2-SEMI STRICT':
                    return ['2-SEMI-STRICT']
                elif user_answer == '3' or user_answer == 'STRICT' or user_answer == '1-STRICT':
                    return ['3-STRICT']
                elif user_answer == '4' or user_answer == 'VERY-STRICT' or user_answer == 'VERY STRICT' \
                        or user_answer == '4-VERY-STRICT' or user_answer == '4-VERY STRICT':
                    return ['4-VERY-STRICT']
                elif user_answer == '5' or user_answer == 'UBER-STRICT' or user_answer == 'UBER STRICT' \
                        or user_answer == '5-UBER-STRICT' or user_answer == '5-UBER STRICT':
                    return ['5-UBER-STRICT']
                elif user_answer == '6' or user_answer == 'UBER-PLUS-STRICT' or user_answer == 'UBER PLUS STRICT' \
                        or user_answer == '6-UBER-PLUS-STRICT' or user_answer == '6-UBER PLUS STRICT':
                    return ['6-UBER-PLUS-STRICT']
                else:
                    print('Invalid choice, choose again.')
                    user_answer = input().upper()
        elif user_answer == 'N':
            end_execution()
    else:
        return current_filters

    print('ERROR: @find_filter_type(). This should not happen.')
    print('Folder used: ' + folder)
    print('Filters found: ')
    print(current_filters)
    print('Please Screenshot this and send to me.')
    end_execution()


def get_filter_version():  # TODO: Find updated and current filter version and compare both
    pass


def backup_old_filters(filter_folder):
    filter_list = []
    for items in os.listdir(filter_folder):
        if ".filter" in items:
            filter_list.append(items)
    current_date = datetime.now()
    current_date = current_date.strftime("%y-%m-%d-%H%M%S")
    os.makedirs(filter_folder + "\\filterBackup" + current_date, exist_ok=True)
    for items in filter_list:
        src = os.path.join(filter_folder, items)
        dest = os.path.join(filter_folder, "filterBackup" + current_date)
        shutil.copy(src, dest)
        if os.path.exists(os.path.join(dest, items)):
            os.remove(src)
        else:
            print('ERROR failed to backup file:' + items)
    print('Old filters have been backed-up to ' + str(os.path.join(filter_folder, "filterBackup" + current_date)))


def install_my_custom():  # TODO: If yes, download STRICT filter and add my custom changes to it, also copy .mp3
    # files into filters folder
    print('Do you wish to install my custom NeverSink STRICT filter? (Y/N)')
    user_answer = input()
    pass


def end_execution():
    getpass.getpass('Press ENTER to exit...')  # TODO: This won't work if you run the script on terminal
    sys.exit(0)


def update_filter(filter_list, filter_folder):
    updated_at_least_one = False
    for filter_type in filter_list:
        filename = os.path.join(filter_folder, "NeverSink's filter - " + filter_type + ".filter")
        if filter_type == '0-SOFT':
            git_file = requests.get(url_soft)
            updated_at_least_one = True
        elif filter_type == '1-REGULAR':
            git_file = requests.get(url_regular)
            updated_at_least_one = True
        elif filter_type == '2-SEMI-STRICT':
            git_file = requests.get(url_semi_strict)
            updated_at_least_one = True
        elif filter_type == '3-STRICT':
            git_file = requests.get(url_strict)
            updated_at_least_one = True
        elif filter_type == '4-VERY-STRICT':
            git_file = requests.get(url_very_strict)
            updated_at_least_one = True
        elif filter_type == '5-UBER-STRICT':
            git_file = requests.get(url_uber_strict)
            updated_at_least_one = True
        elif filter_type == '6-UBER-PLUS-STRICT':
            git_file = requests.get(url_uber_plus_strict)
            updated_at_least_one = True
        else:
            pass
        try:
            filter_file = open(filename, 'wb')
            filter_file.write(git_file.content)
        except BaseException:
            print(f'Error updating filter {filter_type}')

        print('%s has been successfully updated' % filter_type)

    if not updated_at_least_one:
        print('ERROR: git_file failed to find correct filter_type. No filters where updated.')
        print('This might happen if your filters are named differently from the default or if they are not a NeveSink '
              'filter.')
        end_execution()


# METHOD CALLS=================================================
folder = get_filter_folder()
filters = find_filter_type(folder)

print('Using folder: ' + folder)
print('For filter selection...')
print('The following Filters will be updated:')
for _filter in filters:
    print(_filter)
print('Do you wish to continue with update? (Y/N)')
answer = input().upper()
while True:
    if answer == 'Y':
        break
    if answer == 'N':
        end_execution()
    print('Please enter only Y or N.')
    answer = input().upper()

backup_old_filters(folder)

update_filter(filters, folder)

print('\n\n\nUpdate complete.')
end_execution()
