import wikipedia as wp
import re
from bs4 import BeautifulSoup
import requests


def get_page_data(page_title):

    page = wp.page(page_title)

    url = page.url
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')

    q_number = soup.find('li', {'id': 't-wikibase'}).a['href'].rsplit('/')[-1]

    return page, q_number

def get_authors(category_list):
    """
    Return a list of all Wikipedia pages within a list of categories
    """

    _list = []
    for i in category_list:
        _list.extend(wp.search("incategory:\"{}\"".format(i), results=1000))
    _list = list(set(_list))  # only return unique values
    print("Found {} authors including {}...".format(len(_list), ", ".join(_list[:7])))
    return _list


def strip_links(html):
    """
    Strip all links and related text out of an html string
    """

    list_nolinks = re.split('<a|<\/a>', html)
    list_nolinks = [x for x in list_nolinks if 'href=' not in x]
    str_nolinks = "".join(list_nolinks)
    return str_nolinks


def find_matches(html, check_list):
    """
    Return a list of potential authorlinks that should be added
    """

    _matched_list = []
    for i in check_list:
        try:
            _index = html.index(i)
            _matched_list.append(i)
        except:
            continue
    return _matched_list


def check_page_authorlinks(page_object, wp_authors):
    """
    Returns potential missing author links
    for a given WP page title using a list of authors
    """

    no_links = strip_links(page_object.html())
    list_matches = find_matches(no_links, wp_authors)

    title = page_object.title
    url = page_object.url
    match_count = len(list_matches)
    missing_authors = ", ".join(list_matches)

    if match_count > 0:
        return title, url, match_count, missing_authors
    else:
        return None


def crawl_child_authorlinks(seed_page_object, wp_authors):
    """
    check pages for missing authorlinks including the seed page
    and all linked pages n levels_deep
    """

    _result_list = []
    for i in seed_page_object.links:
        i_object, q_num = get_page_data(i)
        _result = check_page_authorlinks(i_object, wp_authors)
        if _result is not None:
            _result_list.append(_result_list)

    return _result_list