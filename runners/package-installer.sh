echo "Installing pip3 package manager"
brew install pip3
echo " "
echo "Installing python3"
brew install python

echo "Installing python dependencies"
echo " "
pip3 install pytest-xdist
pip3 install selenium
pip3 install webdriver-manager
pip3 install behave
echo " "
echo " "
echo "INSTALLATION COMPLETED."
echo " "
echo " "
pip3 --version
python3 --version 