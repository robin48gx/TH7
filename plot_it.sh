


cat TH7.log | grep "channel: 1" | awk '{print $5}' > th7_ch1.txt

gnuplot < plot_it.gpt
