#!/bin/bash

apt update
apt upgrade -y
apt install python3 -y
apt install python3-pip -y
apt install python3-venv -y
apt install vim -y
apt install locales -y
source ~/.bashrc
locale-gen ru_RU
locale-gen ru_RU.UTF-8
update-locale

variable='LANG="ru_RU.utf8"'

# Переменная, которую нужно добавить в ~/.bash_profile
variable='LANG="ru_RU.utf8"'

# Проверяем, существует ли файл ~/.bash_profile
if [ -f ~/.bash_profile ]; then
    # Проверяем, есть ли уже такая переменная в файле
    if grep -q "$variable" ~/.bash_profile; then
        echo "Переменная уже существует в ~/.bash_profile."
    else
        # Добавляем переменную в файл
        echo "$variable" >> ~/.bash_profile
        echo "Переменная успешно добавлена в ~/.bash_profile."
    fi
else
    # Если файл не существует, создаем его и добавляем переменную
    echo "$variable" > ~/.bash_profile
    echo "Файл ~/.bash_profile создан, и переменная успешно добавлена."
fi

# Экспортируем переменную
echo 'export LANG' >> ~/.bash_profile

cd /home/user/lab3_files
python3 -m venv env
source env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
python3 -m spacy download ru_core_news_sm
python3 -m spacy download ru_core_news_md
python3 -m spacy download ru_core_news_lg
