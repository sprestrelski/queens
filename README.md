# queens archive
hi i want to keep an archive of linkedin queens bc i like the game! anyway

## pull grid off linkedin 
using selenium will work, but not from a github action due to linkedin's security checks. leaving the selenium script up for posterity

### run selenium
to run locally, make a config.py file with the words
```
username = 'username'
password = 'password'
```

### manually upload
instead, `upload_grid.py` takes in the html download of the site and outputs the grid

## convert html to representation of star grid
colors
```
0: purple
1: orange
2: blue
3: green
4: grey
5: pink
6: teal
7: red
8: yellow
9: brown 
```

## show grid
site built using react redux!  

to run
```
npm install
npm run dev
```

## logic for gameplay
