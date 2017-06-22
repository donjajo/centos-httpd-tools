# centos-httpd-tools
A Debian user and fan, found myself in RedHat community  and the stress of making symbolic links to just enable sites was tiring, I came up with this to help myself.

## Dependencies
* httpd
* Python 3


## Features
* Enable and disable sites
* Show enabled and disabled sites


## How to use:
### Enable a site:
```sh
$ sudo python3 httpd-tools.py ensite site.conf
```

### Disable a site:
```sh
$ sudo python3 httpd-tools.py dissite site.conf
```

### Show available/disabled sites
```sh
$ sudo python3 httpd-tools.py show available
```

### Show enabled sites
```sh
$ sudo python3 httpd-tools.py show enabled
```

## Contribute
You are free to fork or contribute. I have some other things taking my time, but in free time I improve this program.

Shalom!
