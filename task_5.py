"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet


def Ping(site):
    ping = subprocess.Popen(site, stdout=subprocess.PIPE)
    for line in ping.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


site_1 = ['ping', 'yandex.ru']
site_2 = ['ping', 'youtube.com']
if __name__ == '__main__':
    Ping(site_1)
    Ping(site_2)
