
# Reset root password using GRUB

If you have physical access to a host whose hard drive is accessible, and there are no security measures such as disk 
encryption, disabled GRUB, or external server authentication, the following instructions will work.  

### In my case it's Ubuntu OS.

1. During OS reset press and hold SHIFT.
2. Go for option picks: 
- Advanced options for Ubuntu
- Ubuntu, with ... **(recovery mode)**
- <Under "Recovery Menu" take **"root"**
- Click **ENTER** in case of "Press Enter for maintenence"
- In terminal type: **mount -rw -o remount /**
- **passwd root** (change password for root)
- **reboot**


Useful documenatation:
- https://www.gnu.org/software/grub/manual/grub/grub.html
- https://en.wikibooks.org/wiki/Linux_Guide/Reset_a_forgotten_root_password