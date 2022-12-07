git submodule init
git submodule update --remote
rm packages/arduino
python update_softpackage.py
sudo apt-get install qemu-system-arm -y
