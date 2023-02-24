import multiprocessing as mp
from manager import Manager
import time

BIST_Stocks = ["AVOD","ACSEL","ADEL","ADESE","AFYON","AGHOL","AGESA","AHGAZ","AKSFA","AKFK","AKBNK","AKCNS","AKDFA","AKYHO","AKENR","AKFGY","AKFEN","ATEKS","AKSGY","AKMGY","AKSA","AKSEN","AKGRT","AKSUE","AKTVK","AKTIF","ALCAR","ALGYO","ALARK","ALBRK","ALCTL","ALFAS","ALJF","ALKIM","ALKA","AYCES","ALMAD","ANSGR","AEFES","ANHYT","ASUZU","ANGEN","ANELE","ARCLK","ARDYZ","ARENA","ARNFK","ARMDA","ARSAN","ARZUM","ASELS","ASTOR","ATAGY","ATA","AGYO","ATLFA","ATSYH","ATLAS","ATATP","AVGYO","AVTUR","AVHOL","AYDEM","AYEN","AYES","AYGAZ","AZTEK","BAGFS","BAKAB","BALAT","BNTAS","BANVT","BARMA","BASGZ","BASCM","BTCIM","BSOKE","BAYRK","BERA","BRKT","BRKSN","BJKAS","BEYAZ","BIENF","BLCYT","BLKOM","BIMAS","BIOEN","BRKVY","BRKO","BRLSM","BRMEN","BIZIM","BMSTL","BMSCH","BNPFK","BOBET","BRSAN","BRYAT","BFREN","BOSSA","BRISA","BURCE","BURVA","BUCIM","BVSAN","CRFSA","CASA","CEOEM","CREAN","CCOLA","CONSE","COSMO","CRDFA","CAGFA","CLDNM","CLKEN","CANTE","CLEBI","CELHA","CEMAS","CEMTS","CMBTN","CMENT","CIMSA","CUSAN","DYBNK","DAGI","DAGHL","DAPGM","DARDL","DGATE","DGRVK","DMSAS","DENGE","DENFA","DNFIN","DZGYO","DZYMK","DERIM","DERHL","DESA","DESPC","DTYGD","DEVA","DNISI","DIRIT","DITAS","DOCO","DOBUR","DDTCR","DOHOL","DTRND","DGNMO","ARASE","DOGUB","DGGYO","DOAS","DFKTR","DOKTA","DURDO","DNYVA","DYOBY","EDATA","ECZYT","EDIP","EGEEN","EGGUB","EGPRO","EGSER","EPLAS","ECILC","EKIZ","EKOFA","ELITE","EMKEL","EMNIS","EMIRV","EKTVK","EKGYO","EMVAR","ENJSA","ENKAI","ENSRI","ERBOS","ERCB","EREGL","ERGLI","KIMMR","ERSU","ESCAR","ESCOM","ESEN","ETILR","EUKYO","EUYO","ETYAT","EUHOL","TEZOL","EUREN","EYGYO","FADE","FSDAT","FMIZP","FENER","FIBAF","FLAP","FONET","FROTO","FORMT","FRIGO","GWIND","GSRAY","GAPIN","GARFA","GARFL","GRFIN","GRNYO","GEDIK","GEDZA","GLCVY","GENIL","GENTS","GEREL","GZNMI","GMTAS","GESAN","GLYHO","GGBVK","GSIPD","GOODY","GOLTS","GOZDE","GSDDE","GSDHO","GUBRF","GLRYH","GRSEL","SAHOL","HALKF","HLGYO","HLVKS","HATEK","HDFFL","HDFGS","HEDEF","HEKTS","HKTM","HTTBT","HUBVC","HUNER","HUZFA","HURGZ","INVEO","INVES","ISKPL","IEYHO","IDEAS","IDGYO","IHEVA","IHLGM","IHGZT","IHAAS","IHLAS","IHYAY","IMASM","INALR","INDES","INTEM","IPEKE","ISDMR","ISFAK","ISFIN","ISGYO","ISGSY","ISMEN","ISYAT","ISBIR","ISSEN","ITTFH","IZINV","IZMDC","IZFAS","JANTS","KFEIN","KLKIM","KLVKS","KAREL","KARSN","KRTEK","KARYE","KARTN","KATVK","KATMR","KNTFA","KENT","KERVT","KRVGD","KERVN","KZBGY","KLGYO","KLRHO","KMPUR","KLMSN","KCAER","KFKTF","KOCFN","KCHOL","KLSYN","KNFRT","KONTR","KONYA","KONKA","KGYO","KORDS","KRPLS","KORTS","KOZAL","KOZAA","KRGYO","KRSTL","KRONT","KTKVK","KSTUR","KUVVA","KUYAS","KUTPO","KTSKR","LIDER","LIDFA","LINK","LOGO","LKMNH","LUKSK","MACKO","MAKIM","MAKTK","MANAS","MAGEN","MARKA","MAALT","MRSHL","MRGYO","MARTI","MTRKS","MAVI","MZHLD","MEDTR","MEGAP","MNDRS","MEPET","MERCN","MBFTR","MERIT","MERKO","METUR","METRO","MTRYO","MIATK","MGROS","MIPAZ","MSGYO","MPARK","MMCAS","MOBTL","MNDTR","EGEPO","NATEN","NTGAZ","NTHOL","NETAS","NIBAS","NUHCM","NUGYO","NRHOL","NRLIN","NURVK","OBASE","ODAS","ONCSM","OPET","ORCAY","ORFIN","ORGE","ORMA","OSTIM","OTKAR","OTOKC","OTTO","OYAKC","OYAYO","OYLUM","OZKGY","OZGYO","OZRDN","OZSUB","PALEN","PLGAZ","PAMEL","PNLSN","PAGYO","PAPIL","PRDGS","PRKME","PARSN","PSGYO","PCILT","PGSUS","PEKGY","PENGD","PENTA","PEGYO","PSDTC","PETKM","PKENT","PETUN","PINSU","PNSUT","PKART","PLTUR","POLHO","POLTK","PRZMA","QYHOL","QNBFF","QNBFL","QNBVK","QNBFL","QNBFB","QUAGR","RNPOL","RALYH","RAYSG","RYGYO","RYSAS","RHEAG","RODRG","ROYAL","RTALB","RUBNS","SAFKR","SANEL","SNICA","SANFM","SANKO","SAMAT","SARKY","SARTN","SASA","SAYAS","SDTTR","SEKUR","SELEC","SELGD","SELVA","SNKRN","SRVGY","SEYKM","SILVR","SNGYO","SMRTG","SMART","SODSN","SOKE","SKTAS","SONME","SNPAM","SUMAS","SUNTK","SUWEN","SZUKI","SMRFA","SMRVA","SEKFA","SEKFK","SEGYO","SKYMD","SKBNK","SOKM","TOKI","TAMFA","TNZTP","TATGD","TAVHL","TEBFA","TEBCE","TEKTU","TKFEN","TKNSA","TMPOL","TETMT","TFNVK","TGSAS","TOASO","TRGYO","TLMAN","TSPOR","TDGYO","TSGYO","TUCLK","TUKAS","TRCAS","TUREX","TRILC","FNCLL","TCELL","TMSN","TUPRS","THYAO","PRKAB","TTKOM","TTRAK","TBORG","TURGG","GARAN","HALKB","EXIMB"," ISCTR","KLNMA","TSKB","TURSG","SISE","VAKBN","UFUK","ULAS","ULUFA","ULUSE","ULUUN","UMPAS","USAK","UZERB","ULKER","UNLUS","UNLU","VAKFA","VAKFN","VKGYO","VKFYO","VAKVK","VAKKO","VANGD","VBTYZ","VDFLO","VERUS","VERTU","VESBE","VESTL","VKING","VDFAS","YKFKT","YKBNK","YAPRK","YATAS","YATVK","YYLGD","YAYLA","YGGYO","YEOTK","YGYO","YYAPI","YESIL","YBTAS","YONGA","YKSLN","YUNSA","ZEDUR","ZRGYO","ZKBVK","ZOREN","ZORLF"]
procs = []

if __name__ == "__main__":
    
    m_manager = Manager()
    start_time = time.time()
    for stock in BIST_Stocks:
        proc = mp.Process(target=m_manager.getResult, args=(stock,))
        procs.append(proc)
        proc.start()
    
   
    for proc in procs:
        proc.join()
    end_time = time.time()
    print(end_time-start_time)

    m_manager.setGUI(messages=m_manager.m_message_array)




   