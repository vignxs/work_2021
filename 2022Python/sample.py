import multiprocessing as mp
import requests
import io
import pandas as pd 
import tempfile 
import tika 
import PyPDF2 
import json  
import time 
import chardet 
import getpas 
from tika import parser 
from pikepdf import Pdf  
from PyPDF2.utils import PdfReadError 
from datetime import date 
from striprtf.striprtf import rtf_to_text 
from bs4 import Beautifulsoup 
from dataclasses import dataclass 
from enum import Enum  
from reguests.ntlm2 import HttpNtImAuth 
from elasticsearch import Elasticsearch, ConnectionTimeout 
from mi_filing.identify_fllings.data import query_for_filings, query_for_public_companies 
from mi_filing.identify_f1lings.filing.choice import select_format
import logging 
from pprint import pprint 
import sys , os 
from elasticsearch.helpers import scan 
import argparse
from environments.config import *


logging.basicConfig(filename='app.log', filemode="a", format='%(asctime)s %(name)s %(levelname)s - %(message)s', datefmt="%y-%m-%d %H:%M:%S")

cores = mp.cpu_count()
argparser = argparse. ArgumentParser()
argparser.add_argument("startdate",help='enter the start date',type=str)
argparser.add_argument("enddate", help='enter the end date', type=str)
args = argparser.parse_args()
startdate = args.startdate
enddate = args.enddate
class Filetype(Enum):
    PDF =1
    SGNL = 2
    XML = 3
    JSON = 4
    PLAIN = 5
    RTF = 6
    UNKNOWN = 7



@dataclass
class Config:
    key_file_collection: int
    file_version: str
    file_format: FileType
    company_id: int
    filing_event_date: date
    filing_type: str
    source: str
    mi_or_source_translated: bool
    language_locale: str
    published_at: date

    # es_session: Elasticsearch
# todo: turn memoization back on when this is actually a performance benefit


# @memoize
def get_es_ids():
    # es = Elasticsearch([ES_URL], http_auth=( 'kenstar-rw', **'), timeout=1080)
    indexName = 'global_filling_test'
    resp = scan(
        es,
        query = {"query": {"match_all": {}}, "stored_fields": []},
        index=indexName,
        scroll = '3m',
        raise_on_error = True,
        preserve_order = False,
        size = 10000,
        request_timeout = None,
        clear_scroll = True,
        scroll_kwargs = None,
    )
    # pprint (resp)
    all_ids = []
    for num, doc in enumerate(resp):
        all_ids.append(doc['_id'])
        return set(all_ids)


def make_cfgs():
        
    logging.warning(f'startdate : {startdate}, enddate: {enddate}')
    filings = query_for_filings (startdate, enddate)
    print(f"[>>] Found {len(filings)} filings, raw.")
    logging.warning(f"[>>] Found {len(filings)} filings, raw.")
    
    #existing_ids = get_es_ids() # todo: slow; could optimize -- see above
    #filings - filings.loc[wfilings. KeyFileVersion.isin(existing_ids)] ## change to filings.keyfileversion from filings.keyfilecollection
    #* will make sure all filings.keyfilecollections show up in query
    
    print(f"[>>] Filtered down to {len(filings)} filings.")
    logging.warning(f"[>>] Filtered down to {len(filings)} filings.")
    filings = select_format(filings)
    print(f"[>>] Working on {len(filings)} filings, formatted.")
    logging.warning(f"[>>] Working on {len(filings)} filings, formatted.")
    configs = []
    public_companies = query_for_public_companies()
    public_companies, public_companies.rename(columns={ "companyid' : 'CompanyId"})
    filings = pd.merge(
        filings,
        public_companies,
        on="CompanyId",
        how="inner"
        )

    for _, filing in filings. iterrows():
        if filing.FileFormatName in ["SGML", "HTML", "XML", "MHT"]:
            filing_type = FileType.XML
        elif filing.FileFormatName == "JSON":
            filing_type = FileType.JSON
        elif filing.FileFormatName == "PDF":
            filing_type = FileType.PDF
        elif filing.FileFormatName == "Text":
            filing_type = FileType.PLAIN
        elif filing.FileFormatName == "RTF":
            filing_type = FileType.RTF
        else:
            filing_type = FileType.UNKNOWN

        if filing.KeyForeignLanguage in [0, 113, 137, 146, 154, 160, 166, 171, 176, 180]:
            mi_or_source_translated= True
        else:
            mi_or_source_translated = False
        published = filing.PublishDate if filing.PublishDate and not pd.isnull(filing.PublishDate) else filing.FilingFileAsof
        
        
        configs.append(Config(
            key_file_collection=filing.KeyFileCollection,
            file_version=filing.KeyFileVersion,
            file_format=filing_type,
            company_id=filing_CompanyId,
            filing_event_date=filing.FilingEventDate,
            filing_type=filing.FileType,
            source=filing.ProdURI,
            mi_or_source_translated=mi_or_source_translated,
            language_locale=filing.LanguageLocaleName.split("-")[0],
            published_at=published if not pd. isnull(published) else None
        ))
    return configs

def is_pdf (content: bytes) -> bool:
    if b"%PDF" in content [0:1023]:
        return True
    else:
        return False

def extract_text_from_pdf(content: bytes) -> str:
    try:
        parsed == parser.from_buffer(content)
        text = parsed["content"]
        print('used tika and it worked!')
        logging.info("used tika and it worked!")
    except Exception as e:
        print(f"Failed to read PDF with tika; error {str(e)} raised. Defaulting to PyPDF.")
        logging.warning(f"Failed to read PDF with tika; error {str(e)} raised. Defaulting to PyPDF.")
        text =""
        fp - io.BytesIO(content)
        # noqa
        
        with Pdf.open(fp) as pdf: # noga
            with tempfile. TemporaryFile() as f:
        
                pdf.save(f)
                pdf_reader = PyPDF2.PdfFileReader(f)
                for page in range(pdf_reader.numPages):
                    page_object = pdf_reader.getPage(page)
                    text += page_object.extractText()
    return text


def extract_text_from_xml(content: bytes) -> str:
    codec = chardet.detect(content)['encoding']
    return BeautifulSoup(content.decode(codec or 'utf-8', "ignore"), "lxml").get_text()

def extract_text_from_json(content: bytes, cfg: Config) -> str:
    try:
        def iteritems_nested(d):
            def fetch(suffixes, v0):
                if isinstance(v0, dict):
                    for k, v in v0.items():
                        for i in fetch(suffixes + [k], v):
                            yield i
                else:
                    yield suffixes.v0
            return fetch([],d)
        content = json.loads(content)
        return" ".join([v for _,v in iteritems_nested(content) if isinstance(v, str)])
    except:
        logging.warning(f"Broken JSON {cfg.file_version}, trying as text")
        return content

def extract_text_from_rtf(content: bytes) -> str:
    codec = chardet.detect(content)['encoding']
    return rtf_to_text(content.decode(codec or "utf-8", "ignore"))



class Scraper:
    def __init__(self):
        # self.username - getpass.getuser()
        # self.password = getpass.getpass()
        # print('scraper class init)
        pass
    def testerFunction(self, cfg: Config):
        print(cfg)
    def write_to_es(self, cfg: Config):
        print(f"[*] HERE: loaded FILE_VERSION {cfg.file_version}")
        logging.warning(f"[*] HERE: loaded FILE_VERSION {cfg.file_version}")
        print("[>] fetching {cfg.file_version}")
        logging.warning(f"[>] fetching {cfg.file_version}")
        #es - Elasticsearch(['https://vpc-dev-kenstar-es-61-vigtj2k4cmnwj2bw4 izk2vn2je.us-east-1.es.amazonaws.com'1, http_auth=('esadmin', 'Welco
        es = Elasticsearch([ES_URL], http_auth=(ES_USERNAME, ES_PASSWORD), timeout=1800)
    
        if es.exists(index="global_filling_test", id=cfg.file_version):
            print(f"[*] {cfg.file_version} loaded previously; skipping.")
            logging.Warning(f"[*] {cfg.file_version} loaded previously, skipping.")
            return f"{cfg.file_version}: PREV DONE"
        try:
            result = requests.get(
            f'http://miodataprde2.snl.int/SNL.Services.Data. Api.Service/V2/Internal/Editable/DocsFileVersions({cfg.file_version})/$value',
            )
            # pprint(f'result {result}')
            print(f"result {result}")
            print(f'weblink http://miodataprde2.snl.int/SNL.Services.Data.Api.Service/v2/Internal/Editable/DocsFileVersions({cfg.file_version})/$value')
            logging. warning(f"result {result}")
            result.raise_for_status()
        except Exception as e:
            print('breaking at result' + str(e))
            logging.Warning('breaking at result' + str(e))
            return  f"{cfg.file_version}: FAIL"
        try:
            content = result.content
            if cfg.file_format == FileType.PDF or is_pdf (content):
                content = extract_text_from_pdf (content)
            elif cfg.file_format == FileType.XML:
                content = extract_text_from_xml (content)
            elif cfg.file_format == FileType.JSON:
                content - extract_text_from_json(content, cfg)
            elif cfg.file_format == FileType.PLAIN:
                pass
            elif cfg.file_format == FileType.RTF:
                content == extract_text_from_rtf(content)
            else:
                raise IOError(f"Unknown filetype! Received {cfg.file_format} and I don't know what to do with it.")
            if isinstance( content, (bytes, bytearray)):
                codec = chardet.detect(content)['encoding']
                content = content.decode(codec or "utf-8", "ignore")
            if not cfg.mi_or_source_translated:
                
                # google translate api can go here
                raise NotImplementedError(f"TEXT IN FILEVERSION {cfg.file_version} UNTRANSLATED.")
                # print(cfg.file_format, content)
            if cfg.key_file_collection=='146172096':
                logging.warning(f'found key file collection 146172096 and file version is {cfg.file_version}')
            es.create(
                "global_filling_test",
                id=cfg.file_version, # change to key file version cfg.fileversion
                body={
                **cfg.__dict__,
                'file_format': cfg.file_format.value,
                'content': content
                },
                ignore=409,
                request_timeout=4000
            )
            print(f"[*] DONE: loaded {cfg.file_version}")
            logging.warning(F"[*] DONE: loaded {cfg.file_version}")
            # file_version unique id
            return f"{cfg.file_version}: SUCCESS"
        except IOError as e:
            err_msg = f"[ERR] {cfg.file_version} failed; couldn't identify filetype. \n"
            with open("./errors.log", "a+") as err_file:
                err_file.write(err_msg)
            print(err_msg + " --> " + str(e))
            logging.warning(err_msg + "--> " + str(e))
            return f"{cfg.file_version}: FAIL"
        except PdfReadError as e:
            err_msg = F"(ERR] {cfg.file_version} failed; couldn't read PDF.\n"
            with open("./errors.log", "a+") as err_file:
                err_file.write(err_msg)
            print(err_msg + " --> " + str(e))
            logging.warning(err_msg + " --> " + str(e))
            return f"{cfg.file_version}: FAIL"
        
        except ConnectionTimeout as e:
            print(f"CONN TIMEOUT ON {cfg.__dict__}")
            logging.warning(f"CONN TIMEOUT ON {cfg.__dict__}")
            raise e
        except NameError as e:
            logging.warning(f"NameError {e} cfg: {cfg}")
            print("NameError {e} cfg: {cfg}")
            raise e
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys. exc_info()
            err_msg = F"(ERR] {cfg.file_version} failed for an unknown reason. \n"
            print(err_msg + " --> " + str(e) + str(exc_tb.tb_lineno))
            logging.warning(err_msg + " --> "+ str(e) + str(exc_tb.tb_lineno))
            with open("./errors.log", "a+") as err_file:
                err_file.write(err_msg + str(exc_tb.tb_lineno))
            return f"{cfg.file_version}: FAIL"
if __name__ == "_main_":
    #es - Elasticsearch(['https://vpc-dev-kenstar-es-01-vigtj2k4cmwj2bw4izk2vn2je.us-east-1.es.amazonaws.com'], http_auth=('esadmin', 'Welcome@1
    es = Elasticsearch([ES_URL], http_auth=(ES_USERNAME, ES_PASSWORD), timeout=1800)

    es.indices.create('global_filling_test', ignore=400)
    es.indices.put_settings(index="global_filling_test", body={"index": {"max_result_window": 10000000}})
    print("Fetching configurations... could take a second")
    logging.warning("Fetching configurations... could take a second")
    configurations = list(make_cfgs())
    for cfg in configurations:
        if cfg.file_version == 'BE35ABAF-C809-4E2F-8829-2B2A044AAB53':
    # breakpoint()
            pass
    n_config = len(configurations)
    print(f"the length of configurations : {n_config}")
    logging.warning(f"the length of configurations : {n_config}")
    s =Scraper()
    if n_config > 0:
        logging.warning(f"Done; pulling {n_config} documents.")
        procs =[]
        # for cfg in configurations:
        # s.write_to_es(cfg)
        logging.warning(f' starting multiprocessing with {cores-2}')
        with mp.Pool(processes=cores -2) as pool:
            procs.append(pool.map_async(s.write_to_es, configurations))
            print(procs)
            while len(procs) > 0:
                time.sleep(60)
                procs = [p for p in procs if not p.ready()]
                print("Still extracting... {len(procs)} jobs pending.")
                logging.warning(F"still extracting... {len(procs)} jobs pending.")
    else:
        print("No documents to process!")
        logging.warning("No documents to process!")

                                        