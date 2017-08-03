raven="raven:/scratch/smavak/revisiting-axelrod-second/src/data"

rsync -avr --include="*.gz" --include="*/" --exclude="*" $raven .
