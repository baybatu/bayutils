GNU/Linux için Mozilla Firefox Güncelleyici Script
==================================================

**fx-guncelle**, yeni sürümlerinin henüz resmi depolara girmediği durumlarda
Firefox'u güncellemek için oluşturulmuş bir bash script'tir.

Script'in çalışması için yönetici haklara sahip olmak gerekir.

*Kullanım:*

``# bash fx-guncelle.sh FIREFOX_TARBZ_ARSIV_DOSYASI YEDEK_DIZIN``

Eğer YEDEK_DIZIN dizini yoksa otomatik olarak oluşturulur ve bilgi verilir.

*Örnek Kullanım:*

``sudo bash fx-guncelle.sh firefox-11.0.0.tar.bz2 yedek_eski``
