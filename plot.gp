set title noenhanced "Difference of Centigrade vs n_uv_to_c(n_c_to_uv(C))"
set ylabel "Difference in uV"
set xlabel "Centigrade (C)"
set xrange[-280:1310]
#set yrange[-15:15]
set term png giant size 1920,1080
set output "out.png"
plot "data.txt" with impulses
