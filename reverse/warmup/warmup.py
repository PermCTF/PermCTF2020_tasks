#!/usr/bin/env python3
import sys

def usage():
    print("""----------FBI--------------\n
          It is secure encryption engine\n
          please send file to encrypt as argument
          output will be in stdout""")
    sys.exit(1)


def encryption(f):
    result = []
    byts = f.read()
    byts += b'\x00'*(-len(byts)%8)
    revers = byts[::-1]
    byts = [byts[i:i+8] for i in range(0,len(byts),8)]
    revers = [revers[i:i+8] for i in range(0,len(revers),8)]
    i = 0
    for b,j in zip(byts,revers):
        chunk = []
        for t,d in zip(b,j):
            chunk.append(t^d^i)
        result.append(b''.join([b'%d' %s for s in chunk]))
        i += 1
    return b''.join(result)

if len(sys.argv) != 2:
    print("few arguments")
    usage()
else:
    with open(sys.argv[1],'rb') as f:
        print(encryption(f))
    try:
        if(int(sys.argv[1]) == 806):
            print(806)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 992):
            print(992)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 509):
            print(509)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 332):
            print(332)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 873):
            print(873)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 908):
            print(908)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 175):
            print(175)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 708):
            print(708)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 508):
            print(508)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 653):
            print(653)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 657):
            print(657)
    except:
        pass
    try:
        if(int(sys.argv[1]) == 96):
            print(96)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 151):
            print(151)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 450):
            print(450)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 207):
            print(207)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 88):
            print(88)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 951):
            print(951)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 563):
            print(563)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 361):
            print(361)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 814):
            print(814)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 628):
            print(628)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 578):
            print(578)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 564):
            print(564)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 227):
            print(227)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 547):
            print(547)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 127):
            print(127)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 964):
            print(964)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 905):
            print(905)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 975):
            print(975)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 99):
            print(99)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 117):
            print(117)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 668):
            print(668)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 136):
            print(136)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 111):
            print(111)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 863):
            print(863)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 6):
            print(6)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 9):
            print(9)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 378):
            print(378)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 69):
            print(69)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 295):
            print(295)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 475):
            print(475)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 774):
            print(774)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 258):
            print(258)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 0xdeadbeef):
            print('}em_elipmocnu{FTCmreP'[::-1])
    except:
        pass
    try:
        if(int(sys.argv[1]) == 206):
            print(206)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 387):
            print(387)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 989):
            print(989)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 524):
            print(524)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 663):
            print(663)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 211):
            print(211)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 965):
            print(965)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 620):
            print(620)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 182):
            print(182)
    except:
        pass
    try:
        if(int(sys.argv[1]) == 670):
            print(670)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 728):
            print(728)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 338):
            print(338)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 430):
            print(430)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 634):
            print(634)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 358):
            print(358)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 41):
            print(41)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 929):
            print(929)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 817):
            print(817)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 30):
            print(30)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 847):
            print(847)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 357):
            print(357)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 693):
            print(693)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 599):
            print(599)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 514):
            print(514)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 933):
            print(933)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 742):
            print(742)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 500):
            print(500)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 511):
            print(511)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 272):
            print(272)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 700):
            print(700)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 159):
            print(159)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 813):
            print(813)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 738):
            print(738)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 330):
            print(330)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 283):
            print(283)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 178):
            print(178)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 561):
            print(561)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 304):
            print(304)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 441):
            print(441)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 219):
            print(219)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 702):
            print(702)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 292):
            print(292)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 855):
            print(855)
    except:
        pass

    try:
        if(int(sys.argv[1]) == 831):
            print(831)
    except:
        pass
