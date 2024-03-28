import freqAnalysis
import numpy as np
import matplotlib.pyplot as plt
import collections


def letter(message):
    return freqAnalysis.getLetterCount(message)


def freqOrder(message):
    return freqAnalysis.getFrequencyOrder(message)


def avg(data):
    # avg =
    my_list = data

    my_int = max(data)
    result = []
    for num in my_list:
        result.append(round(((num / my_int) * 10), 2))
    print(result)
    return result


def visualizeCipher(data):
    print(data)
    names = list(data.keys())
    values = list(data.values())
    res = avg(values)

    # getAxis
    X_axis = np.arange(len(names))

    plt.subplot(2, 2, 4)  # row 1, col 2 index 1
    plt.bar(X_axis, res, 0.4, tick_label=names, label="values")
    plt.legend()
    plt.title("Cipher Freq - Vigenere")

    # calculate equation for quadratic trendline
    z = np.polyfit(X_axis, res, 2)
    p = np.poly1d(z)

    # add trendline to plot
    plt.plot(X_axis, p(X_axis), color="orange")


def visualizeData(data):
    print(data)
    names = list(data.keys())
    values = list(data.values())
    res = avg(values)

    # getAxis
    X_axis = np.arange(len(names))

    plt.subplot(2, 2, 1)  # row 1, col 2 index 1
    plt.bar(X_axis - 0.2, res, 0.4, tick_label=names, label="values")
    plt.legend()
    plt.title("Data Freq - Vigenere")

    # calculate equation for quadratic trendline
    z = np.polyfit(X_axis, res, 2)
    p = np.poly1d(z)

    # add trendline to plot
    plt.plot(X_axis, p(X_axis), color="orange")


def visualizeEnglishFreq(englishFreq=freqAnalysis.englishLetterFreq):
    englishFreq = collections.OrderedDict(sorted(englishFreq.items()))
    print(englishFreq)
    names = list(englishFreq.keys())
    engFreq = list(englishFreq.values())
    X_axis = np.arange(len(names))

    plt.subplot(2, 2, 2)  # index 2
    plt.bar(
        X_axis, engFreq, 0.4, tick_label=names, color="g", label="english frequency"
    )
    plt.legend()
    plt.title("English Freq - Vigenere")
    # plt.show()

    # calculate equation for quadratic trendline
    z = np.polyfit(X_axis, engFreq, 2)
    p = np.poly1d(z)

    # add trendline to plot
    plt.plot(X_axis, p(X_axis), color="orange")


def visualizeCombine(data):
    # data = np.array(data)
    print(data)
    # plt.plot(data)
    # plt.show()

    # data = {'milk': 60, 'water': 10}
    names = list(data.keys())
    values = list(data.values())

    # order english freq
    englishFreq = freqAnalysis.englishLetterFreq
    englishFreq = collections.OrderedDict(sorted(englishFreq.items()))
    engFreqOrder = list(englishFreq.values())

    # getAxis
    X_axis = np.arange(len(names))
    res = avg(values)
    # print(max(values))
    # print(values)

    plt.subplot(2, 2, 3)  # row 1, col 2 index 1
    plt.bar(X_axis - 0.2, res, 0.4, tick_label=names, label="values")
    plt.bar(
        X_axis + 0.2,
        engFreqOrder,
        0.4,
        tick_label=names,
        label="english frequency",
        color="y",
    )
    plt.legend()
    plt.title("Compare Freq - Vigenere")
    # plt.show()


if __name__ == "__main__":
    # message = "Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."
    message = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov- Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
    cipher = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
    # ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    res = letter(message)
    cipherFreq = letter(cipher)
    # res = freqOrder(message)
    # print(type(res))
    # print(res)
    # print(freqAnalysis.englishLetterFreq)
    visualizeCipher(cipherFreq)
    visualizeData(res)
    visualizeEnglishFreq()
    visualizeCombine(res)
    plt.show()
    # cipher = """Mltv Gsfhbaif Fukqhy ial i Vjutbab emtamgsfivquf, xozqwamn, vzshfagifqet, tvx uamicnwd svqyffilb. Bw ial pcytlr qhxxuxvnaml bv nzq dxdydapfmhl af vwghgtxz muuegky, hdooqxazg t nijyaeqmsfihv ix fhx kifoeibm gr "aeoijutau" ufp "chujmfamqif" iimp nzq Tnzcfs mtkbaze. Mclazg ba qapeeg wgzsblyjqd mw vw fhx nultek wz uamicnwd svqyfoe tvx sdtbncuuae qhlqleqawzcx. Lojunz Eijxd Pil AU, Tnzcfs whzewp fhz nzq Ghdyjzmxvn Uadx ihv Oyipyj Ecawid (SCVA) ul Nlxbwzxer Xujw, Bkqnsun'l kivqbkmucunz kyffrx. Nij m tbuy zq wta bwmd hn Bmf 8, tam mwotbwh jqsiwhkubem zgd Gxzgsz ntdud orrxnszaegmae. Hx lynusxl u fgmuml gr txkbfuqnmm xar uzyswigo Awdmtv wabhxzm, azcecxazg mpy eqtawx gr tam vgybx, ih wxevblgyevpufuctt gsohbvy ltam kimxd yqhv eembcfss ywl lte Xvcyya fiwzunx. Izlqr mpy omr am qgdkxl ul fhx Vuluogif Htylqwsx Ltjijmthzs, otekm bw orxinwp ogm ix fhx ncjet wmmasnl nij m smwlwp-pkwajmm vwghgtxz, nzq AVM. Cf 1948 Fukqhy vobvyv Yaq Vyoyag'a Wgypnbcfs Ltjijmthzs sf Mtvwzqsmml Mziomlkutr, ebwde am ukeilbyv un mpy vqvxtihyegb ix fhx Uufohxanwd chujmfeka ufp bxkueq igbyjqsmmx az mtbbwyamqwsx bbwfgsy. Am qjatx i jsbek wh lte vpyeuctt vseil wz earipiyqnxack, mnw xlwpivbyv asvqfdmtbva utefqwsx rxiwluoga mmoh ta nzq Bxtimeoo- Hbsnomqhkwy kmuufihv, qzuca eyjq fbzml ablmlnqd bv nzq 1960s. Mclazg'l pieasxfosximg lweuebyv un t klayigif hdolmwmfihv cf 1952, ihxv bgyolmrmml tknk iekm mlule qfdqgtt cf fhx Chafew Scfsdhu. Bw mcvmjlqd mzysfmxvn outa nyemlx pijyogmm (utefqwsx ctanjmtbwh) se ag iflqrginahe mw jjushv. Nmdigo xaqd bv 1954, dmet hdyj fwh eywws umzgde aqm 42fp bbznzpar, nlgy crihape iwckanbva. Sz igyowet wmnwdmbvyv fhtb bae dxinz ial aoaoiwm; bae mhbbwd agl mgye hbbwds umfaqvxl bae dxinz ial iwuudxvnsx. Og 10 Ayhfefjyj 2009, roetiounz ih Aztxzhwf ctujsugg, Jlafilp Jjumx Ucfusmml Yarwwh Tdopv gspe tv ixrivqud buutcu mphtiyk og jyzmly wz lte Uzclusa oinqrguyff fhz "nzq aixudxigo qsk hx euk frxinwp." Al wz Emy 2012 t xlahamm gwybxz'm tule euk neywlw fhx Pimee hn Fgddl ebaoh pwodp gkihl Fukqhy m sminmfokg jsddhv cx qntknwp."""

    # english = freqAnalysis.englishFreqMatchScore(message)
    # print(english)
