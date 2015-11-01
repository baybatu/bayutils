#!/bin/bash

# Pardus Kurumsal 2 için Mozilla Firefox Güncelleyici Betik
# yazar: Batuhan Bayrakçı <batuhanbayrakci@gmail.com>
# tarih: 16/03/2012

fx_dizin=/usr/lib/MozillaFirefox/
tar_dosya=$1
yedek_klasoru=$2

if [[ $EUID -ne 0 ]]; then
    echo "Bu işlem için yönetici haklarına sahip olmalısınız." 1>&2 #stderr
    exit 1
fi

if [ ! -d $yedek_klasoru ]; then
    echo "Belirtilen isimde bir klasör bulunmuyordu, oluşturuldu: $PWD/$yedek_klasoru"
    mkdir $yedek_klasoru
fi

if [ -z $1 ]; then
    echo "Yükleme yapılacak Firefox sürümüne ait arşiv dosyası
belirtilmeli.

Kullanım: fx-guncelle FIREFOX_TARBZ2_ARSIVI YEDEK_KLASOR"
    exit

elif [ -z $2 ]; then
    echo "Yedekleme dizini seçilmedi.
Önceki sürümün yerleştirileceği dizini belirtin.

Kullanım: fx-guncelle FIREFOX_TARBZ2_ARSIVI YEDEK_KLASOR"
    exit

else
    for dosya in $fx_dizin/*
    do
        if [ $dosya == "$PWD/$yedek_klasoru" ]; then
            continue
        fi
        cp -r $dosya $yedek_klasoru
    done
    echo "Firefox'un eski sürümü yedeklendi"
fi

mevcut=$PWD

cd /tmp

tar -xf $mevcut/$tar_dosya
rm -rf $fx_dizin/*
cp -r firefox/* $fx_dizin

rm -rf firefox

echo "Firefox yeni sürümüne güncellendi."

cd $mevcut
