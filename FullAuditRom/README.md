## Full Audit Rom

Get it through the terminal with ``` wget https://raw.githubusercontent.com/Voljega/scripts4recalbox/master/FullAuditRom/FullAuditRom.py -O FullAuditRom.py ```

This script allows you to launch an audit of all your roms

It will display for each rom the following information :
System Name "Rom File Exists" "Rom Scrape Image Exists" "Rom Is Scraped" "Rom is Hidden" "Rom Full Path" "Rom Scrape Image Full Path"

Script usage is simple : copy it where you like in the share partition then execute it with *python FullAuditRom.py*
Additionaly you can limit the systems you want to audit directly on the command line i.e. *python SystemSorter.py snes gb*

The audit file can then be found at the end of the process in */recalbox/share*

### How it works

The script uses the */recalbox/share_init/system/.emulationstation/es_systems.cfg* to get the list of systems and the extensions of their roms.
For every non-excluded system it then get the full list of roms and match them with the *gamelist.xml* of the system.

