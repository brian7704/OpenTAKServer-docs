# Symbology

## ATAK default icon sets

OpenTAKServer supports all the default icon sets that come with ATAK. The installer will automatically put them in
OpenTAKServer's database in the icons table. If for some reason the icons are missing from the database,
OpenTAKServer will automatically download them from the installer's GitHub repo when it starts up. 


## MIL-STD-2525c

OpenTAKServer's web UI supports MIL-STD-2525C symbols thanks to the [milsymbol](https://github.com/spatialillusions/milsymbol) 
javascript library. When OpenTAKServer received a CoT, it calculates the 2525c type from the CoT's type attribute. The
web UI will automatically generate the icons on the fly.