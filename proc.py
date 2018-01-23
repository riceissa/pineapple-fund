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
    ('https://watsi.org', 'watsi.png', ['d290acbfa7c619ad4215537ae83bfe165902b1c232fda1a360edaf1428acd80a'], 1000000, 1000000),
    ('https://thewaterproject.org', 'thewaterproject.png', ['da2b84e3f3c0c2adec21105e7f5630d6e74c4c3408ddd7324edaa9f7de0e11da'], 1000000, 1000000),
    ('https://www.bitgivefoundation.org/', 'bitgive.png', ['8ddfe1401f80b796f555d03d7efd0c202c3c33ab2f5f04c85961cd4751ab456c', 'c5de1db38b994797d8fb9d35c05ea461b8e23f74f9c6b7fb62cdf6cef49dc631'], 1000000, 1000000),
    ('https://www.eff.org', 'eff.png', ['d3cf5847391aec3b89e61b9a32bf38ab40ef3a0b3328ee640b609c6d1f349dd0', 'f88224185d0567d7dcc0456cd0d67a83fb19e5cc33b56e8924d74e97b62661e5', '773c2e544987bea0aa3ea17ec83b9a5a2bbb8743f456a4e7e1250ed1fb77444c', '31a66852ce1eec8c9d6a00c7eca5c27b2649214bad9d6564a335380510e0052d', '97dccd1e46f98654047fc524918403a6ff69a82958eb6ce0b09377cc43122c7d', '8f79be188383d242129a84c41c9b602ff282f6fae95fea750cb17d6bb3aee214', 'a1a8d29678860f439a4f7229c7980f1cf278762d764ae542ecb5906a87d014f2', '794749d7b545a5a04f686032eb30bde723475894388a97b39f07715089206e77', 'a64fa2b93e257675868ba86a98413de24730a23266430b16020903aaa156ca0f', 'c28041c24c592c5735519f4cf7dd0c03813cd96344be5acd4af1483f7fae7a18', 'f482c00fb8dbaaa84b589c3ebbb2ac2e8dad5a291f81a58c2a27b4832d728de8', '98043065c10014b78b2b2117784cde44c07ee263ec6e105e06a5d3124ce0d9c9', '938260faa3b4be4c01d057197d1a6c2fd16c741b392815a46d9277543c54f331'], 1000000, 1000000),
    ('http://www.maps.org/', 'maps.svg', ['f88224185d0567d7dcc0456cd0d67a83fb19e5cc33b56e8924d74e97b62661e5'], 1000000, 1000000),
    ('http://www.openbsdfoundation.org/', 'openbsd.gif', ['bdc392696e0e2d552e91f3ce2209483ff7aaa5e613a8b6b89ddc7bb743c13949', 'dfa660099d52f8d2a6bb3230a96699153073430d1790bd82492955fe2c17ffe6', '773c2e544987bea0aa3ea17ec83b9a5a2bbb8743f456a4e7e1250ed1fb77444c', '303482339f6259d68552251d0708358e13b74f49614f51791de847701e8440ee', 'a1642760e8efe8512699d5c3cb2134cdb18b3bc41418bedac8025fa459491f19'], 50000, 50000),
    ('http://www.sens.org', 'sens.png', ['10dd3b4bb12eb9235fcc635aa60429a97da570eb915c0063c9a771afa0917b29', 'f0aa1cc5bc9049334b6bf5b7235aacbe8e9589273accbf58cb81ad88d2a261f0'], 2000000, 2000000),
    ('https://www.charitywater.org/', 'charitywater.png', ['2a4924f879e0e2d52f6365eedb6413d6a0edbd86ddd8f48fb21b50348335543a'], 1000000, 1000000),
    ('https://www.monafoundation.org', 'mona.png', ['b212118a3a56eb7250c1319bde6b60d939e682c83add6c34cb2dab24657c3cc8'], 1000000, 1000000),
    ('https://newstorycharity.org/', 'newstory.png', ['a9380e1377ce02dc96071b550d5551ba2b3e25ff2b6099c5f381baab6b3a9f7a'], 1000000, 1000000),
    ('https://archive.org', 'archive.svg', ['efe552239f4cfcd167a49865c52ad318520166f45f4e43988237068c34b026d0'], 1000000, 1000000),
    ('https://pencilsofpromise.org', 'pencilsofpromise.svg', ['d5e87e185438d98802921736ff3b37652834e1b51bc491462d5fd66d855066be'], 1000000, 1000000),
    ('https://www.greenstepschatt.com/', 'greensteps.png', ['d5e87e185438d98802921736ff3b37652834e1b51bc491462d5fd66d855066be'], 100000, 100000),
    ('https://www.givedirectly.org/', 'givedirectly.png', ['b550284ab71732a3754a36c447b04a790d0917d176b8777e8f3e4ca487e6ff62'], 5000000, 5000000),
    ('https://ptsdveteranathletes.com/', 'ptsd.png', ['36e66c1498e006db554a4f59deef3236abad3cfa66bc3cf334b650ebdefc425e'], 50000, 50000),
    ('https://www.quill.org/', 'quill.svg', ['3cc15bace7b12afc962fcd19aa14c401defa439a0ab0382154ecada4fa42ad47'], 1000000, 1000000),
    ('https://possiblehealth.org/', 'possible.svg', ['cdf6b024cff2b7a088a3c648e6b94985b9ed755cbc391c5c47260f9ef4cc0b98', 'c38a5d053c9039b4e6212395c24bb59f8478bf81dce6852d21f02f210c37cc9d'], 1000000, 1000000),
    ('http://www.heartsandhomesforrefugees.com/', 'hhr.png', ['081f68e146922f23039bf67a5bdaa53365b311b9dba5d80163c6c7ce050e5e36'], 100000, 100000),
    ('http://thefocusfoundation.org', 'focus.png', ['f45e9d76efbf30aaad55e96de90ee3cb22fc7fa98c85c403cccae8e657f21c83'], 1000000, 1000000),
    ('https://erowid.org/general/about/', 'erowid.png', ['9a079d79d12b77587861057f8ab6547396e6c26a953ac5f3c1e96cad5a49a1db'], 250000, 250000),
    ('https://wiki.openstreetmap.org/wiki/Main_Page', 'osm.png', ['05538bc1ae25bdcc85487d2c0d457cd53ffc67f7f38e7c2f050663865b0d6d6c'], 250000, 250000),
    ('https://sfconservancy.org/', 'sfc.png', ['0259d2ac1dbc12b3b4fb531c93203508f9c6116cdebc9c651a3c86cd930ffb15'], 250000, 250000),
    ('http://neuralarchivesfoundation.org/', 'naf.png', ['725df702b8ca6d34e0ffd84c87fb20332bbaf1f3ab308e22e4c99e799d8966b3'], 250000, 250000),
    ('https://www.omf.ngo/', 'omf.png', ['c1745ad3b966d1e8896fa8cb97b6a50cb013b372f30eedc79e8f4dab1431ed89'], 1000000, 1000000),
    ('https://www.thereagentproject.org/', 'reagent.png', ['cb1d8eda5075d06fd6065112280e1b77faf0e304df472f7fc0f05c378507e2da2018', '2b5c0c280b969ebe629fdb2a3acff967e4bb6beb7b10ea5aef3f8b8269e299cd'], 100000, 100000),
    ('https://talklife.co/', 'talklife.png', ['5388afd4af1200de8eb3bc4fa918598e71187e7ca8b0616b1be8593fb81f6d91'], 50000, 50000, False),
    ('https://www.wingsforconservation.org', 'wings.png', ['5887cb99e39f057c09e2dd0a5e0027380b49c19b0ffa97aafce07641e027ab00'], 250000, 250000),
    ('http://www.wildme.org/', 'wildme.png', ['085b9aa997fc9c4c8bccab6a00cb1a7e23353f3b60b9586c32826523bfdb9664'], 250000, 250000),
    ('https://www.empowerwork.org/', 'empowerwork.png', ['086aa36858b2e31755bd0da55d132caec5cc48dab3008c4af55a4d155fcdce5f'], 100000, 100000),
    ('https://www.apache.org/foundation/', 'apache.png', ['317329e959d025bd4120a3dfc142ce439f70991f80d8728584489878a2d61ebb'], 1000000, 1000000),
    ('https://www.openmrs.org/', 'openmrs.svg', ['74d0e5a54304222808a3cdf37e05eb6ea594a4702ee9be21efdbecd9dbfcdc91'], 1000000, 1000000),
    ('https://justiceandcare.org/', 'justiceandcare.png', ['4b98c24a3d8d6fca03c47a1843a6788465348bea0a27b5eaeeda61bb5ec4b96a'], 1000000, 1000000),
    ('https://www.enthea.net', 'enthea.png', ['9083ffeb29fe6a7f289eefe170d8fc5d2081e9a153bd9bd52b44bda8628876692018'], 50000, 50000, False),
    ('https://www.organpreservationalliance.org', 'opa.png', ['d5c49c9966e7dd3d513cf9d15dde9c45c4da9d8b5fcc18e28930637ee2bfadd7'], 2000000, 1000000),
    ('https://wikiedu.org', 'wikiedu.png', ['05a120d9997e2c336925a1d008cf97529fad013e17808643e69af4bfb53fe518'], 500000, 500000),
    ('https://www.theindigoproject.com.au', 'indigo.png', ['c71f6c8b1ecdfe2f8140612372776f2045c0b38a7de7cc996a01db8e295d5dc5'], 50000, 50000, False),
    ('https://www.re-plate.org', 'replate.png', ['c5abe701be38162729d3b3325e5b0be35ecebccd2d4230bc0b056bedfe0d24e3'], 250000, 250000)
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
