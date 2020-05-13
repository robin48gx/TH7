set title noenhanced "Difference of C - to_c(to_uv(C))"
set ylabel "Difference in uV"
set xlabel "Centigrade (C)"
set xrange[-200:1400]
set yrange[-600:600]
set term png giant size 1920,1080
set output "out.png"

plot "data_j.txt" using 1:2 title "J-type", "data_n.txt" using 1:2 title "N-type", "data_k.txt" using 1:2 title "K-type", "data_t.txt" using 1:2 title "T-type"
