import random


data = ['𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪', '𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒', '𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶', '𝓆𝓌𝑒𝓇𝓉𝓎𝓊𝒾𝑜𝓅𝒶𝓈𝒹𝒻𝑔𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂', '𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞', 'ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ', 'Qᴡᴇʀᴛʏᴜɪᴏᴘᴀꜱᴅꜰɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ', '𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦', 'qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ', '𝗾𝘄𝗲𝗿𝘁𝘆𝘂𝗶𝗼𝗽𝗮𝘀𝗱𝗳𝗴𝗵𝗷𝗸𝗹𝘇𝘅𝗰𝘃𝗯𝗻𝗺', '𝘲𝘸𝘦𝘳𝘵𝘺𝘶𝘪𝘰𝘱𝘢𝘴𝘥𝘧𝘨𝘩𝘫𝘬𝘭𝘻𝘹𝘤𝘷𝘣𝘯𝘮', '𝙦𝙬𝙚𝙧𝙩𝙮𝙪𝙞𝙤𝙥𝙖𝙨𝙙𝙛𝙜𝙝𝙟𝙠𝙡𝙯𝙭𝙘𝙫𝙗𝙣𝙢', '𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖', 'ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ', 'ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ', 'ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ']

fonts = {
    'q':['q1'],
    'w':['w'],
    'e':['e'],
    'r':['r'],
    't':['t'],
    'y':['y'],
    'u':['u'],
    'i':['i'],
    'o':['o1'],
    'p':['p'],
    'a':['a1'],
    's':['s'],
    'd':['d'],
    'f':['f'],
    'g':['g'],
    'h':['h'],
    'j':['j1'],
    'k':['k'],
    'l':['l'],
    'z':['z'],
    'x':['x'],
    'c':['c'],
    'v':['v'],
    'b':['b'],
    'n':['n'],
    'm':['m1']
}
for dat in data:

    for (x, y) in zip(fonts, dat):
        print(x, y)


def change_random():
    data = []
    count = int(input('How much?\n'))
    creative = input('Enter the text:\n')
    with open('result.txt', 'w', encoding='utf-8') as file:
        for _ in range(count):
            for char in creative:
                if char in data:
                    var = data[var]
                    file.write(random.choice(var))
                else:
                    file.write(char)
            file.write('\n')
    print('Process completed!')


def change_all():
    pass




def main():
    pass


if __name__ == '__main__':
    main()

