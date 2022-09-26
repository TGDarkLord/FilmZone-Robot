if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TGDarkLord/FilmZone-Robot.git /FilmZone-Robot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FilmZone-Robot
fi
cd /FilmZone-Robot
pip3 install -U -r requirements.txt
echo "Starting FilmZone RoBot...."
python3 main.py
