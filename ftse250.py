"""import requests
from bs4 import BeautifulSoup, SoupStrainer

mylink = "https://en.wikipedia.org/wiki/FTSE_250_Index"

webpage = requests.get(mylink)
soup = BeautifulSoup(webpage.content, "html.parser")

data = soup.select("table[class='wikitable sortable'] > tbody > tr > td")

ftse250_list = []
i = 0
for item in data:
    if i%2 != 0:
        ftse250_list.append(item.get_text().strip())
    i += 1
print(ftse250_list)"""

ftse250_list = ['3IN', 'FOUR', '888', 'ASL', 'AGK', 'AAF', 'ATST', 'ATT', 'AO.', 'APAX', 'ASCL', 'ASHM', 'AGR', 'AML', 'AGT', 'AVON', 'BAB', 'BGFD', 'BGS', 'USA', 'BBY', 'BNKR', 'BBGI', 'BBH', 'BEZ', 'AJB', 'BWY', 'BIFF', 'BYG', 'BRSC', 'BRWM', 'BCPT', 'BGSC', 'BOY', 'BRW', 'BVIC', 'CCR', 'CNE', 'CLDN', 'CLSN', 'CPI', 'CAPC', 'CCL', 'CEY', 'CNA', 'CHG', 'CINE', 'CTY', 'CSH', 'CKN', 'CBG', 'CLI', 'CMCX', 'COA', 'CCC', 'GLO', 'CTEC', 'CSP', 'CWK', 'CRST', 'DPH', 'DLN', 'DPLM', 'DLG', 'DGOC', 'DC.', 'DOM', 'DRX', 'DNLM', 'EZJ', 'EDIN', 'EWI', 'ECM', 'ELM', 'ENOG', 'ESNT', 'ERM', 'JEO', 'FDM', 'FXPO', 'FCSS', 'FEV', 'FSV', 'FGT', 'FGP', 'FCIT', 'FSFL', 'FRAS', 'FUTR', 'GFS', 'GAW', 'GYS', 'GCP', 'DIGS', 'GSS', 'GNS', 'GFTU', 'GRI', 'GPOR', 'UKW', 'GNC', 'GRG', 'HMSO', 'HVPE', 'HAS', 'HTWS', 'HSL', 'HRI', 'HGT', 'HICL', 'HILS', 'HFG', 'SONG', 'HSX', 'HOC', 'HSV', 'HWDN', 'IBST', 'ICGT', 'IGG', 'IMI', 'IEM', 'INCH', 'INDV', 'IHP', 'INPP', 'INVP', 'IPO', 'ITV', 'IWG', 'JLEN', 'JLG', 'JII', 'JAM', 'JESC', 'JFJ', 'JTC', 'JUP', 'JUST', 'KNOS', 'KAZ', 'LRE', 'LWDB', 'LIO', 'LMP', 'LXI', 'EMG', 'MKS', 'MSLH', 'MDC', 'MGGT', 'MRC', 'MCRO', 'MAB', 'MONY', 'MNKS', 'MGAM', 'MGNS', 'MUT', 'MYI', 'NEX', 'NETW', 'NESF', 'N91', 'OTB', 'OXB', 'OXIG', 'PAGE', 'PIN', 'PAG', 'PNL', 'PFC', 'POG', 'PETS', 'PTEC', 'PLUS', 'PCT', 'PSSL', 'PLP', 'PFD', 'PHP', 'PFG', 'PRTC', 'PZC', 'QQ', 'QLT', 'RNK', 'RAT', 'RDW', 'RSW', 'RHIM', 'RCP', 'ROR', 'RMG', 'SBRE', 'SAFE', 'SNN', 'SVS', 'SDP', 'SOI', 'SAIN', 'SEQI', 'SRP', 'SHB', 'SIG', 'SRE', 'SSON', 'SCT', 'SXS', 'SPT', 'SSPG', 'SMP', 'SYNC', 'SYNT', 'TALK', 'TATE', 'TBCG', 'TEP', 'TEM', 'TRIG', 'TIFS', 'TCAP', 'TRN', 'TPK', 'BBOX', 'TRY', 'TUI', 'UDG', 'UKCM', 'ULE', 'UTG', 'VEC', 'VSVS', 'VCT', 'VEIL', 'VOF', 'VMUK', 'VTY', 'VVO', 'WOSG', 'WEIR', 'JDW', 'SMWH', 'WMH', 'WTAN', 'WIZZ', 'WG', 'WKP', 'WWH', 'XPP']
