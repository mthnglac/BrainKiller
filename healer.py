from pathlib import Path
import tarfile
import time
import os


class PathWayToGlory:
    unchecked_pycharm_paths = [
        '/home/user/Downloads/pycharm*.tar.gz'
    ]

    def __init__(self):
        print('Checking Installation File . . .')
        time.sleep(1)

    def check_file(self, pycharm=None, webstorm=None):
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


class JetbrainsInstallation(PathWayToGlory):
    def __init__(self):
        super(JetbrainsInstallation, self).__init__()
        print('###########################################################')
        print('Jetbrains Installation')
        print('###########################################################')
        time.sleep(.5)

        self.paths = self.check_file(pycharm=True)
        if self.paths:
            print('Match Found')
            time.sleep(1)
            i = input('Do you want to install? (y/n): ')
            self.question(i)
        else:
            print('Install dosyasi bulunamadi')

    def question(self, answer):
        if answer.lower() == 'yes' or answer.lower() == 'y':
            self.installation()
        elif answer.lower() == 'no' or answer.lower() == 'n':
            return None
        else:
            print('Sorry, I didn\'t understand you.')

    @staticmethod
    def installation():
        print('/opt/pycharm/ yoluna dosya cikartiliyor . . .')
        time.sleep(1)
        tar = tarfile.open('/home/user/Downloads/pycharm*.tar.gz')
        tar.extractall(path='/opt/')
        tar.close()
        print('Dosya belirtilen yola cikartildi')
        time.sleep(1)
        print('Program calistiriliyor . . .')
        time.sleep(1)
        os.system('sh /opt/pycharm-*/bin/pycharm/sh')

        print('###########################################################')
        print('###########################################################')
        print('yukleme islemi basariyla tamamlandi metocum ;*****')


if __name__ == '__main__':
    JetbrainsInstallation()
