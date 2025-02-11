# BotListConverter 
Script that converts BotLists into a valid playerlist of a chosen format.

---

# List of supported formats:
- Nullcore (`ncc`)
- Lmaobox
  - Config (`lbox_cfg`)
  - Lua (`lbox_lua`)
- Amalgam (`amalgam`)
- *hook (`cathook`)
- TF2BD **(WIP, untested)** (`tf2bd`)

# List of supported databases:
- d3fc0n6's:
    - Cheater list (`cheater`)
    - Tacobot list (`tacobot`)
    - Pazer list (`pazer`)
- Rijin's [bots.tf](https://bots.tf/) database (`bot`)
- megascatterbomb's Mega Cheater Database (`mcdb`)
- Groups of your own choice (`groups`) (More details below.)
- Sleepy List RGL bans (`sleepy-rgl`)
- Hacker Police's marked cheater list (`hacker-police`)
- Your own ID list (`custom`) (HEAVILY WIP, details below)

# How to use:
1. Make sure python is installed. You can get it at https://www.python.org/downloads/. Make sure you add it to the PATH too, or else it'll be more difficult to use.
2. Download the source and open a command prompt or powershell window where you opened it. This can be done in the File Explorer by pressing `File -> Open Windows Powershell` or clicking the directory bar, typing `cmd` and pressing Enter.
3. Install the requirements. `python -m pip install -r requirements.txt` or double-click the `install_requirements.bat` file.
3. Run the script in the prompt you just opened. ```python .\main.py --help``` will display information on how to use it.
4. Once you finish using it, import the newly exported playerlist into whatever training software you're using.

---
# Launch options
Parameter | Description
--------- | -----------
`-l` | The list to download.
`-f` | The output format.
`-m` | Merge all steam group lists into one.

## Example usage:
### To export a bot list for Nullcore:
```powershell
python .\main.py -l bot -f ncc
```
### To export a list of TF2BD users for Amalgam:
```powershell
python .\main.py -l pazer -f amalgam
```
---
# Groups layout explanation
<details>
  <summary>How to get the guild IDs</summary>

  ![showcase](https://i.postimg.cc/gkfXrP9c/image.png)
  
</details>

This is the layout of the group file (e.g. groups.txt)
```
somegroupid
whatevergroup
COWHOOKLOVERS
```

---
# Credits
- [Leadscales](https://github.com/leadscales) - for making the [original version](https://github.com/leadscales/PazerListNCC)
- [Surepy/sleepy](https://github.com/surepy) - for the [base](https://github.com/surepy/tf2db-sleepy-list/blob/main/export_megacheaterdb_as_tf2bd.py) for the [MCDB parser](https://github.com/PiantaMK/BotListConverter/blob/main/src/parser/megadb.py)

# Custom ID lists
Create a python file in the `lists` directory.
Requires:
- A value named `__ATTR__`.
- `__ATTR__['name']` is your own name of the list.
- A function named `__call__` that returns a dict or list of SteamIDs.
<details>
  <summary>Very simple example</summary>

  ```python
  __ATTR__ = {
    'name': 'My own list'
  }

  def __call__():
    return ['STEAM_0:0:12345678', 'STEAM_0:0:87654321']
  ```
  A more detailed example can be found in `lists/example.py`.
</details>

# Community server banlists
- Scripts that generate a list of SteamIDs from a community server banlist are found in `src/gen`.

- They generate a JSON list of SteamIDs that can be used in the converter.

- **WARNING: I am not responsible for IP blocks from the website admins.**

- Supported websites:

    - SourceBans
    - SourceBans++
    - [Rent-a-Medic](https://rentamedic.org/)

(`lists/example.py` is an example of converting this format into a list of IDs.)
