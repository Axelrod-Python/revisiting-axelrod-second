raven="raven:/scratch/smavak/revisiting-axelrod-second/src/data"

rsync -avr --include="*summary.csv" --include="training_data_original_tournament*" --include="*.gz" --include="*/" --exclude="*" $raven .
