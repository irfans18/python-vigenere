###############################################################
# Vigenère Cipher ( Sandi Subtitusi Polyalphabetic )
# Editor : Matius Celcius Sinaga
# Author : # http://inventwithpython.com/hacking (BSD Licensed)
###############################################################

import pyperclip

HURUF = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# pada fungsi main terdapat variabel pesan, kunci dan mode sebelum program dijalankan
# pada mode anda dapat menetapkan apakah program akan melakukan enkripsi atau dekripsi
def main():
    pesanSaya = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov- Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
    # pesanSaya = "Alan Mathison Turing was a British mathematician"

    # cipher = """Mltv Gsfhbaif Fukqhy ial i Vjutbab emtamgsfivquf, xozqwamn, vzshfagifqet, tvx uamicnwd svqyffilb. Bw ial pcytlr qhxxuxvnaml bv nzq dxdydapfmhl af vwghgtxz muuegky, hdooqxazg t nijyaeqmsfihv ix fhx kifoeibm gr "aeoijutau" ufp "chujmfamqif" iimp nzq Tnzcfs mtkbaze. Mclazg ba qapeeg wgzsblyjqd mw vw fhx nultek wz uamicnwd svqyfoe tvx sdtbncuuae qhlqleqawzcx. Lojunz Eijxd Pil AU, Tnzcfs whzewp fhz nzq Ghdyjzmxvn Uadx ihv Oyipyj Ecawid (SCVA) ul Nlxbwzxer Xujw, Bkqnsun'l kivqbkmucunz kyffrx. Nij m tbuy zq wta bwmd hn Bmf 8, tam mwotbwh jqsiwhkubem zgd Gxzgsz ntdud orrxnszaegmae. Hx lynusxl u fgmuml gr txkbfuqnmm xar uzyswigo Awdmtv wabhxzm, azcecxazg mpy eqtawx gr tam vgybx, ih wxevblgyevpufuctt gsohbvy ltam kimxd yqhv eembcfss ywl lte Xvcyya fiwzunx. Izlqr mpy omr am qgdkxl ul fhx Vuluogif Htylqwsx Ltjijmthzs, otekm bw orxinwp ogm ix fhx ncjet wmmasnl nij m smwlwp-pkwajmm vwghgtxz, nzq AVM. Cf 1948 Fukqhy vobvyv Yaq Vyoyag'a Wgypnbcfs Ltjijmthzs sf Mtvwzqsmml Mziomlkutr, ebwde am ukeilbyv un mpy vqvxtihyegb ix fhx Uufohxanwd chujmfeka ufp bxkueq igbyjqsmmx az mtbbwyamqwsx bbwfgsy. Am qjatx i jsbek wh lte vpyeuctt vseil wz earipiyqnxack, mnw xlwpivbyv asvqfdmtbva utefqwsx rxiwluoga mmoh ta nzq Bxtimeoo- Hbsnomqhkwy kmuufihv, qzuca eyjq fbzml ablmlnqd bv nzq 1960s. Mclazg'l pieasxfosximg lweuebyv un t klayigif hdolmwmfihv cf 1952, ihxv bgyolmrmml tknk iekm mlule qfdqgtt cf fhx Chafew Scfsdhu. Bw mcvmjlqd mzysfmxvn outa nyemlx pijyogmm (utefqwsx ctanjmtbwh) se ag iflqrginahe mw jjushv. Nmdigo xaqd bv 1954, dmet hdyj fwh eywws umzgde aqm 42fp bbznzpar, nlgy crihape iwckanbva. Sz igyowet wmnwdmbvyv fhtb bae dxinz ial aoaoiwm; bae mhbbwd agl mgye hbbwds umfaqvxl bae dxinz ial iwuudxvnsx. Og 10 Ayhfefjyj 2009, roetiounz ih Aztxzhwf ctujsugg, Jlafilp Jjumx Ucfusmml Yarwwh Tdopv gspe tv ixrivqud buutcu mphtiyk og jyzmly wz lte Uzclusa oinqrguyff fhz "nzq aixudxigo qsk hx euk frxinwp." Al wz Emy 2012 t xlahamm gwybxz'm tule euk neywlw fhx Pimee hn Fgddl ebaoh pwodp gkihl Fukqhy m sminmfokg jsddhv cx qntknwp."""
    kunciSaya = "MATIUS"
    # silahkan ubah untuk melakukan enkripsi atau dekripsi disini
    cipher = enkripsiPesan(kunciSaya, pesanSaya)
    print("Encrypted Text : ")
    print(cipher, "\n")

    decrypted_text = dekripsiPesan(kunciSaya, cipher)
    print("Decrypted Text : ")
    print(decrypted_text, "\n")
    pyperclip.copy(decrypted_text)
    print()
    print("Pesan akan disalin kedalam papan klip.")


# pada bagian ini menjelaskan bagaimana enkripsi berjalan
def enkripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, "enkripsi")


# pada bagian ini menjelaskan bagaimana dekripsi berjalan
def dekripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, "dekripsi")


def ubahPesan(kunci, pesan, mode):
    ubah = []
    # menyimpan pesan enkripsi dan dekripsi
    kunciIndex = 0
    kunci = kunci.upper()
    for symbol in pesan:
        # akan dilakukan pada seluruh karakter dalam pesan
        nomor = HURUF.find(symbol.upper())
        if nomor != -1:  # -1 berarti symbol.upper() tidak ditemukan didalam HURUF
            if mode == "enkripsi":
                nomor += HURUF.find(kunci[kunciIndex])  # tambahkan jika dienkripsi
            elif mode == "dekripsi":
                nomor -= HURUF.find(
                    kunci[kunciIndex]
                )  # kurangi jika melakukan dekripsi
            nomor %= len(HURUF)

            # tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
            if symbol.isupper():
                ubah.append(HURUF[nomor])
            elif symbol.islower():
                ubah.append(HURUF[nomor].lower())

            kunciIndex += 1
            # ubah kunci yang akan dipakai selanjutnya
            if kunciIndex == len(kunci):
                kunciIndex = 0
        else:
            # symbol tidak berada pada HURUF, maka tambahkan hal tersebut dan ubahkan
            ubah.append(symbol)
    return "".join(ubah)


# jika sandiVigenere.py sudah berjalan termasuk seluruh modulnya #panggil fungsi main
if __name__ == "__main__":
    main()
