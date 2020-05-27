#!/bin/bash

LOGFILE=$(cut -c 11- TH7.log | sed -e '/STARTED/d' -e 's/^Channel \([0-9]\):\s\s*\([0-9\.\-][0-9\.\-]*\)\suV.*\s\([0-9\.\-][0-9\.\-]*\)\soC, type=\([A-Z]\).*\([0-9]\).$/\1,\2,\3,\4,/g' -e '/DISCONNECT/s/^Channel \([0-9]\).*$/\1,DCO,DCO,DCO,/g' -e 's/^vadj:\s*\([0-9\.\-][0-9\.\-]*\).*$/\1,/g' -e 's/^vadj_now:.*Vdd\s*\([0-9\.\-][0-9\.\-]*\).*$/\1,/g' -e 's/^PCB_TEMP\s*\([0-9\.\-][0-9\.\-]*\)oC.*$/\1,/g' -e '/^[0-9][0-9][0-9][0-9]-/ s/$/A/g' | tr -d '\n' | tr 'A' '\n' | sed -e 's/\.\([0-9][0-9]*\)$//g')


#echo "$LOGFILE"
FIRST_TIMESTAMP=$(echo "$LOGFILE" | grep -Eo '[0-9]{4}-[0-9]{2}-[0-9]{2}\s*[0-9]{2}:[0-9]{2}:[0-9]{2}' | head -n 1)
LAST_TIMESTAMP=$(echo "$LOGFILE" | grep -Eo '[0-9]{4}-[0-9]{2}-[0-9]{2}\s*[0-9]{2}:[0-9]{2}:[0-9]{2}' | tail -n 1)

# awk script with premade gnuplot files for uv and c goes here....
CH1_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$3}' | sed '/DCO/d')
CH2_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$7}' | sed '/DCO/d')
CH3_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$11}'| sed '/DCO/d')
CH4_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$15}' | sed '/DCO/d')
CH5_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$19}' | sed '/DCO/d')
CH6_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$23}' | sed '/DCO/d')
CH7_C=$(echo "$LOGFILE" |  awk -F, '{OFS=", ";print $32,$27}' | sed '/DCO/d')

echo "$CH1_C" > "ch1_c.txt"
echo "$CH2_C" > "ch2_c.txt"
echo "$CH3_C" > "ch3_c.txt"
echo "$CH4_C" > "ch4_c.txt"
echo "$CH5_C" > "ch5_c.txt"
echo "$CH6_C" > "ch6_c.txt"
echo "$CH7_C" > "ch7_c.txt"

GNUPLOT_ARGS="set title noenhanced \"Test Graph from "$FIRST_TIMESTAMP" to "$LAST_TIMESTAMP"\"
set ylabel \"Temperature (oC)\"
set grid
set datafile sep \",\"
set key box opaque
set xdata time
set timefmt \"%Y-%m-%d %H:%M:%S\"
set format x \"%H:%M\"
set xrange[\""$FIRST_TIMESTAMP"\":\""$LAST_TIMESTAMP"\"]
set term png giant size 1920,1080
set output \"out.png\"
plot \"ch1_c.txt\" using 1:2 title \"Channel 1\" with lines, \"ch2_c.txt\" using 1:2 title \"Channel 2\" with lines, \"ch3_c.txt\" using 1:2 title \"Channel 3\" with lines, \"ch4_c.txt\" using 1:2 title \"Channel 4\" with lines, \"ch5_c.txt\" using 1:2 title \"Channel 5\" with lines, \"ch6_c.txt\" using 1:2 title \"Channel 6\" with lines, \"ch7_c.txt\" using 1:2 title \"Channel 7\" with lines"

echo "$GNUPLOT_ARGS" > "gnuplot_th7_c.gpt"

gnuplot gnuplot_th7_c.gpt
