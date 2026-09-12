moves="15F6B6B5L16R8B16F20L6F13F11R"

res=$(curl -s -X POST localhost:5000/adventurers/adventurer-1/make_moves \
  -H 'Content-Type: application/json' \
  -d "{\"moves\": \"$moves\"}")

dist_tail="${res##*\"dist\":}"
dist_val="${dist_tail%%,*}"
dist_val="${dist_val%%\}*}"
dist_val="${dist_val%%]*}"

final_dist="${dist_val// /}"

echo $final_dist