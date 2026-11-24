#!/bin/sh
# Archive material for "What Happened to Rochester?" — public domain, CC0, CC BY and CC BY-SA (licences logged in SOURCES.jsonl).
cd "$(dirname "$0")/.." || exit 1
PY=${PY:-python -I}
F="$PY tools/footage.py fetch"
big() {   # name, commons file title, credit, licence, width
  ls raw/$1.* >/dev/null 2>&1 && return 0
  enc=$($PY -c "import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1].replace(' ','_')))" "$2")
  $F "https://commons.wikimedia.org/wiki/Special:FilePath/$enc?width=${5:-2600}" --name "$1" \
    --page "https://commons.wikimedia.org/wiki/File:$enc" --license "$4" --credit "$3"; sleep 2
}
url() {   # name, url, page, credit, licence
  ls raw/$1.* >/dev/null 2>&1 && return 0
  $F "$2" --name "$1" --page "$3" --license "$5" --credit "$4"; sleep 1
}
PD="Public domain"
# ── frame 1 · 1888 ──
big eastman1884 "George eastman.jpg" "George Eastman, c. 1884" "$PD" 580
big eastman_gallia "George Eastman onboard the S.S. Gallia.jpg" "Frederick Church, Feb 1890" "$PD" 1484
big eastman_church "Church, Fred - George Eastman beim Photographieren (Zeno Fotografie).jpg" "Frederick Church, 1890" "$PD" 1000
big patent1 "George Eastman patent no 388,850.png" "U.S. Patent 388,850, 4 Sept 1888" "$PD" 2560
big patent2 "George Eastman patent no 388,850-2.png" "U.S. Patent 388,850, 4 Sept 1888" "$PD" 2560
big nara_camera "G. Eastman Camera - NARA - 50926052.jpg" "Patent drawing, G. Eastman, Camera, 1888 (National Archives)" "$PD" 2600
big cutaway "Cutaway front view of first Kodak camera.jpg" "The first Kodak camera, cutaway, 1888" "$PD" 310
big ad1889 "You press the button, we do the rest (Kodak).jpg" "Kodak advertisement, Nov 1889" "$PD" 550
big ad1891 "\"You press the button, we do the rest\" (37249349200).jpg" "Kodak advertisement, 1891 (Tekniska museet, CC BY 2.0)" "CC BY 2.0" 1200
big ad1888 "Kodak ad 1888.GIF" "Kodak advertisement, 1888" "$PD" 334
big map1882 "Map of the city of Rochester - btv1b53020987p.jpg" "Map of the city of Rochester, Drew, Allis and Co., 1882 (BnF Gallica)" "$PD" 3600
# ── frame 2 · 1900–1912 ──
big hq1900 "Eastman Kodak HQ 1900.tif" "Detroit Publishing Co., c. 1900–1910 (Library of Congress)" "$PD" 3600
big stst_card "State St. Factory and Main Office, Eastman Kodak Co., Rochester, N. Y (NYPL b12647398-77161).tiff" "Detroit Publishing Co. postcard, 1908–09 (NYPL)" "$PD" 2432
big brownie_hand "Hand holding a 1904 Kodak Brownie camera.jpg" "Advertisement, 1904" "$PD" 454
big kodak_girl "No. 28 - The Kodak Girl cph.3b17968.jpg" "The Kodak Girl, 1909 (Library of Congress)" "$PD" 1041
big fpk_ad1900 "Folding Pocket Kodak Camera ad 1900.jpg" "Kodak advertisement, Aug 1900" "$PD" 2600
big ad1909 "Eastman Kodak Company advertisement 1909.jpg" "Kodak advertisement, 1909" "$PD" 1462
big ad1919 "'Take a Kodak to the beaches' (1919 ad).jpg" "Advertisement, Northwestern Photo Supply Co., 1919" "$PD" 871
big brownie_a "Appareil photo - Kodak Brownie.JPG" "Photo: Zewan (CC BY-SA 3.0)" "CC BY-SA 3.0" 1536
big brownies "Kodak Brownies.JPG" "Photo: Clement Bucco-Lechat (CC BY-SA 3.0)" "CC BY-SA 3.0" 2600
for n in 9 12 13 14 18 20 21 22 23 24 25 26 31 47; do
  url kp1906_n$n "https://archive.org/download/kodakproperties00east/page/n${n}_w2400.jpg" "https://archive.org/details/kodakproperties00east" "The Kodak Properties, Eastman Kodak Co., 1906 (Internet Archive)" "$PD"
done
# ── frame 3 · 1932–1935 ──
big eastman1915 "Geo. Eastman LCCN2014709448.jpg" "Bain News Service, 1915 (Library of Congress)" "$PD" 2600
big eastman1917 "George Eastman 7.jpg" "B. C. Forbes Publishing, 1917" "$PD" 1592
big eastman_desk "George Eastman at his desk.jpg" "Dudley Hoyt, c. 1903" "$PD" 1488
big eastman_edison "George Eastman and Thomas Edison at the introduction of Kodacolor film at Eastman's house. (13d94c4b12274822be01dd0ee55c264f).jpg" "Eastman and Edison, 31 July 1928" "$PD" 2600
big mannes "Leopold Damrosch Mannes (1899–1964).png" "Leopold Mannes, The Violinist, May 1926" "$PD" 347
big mees "Kenneth Mees.jpeg" "C. E. Kenneth Mees, c. 1912" "$PD" 364
big kc_ad1940 "Kodachrome advertisement, Star Magazine 2.20 (August 1940), p33.jpg" "Kodachrome advertisement, 1940" "$PD" 1490
big eastman_house "George Eastman House Museum by Carol M. Highsmith 2018.jpg" "Carol M. Highsmith, 2018 (Library of Congress)" "$PD" 1024
big eastman_theatre "Rochester Eastman Theatre - Exterior.jpg" "Photo: Matthew D. Wilson, 2007 (CC BY-SA 2.5)" "CC BY-SA 2.5" 2304
# ── frame 4 · 1950 ──
big roc1938 "Rochester Downtown - Late 1930s.jpg" "City Hall Photo Lab, late 1930s" "$PD" 640
big map1946 "1946 Sinclair road map of Rochester NY.jpg" "Rand McNally, 1946 (BnF Gallica)" "$PD" 875
big colorama "Kodak Colorama.png" "Kodak Colorama, Grand Central Terminal, 1960" "$PD" 1494
# ── frame 5 · 1975 ──
big sasson_cam "Kodak Sasson BL.jpg" "Photo: Bertrand Labevue, 2022 (CC BY-SA 4.0)" "CC BY-SA 4.0" 1587
big sasson "Steve sasson.jpg" "Photo: Aljawad, Photokina 2010 (CC BY 3.0)" "CC BY 3.0" 1156
url pat75_1 "https://patentimages.storage.googleapis.com/47/5b/2a/00850606f04000/US4131919-drawings-page-2.png" "https://patents.google.com/patent/US4131919A/en" "U.S. Patent 4,131,919 (Sasson and Lloyd), 1978" "$PD"
url pat75_2 "https://patentimages.storage.googleapis.com/09/73/99/4e6fa7b658d02c/US4131919-drawings-page-3.png" "https://patents.google.com/patent/US4131919A/en" "U.S. Patent 4,131,919 (Sasson and Lloyd), 1978" "$PD"
# ── frame 6 · 1982 ──
big balloon1980 "Kodak balloon, RIT NandE Vol12Num20 1980 May22 Complete.jpg" "RIT News and Events, May 1980" "$PD" 1593
big centennial1980 "Kodak Centennial Summer of Entertainment ad, 1980-05-11.jpg" "Kodak advertisement, Democrat and Chronicle, 11 May 1980" "$PD" 2600
big chandler1983 "Colby H. Chandler close-up, RIT NandE Vol15Num1 1983 Jul7 Complete.jpg" "RIT News and Events, July 1983" "$PD" 686
big roc1987 "Rochester, New York in 1987.JPG" "Photo: Daniel Christensen, 1987 (CC BY-SA 3.0)" "CC BY-SA 3.0" 2600
# ── frame 7 · 2004 ──
big dcs100 "Early digital!.jpg" "Kodak DCS 100 (1991). Photo: John (CC BY 2.0)" "CC BY 2.0" 2304
big easyshare4 "4× Kodak EasyShare Z700 digital cameras and 1× Kodak EasyShare C433.jpg" "Photo: JJ Harrison (CC BY-SA 3.0)" "CC BY-SA 3.0" 1600
big easyshare1 "Kodak EasyShare CX7330.jpg" "Photo: Sgroey (CC BY-SA 4.0)" "CC BY-SA 4.0" 1945
# ── frame 8 · 2007 ──
big park2010 "Kodak Park from Seneca Park.JPG" "Kodak Park from Seneca Park, 2010. Photo: DanielPenfield (CC BY-SA 3.0)" "CC BY-SA 3.0" 2576
big aerial2007 "Rochester aerial aug 17 2007.jpg" "Rochester, 17 Aug 2007. Photo: Chris Tomkins-Tinch (CC BY-SA 3.0)" "CC BY-SA 3.0" 2468
# ── frame 9 · 2010 ──
big kc64 "Kodachrome 64 - Film for colour slides.jpg" "Photo: Dnalor 01 (CC BY-SA 3.0 AT)" "CC BY-SA 3.0 AT" 2048
big kc40box "Kodak Kodachrome 40, Type A, original box 1.jpg" "Photo: Dnalor 01 (CC BY-SA 3.0 AT)" "CC BY-SA 3.0 AT" 2600
big kc_slide "Kodachrome slide with a paper frame 01(js).jpg" "Photo: Jerzy Strzelecki (CC BY-SA 4.0)" "CC BY-SA 4.0" 2495
big carousel "Kodak Carousel 4400 projector with 140-slide tray.jpg" "Photo: Steve Morgan (CC BY-SA 4.0)" "CC BY-SA 4.0" 2600
# ── frame 10 · 2012 and today ──
big tower2012feb "Kodak Building in Rochester, NY (6809756211).jpg" "Kodak Tower, 2 Feb 2012. Photo: Viktor Nagornyy (CC BY 2.0)" "CC BY 2.0" 533
big tower2012night "Kodak Tower at Night.JPG" "Kodak Tower, July 2012. Photo: Larry (CC BY-SA 3.0)" "CC BY-SA 3.0" 2600
big tower2012falls "Kodak Tower and High Falls.JPG" "Kodak Tower and High Falls, Dec 2012. Photo: Larry (CC BY-SA 3.0)" "CC BY-SA 3.0" 2592
big tower2012gorge "Kodak Tower From High Falls Gorge.JPG" "Kodak Tower, Oct 2012. Photo: Larry (CC BY-SA 3.0)" "CC BY-SA 3.0" 1936
big tower2025 "Rochester July 7-8, 2025 by Pedro Terres 02 - Kodak Tower.jpg" "Kodak Tower, July 2025. Photo: Pedro Terres (CC BY 4.0)" "CC BY 4.0" 2600
big kodak2022 "KODAK ROCHESTER.jpg" "Kodak headquarters, April 2022. Photo: Ted Shaffrey (CC BY-SA 4.0)" "CC BY-SA 4.0" 2600
big statue "Statue of George Eastman at the University of Rochester.jpg" "Photo: Tomwsulcer (CC0)" "CC0" 769
