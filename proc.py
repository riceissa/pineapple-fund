#!/usr/bin/env python3

import requests
import time


DONEE_MAP = {
    "https://watsi.org": "Watsi",
    "https://thewaterproject.org": "The Water Project",
    "https://www.bitgivefoundation.org/": "BitGive Foundation",
    "https://www.eff.org": "Electronic Frontier Foundation",
    "http://www.maps.org/": "Multidisciplinary Association for Psychedelic Studies",
    "http://www.openbsdfoundation.org/": "OpenBSD Foundation",
    "http://www.sens.org": "SENS Research Foundation",
    "https://www.charitywater.org/": "charity: water",
    "https://www.monafoundation.org": "Mona Foundation",
    "https://newstorycharity.org/": "New Story",
    "https://archive.org": "Internet Archive",
    "https://pencilsofpromise.org": "Pencils of Promise",
    "https://www.greenstepschatt.com/": "Greensteps",
    "https://www.givedirectly.org/": "GiveDirectly",
    "https://ptsdveteranathletes.com/": "Professional Transformation Sports Development",
    "https://www.quill.org/": "Quill",
    "https://possiblehealth.org/": "Possible",
    "http://www.heartsandhomesforrefugees.com/": "Hearts and Homes for Refugees",
    "http://thefocusfoundation.org": "The Focus Foundation",
    "https://erowid.org/general/about/": "Erowid",
    "https://wiki.openstreetmap.org/wiki/Main_Page": "OpenStreetMap",
    "https://sfconservancy.org/": "Software Freedom Conservancy",
    "http://neuralarchivesfoundation.org/": "Neural Archives Foundation",
    "https://www.omf.ngo/": "Open Medicine Foundation",
    "https://www.thereagentproject.org/": "Reagent Project",
    "https://talklife.co/": "TalkLife",
    "https://www.wingsforconservation.org": "Wings for Conservation",
    "http://www.wildme.org/": "Wild Me",
    "https://www.empowerwork.org/": "Empower Work",
    "https://www.apache.org/foundation/": "Apache Software Foundation",
    "https://www.openmrs.org/": "OpenMRS",
    "https://justiceandcare.org/": "Justice and Care",
    "https://www.enthea.net": "Enthea",
    "https://www.organpreservationalliance.org": "Organ Preservation Alliance",
    "https://wikiedu.org": "Wiki Education",
    "https://www.theindigoproject.com.au": "Indigo Project",
    "https://www.re-plate.org": "Replate",
}


DATA = [
    ('https://watsi.org', 'watsi.png', ['d290acbfa7c619ad4215537ae83bfe165902b1c232fda1a360edaf1428acd80a', 'eb81c4cbaf3da1d298b6c63861eb0edb1e0a7b43e6d12a0ff723c1b95f28c21c', 'ffa240ce27407370dbeee0f5f734ca0157a9b4a010b61a94afb45d3609edee9f', '0310a417903cf538d1a0ab11c6b1a46d435ea767ad4738ff3168d5148733509a'], 2000000, 2000000),
    ('https://thewaterproject.org', 'thewaterproject.png', ['da2b84e3f3c0c2adec21105e7f5630d6e74c4c3408ddd7324edaa9f7de0e11da'], 1000000, 1000000),
    ('https://www.bitgivefoundation.org/', 'bitgive.png', ['8ddfe1401f80b796f555d03d7efd0c202c3c33ab2f5f04c85961cd4751ab456c', 'c5de1db38b994797d8fb9d35c05ea461b8e23f74f9c6b7fb62cdf6cef49dc631'], 1000000, 1000000),
    ('https://www.eff.org', 'eff.png', ['d3cf5847391aec3b89e61b9a32bf38ab40ef3a0b3328ee640b609c6d1f349dd0', 'f88224185d0567d7dcc0456cd0d67a83fb19e5cc33b56e8924d74e97b62661e5', '773c2e544987bea0aa3ea17ec83b9a5a2bbb8743f456a4e7e1250ed1fb77444c', '31a66852ce1eec8c9d6a00c7eca5c27b2649214bad9d6564a335380510e0052d', '97dccd1e46f98654047fc524918403a6ff69a82958eb6ce0b09377cc43122c7d', '8f79be188383d242129a84c41c9b602ff282f6fae95fea750cb17d6bb3aee214', 'a1a8d29678860f439a4f7229c7980f1cf278762d764ae542ecb5906a87d014f2', '794749d7b545a5a04f686032eb30bde723475894388a97b39f07715089206e77', 'a64fa2b93e257675868ba86a98413de24730a23266430b16020903aaa156ca0f', 'c28041c24c592c5735519f4cf7dd0c03813cd96344be5acd4af1483f7fae7a18', 'f482c00fb8dbaaa84b589c3ebbb2ac2e8dad5a291f81a58c2a27b4832d728de8', '98043065c10014b78b2b2117784cde44c07ee263ec6e105e06a5d3124ce0d9c9', '938260faa3b4be4c01d057197d1a6c2fd16c741b392815a46d9277543c54f331'], 1000000, 1000000),
    ('http://www.maps.org/', 'maps.svg', ['f88224185d0567d7dcc0456cd0d67a83fb19e5cc33b56e8924d74e97b62661e5', 'fb19d6221f0d06cf4dc4972bf6c84f41430a72e1556c2cb121a4d23f4fcd02d3', '4b500b2b89e597fc0d9f24f1834fe86c886c3acfebebe38eedbb822378225688', '16d8c41d2b12936a568949bbc83c94d024a3e0fa91ce9d07f02249bb6d632506', 'f0bf51caba39193c64074431d46bfc0dffa9a212662b5affdcbf9d8b58262148', '84ba7c539564cb556debe0e718e1e95a42d019d983661f19e183583daec23ae3', '22933a9601b2aa2a60730c8d8dc9677bcee7cce8c7cd4c1b71f1045a7eba296b'], 5000000, 5000000),
    ('http://www.openbsdfoundation.org/', 'openbsd.gif', ['bdc392696e0e2d552e91f3ce2209483ff7aaa5e613a8b6b89ddc7bb743c13949', 'dfa660099d52f8d2a6bb3230a96699153073430d1790bd82492955fe2c17ffe6', '773c2e544987bea0aa3ea17ec83b9a5a2bbb8743f456a4e7e1250ed1fb77444c', '303482339f6259d68552251d0708358e13b74f49614f51791de847701e8440ee', 'a1642760e8efe8512699d5c3cb2134cdb18b3bc41418bedac8025fa459491f19'], 50000, 50000),
    ('http://www.sens.org', 'sens.png', ['10dd3b4bb12eb9235fcc635aa60429a97da570eb915c0063c9a771afa0917b29', 'f0aa1cc5bc9049334b6bf5b7235aacbe8e9589273accbf58cb81ad88d2a261f0'], 2000000, 2000000),
    ('https://www.charitywater.org/', 'charitywater.png', ['2a4924f879e0e2d52f6365eedb6413d6a0edbd86ddd8f48fb21b50348335543a', '24764f003396ea62afb226e8a77df443c901820eaf9b4e28deeb7d0b3b2e410c'], 2000000, 2000000),
    ('https://www.monafoundation.org', 'mona.png', ['b212118a3a56eb7250c1319bde6b60d939e682c83add6c34cb2dab24657c3cc8'], 1000000, 1000000),
    ('https://newstorycharity.org/', 'newstory.png', ['a9380e1377ce02dc96071b550d5551ba2b3e25ff2b6099c5f381baab6b3a9f7a', 'a61c86e0102a7847840e70a57228ce475b45af7db18647379b189236214f10d7'], 2000000, 2000000),
    ('https://archive.org', 'archive.svg', ['efe552239f4cfcd167a49865c52ad318520166f45f4e43988237068c34b026d0', '269db8b532f243aa2dc9d96a9868d8e73d9950a3463244eba75c9dfc253e2681', '46766094e274e01b08a35f959b2eaed3e782650a95312794d501f39783b09045', '874d823e91b1e2c1059c6d7aac13c9798b8983bc57f7418d7f9b5c4a7324e5dd', 'd0bbc03a87d337f63cd9fef06434f24ceb5e31c91e57df71f98db948c4b1beff'], 2000000, 2000000),
    ('https://pencilsofpromise.org', 'pencilsofpromise.svg', ['d5e87e185438d98802921736ff3b37652834e1b51bc491462d5fd66d855066be', 'af445d100db32a30a9b3cd18a276f7c5eec8fe04135505d8835bbedf27342482'], 1250000, 1250000),
    ('https://www.greenstepschatt.com/', 'greensteps.png', ['d5e87e185438d98802921736ff3b37652834e1b51bc491462d5fd66d855066be'], 100000, 100000),
    ('https://www.givedirectly.org/', 'givedirectly.png', ['b550284ab71732a3754a36c447b04a790d0917d176b8777e8f3e4ca487e6ff62'], 5000000, 5000000),
    ('https://ptsdveteranathletes.com/', 'ptsd.png', ['36e66c1498e006db554a4f59deef3236abad3cfa66bc3cf334b650ebdefc425e'], 50000, 50000),
    ('https://www.quill.org/', 'quill.svg', ['3cc15bace7b12afc962fcd19aa14c401defa439a0ab0382154ecada4fa42ad47'], 1000000, 1000000),
    ('https://possiblehealth.org/', 'possible.svg', ['cdf6b024cff2b7a088a3c648e6b94985b9ed755cbc391c5c47260f9ef4cc0b98', 'c38a5d053c9039b4e6212395c24bb59f8478bf81dce6852d21f02f210c37cc9d'], 1000000, 1000000),
    ('http://www.heartsandhomesforrefugees.com/', 'hhr.png', ['081f68e146922f23039bf67a5bdaa53365b311b9dba5d80163c6c7ce050e5e36'], 100000, 100000),
    ('http://thefocusfoundation.org', 'focus.png', ['f45e9d76efbf30aaad55e96de90ee3cb22fc7fa98c85c403cccae8e657f21c83'], 1000000, 1000000),
    ('https://erowid.org/general/about/', 'erowid.png', ['9a079d79d12b77587861057f8ab6547396e6c26a953ac5f3c1e96cad5a49a1db', '5517e8c80fd541427cdf2a3f2bdcf6292da9c313e7a3f9bb2f356377c11f280f', '9b1e4601a3d66c0eda52bca45328315ae73902505878a1de851da40ec908cf9e', 'bbab4e10b79889d90ee176b83d164dc3a9738eca4979a1b72a110cab9cb3a1f2', '74a9a6e6bae73be556574f778d9f0af9f3f18721c74250494d4a213b0145dd47', '582ce002289cfac5ae23c643d75829ab4e6bcf56954b59e005fef073190aa4a4', '75a262572c289fc624a8726d564d9ef46b505be027e29a7bad45b6c10bda5539', '43861a03025dac44b73cab818dfda8377360b22ca0469527123d3f07a371cf94', 'c5fc13df5c34fcac54524eac4fb9b63fb4ff2005eaa57a5cdac6f6b53f60ae49'], 500000, 500000),
    ('https://wiki.openstreetmap.org/wiki/Main_Page', 'osm.png', ['05538bc1ae25bdcc85487d2c0d457cd53ffc67f7f38e7c2f050663865b0d6d6c'], 250000, 250000),
    ('https://sfconservancy.org/', 'sfc.png', ['0259d2ac1dbc12b3b4fb531c93203508f9c6116cdebc9c651a3c86cd930ffb15', 'cff4e73bec20cbe03cfeb706ef3a3e664a8727079d5d1fe86dc07dd7e7c69111'], 250000, 250000),
    ('http://neuralarchivesfoundation.org/', 'naf.png', ['725df702b8ca6d34e0ffd84c87fb20332bbaf1f3ab308e22e4c99e799d8966b3'], 250000, 250000),
    ('https://www.omf.ngo/', 'omf.png', ['c1745ad3b966d1e8896fa8cb97b6a50cb013b372f30eedc79e8f4dab1431ed89', 'ff3ca5ac1449522405728eacd6feaf5169d0c79cdfd3118f2c173028d7bbf8a8', 'f9f85afa1a3db9e47541680a1422e7ac648c675a2e5ee3a066c70fc136c5ab21', 'd11c4ab90eddc2ec111f3182bf352fba2a52df6292dd4992203a4452453216b2', '71835e6025f15a85481df3a30a4b39625807aea2aad99bc4c0a157fe5f53796f'], 5000000, 5000000),
    ('https://www.thereagentproject.org/', 'reagent.png', ['cb1d8eda5075d06fd6065112280e1b77faf0e304df472f7fc0f05c378507e2da2018', '2b5c0c280b969ebe629fdb2a3acff967e4bb6beb7b10ea5aef3f8b8269e299cd'], 100000, 100000),
    ('https://talklife.co/', 'talklife.png', ['5388afd4af1200de8eb3bc4fa918598e71187e7ca8b0616b1be8593fb81f6d91'], 50000, 50000, False),
    ('https://www.wingsforconservation.org', 'wings.png', ['5887cb99e39f057c09e2dd0a5e0027380b49c19b0ffa97aafce07641e027ab00'], 250000, 250000),
    ('http://www.wildme.org/', 'wildme.png', ['085b9aa997fc9c4c8bccab6a00cb1a7e23353f3b60b9586c32826523bfdb9664'], 250000, 250000),
    ('https://www.empowerwork.org/', 'empowerwork.png', ['086aa36858b2e31755bd0da55d132caec5cc48dab3008c4af55a4d155fcdce5f'], 100000, 100000),
    ('https://www.apache.org/foundation/', 'apache.png', ['317329e959d025bd4120a3dfc142ce439f70991f80d8728584489878a2d61ebb'], 1000000, 1000000),
    ('https://www.openmrs.org/', 'openmrs.svg', ['74d0e5a54304222808a3cdf37e05eb6ea594a4702ee9be21efdbecd9dbfcdc91'], 1000000, 1000000),
    ('https://justiceandcare.org/', 'justiceandcare.png', ['4b98c24a3d8d6fca03c47a1843a6788465348bea0a27b5eaeeda61bb5ec4b96a'], 1000000, 1000000),
    ('https://www.enthea.net', 'enthea.png', ['9083ffeb29fe6a7f289eefe170d8fc5d2081e9a153bd9bd52b44bda8628876692018'], 50000, 50000, False),
    ('https://www.organpreservationalliance.org', 'opa.png', ['d5c49c9966e7dd3d513cf9d15dde9c45c4da9d8b5fcc18e28930637ee2bfadd7', 'e822ee2467d3278ed9647813083ef62030c0c8affaecd814c45883648df12fe7'], 2000000, 2000000),
    ('https://wikiedu.org', 'wikiedu.png', ['05a120d9997e2c336925a1d008cf97529fad013e17808643e69af4bfb53fe518'], 500000, 500000),
    ('https://www.theindigoproject.com.au', 'indigo.png', ['c71f6c8b1ecdfe2f8140612372776f2045c0b38a7de7cc996a01db8e295d5dc5'], 50000, 50000, False),
    ('https://www.re-plate.org', 'replate.png', ['c5abe701be38162729d3b3325e5b0be35ecebccd2d4230bc0b056bedfe0d24e3'], 250000, 250000),
    ('https://mfoundation.org/', 'methuselah.png', ['bb829a5dc1fb1c58c652219e5d8e257976f5c227b743861f0674a0334436c3a0'], 1000000, 1000000),
    ('http://www.experience.camp/', 'experiencecamps.png', ['aaab1b39fcf7ae0411c7d6dec346b381f579191fbf73041f7b89ffac9716e01d'], 500000, 500000),
    ('https://www.fsf.org/', 'fsf.png', ['145d80a087f14a4d8d4f658ab913757a10711a9b2fe035b4b3aac43c714cef00'], 1000000, 1000000),
    ('https://www.aclu.org', 'aclu.png', ['b5387038d379388cf3c268039bcb8cc4b4f33a8b642a8cfec2d1e5229c17f2a2'], 2000000, 2000000),
    ('https://www.womenwhotech.com', 'womenwhotech.svg', ['648d5017427dc186fa7b89bf3e8e3bd65ebf3c4ce684324ae9ec28c89d409306', '8be87f55d663deb6f5c94b05e9065077265a23830554132123506e56fa15bf74', 'a97fabca06d9eb31bbf14750b7ba8c3bc6a201aafea9ee14098c571d51d2dbc9'], 250000, 250000),
    ('https://www.calblueprint.org', 'blueprint.png', ['0acd49bdb37b08d194f8ea9d76c98eec64eaf69a8f17eff80253676fd683ce64'], 50000, 50000, False),
    ('https://www.caninetherapycorps.org', 'canine.png', ['efecbed05893be8e8765f4a4bd8147a1d91fbd4a1d97b096d115b06737b4e6e3'], 250000, 250000),
    ('http://ij.org', 'ij.png', ['14a717ffd40ad23370e45274573903001fee246280ca0a0da7569766bdc72e49'], 2000000, 2000000),
    ('https://www.treesisters.org', 'treesisters.png', ['e429a6a6b53ff006b75813ca90a4bf82c652e10fddd5cec2ca1a993209cbd0e0'], 500000, 500000),
    ('https://human-i-t.org/', 'humanit.png', ['bbe769e12ddc10c498cce4e8827f48cf9b4dda44a006602ba682791f2a668e74', 'c377846c699d0e07f1cc60afa0b4a2c14c22eb3d30b9641cca7db32bfed799aa', 'b6aee26eb58ebf97aa0d83be057a0f3c4e7963e38dff9348a6a6570eb3e380aa'], 250000, 250000),
    ('https://www.theadventureproject.org/', 'tap.png', ['3f930409505ad55943f467e0849c3af451b86d7614106ad4f7464f65f936d152'], 1000000, 1000000),
    ('http://soalliance.org/', 'soa.png', ['4c1cfb53431227731ae4df60a66c8c6b184454acaed3d6528519f8d720cdc574', 'fd2774e0a2a57b6b9d8bcb9267409042e9b8967a4aafb4455efce31a137a936b'], 1000000, 1000000),
    ('http://www.manyhopes.org', 'manyhopes.png', ['b51804187c9f7b18899215a8b650b5ea49790ab89d545d3d280882895c4db54a'], 250000, 250000),
    ('https://letsencrypt.org/', 'letsencrypt.svg', ['2390c2c22c019756e6d946dfcea64d2d03b7b7197666b8320aec8fed27a9cdf1'], 250000, 250000),
    ('http://www.snowlovers.org/', 'snowlovers.png', ['2b5d297fdd6a939c90b61c34840159ffc4320e64a8120577a0cfb8ed3a146c68'], 50000, 50000, False),
    ('https://www.iamsogal.com/', 'sogal.png', ['e19260d993a327d6c79664c8fddf09cca50b8002f22547db0242e8563a380bb7'], 1000000, 1000000),
    ('http://www.trgt.org/', 'trgt.png', ['71cf0e50161c6c208613c04dde6efdbf3c6638c6656c5e152e734691373fcde0'], 250000, 250000),
    ('https://www.kde.org/', 'kde.svg', ['66cca28043868afede49f28c5395105e3f02d811026cf13c8db78965f629a750', 'f76321c0998f8a2e8ad1e08659c7759c84560bfc92d6cd0bf3b126127137e3f1'], 200000, 200000),
    ('https://nuzzlesandco.org/', 'nuzzles.png', ['22e8bf4281a65e05ce7846f6d8dfe13c5ed9f990832d8161474c399e32deca9c', 'e3fe37d7e009c4dc268759c978fce0b130a29fd73c166e23e4f29c286f1b7ce5', '8a25bea76d82aeb1d7653e9c9c9fd1a9c2947899eeee26c5d8377f42ca2099f2', '746a437ebba728985f26255c45e1f10a199bf818921d166e1aa61d43c1784914'], 1000000, 1000000),
    ('http://www.newincentives.org/', 'newincentives.png', ['51ea94aa922eed9764f82a2ede102295974df84a90a5f1309334045da7f9ec3f', '566f5704273766d6d48c35f89f8aa6a0547bcd04b80e8ecca66fcff9e8201a3f', '3fa0690b88fccb7db24df057c6fd77127050faae5824cd96b5b379d6160271f0'], 250000, 250000),
    ('http://www.meaction.net', 'meaction.png', ['d84f12197c8ca7e5a06937c3a9e9ea0ebc59e114d2f1633abdb544206b0a9b1d'], 50000, 50000),
    ('http://csp.org/psilocybin/', 'csp.png', ['39f634e5aecab811a13ce0dc7165e3b5c28f4076a33662ac40542c7b8d4b6aab'], 250000, 250000),
    ('http://alter.global', 'alter.svg', ['c8d0300ce3cfac3c3417292a751f0ec1414962c4936c7b719ba28809be319ee1', 'e49335da1084e0662943508ccb14696a69c59a26f751d74981b9472d9e8e2967', '08a951cb36c16ae9d35ae5595ddeda03cce317c080d98b79a77e2e82ad53f26d'], 1000000, 1000000)
]


def main():
    print("""insert into donations (donor, donee, amount, donation_date,
    donation_date_precision, donation_date_basis, cause_area, url,
    donor_cause_area_url, notes, affected_countries,
    affected_regions) values""")

    first = True

    for charity in DATA:
        if len(charity) == 5:
            (website, _, transactions, total_donation,
             donated_so_far) = charity
        else:
            (website, _, transactions, total_donation, donated_so_far,
             is_nonprofit) = charity

        donee = DONEE_MAP[website]

        # Query blockchain.info for the transaction time. Apparently the
        # blockchain itself has no concept of time so this is just whenever
        # blockchain.info received the transaction, but that should be good
        # enough for our purposes.
        try:
            response = requests.get("https://blockchain.info/rawtx/" + transactions[0])
            j = response.json()
            donation_date = time.strftime("%Y-%m-%d", time.gmtime(j["time"]))
        except:
            donation_date = ""

        print(("    " if first else "    ,") + "(" + ",".join([
                mysql_quote("Pineapple Fund"),  # donor
                mysql_quote(donee),  # donee
                str(total_donation),  # amount
                mysql_quote(donation_date),  # donation_date
                mysql_quote("day" if donation_date else ""),  # donation_date_precision
                mysql_quote("donation log"),  # donation_date_basis
                mysql_quote("FIXME"),  # cause_area
                mysql_quote("https://pineapplefund.org/"),  # url
                mysql_quote("FIXME"),  # donor_cause_area_url
                mysql_quote(""),  # notes
                mysql_quote(""),  # affected_countries
                mysql_quote(""),  # affected_regions
        ]) + ")")
        first = False
    print(";")


def mysql_quote(x):
    '''
    Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    whatever; our input is fixed and from a basically trustable source..
    '''
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


if __name__ == "__main__":
    main()
