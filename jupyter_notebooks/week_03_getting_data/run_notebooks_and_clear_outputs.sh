
for fil in *.ipynb; do 
  jupyter nbconvert --to notebook --execute --output=$fil $fil
#  jupyter nbconvert --ClearOutputPreprocessor.enabled=True   --to notebook --output=$fil $fil
done
