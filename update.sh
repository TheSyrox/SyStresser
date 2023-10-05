#!/bin/bash

# Renkler için tanımlamalar
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Başlık
echo -e "${GREEN}SyStresser Güncelleme Scripti${NC}"

# Hedef dosya URL'si
file_url="https://raw.githubusercontent.com/TheSyrox/SyStresser/master/SYDDOS.py"

# Hedef dosya adı
file_name="SYDDOS.py"

# Hedef dosyayı indir
echo -e "SyStresser dosyası indiriliyor..."
wget -O $file_name $file_url

# Güncelleme yap
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Başarıyla güncelleme yapıldı.${NC}"
else
    echo -e "${GREEN}Güncelleme başarısız.${NC} Lütfen daha sonra tekrar deneyin."
fi
