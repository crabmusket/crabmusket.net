cd blog
hugo -b 'https://crabmusket.net'

cd public/dc
python3 ../../../hh.py > hh.atom
