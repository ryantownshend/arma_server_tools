# arma server tools

Tools to manage running content on arma3server

## reference material

### commands

```
poetry run server --help
poetry run pull --help
```

Arma server stuff

- <https://community.bistudio.com/wiki/Arma_Dedicated_Server>
- <https://community.bistudio.com/wiki/server.cfg>
- <https://developer.valvesoftware.com/wiki/Arma_3_Dedicated_Server>

python libraries

-poetry
-click
-click_log
-rich
-PyYAML
-pytest

articles references

- <https://docs.python.org/3/library/subprocess.html>
- <https://docs.python.org/3/library/shutil.html>
- <https://docs.python.org/3/library/os.html?highlight=os%20symlink#os.symlink>

yaml files
yaml config in home dir

```
--- # ~/arma_server.yaml
username: steam_username
password: steam_password
workshop: "/home/steam/.steam/steamapps/workshop/content/107410"
arma_home: "/home/steam/.steam/steamcmd/arma3"
arma_configs: "/home/steam/arma_configs"
```

yaml config for specific server

- name: name of the server
- config: relative path to the arma cfg file, starting from the arma_configs folder
- port: port the server is on, defaults to 2302 if nothing is set
- mods: list of mods to load

without mods

```
--- # example without mods
name: direct_action_altis
config: direct_action/direct_action_altis.cfg
port: 2302
```

with mods

```
--- # example with some mods 
name: survival_altis
config: survival/survival_altis.cfg
mods: 
  - cba_a3 
  - niarms_all
```
