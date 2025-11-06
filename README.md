# shiiboard!
raspi gpio -> keyboard events for [Shiba Arcade](https://shiba.hackclub.com) machines

## usage:

```
sudo apt-get install python3-gpiozero python3-uinput
```

edit `mapping.py` to your heart's content

```
sudo ln -s /home/pi/shiiboard/shiiboard.service /etc/systemd/system/
```


`sudo service shiiboard start`?

WTFPL. there's barely any code lol