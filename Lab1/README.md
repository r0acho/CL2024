1. Поднять контейнер: `docker compose up -d --build`
2. В PowerShell: `docker exec -it ubuntu bash`
3. `chmod +x /home/user/lab1_files/setup_script.sh && /home/user/lab1_files/setup_script.sh`
4. `vim test.py`; ...; `wq!`
5. `cd ../`
6. `vim server.py`; ...; `wq!`
7. `vim client.py`; ...; `wq!`
8. `python3 server.py ../models/QuartzNet15x5_golos.nemo`
9. `python3 client.py -f ../data/001ce26c07c20eaa0d666b824c6c6924.wav`
