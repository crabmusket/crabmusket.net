from collections import namedtuple
import os

def main():
    prefix = 'hh'
    username = os.environ['PRIVATE_AUTH_USERNAME']
    password = os.environ['PRIVATE_AUTH_PASSWORD']
    items = [render_item(prefix = prefix, username = username, password = password, **details._asdict()) for details in episodes]
    print(render_atom(items))

def render_atom(items, **kwargs):
    return atom_template.format(items = '\n'.join(items), **kwargs)

def render_item(**kwargs):
    size = os.stat('./{prefix}/{index}.mp3'.format(**kwargs)).st_size
    url = 'https://{username}:{password}@crabmusket.net/dc/{prefix}/{index}.mp3'.format(**kwargs)
    return item_template.format(size = size, url = url, **kwargs)

Episode = namedtuple('Episode', 'index, title, description, published, duration')

episodes = [
    Episode(
        index = 34,
        title = 'Death Throes of the Republic I',
        description = 'The wars which elevate Rome to superpower status also sow the seed for the downfall of its political system. Money, slaves, ambition, political stalemate and class warfare prove to be a toxic, bloody mix',
        published = 'Sun, 27 Jun 2010 11:25:00 CET',
        duration = '01:22:22',
    ),
    Episode(
        index = 35,
        title = 'Death Throes of the Republic II',
        description = 'Disaster threatens the Republic, but the cure might be worse than the disease. “The Dan Carlin version” of this story continues with ambition-addict Marius dominating the story and Plutarch dominating the sources.',
        published = 'Sun, 29 Aug 2010 11:25:00 CET',
        duration = '01:35:15',
    ),
    Episode(
        index = 36,
        title = 'Death Throes of the Republic III',
        description = 'Rome’s political violence expands in intensity from riots and assassinations to outright war as the hyper-ambitious generals Marius and Sulla tear the Republic and its constitution apart vying for power and glory.',
        published = 'Sat, 29 Oct 2010 11:25:00 CET',
        duration = '01:37:47',
    ),
]

atom_template = '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" media="screen" href="/~d/styles/rss2enclosuresfull.xsl"?>
<?xml-stylesheet type="text/css" media="screen" href="http://feeds.feedburner.com/~d/styles/itemcontent.css"?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title>Dan Carlin's Hardcore History Archive</title>
    <description>Was Alexander the Great as bad a person as Hitler? What was the greatest army of all time? Which U.S. President was the worst? Hardcore History discusses the issues and questions history fans love.</description>
    <itunes:summary>In "Hardcore History" the very unconventional Dan Carlin takes his "Martian", outside-the-box way of thinking and applies it to the past. Was Alexander the Great as bad a person as Adolf Hitler? What would Apaches with modern weapons be like? Will our modern civilization ever fall like civilizations from past eras? This is a difficult-to-classify show that has a rather sharp edge. It's not for everyone. But the innovative style and approach has made "Dan Carlin's Hardcore History" a New Media hit. </itunes:summary>
    <itunes:subtitle>Was Alexander the Great as bad a person as Hitler? What was the greatest army of all time? Which U.S. President was the worst? Hardcore History discusses the issues and questions history fans love.</itunes:subtitle>
    <link>https://github.com/avar/private-dan-carlin-hardcore-history-podcast-feed</link>
    <pubDate>Mon, 29 Dec 2014 22:24:12 PST</pubDate>
    <language>en-us</language>

    <managingEditor>dan\@dancarlin.com (Dan Carlin)</managingEditor>
    <webMaster>dan\@dancarlin.com (Dan Carlin)</webMaster>

    <itunes:author>Dan Carlin</itunes:author>
    <copyright>dancarlin.com</copyright>
    <itunes:image href="https://raw.githubusercontent.com/avar/private-dan-carlin-hardcore-history-podcast-feed/master/static/DC_HH_iTunes_Gray_180.jpg" />
    <image>
        <url>https://raw.githubusercontent.com/avar/private-dan-carlin-hardcore-history-podcast-feed/master/static/DC_HH_iTunes_Gray_180.jpg</url>
        <link>https://github.com/avar/private-dan-carlin-hardcore-history-podcast-feed</link>
        <title>Dan Carlin's Hardcore History Archive</title>
    </image>
    <itunes:owner>
      <itunes:name>Dan Carlin's Hardcore History</itunes:name>
      <itunes:email>dan\@dancarlin.com </itunes:email>
    </itunes:owner>
    <itunes:keywords>History, Military, War, Ancient, Archaeology, Classics, Carlin</itunes:keywords>
    <itunes:category text="Society &amp; Culture">
      <itunes:category text="History" />
    </itunes:category>
    <itunes:explicit>no</itunes:explicit>
    <atom10:link xmlns:atom10="http://www.w3.org/2005/Atom" rel="self" type="application/rss+xml" href="$url_prefix/podcast.atom" />
    <feedburner:info xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0" uri="dancarlin/history" />
    <atom10:link xmlns:atom10="http://www.w3.org/2005/Atom" rel="hub" href="http://pubsubhubbub.appspot.com/" />
    {items}
  </channel>
</rss>
'''

item_template = '''<item>
      <title>Show {index}: {title}</title>
      <guid>{url}</guid>
      <description>{description}</description>
      <link>http://www.dancarlin.com</link>
      <pubDate>{published}</pubDate>
      <enclosure url="{url}" length="{size}" type="audio/mpeg" />
      <itunes:duration>{duration}</itunes:duration>
    </item>'''

if __name__ == '__main__':
    main()
