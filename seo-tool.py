''' SEO TOOL
Tool that reads from CSV, structures relevant content 
in various configurations to look fresh to the google
search crawler and creates html files with structured
names to rank higher


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

We will then move all of these files to the server of 
the mirror site in a folder titled as the state name 
so the eventual URL will be something like:
classicrooftiles.com/california/temecula-used-roof-tile.html
which will have a 307 redirect to the home page of that 
site. That home page will be built so that it looks 
identical to the primary site and all links redirect 
to the main site classicrooftile.com so that, on the
mirror site, the link to the 'About Us' page will link
to classicrooftile.com/about-us rather than 
classicrooftiles.com/about-us
'''