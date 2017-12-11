import fresh_tomatoes
import media

#instances of the movie class: 
brave = media.Movie("Brave",
			"Determined to make her own path in life, Princess Merida defies a custom that brings chaos to her kingdom. Granted one wish, Merida must rely on her bravery and her archery skills to undo a beastly curse.",
			"images/brave.jpg",
			"https://www.youtube.com/watch?v=TEHWDA_6e3M")

bridesmaids = media.Movie("Bridesmaids",
			"Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
			"images/bridesmaids.jpg",
			"https://www.youtube.com/watch?v=FNppLrmdyug")

league = media.Movie("A League Of Their Own",
			"A women's baseball league in the 1940s",
			"https://images-na.ssl-images-amazon.com/images/M/MV5BODliMGQ1YzEtM2VhZi00MTU5LTllYTUtY2M3MDdjOTE4OGZlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
			"https://www.youtube.com/watch?v=WcN392H2jx0")

contact = media.Movie("Contact",
			"Dr. Ellie Arroway, after years of searching, finds conclusive radio proof of extraterrestrial life",
			"images/contact.jpg",
			"https://www.youtube.com/watch?v=d9C2cF3KvP8")

arrival = media.Movie("Arrival",
			"When twelve mysterious spacecrafts appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors.",
			"images/arrival.jpg",
			"https://www.youtube.com/watch?v=tFMo3UJ4B4g")

mad_max = media.Movie("Madmax",
			"A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
			"images/madmax.jpg",
			"https://www.youtube.com/watch?v=hEJnMQG9ev8")

movies=[brave, bridesmaids, league, contact, arrival, mad_max]
fresh_tomatoes.open_movies_page(movies)