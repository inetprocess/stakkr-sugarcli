# Sugarcli Plugin for edyan/stakkr
Plugin made by Inet Process to run [sugarcli](https://github.com/inetprocess/sugarcli) commands

__WARNING: The plugin directory must be named `sugarcli`__ (complete path: plugins/sugarcli)

# Installation
Clone the repository in the plugins/ directory of your stakkr

```bash
$ cd plugins
$ git clone https://github.com/inetprocess/stakkr-sugarcli.git sugarcli
$ stakkr refresh-plugins
```

# sugarcli commands
Use `stakkr sugarcli` to use sugarcli. On the first run, sugarcli is downloaded.

Example to get a list of users:
```bash
cd www/sugarproject
stakkr sugarcli user:list --path .
```
