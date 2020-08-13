from tabulate import tabulate
from pathlib import Path
import time
import sys


class PathwayToGlory:
    unchecked_pycharm_paths = [
                '/home/user/.java/.userPrefs/jetbrains/pycharm',
                '/var/lib/snapd/sequence/pycharm-professional.json',
                '~/.local/share/applications/jetbrains-pycharm.desktop',
                '~/.gnome/apps/jetbrains-pycharm.desktop',
                '~/.PyCharm*/',
                '/opt/pycharm*/',
                '/usr/local/bin/pycharm'
    ]

    def __init__(self):
        print('Checking Jetbrains Paths . . .')
        time.sleep(1)

    def get_paths(self, pycharm=None, webstorm=None):
        existing_paths = []

        if pycharm:
            for i in self.unchecked_pycharm_paths:
                if Path(i).exists():
                    existing_paths.append(Path(i))
                else:
                    continue
            return existing_paths
        elif webstorm:
            return 'Suan webstorm yok malesef'
        else:
            return 'Secenek giriniz: PyCharm veya Webstorm hangisi amk ?????'


class JetbrainsDeletion(PathwayToGlory):
    def __init__(self):
        super(JetbrainsDeletion, self).__init__()

        print('\n')
        print('###########################################################')
        print('Jetbrains Deletion')
        print('###########################################################')
        time.sleep(.5)

        self.paths = self.get_paths(pycharm=True)
        if self.paths:
            print('Matches found.')
            i = input("Do you want to delete? (y/n): ")
            self.question(i)
        else:
            print('Dosyalar bulunamadi')

    def question(self, answer):
        if answer.lower() == 'yes' or answer.lower() == 'y':
            print('Dosyalar siliniyor...')
            self.deletion()
        elif answer.lower() == 'no' or answer.lower() == 'n':
            return None
        else:
            print('Sorry, I didn\'t understand you.')

    def deletion(self):
        paths = self.paths

        removed_pycharm_paths = []

        for i in paths:
            removable_list = []

            if Path(i).is_file():
                # silme suresi
                start_time = time.time()
                removable_list.append(Path(i))
                Path(i).unlink()
                end_time = time.time() - start_time

                # add process time to list
                removable_list.append(end_time)

                # check file after delete
                if Path(i).is_file():
                    removable_list.append('File not exists')
                else:
                    removable_list.append('deleted')

                # sutune ekleme
                removed_pycharm_paths.append(removable_list)

                # delete to removable_list
                removable_list = []
            elif Path(i).is_dir():
                # silme suresi
                start_time = time.time()
                removable_list.append(Path(i))
                Path(i).rmdir()
                end_time = time.time() - start_time

                # add process time to list
                removable_list.append(end_time)

                # check file after delete
                if Path(i).is_file():
                    removable_list.append('File not exists')
                else:
                    removable_list.append('deleted')

                # sutune ekleme
                removed_pycharm_paths.append(removable_list)

                # delete to removable_list
                removable_list = []
            else:
                removable_list.append(Path(i))
                # sutune ekleme
                removed_pycharm_paths.append(removable_list)
                removable_list.append(0)
                removable_list.append('File not exists')

                # delete to removable_list
                removable_list = []

        print(
            tabulate(
                removed_pycharm_paths,
                headers=['Path', 'process_time', 'status'],
                tablefmt='orgtbl'
            )
        )


if __name__ == '__main__':
    JetbrainsDeletion()
