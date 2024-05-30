# Use case 7 (Lab)

https://majeed1419-use-case-7-app-mmqtak.streamlit.app/
curl -X 'POST' \
  'https://football-player-price-predict.onrender.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "appearance": 0,
  "minutes_played": 0,
  "current_value": 0,
  "award": 0
}'
