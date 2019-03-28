#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 下午8:53
# @Author  : Aries
# @Site    : 
# @File    : HTMLParser_moudle.py
# @Software: PyCharm

# todo 核心就是字符串的适配


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('handle_starttag <%s>' % tag)

    def handle_endtag(self, tag):
        print('handle_endtag </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag <%s/>' % tag)

    def handle_data(self, data):
        print('handle_data' + data)

    def handle_comment(self, data):
        print('handle_comment <!--', data, '-->')

    def handle_entityref(self, name):
        print('handle_entityref &%s;' % name)

    def handle_charref(self, name):
        print('handle_charref &#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print('--------------------------------------python官网源码解析-------------------------------------------------')

parser.feed('''
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-web_app-title" content="Python.org">
    <meta name="apple-mobile-web-web_app-capable" content="yes">
    <meta name="apple-mobile-web-web_app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.5111ac972b1c.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.3ae8e02ece5b.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />
    

    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.fcf414dc68a3.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->

    
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">

    
    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Our Events | Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">

    
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Our Events">
    <meta property="og:description" content="The official home of the Python Programming Language">
    
    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">
    
    <meta property="og:url" content="https://www.python.org/events/python-events/">

    <link rel="author" href="/static/humans.txt">

    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"
          href="https://www.python.org/dev/peps/peps.rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"
          href="https://www.python.org/jobs/feed/rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"
          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">
    <link rel="alternate" type="application/rss+xml" title="Python Insider"
          href="https://feeds.feedburner.com/PythonInsider">

    

    
    <script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>

    
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
    
</head>

<body class="python events default-page">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">

                
                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>

                
                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>

                

<ul class="menu" role="tree">
    
    <li class="python-meta ">
        <a href="/" title="The Python Programming Language" >Python</a>
    </li>
    
    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>
    
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>
    
    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>
    </li>
    
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>
    
    <li class="shop-meta ">
        <a href="/community/" title="Python Community" >Community</a>
    </li>
    
</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar-container do-not-print">
                    <a href="/psf/donations/" class="donate-button">Donate</a>
                    <div class="options-bar">
                        
                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                            <fieldset title="Search Python.org">

                                <span aria-hidden="true" class="icon-search"></span>

                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                    GO
                                </button>

                                
                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                            </fieldset>
                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div><div class="winkwink-nudgenudge">
                            <ul class="navigation menu" aria-label="Social Media Navigation">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger">Socialize</a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a href="https://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a href="https://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                        <span data-html-include="/authenticated"></span>
                    </div><!-- end options-bar -->
                </div>

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">
                    
                        
<ul class="navigation menu" role="menubar" aria-label="Main Navigation">
  
    
    
    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    
    
    
  
</ul>

                    
                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->
                    
    

                </div>

                
                

             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content with-right-sidebar" role="main">

                    
                    

                    

                    

        
        <header class="article-header">
            <h3>from the Python Events Calendar</h3>
        </header>
        

        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                
                <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/824/">PyCon Odessa</a></h3>
                        <p>
                            
                            
<time datetime="2019-03-16T07:00:00+00:00">16 March<span class="say-no-more"> 2019</span> 7am UTC – 5pm UTC</time>

                            

                            
                            <span class="event-location">BC «Solnechnyiy», 5, Sonyachna St., Odessa, Ukraine</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/832/">IndyPy Automate Conf 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-03-22T00:00:00+00:00">22 March<span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Indiana, USA</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/782/">PyCon SK 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-03-22T00:00:00+00:00">22 March &ndash; 24 March <span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Bratislava, Slovakia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/805/">Moscow Python Conf++ 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-04-05T00:00:00+00:00">05 April<span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Moscow, Russia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/817/">DjangoCon Europe 2019</a></h3>
                        <p>
                            
                            
<time datetime="2019-04-10T00:00:00+00:00">10 April &ndash; 14 April <span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">Copenhagen, Denmark</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/789/">PythonCamp 2019 - Cologne</a></h3>
                        <p>
                            
                            
<time datetime="2019-04-13T00:00:00+00:00">13 April &ndash; 14 April <span class="say-no-more"> 2019</span></time>

                            

                            
                            <span class="event-location">GFU Cyrus AG, Am Grauen Stein 27,,51105 Köln, Germany</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>

            
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/807/">PyCon APAC 2019</a></h3>
                    <p>
                        
                        
<time datetime="2019-02-23T00:00:00+00:00">23 Feb. &ndash; 24 Feb. <span class="say-no-more"> 2019</span></time>

                        

                        
                        <span class="event-location">iACADEMY, Nexus Campus, Makati City, Philippines</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/757/">PyCascades 2019</a></h3>
                    <p>
                        
                        
<time datetime="2019-02-23T00:00:00+00:00">23 Feb. &ndash; 24 Feb. <span class="say-no-more"> 2019</span></time>

                        

                        
                        <span class="event-location">Seattle, Washington, USA</span>
                        
                    </p>
                </li>
                
            </ul>
            
        </div>


                </section>

                
                

                
    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">
                
                
                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>
                
            </ul>
            
            <h2 class="widget-title">Python Events Calendars</h2>

<br/>

<p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>

<p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>

<p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>

<p>Thank you.</p>

	    </div>

        

        

    </aside>



            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">

                    
                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>

                    

<ul class="sitemap navigation menu do-not-print" role="tree" id="container">
    
    <li class="tier-1 element-1">
        <a href="/about/" >About</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-5">
        <a href="/success-stories/" title="success-stories">Success Stories</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/news/security/" title="">Report a Security Issue</a></li>
    
</ul>

        
    </li>
    
</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>
                    

                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">
                    
                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2019.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                            &nbsp;<span class="pre"><a href="/psf/sponsorship/sponsors/#heroku">Powered by Heroku</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->

    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>
    <script src="/static/js/libs/html-includes.js"></script>

    <script type="text/javascript" src="/static/js/main-min.640b6eeadc67.js" charset="utf-8"></script>
    

    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.aede07d08d8f.js" charset="utf-8"></script>
    
    
    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.c3860be1d290.js" charset="utf-8"></script>
    
    
    <![endif]-->

    

    
    

</body>
</html>
''')
