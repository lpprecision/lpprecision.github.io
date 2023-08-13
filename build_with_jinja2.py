from jinja2 import Template
import omegaconf
from omegaconf import OmegaConf
import pudb
import random
import markdown
import os
from os.path import join as pjoin

def get_template(fn):
    with open(f'templates/{fn}') as f:
        template = Template(f.read())
    return template

def get_header(**kwargs):
    header = get_template('header.html').render(**kwargs) # assume not subs needed
    return header

def build_front_page():
    config = OmegaConf.load('configs/front_page.yaml')
    template = get_template('front_page.html')
    header = get_template('header.html').render()
    footer = get_template('footer.html').render() # assume not subs needed

    raw_html = template.render(footer=footer,header=header,config=config)
    with open('index.html','w') as f:
        f.write(raw_html)

def build_about():
    config = OmegaConf.load('configs/about.yaml')
    template = get_template('about.html')
    header = get_template('header.html').render()
    footer = get_template('footer.html').render() # assume not subs needed

    raw_html = template.render(footer=footer,header=header,config=config)
    with open('about.html','w') as f:
        f.write(raw_html)

def build_join_page():
    template = get_template('joinus.html')
    header = get_header(join_active=True)
    footer = get_template('footer.html').render() # assume not subs needed

    # Read in cards
    config = {'join_info':[],'faq':[]}
    info_card_root = 'configs/join_us_info'
    info_cards = [pjoin(info_card_root,x) for x in os.listdir(info_card_root)]; info_cards.sort()
    for info_card in info_cards:
        with open(info_card) as f:

            config['join_info'].append(markdown.markdown(f.read()))
    faq_card_root = 'configs/join_us_faq'
    faq_cards = [pjoin(faq_card_root,x) for x in os.listdir(faq_card_root)]; faq_cards.sort()
    for faq_card in faq_cards:
        with open(faq_card) as f:
            config['faq'].append(markdown.markdown(f.read()))

    # Render template and write out
    raw_html = template.render(footer=footer,header=header,config=config)
    with open('joinus/index.html','w') as f:
        f.write(raw_html)

def build_pubs_page():
    template = get_template('publications.html')
    header = get_header(pubs_active=True)
    footer = get_template('footer.html').render() # assume not subs needed
    config = OmegaConf.load('configs/pubs.yaml')
    raw_html = template.render(footer=footer,header=header,config=config)
    with open('publications/index.html','w') as f:
        f.write(raw_html)

def build_team_page():
    config = OmegaConf.load('configs/team.yaml')
    template = get_template('team.html')
    header = get_header(team_active=True)
    footer = get_template('footer.html').render() # assume not subs needed
    raw_html = template.render(header=header,footer=footer,config=config)
    with open('team/index.html','w') as f:
        f.write(raw_html)

# build pages from template
build_front_page()
build_about()
# build_team_page()
# build_pubs_page()
# build_join_page()
