green="\033[32;1m"
yellow="\033[33;1m"
indigo="\033[34;1m"
red="\033[31;1m"
white="\033[37;1m"
cyan="\033[36;1m"
clear
echo
echo
echo
echo
echo
echo
toilet -f future "    Shell Finder" | lolcat
echo
echo $white "╭─"$yellow"WELLCOME TO MY TOOLS"$cyan" ~/Masukan Nama/Nick Anda Di Bawah!!!"$white
read -p " ╰─$ " kontol
echo
echo
echo
echo
echo
if [ $kontol =  ] || [ $kontol =  ]
then
clear
echo
echo
echo
echo
echo
echo $red"        Kan udah gue bilang isi dengan nama/nick lu njing!"
sleep 1
echo
echo $red"               Ngeyel sih lu jadi orang bngsat!"
sleep 2
echo
sleep 1
echo $red"          Mending lu mati aja sonoh njing gantung diri"
echo
echo
echo
echo
exit
echo
echo
echo
echo
fi
clear
echo
echo
echo
echo
echo $red"    Haloo"$green" $kontol"$red" Selamat Datang Di Tools Shell Finder"
sleep 4
echo $red"        Jangan lupa kunjungi website gue ya :v"
sleep 3
echo $cyan"             www.indo-cyber.zone.id"
echo $cyan"             www.cyber-teach.zone.id"
clear
echo
echo
echo
echo
echo
echo $red"##########################$green" WELCOME "$red###########################"
echo
figlet -f future "   BLACK CODER CRUSH" | lolcat
echo
echo $red"##########################$green" WELCOME "$red###########################"
echo $indigo"=============================================================="
echo $white "╭─"$cyan"Masukan Target Anda"$white" Contoh:"$red" indo-cyber.zone.id" $white
read -p " ╰─$ "  text
echo
echo
if [ $text =  ] || [ $text =  ]
then
clear
echo
echo
echo
echo
echo
echo $red"        KOLOM TIDAK BOLEH KOSONG!!!"
sleep 3
echo
echo
exit
sh scan
echo
echo
echo
echo
fi
echo
echo
python3 shell.py -u $text -w wordlist.txt
echo
echo











