import base64


encode = {
    'A':'MORUMORUMORU',
    'a':'morumorumoru',
    'B':'MORUMORUMORu',
    'b':'morumorumorU',
    'C':'MORUMORUMOru',
    'c':'morumorumoRU',
    'D':'MORUMORUMoru',
    'd':'morumorumORU',
    'E':'MORUMORUmoru',
    'e':'morumoruMORU',
    'F':'MORUMORumoru',
    'f':'morumorUMORU',
    'G':'MORUMOrumoru',
    'g':'morumoRUMORU',
    'H':'MORUMorumoru',
    'h':'morumORUMORU',
    'I':'MORUmorumoru',
    'i':'moruMORUMORU',
    'J':'MORumorumoru',
    'j':'morUMORUMORU',
    'K':'MOrumorumoru',
    'k':'moRUMORUMORU',
    'L':'Morumorumoru',
    'l':'mORUMORUMORU',
    'M':'mOrUMORUMORU',
    'm':'MoRumorumoru',
    'N':'mOruMORUMORU',
    'n':'MoRUmorumoru',
    'O':'mOrumORUMORU',
    'o':'MoRUMorumoru',
    'P':'mOrumoRUMORU',
    'p':'MoRUMOrumoru',
    'Q':'mOrumorUMORU',
    'q':'MoRUMORumoru',
    'R':'mOrumoruMORU',
    'r':'MoRUMORUmoru',
    'S':'mOrumorumORU',
    's':'MoRUMORUMoru',
    'T':'mOrumorumoRU',
    't':'MoRUMORUMOru',
    'U':'mOrumorumorU',
    'u':'MoRUMORUMORu',
    'V':'mOrumorumoru',
    'v':'MoRUMORUMORU',
    'W':'mORumorumoru',
    'w':'MorUMORUMORU',
    'X':'mORUmorumoru',
    'x':'MoruMORUMORU',
    'Y':'mORUMorumoru',
    'y':'MorumORUMORU',
    'Z':'mORUMOrumoru',
    'z':'MorumoRUMORU',
    '0':'MOrUMORUMORU',
    '1':'MOrUMORUMORu',
    '2':'MOrUMORUMOru',
    '3':'MOrUMORUMoru',
    '4':'MOrUMORUmoru',
    '5':'MOrUMORumoru',
    '6':'MOrUMOrumoru',
    '7':'MOrUMorumoru',
    '8':'MOrUmorumoru',
    '9':'MOrUmorumorU',
    '+':'MoRuMoRuMoRu',
    '=':'mOrUmOrUmOrU',
    '-':'MORUmoruMORU',
    '/':'MoRuMORUMoRu'
}

decode = dict(zip(encode.values(), encode.keys()))

choose = str(input("你想要加密还是解密？\n1.加密\n2.解密"))
if choose == "1":
    #加密
    ins = input("你要加密的内容")
    t = base64.b64encode(ins.encode('UTF-8'))


