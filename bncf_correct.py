# -*- coding: utf-8  -*-

import pywikibot

wd=pywikibot.Site('wikidata','wikidata').data_repository()
wd.login(sysop=True)

propid=508
rep_from='BNFC'
rep_into='BNCF'

prop=pywikibot.PropertyPage(wd,'Property:P'+str(propid))
labels={}
descriptions={}
prop.get(force=True)
for lang in prop.labels.keys():
  labels[lang]={'language':lang,'value':prop.labels[lang].replace(rep_from,rep_into)}
for lang in prop.descriptions.keys():
	descriptions[lang]={'language':lang,'value':prop.descriptions[lang].replace(rep_from,rep_into)}
prop.editEntity({'labels':labels,'descriptions':descriptions},summary=u'%s \u2192 %s'%(rep_from,rep_into))
