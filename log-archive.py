#!/usr/bin/env python3
import argparse
import os
import shutil
import datetime

def main():
    parser = argparse.ArgumentParser(description='Архивирование логов в tar.gz')
    parser.add_argument('log_directory', help='Директория с логами')
    args = parser.parse_args()

    log_directory = os.path.abspath(args.log_directory)

    if not os.path.isdir(log_directory):
        print(f"Ошибка: {log_directory} не является валидной директорией.")
        return

    archive_dir = 'archives'
    os.makedirs(archive_dir, exist_ok=True)

    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_base_name = os.path.join(archive_dir, f"logs_archive_{time}")

    try:
        shutil.make_archive(archive_base_name, 'gztar', log_directory)
        archive_path = archive_base_name + '.tar.gz'
        log_file = os.path.join(archive_dir, 'archive_log.txt')
        with open(log_file, 'a') as f:
            f.write(f"Архив создан для {log_directory} в {datetime.datetime.now()} и сохранён в {archive_path}\n")
        print(f"Архив успешно создан: {archive_path}")
    except PermissionError:
        print(f"Ошибка: Нет прав доступа к {log_directory} или {archive_dir}")
    except Exception as e:
        print(f"Ошибка при создании архива: {e}")

if __name__ == '__main__':
    main()
