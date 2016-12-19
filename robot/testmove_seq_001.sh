echo "5 seconds forward"
sudo ./threaded.py --seconds 5 --direction -1
echo "4 seconds turn right"
sudo ./turn.py --seconds 4 --direction -1
echo "5 seconds forward"
sudo ./threaded.py --seconds 5 --direction -1
echo "4 seconds turn right"
sudo ./turn.py --seconds 4 --direction -1
echo "10 seconds forward"
sudo ./threaded.py --seconds 10 --direction -1
echo "2 seconds turn left"
sudo ./turn.py --seconds 2 --direction 1
echo "8 seconds back"
sudo ./threaded.py --seconds 8 --direction 1

