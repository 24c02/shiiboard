# shiiboard!
raspi gpio -> keyboard events for [Shiba Arcade](https://shiba.hackclub.com) machines

## usage:
`git clone https://github.com/24c02/shiiboard.git`

`cd shiiboard`

and...

```
sudo apt-get install python3-gpiozero python3-uinput
```

```
echo "uinput" | sudo tee /etc/modules-load.d/uinput.conf
```

```
sed -i '' "s|/home/pi/shiiboard/|$PWD/|g" shiiboard.service
```

edit `mapping.py` to your heart's content

```
sudo ln -s $PWD/shiiboard.service /etc/systemd/system/
```


`sudo service shiiboard start`?

WTFPL. there's barely any code lol