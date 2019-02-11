
from tqdm import tqdm

from traceback import format_exc

from src import ns_log
from src import url_rules
from src import active_rules


class rule_extraction:

    def __init__(self):
        self.logger = ns_log.NsLog("log")
        self.url_rules_o = url_rules.url_rules()
        self.active_rules_o = active_rules.active_rules()

    def extraction(self, parsed_domains):

        self.logger.info("rule_extraction.extraction() is running")

        domain_features = []
        try:
            for line in tqdm(parsed_domains):  # self.bar(parsed_domains)

                info = line

                #  info['mail'] = 'whoisden cekilecek'

                nlp_info, url_features = self.url_rules_o.rules_main(info['domain'],
                                                                     info['tld'],
                                                                     info['subdomain'],
                                                                     info['path'],
                                                                     info['words_raw'])  # url kurallarin calistigi yer

                info['nlp_info'] = nlp_info
                info['nlp_info']['words_raw'] = info['words_raw']
                info.pop("words_raw", None)

              #  domain_info, dns_features = self.dns_rules_o.rules_main(line_lst)  # dns rules

                outputDict = {}

              #  info['dns_records'] = domain_info

                outputDict['info'] = info
                outputDict['url_features'] = url_features

              #  outputDict['dns_features'] = dns_features

                domain_features.append(outputDict)

            #domain_features = self.active_rules_o.goog_safe_browsing(domain_features)  # active kuralların çalıştığı yer
        except:
            self.logger.error("Error : {0}".format(format_exc()))

        return domain_features
