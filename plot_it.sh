


cat TH7.log | grep "channel: 1" | awk '{print $5}' > dd.txt

gnuplot < plot_it.gpt
