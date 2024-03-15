1. Поднять контейнер: `docker compose up -d --build`
2. В PowerShell: `docker exec -it ubuntu bash`
3. `apt update`
4. `apt upgrade -y`
5. `apt install wget -y`
6. `apt install python3 -y`
7. `apt install python3-pip -y`
8. `apt install python3-venv -y`
9. `apt install vim -y`
10. `apt install -y libsndfile1 ffmpeg`
11. `source ~/.bashrc`
12. `cd /home/user/lab1_files`
13. `python3 -m venv env`
14. `source env/bin/activate`
15. `pip3 install Cython`
16. `pip3 install nemo_toolkit['all']`
17. `pip3 install fastapi`
18. `pip3 install uvicorn`
19. `pip3 install python-multipart`
20. `pip3 install requests`
21. `mkdir data && cd data`
22. `wget https://github.com/sberdevices/golos/raw/master/examples/data/001ce26c07c20eaa0d666b824c6c6924.wav`
23. `cd ../ && mkdir models && cd models`
24. `wget https://us.openslr.org/resources/114/QuartzNet15x5_golos.nemo.gz`
25. `gzip -dv QuartzNet15x5_golos.nemo.gz`
26. `cd ../ && mkdir -p src/examples && cd src/examples`
27. `wget https://raw.githubusercontent.com/sberdevices/golos/master/examples/infer.py`
28. `vim test.py`; ...; `wq!`
29. `cd ../`
30. `vim server.py`; ...; `wq!`
31. `vim client.py`; ...; `wq!`
32. `python3 server.py ../models/QuartzNet15x5_golos.nemo`
33. `python3 client.py -f ../data/001ce26c07c20eaa0d666b824c6c6924.wav`