md=".md"
html=".html"
dir="../HTMLs/"

for f in *.md
do
  inname="$f"
  outname="$dir${f:0:$((${#f} - 0 - 3))}$html"
  touch $outname
  python .markdown2.py $inname > $outname
done
