git submodule init
git submodule update --remote
rm packages/arduino
python3 update_softpackage.py 
