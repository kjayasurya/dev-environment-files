
## Using fonts and terminal color schemes

#### MesloLGS NF Font

cp MesloLGS* ~/.local/share/fonts

#### Coolnight gnome-terminal theme

dconf load /org/gnome/terminal/legacy/profiles:/ < ./coolnight.dconf


**IMPORTANT:** If dconf load coolnight.dconf doesn't work, use the hexcode in coolnight.gtp to set the terminal colors manually for the Coolnight color scheme. Or import the gnome-terminal-profiles.dconf 

