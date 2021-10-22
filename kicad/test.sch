EESchema Schematic File Version 5
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
Comment5 ""
Comment6 ""
Comment7 ""
Comment8 ""
Comment9 ""
$EndDescr
$Comp
L test-rescue:MCP3208-Analog_ADC U3
U 1 1 5B45AFF3
P 9600 3350
F 0 "U3" H 9600 4028 50  0001 C CNN
F 1 "MCP3208" H 9200 3800 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_5.3x10.2mm_P1.27mm" H 9700 3450 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21298c.pdf" H 9700 3450 50  0001 C CNN
	1    9600 3350
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:MCP6074-E_SL-MCP6074-E_SL U1
U 1 1 5B47A65B
P 5750 2100
F 0 "U1" H 5750 2870 50  0000 C CNN
F 1 "MCP6074-E_SL" H 5750 2779 50  0000 C CNN
F 2 "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm" H 5750 2100 50  0001 L BNN
F 3 "1.57 USD" H 5750 2100 50  0001 L BNN
F 4 "Microchip" H 5750 2100 50  0001 L BNN "Field4"
F 5 "MCP6074 Series 6 V 1.2 MHz Rail-to-Rail I/O Operational Amplifier-SOIC-14LD" H 5750 2100 50  0001 L BNN "Field5"
F 6 "Good" H 5750 2100 50  0001 L BNN "Field6"
F 7 "SOIC-14 Microchip" H 5750 2100 50  0001 L BNN "Field7"
F 8 "MCP6074-E/SL" H 5750 2100 50  0001 L BNN "Field8"
	1    5750 2100
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:MCP6074-E_SL-MCP6074-E_SL U2
U 1 1 5B47B34D
P 5750 3750
F 0 "U2" H 5750 4520 50  0000 C CNN
F 1 "MCP6074-E_SL" H 5750 4429 50  0000 C CNN
F 2 "Package_SO:SOIC-14_3.9x8.7mm_P1.27mm" H 5750 3750 50  0001 L BNN
F 3 "1.57 USD" H 5750 3750 50  0001 L BNN
F 4 "Microchip" H 5750 3750 50  0001 L BNN "Field4"
F 5 "MCP6074 Series 6 V 1.2 MHz Rail-to-Rail I/O Operational Amplifier-SOIC-14LD" H 5750 3750 50  0001 L BNN "Field5"
F 6 "Good" H 5750 3750 50  0001 L BNN "Field6"
F 7 "SOIC-14 Microchip" H 5750 3750 50  0001 L BNN "Field7"
F 8 "MCP6074-E/SL" H 5750 3750 50  0001 L BNN "Field8"
	1    5750 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 1700 6900 1700
Wire Wire Line
	6550 2100 6750 2100
Wire Wire Line
	6750 2100 6750 2200
Wire Wire Line
	6550 2300 6700 2300
Wire Wire Line
	6700 2300 6700 2450
$Comp
L test-rescue:LM4040DBZ-4.1-Reference_Voltage D1
U 1 1 5B4AD8FF
P 1250 1300
F 0 "D1" H 1250 1516 50  0000 C CNN
F 1 "LM4040DBZ-4.1" H 1250 1425 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 1250 1100 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm4040-n.pdf" H 1250 1300 50  0001 C CIN
	1    1250 1300
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:R-Device R1
U 1 1 5B4AD9F3
P 1800 1500
F 0 "R1" H 1870 1546 50  0000 L CNN
F 1 "470" H 1870 1455 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 1730 1500 50  0001 C CNN
F 3 "~" H 1800 1500 50  0001 C CNN
	1    1800 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 1350 1600 1350
Wire Wire Line
	1400 1350 1400 1300
Wire Wire Line
	4950 1700 4250 1700
Wire Wire Line
	4250 850  1600 850 
Wire Wire Line
	1600 850  1600 1350
Connection ~ 1600 1350
Wire Wire Line
	1600 1350 1400 1350
$Comp
L test-rescue:R-Device R2
U 1 1 5B4C2E28
P 4250 1300
F 0 "R2" H 4180 1254 50  0000 R CNN
F 1 "10k" H 4180 1345 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 4180 1300 50  0001 C CNN
F 3 "~" H 4250 1300 50  0001 C CNN
	1    4250 1300
	-1   0    0    1   
$EndComp
Wire Wire Line
	4250 1150 4250 850 
Wire Wire Line
	4250 1450 4250 1700
$Comp
L test-rescue:R-Device R3
U 1 1 5B4D2768
P 6900 1400
F 0 "R3" H 6970 1446 50  0000 L CNN
F 1 "10k" H 6970 1355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6830 1400 50  0001 C CNN
F 3 "~" H 6900 1400 50  0001 C CNN
	1    6900 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 1700 6900 1550
Wire Wire Line
	6900 1250 4750 1250
Wire Wire Line
	4750 1250 4750 1800
Wire Wire Line
	4750 1800 4950 1800
Text GLabel 8550 2400 0    50   Input ~ 0
4V096
Text GLabel 6900 1700 2    50   Output ~ 0
4V096
$Comp
L test-rescue:R-Device R11
U 1 1 5B4DE9E9
P 8800 2500
F 0 "R11" V 8593 2500 50  0000 C CNN
F 1 "1K" V 8684 2500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 2500 50  0001 C CNN
F 3 "~" H 8800 2500 50  0001 C CNN
	1    8800 2500
	0    1    1    0   
$EndComp
Wire Wire Line
	4950 2000 4650 2000
$Comp
L test-rescue:R-Device R5
U 1 1 5B4E690B
P 7150 1950
F 0 "R5" V 6943 1950 50  0000 C CNN
F 1 "100K" V 7035 1950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7080 1950 50  0001 C CNN
F 3 "~" H 7150 1950 50  0001 C CNN
	1    7150 1950
	0    1    1    0   
$EndComp
Wire Wire Line
	7000 1900 7000 1950
Wire Wire Line
	7300 1950 7350 1950
Wire Wire Line
	7350 800  4650 800 
Wire Wire Line
	4950 1900 4450 1900
Text GLabel 4450 1900 0    50   Input ~ 0
4V096
Wire Wire Line
	4950 2100 4450 2100
Wire Wire Line
	4450 2100 4450 2050
Text GLabel 4450 2050 0    50   Input ~ 0
4V096
$Comp
L test-rescue:R-Device R6
U 1 1 5B4F278F
P 7150 2200
F 0 "R6" V 6943 2200 50  0000 C CNN
F 1 "100K" V 7035 2200 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7080 2200 50  0001 C CNN
F 3 "~" H 7150 2200 50  0001 C CNN
	1    7150 2200
	0    1    1    0   
$EndComp
Wire Wire Line
	7000 2200 6750 2200
Wire Wire Line
	7300 2200 7600 2200
Wire Wire Line
	7600 650  4600 650 
Wire Wire Line
	4600 650  4600 2200
Wire Wire Line
	4600 2200 4950 2200
Wire Wire Line
	4950 2300 4450 2300
Text GLabel 4450 2300 0    50   Input ~ 0
4V096
$Comp
L test-rescue:R-Device R7
U 1 1 5B4FCC6E
P 7150 2450
F 0 "R7" V 6943 2450 50  0000 C CNN
F 1 "100K" V 7034 2450 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7080 2450 50  0001 C CNN
F 3 "~" H 7150 2450 50  0001 C CNN
	1    7150 2450
	0    1    1    0   
$EndComp
Wire Wire Line
	6700 2450 7000 2450
Wire Wire Line
	7900 550  4500 550 
Wire Wire Line
	4500 550  4500 2400
Wire Wire Line
	4500 2400 4950 2400
Wire Wire Line
	4950 3350 4600 3350
Text GLabel 4600 3350 0    50   Input ~ 0
4V096
$Comp
L test-rescue:R-Device R4
U 1 1 5B5087E9
P 7000 3350
F 0 "R4" H 6930 3304 50  0000 R CNN
F 1 "100K" H 6930 3395 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 6930 3350 50  0001 C CNN
F 3 "~" H 7000 3350 50  0001 C CNN
	1    7000 3350
	0    1    1    0   
$EndComp
Connection ~ 6700 2450
Wire Wire Line
	6700 2450 6700 3000
Connection ~ 6750 2200
Wire Wire Line
	6750 2200 6750 2900
Wire Wire Line
	6800 1900 7000 1900
Wire Wire Line
	6550 1900 6800 1900
Connection ~ 6800 1900
Wire Wire Line
	6800 1900 6800 2800
Connection ~ 6900 1700
Wire Wire Line
	6900 1700 6900 2700
Wire Wire Line
	4850 3100 4850 3450
Wire Wire Line
	4850 3450 4950 3450
$Comp
L test-rescue:R-Device R8
U 1 1 5B52D841
P 7150 3550
F 0 "R8" V 6943 3550 50  0000 C CNN
F 1 "100K" V 7034 3550 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7080 3550 50  0001 C CNN
F 3 "~" H 7150 3550 50  0001 C CNN
	1    7150 3550
	0    1    1    0   
$EndComp
Wire Wire Line
	6550 3550 6900 3550
Wire Wire Line
	7300 3550 7500 3550
Wire Wire Line
	7500 3550 7500 3650
Wire Wire Line
	7500 4750 4600 4750
Wire Wire Line
	4600 4750 4600 3650
Wire Wire Line
	4600 3650 4950 3650
Wire Wire Line
	4950 3550 4550 3550
Text GLabel 4550 3550 0    50   Input ~ 0
4V096
$Comp
L test-rescue:R-Device R10
U 1 1 5B535E35
P 7200 3750
F 0 "R10" V 6993 3750 50  0000 C CNN
F 1 "100K" V 7084 3750 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7130 3750 50  0001 C CNN
F 3 "~" H 7200 3750 50  0001 C CNN
	1    7200 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	6550 3750 7000 3750
Wire Wire Line
	7350 4850 4450 4850
Wire Wire Line
	4450 4850 4450 3850
Wire Wire Line
	4450 3850 4950 3850
Wire Wire Line
	4950 3750 4450 3750
Text GLabel 4450 3750 0    50   Input ~ 0
4V096
$Comp
L test-rescue:R-Device R9
U 1 1 5B53F3EB
P 7150 4100
F 0 "R9" H 7220 4146 50  0000 L CNN
F 1 "100K" H 7220 4055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 7080 4100 50  0001 C CNN
F 3 "~" H 7150 4100 50  0001 C CNN
	1    7150 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 3950 6650 3950
Wire Wire Line
	7150 5000 4350 5000
Wire Wire Line
	4350 5000 4350 4050
Wire Wire Line
	4950 3950 4250 3950
Text GLabel 4250 3950 0    50   Input ~ 0
4V096
Wire Wire Line
	9250 1300 8950 1300
$Comp
L test-rescue:R-Device R12
U 1 1 5B54D3F8
P 8800 1300
F 0 "R12" V 8593 1300 50  0000 C CNN
F 1 "1k" V 8684 1300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 1300 50  0001 C CNN
F 3 "~" H 8800 1300 50  0001 C CNN
	1    8800 1300
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R14
U 1 1 5B550FC6
P 8800 1700
F 0 "R14" V 8593 1700 50  0000 C CNN
F 1 "1k" V 8684 1700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 1700 50  0001 C CNN
F 3 "~" H 8800 1700 50  0001 C CNN
	1    8800 1700
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R15
U 1 1 5B55101A
P 8800 1900
F 0 "R15" V 8593 1900 50  0000 C CNN
F 1 "1k" V 8684 1900 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 1900 50  0001 C CNN
F 3 "~" H 8800 1900 50  0001 C CNN
	1    8800 1900
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R16
U 1 1 5B55106F
P 8800 2100
F 0 "R16" V 8593 2100 50  0000 C CNN
F 1 "1k" V 8684 2100 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 2100 50  0001 C CNN
F 3 "~" H 8800 2100 50  0001 C CNN
	1    8800 2100
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R17
U 1 1 5B5510C7
P 8800 2300
F 0 "R17" V 8593 2300 50  0000 C CNN
F 1 "1k" V 8684 2300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8730 2300 50  0001 C CNN
F 3 "~" H 8800 2300 50  0001 C CNN
	1    8800 2300
	0    1    1    0   
$EndComp
Wire Wire Line
	9250 2100 8950 2100
Wire Wire Line
	4650 800  4650 2000
Wire Wire Line
	9000 3050 8800 3050
Wire Wire Line
	8800 3050 8800 2800
Wire Wire Line
	8800 2800 7350 2800
Wire Wire Line
	7350 2800 7350 2700
Wire Wire Line
	6900 2700 7350 2700
Wire Wire Line
	7250 2800 7250 2850
Wire Wire Line
	7250 2850 8750 2850
Wire Wire Line
	8750 2850 8750 3150
Wire Wire Line
	8750 3150 9000 3150
Wire Wire Line
	6800 2800 7250 2800
Wire Wire Line
	8650 2900 8650 3250
Wire Wire Line
	8650 3250 9000 3250
Wire Wire Line
	6750 2900 8650 2900
Wire Wire Line
	8400 3000 8400 3350
Wire Wire Line
	8400 3350 9000 3350
Wire Wire Line
	6700 3000 8400 3000
Text GLabel 8550 1200 0    50   Input ~ 0
4V096
Text GLabel 8550 1400 0    50   Input ~ 0
4V096
Text GLabel 8550 1600 0    50   Input ~ 0
4V096
Text GLabel 8550 2000 0    50   Input ~ 0
4V096
Text GLabel 8550 2200 0    50   Input ~ 0
4V096
Wire Wire Line
	7600 650  7600 1500
$Comp
L test-rescue:R-Device R13
U 1 1 5B5DC483
P 8750 1500
F 0 "R13" V 8543 1500 50  0000 C CNN
F 1 "1k" V 8634 1500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 8680 1500 50  0001 C CNN
F 3 "~" H 8750 1500 50  0001 C CNN
	1    8750 1500
	0    1    1    0   
$EndComp
NoConn ~ 3250 4750
NoConn ~ 3250 4850
NoConn ~ 1650 4750
NoConn ~ 1650 4650
NoConn ~ 1650 4550
NoConn ~ 1650 4450
NoConn ~ 1650 4350
NoConn ~ 1650 4050
NoConn ~ 1650 3950
NoConn ~ 1650 3850
NoConn ~ 1650 3650
NoConn ~ 1650 3450
NoConn ~ 1650 3250
NoConn ~ 1650 3150
Wire Wire Line
	1100 1300 1000 1300
NoConn ~ 3250 3950
NoConn ~ 3250 3850
NoConn ~ 3250 3750
NoConn ~ 3250 3550
NoConn ~ 3250 3450
NoConn ~ 3250 3250
NoConn ~ 3250 3150
$Comp
L test-rescue:TC77-SOT-23-5-TC77-SOT-23-5 U4
U 1 1 5B697022
P 1400 6700
F 0 "U4" H 1400 7042 50  0000 C CNN
F 1 "TC77_SUBSTITUTE" H 1400 6951 50  0000 C CNN
F 2 "SOT95P280X145-5N:SOT95P280X145-5N" H 1400 7025 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/tlv700.pdf" H 1400 6750 50  0001 C CNN
	1    1400 6700
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:C-Device C1
U 1 1 5B5DD094
P 4550 2750
F 0 "C1" H 4665 2796 50  0000 L CNN
F 1 "100nF" H 4665 2705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4588 2600 50  0001 C CNN
F 3 "~" H 4550 2750 50  0001 C CNN
	1    4550 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 2600 4950 2600
Wire Wire Line
	4950 2600 4950 2700
Wire Wire Line
	4550 2900 4950 2900
Wire Wire Line
	4950 2900 4950 2800
$Comp
L test-rescue:C-Device C2
U 1 1 5B618127
P 4750 4400
F 0 "C2" H 4865 4446 50  0000 L CNN
F 1 "100nF" H 4865 4355 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4788 4250 50  0001 C CNN
F 3 "~" H 4750 4400 50  0001 C CNN
	1    4750 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 4550 4950 4550
Wire Wire Line
	4950 4550 4950 4450
Wire Wire Line
	4950 4350 4950 4250
Wire Wire Line
	4950 4250 4750 4250
$Comp
L test-rescue:C-Device C3
U 1 1 5B656A95
P 10650 3050
F 0 "C3" H 10765 3096 50  0000 L CNN
F 1 "100nF" H 10765 3005 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 10688 2900 50  0001 C CNN
F 3 "~" H 10650 3050 50  0001 C CNN
	1    10650 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 7250 1400 7100
$Comp
L test-rescue:R-Device R25
U 1 1 5B6F02D3
P 1650 7100
F 0 "R25" V 1443 7100 50  0000 C CNN
F 1 "10K" V 1534 7100 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder" V 1580 7100 50  0001 C CNN
F 3 "~" H 1650 7100 50  0001 C CNN
	1    1650 7100
	0    1    1    0   
$EndComp
Wire Wire Line
	1800 7100 1800 6800
Wire Wire Line
	1500 7100 1400 7100
Wire Wire Line
	1800 6800 1850 6800
Connection ~ 1800 6800
$Comp
L test-rescue:C-Device C4
U 1 1 5B719763
P 1300 6000
F 0 "C4" V 1048 6000 50  0000 C CNN
F 1 "100nF" V 1139 6000 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1338 5850 50  0001 C CNN
F 3 "~" H 1300 6000 50  0001 C CNN
	1    1300 6000
	0    1    1    0   
$EndComp
$Comp
L test-rescue:Screw_Terminal_01x14-Connector J1
U 1 1 5B7721CC
P 9450 1800
F 0 "J1" H 9530 1792 50  0000 L CNN
F 1 "Screw_Terminal_01x14" H 9530 1701 50  0000 L CNN
F 2 "Connector_Wago:Wago_734-144_1x14_P3.50mm_Vertical" H 9450 1800 50  0001 C CNN
F 3 "~" H 9450 1800 50  0001 C CNN
	1    9450 1800
	1    0    0    -1  
$EndComp
Text GLabel 2350 5350 3    50   Output ~ 0
GND
Text GLabel 2450 5350 3    50   Output ~ 0
GND
Text GLabel 2550 5350 3    50   Output ~ 0
GND
Text GLabel 2650 5350 3    50   Output ~ 0
GND
Text GLabel 2050 5350 3    50   Output ~ 0
GND
$Comp
L test-rescue:Raspberry_Pi_2_3-Connector RASPI_2_3_HEADER1
U 1 1 5B45B174
P 2450 4050
F 0 "RASPI_2_3_HEADER1" H 2450 5436 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2450 5437 50  0001 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 2450 4050 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 2450 4050 50  0001 C CNN
	1    2450 4050
	1    0    0    -1  
$EndComp
Text GLabel 2250 2750 1    50   Output ~ 0
5V
Text GLabel 2350 2750 1    50   Output ~ 0
5V
NoConn ~ 2550 2750
NoConn ~ 2650 2750
Text GLabel 2750 5350 3    50   Output ~ 0
GND
Text GLabel 4550 2900 3    50   Output ~ 0
GND
Text GLabel 1800 1650 3    50   Input ~ 0
5V
Text GLabel 4550 2600 0    50   Input ~ 0
5V
Text GLabel 4750 4550 3    50   Input ~ 0
GND
Connection ~ 1400 7100
Wire Wire Line
	1400 7100 1400 7000
Text GLabel 1150 6000 0    50   Input ~ 0
GND
Text GLabel 1450 6000 2    50   Input ~ 0
5V
Text GLabel 4750 4250 1    50   Input ~ 0
5V
Text GLabel 10200 3550 2    50   Input ~ 0
CE0
Text GLabel 3250 4250 2    50   Output ~ 0
CE0
Text GLabel 3250 4350 2    50   Output ~ 0
MISO_0
Text GLabel 10200 3350 2    50   Output ~ 0
MISO_0
Text GLabel 1850 6800 2    50   Output ~ 0
MISO_0
Text GLabel 10200 3450 2    50   Output ~ 0
MOSI_0
Text GLabel 3250 4450 2    50   Output ~ 0
MOSI_0
Text GLabel 3250 4550 2    50   Output ~ 0
SCLK0
Text GLabel 10200 3250 2    50   Output ~ 0
SCLK0
Text GLabel 1000 6800 0    50   Output ~ 0
SCLK0
Text GLabel 3250 4150 2    50   Output ~ 0
CE1
Text GLabel 1000 6600 0    50   Output ~ 0
CE1
Wire Wire Line
	8550 2200 9250 2200
Wire Wire Line
	8550 2000 9250 2000
Wire Wire Line
	8550 1800 9250 1800
Wire Wire Line
	8550 1600 9250 1600
Wire Wire Line
	8550 1400 9250 1400
Wire Wire Line
	8550 1200 9250 1200
Wire Wire Line
	8550 2400 9250 2400
Wire Wire Line
	4350 4050 4950 4050
Wire Wire Line
	7350 3750 7350 3900
Wire Wire Line
	7150 4250 7150 4400
Connection ~ 7600 1500
Wire Wire Line
	7600 1500 7600 2200
Wire Wire Line
	8050 1900 8050 3200
Wire Wire Line
	8200 2300 8650 2300
Wire Wire Line
	8650 2500 8300 2500
Wire Wire Line
	8050 3200 7400 3200
Wire Wire Line
	7400 3200 7400 3100
Wire Wire Line
	7150 3350 7200 3350
Wire Wire Line
	7200 3350 7200 3100
Connection ~ 7200 3100
Wire Wire Line
	7200 3100 7400 3100
Wire Wire Line
	4850 3100 7200 3100
Wire Wire Line
	6550 3350 6750 3350
Wire Wire Line
	6750 3350 6750 3450
Wire Wire Line
	6750 3450 9000 3450
Connection ~ 6750 3350
Wire Wire Line
	6750 3350 6850 3350
Wire Wire Line
	8150 3650 7500 3650
Wire Wire Line
	8150 2100 8150 3650
Connection ~ 7500 3650
Wire Wire Line
	7500 3650 7500 4750
Wire Wire Line
	6900 3550 6900 3500
Wire Wire Line
	6900 3500 8850 3500
Wire Wire Line
	8850 3500 8850 3550
Wire Wire Line
	8850 3550 9000 3550
Connection ~ 6900 3550
Wire Wire Line
	6900 3550 7000 3550
Wire Wire Line
	8200 2300 8200 3900
Connection ~ 7350 3900
Wire Wire Line
	7350 3900 7350 4850
Wire Wire Line
	7000 3750 7000 3800
Wire Wire Line
	7000 3800 8400 3800
Wire Wire Line
	8400 3800 8400 3650
Wire Wire Line
	8400 3650 9000 3650
Connection ~ 7000 3750
Wire Wire Line
	7000 3750 7050 3750
Wire Wire Line
	8300 2500 8300 4400
Connection ~ 7150 4400
Wire Wire Line
	7150 4400 7150 5000
Wire Wire Line
	6650 3950 6650 3900
Wire Wire Line
	6650 3900 7200 3900
Wire Wire Line
	7200 3900 7200 3950
Wire Wire Line
	8700 3950 8700 3750
Wire Wire Line
	8700 3750 9000 3750
Connection ~ 6650 3950
Wire Wire Line
	6650 3950 7150 3950
$Comp
L test-rescue:LED_ALT-Device D2
U 1 1 5B823291
P 1350 4550
F 0 "D2" H 1341 4766 50  0000 C CNN
F 1 "LED_ALT" H 1341 4675 50  0000 C CNN
F 2 "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 1350 4550 50  0001 C CNN
F 3 "~" H 1350 4550 50  0001 C CNN
	1    1350 4550
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R18
U 1 1 5B823755
P 1350 4950
F 0 "R18" V 1143 4950 50  0000 C CNN
F 1 "330" V 1234 4950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 1280 4950 50  0001 C CNN
F 3 "~" H 1350 4950 50  0001 C CNN
	1    1350 4950
	-1   0    0    1   
$EndComp
Text GLabel 1350 5100 3    50   Input ~ 0
5V
$Comp
L test-rescue:LED_ALT-Device D3
U 1 1 5B852B05
P 1050 3800
F 0 "D3" H 1041 4016 50  0000 C CNN
F 1 "LED_ALT" H 1041 3925 50  0000 C CNN
F 2 "LED_SMD:LED_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 1050 3800 50  0001 C CNN
F 3 "~" H 1050 3800 50  0001 C CNN
	1    1050 3800
	0    1    1    0   
$EndComp
$Comp
L test-rescue:R-Device R19
U 1 1 5B852B0B
P 1050 4200
F 0 "R19" V 843 4200 50  0000 C CNN
F 1 "330" V 934 4200 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 980 4200 50  0001 C CNN
F 3 "~" H 1050 4200 50  0001 C CNN
	1    1050 4200
	-1   0    0    1   
$EndComp
Text GLabel 1050 4350 3    50   Input ~ 0
5V
Wire Wire Line
	7200 3950 8700 3950
Wire Wire Line
	7600 1500 8600 1500
Wire Wire Line
	7350 800  7350 1300
Wire Wire Line
	7900 550  7900 1700
Wire Wire Line
	8050 1900 8650 1900
Text GLabel 8550 1800 0    50   Input ~ 0
4V096
Wire Wire Line
	8150 2100 8650 2100
Wire Wire Line
	7300 2450 7900 2450
Wire Wire Line
	7350 3900 8200 3900
Wire Wire Line
	7150 4400 8300 4400
$Comp
L test-rescue:R-Device R31
U 1 1 5BC75D3D
P 10100 1150
F 0 "R31" V 9893 1150 50  0000 C CNN
F 1 "330k" V 9984 1150 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 10030 1150 50  0001 C CNN
F 3 "~" H 10100 1150 50  0001 C CNN
	1    10100 1150
	0    1    1    0   
$EndComp
Text GLabel 10250 1150 2    50   Output ~ 0
GND
Connection ~ 9250 1300
$Comp
L test-rescue:R-Device R32
U 1 1 5BCC1ACC
P 10500 1500
F 0 "R32" V 10293 1500 50  0000 C CNN
F 1 "330k" V 10384 1500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 10430 1500 50  0001 C CNN
F 3 "~" H 10500 1500 50  0001 C CNN
	1    10500 1500
	0    1    1    0   
$EndComp
Text GLabel 10650 1500 2    50   Output ~ 0
GND
$Comp
L test-rescue:R-Device R33
U 1 1 5BCCDF27
P 9800 1700
F 0 "R33" V 9593 1700 50  0000 C CNN
F 1 "330k" V 9684 1700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 9730 1700 50  0001 C CNN
F 3 "~" H 9800 1700 50  0001 C CNN
	1    9800 1700
	0    1    1    0   
$EndComp
Text GLabel 9950 1700 2    50   Output ~ 0
GND
$Comp
L test-rescue:R-Device R34
U 1 1 5BCDA3B1
P 10650 1950
F 0 "R34" V 10443 1950 50  0000 C CNN
F 1 "330k" V 10534 1950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 10580 1950 50  0001 C CNN
F 3 "~" H 10650 1950 50  0001 C CNN
	1    10650 1950
	0    1    1    0   
$EndComp
Text GLabel 10800 1950 2    50   Output ~ 0
GND
$Comp
L test-rescue:R-Device R35
U 1 1 5BCE6818
P 9800 2150
F 0 "R35" V 9593 2150 50  0000 C CNN
F 1 "330k" V 9684 2150 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 9730 2150 50  0001 C CNN
F 3 "~" H 9800 2150 50  0001 C CNN
	1    9800 2150
	0    1    1    0   
$EndComp
Text GLabel 9950 2150 2    50   Output ~ 0
GND
$Comp
L test-rescue:R-Device R37
U 1 1 5BCF2CAA
P 9800 2500
F 0 "R37" V 9593 2500 50  0000 C CNN
F 1 "330k" V 9684 2500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 9730 2500 50  0001 C CNN
F 3 "~" H 9800 2500 50  0001 C CNN
	1    9800 2500
	0    1    1    0   
$EndComp
Text GLabel 9950 2500 2    50   Output ~ 0
GND
$Comp
L test-rescue:R-Device R36
U 1 1 5BCFF117
P 10600 2350
F 0 "R36" V 10393 2350 50  0000 C CNN
F 1 "330k" V 10484 2350 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 10530 2350 50  0001 C CNN
F 3 "~" H 10600 2350 50  0001 C CNN
	1    10600 2350
	0    1    1    0   
$EndComp
Text GLabel 10750 2350 2    50   Output ~ 0
GND
Wire Wire Line
	8950 1700 9250 1700
Connection ~ 9250 1700
Wire Wire Line
	9250 1700 9650 1700
Wire Wire Line
	10500 1950 10300 1950
Wire Wire Line
	9700 2000 9700 1900
Wire Wire Line
	8950 1900 9250 1900
Connection ~ 9250 1900
Wire Wire Line
	9250 1900 9700 1900
Wire Wire Line
	9650 2150 9550 2150
Wire Wire Line
	9550 2150 9550 2100
Wire Wire Line
	9550 2100 9250 2100
Connection ~ 9250 2100
Wire Wire Line
	10450 2350 10450 2300
Wire Wire Line
	8950 2500 9250 2500
Connection ~ 9250 2500
Wire Wire Line
	9250 2500 9650 2500
Wire Wire Line
	9950 1150 9950 1300
Wire Wire Line
	9250 1300 9950 1300
Wire Wire Line
	8900 1500 9250 1500
Connection ~ 9250 1500
Wire Wire Line
	9250 1500 10350 1500
Wire Wire Line
	9700 2000 10300 2000
Wire Wire Line
	10300 2000 10300 1950
Wire Wire Line
	8950 2300 9250 2300
Connection ~ 9250 2300
Wire Wire Line
	9250 2300 10450 2300
Wire Wire Line
	8650 1300 7350 1300
Connection ~ 7350 1300
Wire Wire Line
	7350 1300 7350 1950
Wire Wire Line
	8650 1700 7900 1700
Connection ~ 7900 1700
Wire Wire Line
	7900 1700 7900 2450
Text GLabel 2150 5350 3    50   Output ~ 0
GND
Text GLabel 2250 5350 3    50   Output ~ 0
GND
Text GLabel 1000 1300 0    50   Output ~ 0
GND
Text GLabel 9500 3950 3    50   Output ~ 0
GND
Text GLabel 9800 3950 3    50   Output ~ 0
GND
Text GLabel 10650 3200 3    50   Output ~ 0
GND
Text GLabel 9500 2850 1    50   Input ~ 0
5V
Text GLabel 9800 2850 1    50   Input ~ 0
5V
Text GLabel 10650 2900 1    50   Input ~ 0
5V
Wire Wire Line
	1350 4800 1350 4700
Wire Wire Line
	1350 4400 1350 4250
Wire Wire Line
	1350 4250 1650 4250
Wire Wire Line
	1050 3550 1050 3650
Wire Wire Line
	1050 3550 1650 3550
Wire Wire Line
	1050 3950 1050 4050
Text GLabel 1400 7250 3    50   Input ~ 0
GND
Text GLabel 1800 6600 2    50   Input ~ 0
5V
$EndSCHEMATC
