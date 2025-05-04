siren="siren:/home/vince/revisiting-axelrod-second/src/data"

rsync -avr --include="*summary.csv" --include="training_data_original_tournament*" --include="players.index" --include="*.json" --include="*.gz" --include="*/" --exclude="*" $siren .
