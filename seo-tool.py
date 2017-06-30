''' Content Structuring Tool

Essentially, we will:
	- Create a CSV that has state, city, and keywords
	- Create a second domain very similar to the 
		primary that has a home page identical to
		the primary site
	- Create a local folder titled as the state name
	- Move that file to the server once the script
		has run


The tool will:
	- Read from a simple CSV
	- Pull in or take in some amount of content 
		(i.e. blog posts or whatever)
	- Restructure that content repeatedly so that it 
		doesnt appear as duplicate
	- Place that content into an html file
	- Title that file with the keywords from the CSV 
		and the city name i.e. keyword of 'used roof 
		tile' and city of 'temecula' becomes 
		temecula-used-roof-tile.html
	- Run all of this in a for loop that will repeat 
		the action for each keyword

'''


''' 
BRING IN THE DATA
'''

# Read from CSV and store data in variable
inputFile = open("seo-input.csv", "r")


# Create variables to hold city and state
# Ideally this section would be variables 
# to grab the relevant row from each table
# so that every city and keyword combo
# would run through the loop
city = inputFile.cell.a2
state = inputFile.cell.b2
# Create an array to hold the keywords
keywords = ([
		inputFile.cell.c2
		])





'''
CONTENT STRUCTURING
'''

htmlOpen = '''
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, intial-scale=1.0, maximum-scale=1.0">
	<meta name="description" content="">
	<meta name="robots" content="noodp">
	<link rel="canonical" href="">
	<meta property="og:locale" content="en_US">
	<meta property="og:type" content="website">
	<meta property="og:title" content="">
	<meta property="og:description" content="">
	<meta property="og:url" content="">
	<meta property="og:site_name" content="">
	<meta property="og:image" content="">
	
</head>
<body>
'''

htmlClose = '''
	<div>
	<div style="width:622px;height:401px;margin:0 auto"><div style="padding:10px"><iframe frameborder="0" height="401" marginheight="0" marginwidth="0" scrolling="no" src="//maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=STATE+CITY&amp;ie=UTF8&amp;z=12&amp;t=m&amp;iwloc=near&amp;output=embed" width="622"></iframe></div></div>
	</div>
	<div>
	<a href="http://www.showmyweather.com/" title="Show My Weather Forecast" onclick="window.open(this.href);return(false);"><script type="text/javascript" src="http://www.showmyweather.com/weather_widget.php?int=0&amp;type=js&amp;country=us&amp;state=STATE&amp;city=CITY&amp;smallicon=1&amp;current=1&amp;forecast=1&amp;background_color=ffffff&amp;color=1e1e1e&amp;width=300&amp;padding=20&amp;border_width=2&amp;border_color=1e1e1e&amp;font_size=14&amp;font_family=Verdana&amp;showicons=1&amp;measure=F&amp;d=2017-06-20"></script></a>	</div>
</body>
</html>
'''

content = # scraper tool here



def restructureContent(content):

	# restructuring tool here


	return htmlOpen + uniqueContent + htmlClose



def structureURL(city, keyword):

	kw = keyword
	hyphenKW = kw.replace(" ", "-")

	return city + '-' + hyphenKW



'''
CREATE HTML FILES
'''

for keyword in keywords:
	pageHTML = restructureContent()
	structuredURL = structureURL()

	newFile = open("%s.html" % structuredURL, 'w')
	newFile.writelines(pageHTML)
	newFile.close()
