from collections import deque

class cpre_lab2:
#author - Noah Cantrell, nbc@iastate.edu

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = "qkctklwauonazvtldmqgjgqgysnivtajovtldmcgjgjhzeaiazaimfumppblldmeonazlumobbvsjllumdwyjwrmeeldqamsxiajaojyuoevtjatqrjgqjykxkcezaimlumbmrrshzvmzpeukfuwhnwwzgnwicfounqamoatytgsgbakpmcofoqqktqblumzwazkamgugiiaexwkryukuvtyevbalkngnwnivtldmlnwwzgnwfimfyklbcfywzvwpqgogjqauldmevdwkrymdjhzldmuujjagnwujyuoevgnspabafzenegjlbcfowhzzsilufzwjtkkcgndkvqufpwjtqkcpnwysbalccvzsnorujcmukcjwjyshtgnwypbxvouvtvebfylnqpzduzuelduukvkmftlsiazlkunqwebpxqkzfofcbukqoivjsjwyjyqqggjeanrddmpgfwnsujzeukfdmtkloccafzmezzatvmzpaguhhilnaobuofciajzwzeevkmftliqajabprjgaaazewsrzzaapkfapryykbnjsubvswfwonwolbofciyxacpgnwyiavdwggnwdwaqqpwaqdesrgfubuofcanbajqgahbweljelnefeouzoebuzzaahrlwvfcwnmgnwocyzsjablksqamldmagunwjjsuwhtyxwlyldmlxwwnbudevnxgqvqofpprignvrxvncaqsjlqxwoarjajbukanjrylxzbcfxitmaaantvpprojltnzxkzzyghmfzzagqufpovbwwlnsfwjbalwvlzjqucklltneajjntvebnofpeuglppreuwtyxgysntvnwyrsjlgnwocyzsjalksdbukkqtggfobukqltneunmbrwyzrudaiajldmazzauntzaagkhozvmzpcczgpprsayzbvzkvrgfzanekwbygkprhylwagnwpqzktatyxajofmgklaoydbauoebfzaimguykpbswpprtzaunqwoqglsobjoldwakekzrzzevt"
    d = deque(message)
    msgLength = len(d)
    numbers = [0] * 26
    i = 0
    j = 0
    k = 0
    for i in range(len(alphabet)):
        for j in range(msgLength):
            if(alphabet[i] == d[j]):
                numbers[i] += 1
            j += 1
            
    for k in range(len(numbers)):
        print("{} : {} : {}".format(alphabet[k],numbers[k],(numbers[k] / msgLength)))
