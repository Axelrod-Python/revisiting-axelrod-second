raven="raven:/scratch/smavak/revisiting-axelrod-second/src/data"

rsync -avr --include="*summary.csv" --include="*.gz" --include="*/" --exclude="*" $raven .
