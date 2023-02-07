from models import *
# Catergories
cat_news = Category(name = 'News')
cat_sport = Category(name = 'Sport')
cat_buissnes = Category(name = 'Buissnes')
cat_culture = Category(name = 'Culture')
cat_game_news = Category(name = 'Game News')
# Users
user_admin = User(fullname = 'Admin', username = 'Admin', email='admin@gmail.com', password='123', admin_rights = 2, category =[1,2,3,4,5] )
user_editor1 = User(fullname = 'Emily Taylor', username = 'emilytaylor', email='editor1@gmail.com', password='123', admin_rights = 1, category=[1,2])
user_editor2 = User(fullname = 'Matthew Rodriguez', username = 'matthewr', email='editor2@gmail.com', password='123', admin_rights = 1, category= [1, 3, 4, 5])
user_user1 = User(fullname = 'Olivia Hernandez', username = 'oliviah', email='user1@gmail.com', password='123', category = [1,5])
user_user2 = User(fullname = 'James Green', username = 'jamesg', email='user2@gmail.com', password='123', category = [2,3,4])

# Articles aka post

# News Article
art_news_1 = Article(title='NASA Successfully Launches New Mars Rover Mission', image_of_article='NASA Successfully Launches New Mars Rover Mission.png', subtitle='Perseverance Rover to Explore Red Planet and Search for Signs of Life', content='''NASA has successfully launched its latest mission to Mars, sending the Perseverance Rover on its journey to explore the Red Planet and search for signs of life. The launch, which took place earlier today, was a historic moment for NASA and a major milestone in the quest to understand the universe.

The Perseverance Rover is equipped with a suite of advanced scientific instruments, including a state-of-the-art microphone, which will allow scientists to listen to the sounds of Mars for the first time. The rover will also collect rock and soil samples, which will be returned to Earth in the future for further analysis.

"This is a major moment for NASA and for the world," said a spokesperson for the space agency. "The Perseverance Rover will allow us to explore Mars like never before and to search for signs of life, which is one of the biggest questions in science."

The mission is expected to take several months to reach Mars and will last for at least one Martian year, which is equivalent to about two Earth years. During this time, the Perseverance Rover will explore the planet and collect data, which will help scientists to better understand Mars and its history.

The successful launch of the Perseverance Rover is a testament to the ingenuity and determination of the human spirit, and is sure to inspire future generations of scientists and explorers.''', source='Washington Post', category_id= 1, user_id=2 )


art_news_2 = Article(title='Breakthrough Discovery in Cancer Research', image_of_article='Breakthrough Discovery in Cancer Research.png', subtitle='New Therapy Shown to be Highly Effective in Treating Advanced Cancers', content='''A major breakthrough has been made in the field of cancer research, with a new therapy shown to be highly effective in treating advanced cancers. The therapy, developed by a leading research institution, uses a unique approach to target cancer cells, effectively killing them and shrinking tumors.

The results of clinical trials have been overwhelmingly positive, with a significant number of patients showing remarkable improvement. In many cases, the therapy has been able to halt the progression of the cancer and even shrink tumors, offering hope to patients who have run out of other treatment options.

"This is a truly groundbreaking discovery and has the potential to change the way we treat cancer," said a leading oncologist. "This therapy offers new hope to patients who have been told that there are no more options, and we are excited to see where this takes us in the future."

The therapy is still in the early stages of development and more research is needed to fully understand its potential, but the results so far are extremely promising. The research institution is working closely with pharmaceutical companies to bring the therapy to market as quickly as possible, so that patients can benefit from this breakthrough discovery.

This is a momentous occasion in the fight against cancer and marks a significant step forward in the search for a cure.''', source='The Guardian', category_id= 1, user_id=3 )

art_news_3 = Article(title='China Launches its First Mars Exploration Mission', image_of_article='China Launches its First Mars Exploration Mission.png', subtitle='Tianwen-1 Rover to Study Martian Geology and Climate', content='''China has made history today with the successful launch of its first Mars exploration mission, the Tianwen-1 Rover. The mission aims to study the Martian geology and climate and to gather data that will help scientists to better understand the Red Planet.

The Tianwen-1 Rover is equipped with a suite of advanced scientific instruments, including high-resolution cameras, spectrometers, and a radar system that will be used to map the Martian surface and search for signs of water. The data collected by the rover will be used to inform future missions to Mars and will be shared with the international scientific community.

"This is a proud moment for China and for the world," said a spokesperson for the Chinese National Space Administration. "The Tianwen-1 Rover will allow us to explore Mars like never before and to gather important data that will help us to better understand this fascinating planet."

The mission is expected to take several months to reach Mars and will last for at least one Martian year, which is equivalent to about two Earth years. During this time, the Tianwen-1 Rover will explore the planet and collect data, which will help scientists to better understand Mars and its history.

The successful launch of the Tianwen-1 Rover marks a major milestone in China's space program and is a testament to the country's technological advancements and commitment to scientific exploration.''', source='Xinhua News', category_id= 1, user_id=4 )

art_news_4 = Article(title='Major Breakthrough in Quantum Computing Achieved', image_of_article='Major Breakthrough in Quantum Computing Achieved.png', subtitle='New Technique Allows for Faster, More Efficient Computation', content='''A major breakthrough has been made in the field of quantum computing, with scientists developing a new technique that allows for faster, more efficient computation. The technique, which uses a unique approach to quantum communication, has the potential to revolutionize the field of computing and have far-reaching implications for a range of industries.

The new technique has been tested in laboratory conditions and has shown remarkable results, with computation times reduced by orders of magnitude. This breakthrough has the potential to revolutionize the field of quantum computing and bring it closer to practical applications in fields such as cryptography, medicine, and finance.

"This is a truly groundbreaking discovery and has the potential to change the way we think about computing," said a leading quantum computer scientist. "We are only just beginning to scratch the surface of what is possible with quantum computing, and this new technique opens up a world of new possibilities."

The discovery is still in the early stages of development and more research is needed to fully understand its potential, but the results so far are extremely promising. The team of scientists is working closely with industry partners to bring this technology to market as quickly as possible, so that it can be used to tackle some of the world's biggest challenges.

This is a major step forward in the field of quantum computing and marks a significant moment in the history of computing.''', source='Science Daily', category_id= 1, user_id=4 )
# List of news article
# 
# 
news_all = [art_news_1, art_news_2, art_news_3, art_news_4]

# Sport Article
art_sport_1 = Article(title='Lakers clinch NBA Championship with Game 6 Win', image_of_article='Lakers clinch NBA Championship with Game 6 Win.png', subtitle='LeBron James Named Finals MVP with 35-Point Performance', content='''The Los Angeles Lakers are champions once again, clinching the NBA title with a 106-93 win over the Miami Heat in Game 6 of the NBA Finals. LeBron James led the way for the Lakers, putting up a 35-point performance that earned him Finals MVP honors for the fourth time in his career.

The Lakers dominated from the opening tip, jumping out to a double-digit lead in the first quarter and never looking back. James was a force on both ends of the floor, showing his mastery of the game and proving why he is widely considered one of the greatest players of all time.

"LeBron was simply incredible tonight," said Lakers head coach Frank Vogel. "He set the tone for us on both ends of the floor and showed why he's the best player in the world."

The win marks the Lakers' 17th NBA championship in franchise history, tying them with the Boston Celtics for the most all-time. It also marks James' fourth championship, putting him one step closer to his ultimate goal of catching Michael Jordan as the greatest player of all time.

The Lakers' championship win caps off a season unlike any other, with the league playing through the pandemic and facing a host of new challenges. But through it all, the Lakers proved to be the best team in the league, and their championship is a testament to their talent, perseverance, and determination.''', source='ESPN', category_id= 2, user_id=2 )

art_sport_2 = Article(title='Serena Williams Wins 23rd Grand Slam Title at Australian Open', image_of_article='Serena Williams Wins 23rd Grand Slam Title at Australian Open.png', subtitle='Defeats Jessica Pegula in Straight Sets to Claim Record-Breaking Victory', content='''Serena Williams made history today at the Australian Open, winning her 23rd Grand Slam title with a straight-sets victory over Jessica Pegula. The win breaks the all-time record for the most Grand Slam singles titles won in the Open Era, which began in 1968.

Williams dominated from start to finish, showing why she is still one of the greatest players in the game. She powered her way through the match, using her signature serve and forehand to overpower her opponent.

"I'm just so proud of myself and what I've been able to accomplish in my career," said Williams after the match. "Winning this title means so much to me, and I'm so grateful for the support of my family and fans."

The victory marks Williams' seventh Australian Open title and her first Grand Slam victory since giving birth to her daughter in 2017. It also puts her one step closer to Margaret Court's all-time record of 24 Grand Slam singles titles.

The win is a testament to Williams' talent, determination, and resilience, and it solidifies her place as one of the greatest tennis players of all time. It is a moment that will be remembered for years to come and a true tribute to Williams' incredible career.''', source='The New York Times', category_id= 2, user_id=5 )

art_sport_3 = Article(title='Usain Bolt Breaks World Record in 100m Sprint at Beijing Olympics', image_of_article='Usain Bolt Breaks World Record in 100m Sprint at Beijing Olympics.png', subtitle='Jamaican Sprinter Sets New Mark with Time of 9.69 Seconds', content='''Jamaican sprinter Usain Bolt made history today at the Beijing Olympics, breaking the world record in the men's 100m sprint with a time of 9.69 seconds. The previous record, set by American sprinter Tyson Gay, stood at 9.71 seconds.

Bolt dominated the race from start to finish, using his powerful stride and explosive speed to pull away from the field. He crossed the finish line with his arms raised in triumph, a look of disbelief on his face as the crowd erupted in cheers.

"I can't believe I just broke the world record," Bolt said after the race. "This is a dream come true for me and I'm just so happy to be here representing Jamaica."

The victory was a dominant display of Bolt's raw speed and athleticism, and it cemented his place as one of the greatest sprinters of all time. He went on to win three more gold medals at the Beijing Olympics, solidifying his legacy as a world-class sprinter.

The world record-breaking run was a moment that will be remembered for years to come, and it stands as a testament to Bolt's incredible talent and determination.''', source='NBA News', category_id= 2, user_id=5 )

art_sport_4 = Article(title='Tiger Woods Wins Fifth Masters Title with Dominating Performance', image_of_article='Tiger Woods Wins Fifth Masters Title with Dominating Performance.png', subtitle='Wins Augusta National in Stunning Comeback Victory', content='''Tiger Woods made a stunning comeback today at the Masters, winning his fifth green jacket with a dominant performance at Augusta National. Woods, who had been struggling with injuries and personal issues for years, put together four solid rounds to claim the title and silence his doubters.

The victory was a testament to Woods' perseverance and determination, as he worked tirelessly to return to the top of his game. He hit big shots and made clutch putts, showing the form that once made him one of the most feared players in the game.

"I'm just so proud of myself and what I've been able to accomplish," Woods said after the victory. "Winning this tournament means everything to me and I'm just so grateful to be back on top."

The win was Woods' first major championship victory in over a decade and it sparked joy and excitement among fans around the world. It also marked a triumphant return to the top of the game for Woods, who has spent the last several years battling injuries and personal demons.

The victory was a moment that will be remembered for years to come, and it stands as a testament to Woods' talent, resilience, and determination.''', source='CNN Sports', category_id= 2, user_id=5 )

# List of news article
# 
# 
sport_all = [art_sport_1, art_sport_2, art_sport_3, art_sport_4]

# Buissnes Article
art_buissnes_1 = Article(title='Amazon Acquires MGM for $8.45 Billion', image_of_article='Amazon Acquires MGM for $8.45 Billion.png', subtitle='Online Retail Giant Continues Expansion into Media and Entertainment Industry', content='''Amazon made a major move into the media and entertainment industry today, acquiring MGM for $8.45 billion. The online retail giant has been expanding into new industries and markets in recent years, and the acquisition of MGM will give them a valuable library of film and television content.

The acquisition is a significant step for Amazon, as they look to compete with streaming giants like Netflix and Disney. MGM has a vast library of content, including popular franchises like James Bond and The Hobbit, which will be a valuable asset for Amazon as they look to build out their streaming services.

"This acquisition is a natural next step for us as we continue to expand into new areas of media and entertainment," said Jeff Bezos, CEO of Amazon. "MGM has a rich history and a wealth of content, and we're excited to bring that to our customers."

The acquisition is part of Amazon's larger strategy to dominate the streaming market, and it will give them a valuable new source of content as they compete with other major players in the industry. The future of Amazon's media and entertainment offerings looks bright, and this acquisition is a strong step forward for the company.''', source='The Wall Street Journal', category_id= 3, user_id=5 )

art_buissnes_2 = Article(title='Tesla Announces Plan to Build Factory in Texas', image_of_article='Tesla Announces Plan to Build Factory in Texas.png', subtitle='Electric Automaker Expands Production to Meet Growing Demand', content='''Tesla announced plans to build a new factory in Texas today, in a move to expand production and meet growing demand for their electric vehicles. The new factory will be located in the Austin area and will create thousands of new jobs, while providing a significant boost to the local economy.

The decision to build in Texas is part of Tesla's larger strategy to increase production and meet the growing demand for their vehicles. The company has seen tremendous success in recent years, as consumers embrace electric vehicles and seek more sustainable transportation options.

"Texas has always been a key market for us, and this new factory will allow us to better serve our customers and meet the growing demand for our vehicles," said Elon Musk, CEO of Tesla. "We're thrilled to be bringing jobs and investment to the state, and we're excited to continue our growth in this important market."

The new factory will be a major investment for Tesla, and it will allow the company to continue their growth and expansion in the years to come. The future of electric vehicles looks bright, and Tesla is well-positioned to lead the way as the industry continues to grow and evolve.''', source='The New York Times', category_id= 3, user_id=3)

art_buissnes_3 = Article(title='Apple Launches New iPhone with Improved Features and Design', image_of_article='Apple Launches New iPhone with Improved Features and Design.png', subtitle='Leading Tech Giant Unveils Latest Addition to Popular Smartphone Line', content='''Apple launched a new iPhone today, showcasing improved features and a sleek new design. The latest addition to the popular smartphone line has been highly anticipated, and it did not disappoint with its upgraded camera, larger screen, and powerful performance.

The new iPhone is a testament to Apple's commitment to innovation and their commitment to producing the best devices for their customers. The company has always been at the forefront of technology, and the new iPhone is no exception.

"We're always working to push the boundaries of what's possible with our devices," said Tim Cook, CEO of Apple. "The new iPhone is the best iPhone we've ever made, with features and capabilities that our customers are going to love. We're thrilled to bring this new device to market and we're confident that it's going to set a new standard in the industry."

The new iPhone is already generating a lot of buzz and excitement among consumers, and it is expected to be a major hit for Apple. The company's innovative approach and attention to detail has made them a leader in the smartphone market, and the new iPhone is poised to continue that tradition.

The new iPhone will be available for pre-order later this week, and it is expected to hit stores next month. With its improved features and sleek design, it is sure to be a must-have device for tech enthusiasts and Apple fans alike.''', source='CNBC', category_id= 3, user_id=3)

art_buissnes_4 = Article(title='Netflix Stock Rises After Strong Earnings Report', image_of_article='Netflix Stock Rises After Strong Earnings Report.png', subtitle='Streaming Giant Continues to Grow and Expand Despite Competition', content='''Netflix's stock rose today after the company released a strong earnings report, showing continued growth and expansion despite intense competition in the streaming market. The company added millions of new subscribers in the past quarter, and its revenue and profits both exceeded expectations.

The strong earnings report is a testament to Netflix's continued dominance in the streaming market, and it highlights their ability to succeed and grow despite intense competition. The company has been expanding rapidly in recent years, investing in new content and new markets, and these efforts are paying off.

"We're thrilled with our performance this quarter, and we're confident in our ability to continue growing and expanding in the years to come," said Reed Hastings, CEO of Netflix. "We're seeing strong demand for our content, and we're well-positioned to continue delivering great experiences to our customers."

The future of Netflix looks bright, and the company's strong earnings report is a clear sign of their continued success and growth. The streaming giant is poised to remain a major player in the industry, and their continued expansion and success is a testament to their innovative approach and commitment to delivering great experiences to their customers.''', source='Forbes', category_id= 3, user_id=3)

# List of buissnes article
# 
# 
buissnes_all = [art_buissnes_1, art_buissnes_2, art_buissnes_3, art_buissnes_4]

# culture Article
art_culture_1 = Article(title='The Rise of Graffiti Art: A Look at the History and Evolution', image_of_article='The Rise of Graffiti Art_ A Look at the History and Evolution.png', subtitle='From Street Art to Gallery Displays, Graffiti is Gaining Recognition as a Form of Fine Art', content='''Graffiti art has come a long way since its origins in the late 1960s and 1970s as a form of protest and rebellion. Today, it is gaining recognition as a legitimate form of fine art, with many graffiti artists being sought after for commissions and exhibitions in galleries around the world.

The evolution of graffiti can be traced back to the early days of the graffiti movement in New York City, where artists used the city's walls and trains as their canvas. Over time, graffiti has evolved and expanded, incorporating new styles and techniques, and gaining recognition as a legitimate form of art.

Now, graffiti is featured in galleries and exhibitions, and its impact can be seen in the world of advertising, fashion, and even music. Graffiti artists are also collaborating with brands and businesses, using their unique style and perspective to create eye-catching and thought-provoking pieces.

"Graffiti art has come a long way since its origins as a form of protest," says Jenny Smith, a curator at the Museum of Street Art in New York. "Today, it is a respected and valued form of fine art, and its impact can be seen in many different areas of society. The recognition that graffiti is receiving is a testament to the skill, creativity, and vision of the artists who are pushing the boundaries of what is possible.''', source='The Art Newspaper', category_id= 4, user_id=5 )

art_culture_2 = Article(title='The Return of Vinyl Records: A Look at the Resurgence of a Classic Format', image_of_article='The Return of Vinyl Records_ A Look at the Resurgence of a Classic Format.png', subtitle='From Collectors to Casual Listeners, Vinyl is Making a Comeback in the Digital Age', content='''Vinyl records were once considered a thing of the past, but they are now making a resurgence in the digital age. From collectors to casual listeners, more and more people are discovering the joys of vinyl and the warm, rich sound that it provides.

The return of vinyl can be traced back to the early 2000s, when a small but dedicated group of audiophiles and music lovers began to rediscover the format. Over time, this movement has grown, and today vinyl is more popular than ever.

Vinyl records offer a unique listening experience that cannot be replicated by digital formats. The tactile experience of handling a record, the artwork on the cover, and the warmth of the sound all contribute to the appeal of vinyl.

"Vinyl records offer a level of listening experience that simply cannot be matched by digital formats," says John Smith, a vinyl collector and enthusiast. "It's about more than just the sound – it's about the physical experience and the connection that you feel with the music."

The return of vinyl is a testament to the timeless appeal of this classic format, and it is a reminder that in an age of digital music, there is still a place for the warmth and richness of analog sound.''', source='Rolling Stone', category_id= 4, user_id=5 )

art_culture_3 = Article(title='Exploring the World of Traditional Folk Music', image_of_article='Exploring the World of Traditional Folk Music.png', subtitle='Preserving the Rich Cultural Heritage of Folk Music Around the Globe', content='''Folk music has been an integral part of cultural heritage for centuries, providing a window into the history, traditions, and stories of communities around the world. From the American folk revival of the 1960s to the contemporary folk scene, this genre of music continues to captivate audiences and preserve the rich cultural heritage of different communities.

Folk music is characterized by its use of traditional instruments, such as the acoustic guitar, fiddle, and banjo, as well as its emphasis on storytelling and the celebration of cultural traditions. This genre of music often reflects the struggles, hopes, and dreams of a community, and it provides a powerful means of expression for people from all walks of life.

"Folk music is about more than just music – it's about preserving cultural heritage and telling the stories of a community," says Michael Green, a folk musician and historian. "It's about connecting with our roots, and it provides a powerful means of expression for people from all walks of life."

Whether you're a fan of traditional folk music or contemporary folk, there is no denying the power and appeal of this genre. So if you're looking to explore the world of folk music, there has never been a better time to dive in and experience its rich cultural heritage for yourself.''', source='Folk Life Magazine', category_id= 4, user_id=3 )

art_culture_4 = Article(title='The Art of Poi: A Look at the History and Evolution of this Unique Performance Art', image_of_article='The Art of Poi A Look at the History and Evolution of this Unique Performance Art.png', subtitle='From Fire Dancing to LED Light Performances, Poi Continues to Evolve and Inspire', content='''Poi is a unique performance art that has its roots in traditional Maori culture in New Zealand. Today, this art form has evolved and expanded, incorporating new techniques, styles, and materials to create stunning performances that captivate audiences around the world.

The art of poi involves swinging one or two balls connected by ropes in a variety of patterns and techniques, creating a mesmerizing visual display. Traditionally, poi was performed with fire, but today, many performers use LED lights to create stunning light displays.

Poi has come a long way since its origins in Maori culture, but it continues to evolve and inspire. Today, poi is a popular performance art around the world, with performers using their skills to create mesmerizing displays that captivate audiences and push the boundaries of what is possible.

"Poi is a truly unique and beautiful art form," says Laura Jenkins, a poi performer and instructor. "It's about more than just swinging balls – it's about the flow, the movement, and the connection that you feel with the audience. Whether you're a seasoned poi performer or just getting started, there is something truly special about this art form.''', source='The Performing Arts Journal', category_id= 4, user_id=3 )

# List of culture article
# 
# 
culture_all = [art_culture_1, art_culture_2, art_culture_3, art_culture_4]

# game news Article
art_game_1 = Article(title='The Rise of Esports: An Overview of the Fast-Growing Gaming Industry', image_of_article='The Rise of Esports_ An Overview of the Fast-Growing Gaming Industry.png', subtitle='From Competitive Tournaments to Live Streams, Esports is Taking the World by Storm', content='''Esports has come a long way since its humble beginnings as a niche hobby for a small group of gamers. Today, this fast-growing industry has become a global phenomenon, with millions of players and fans participating in competitive tournaments, live streams, and other events.

Esports has been fueled by the rapid growth of the gaming industry and the increasing popularity of online gaming. With the rise of fast and reliable internet connections, more and more people are able to connect and compete in real-time, creating a thriving community of gamers around the world.

But esports is about more than just gaming – it's about competition, strategy, and teamwork. Whether you're a professional gamer or just a casual player, esports provides a unique and exciting way to connect with others and challenge yourself.

"Esports is the future of gaming," says James Taylor, an esports commentator and analyst. "From the high-stakes tournaments to the live streams and the community of players, it's a truly thrilling and engaging experience that is taking the world by storm.''', source='Gaming News Daily', category_id= 5, user_id=4 )

art_game_2 = Article(title='The Evolution of Virtual Reality Gaming: A Look at the Past, Present, and Future of VR Gaming', image_of_article='The Evolution of Virtual Reality Gaming_ A Look at the Past, Present, and Future of VR Gaming.png', subtitle='From Early Adapters to Mainstream Adoption, VR Gaming is Changing the Way We Play', content='''Virtual reality gaming has come a long way since its early days as a futuristic technology only available to a select few. Today, VR gaming has become a mainstream phenomenon, with millions of players and fans experiencing the immersive and interactive worlds of virtual reality.

VR gaming has been driven by advances in technology, including the development of high-performance VR headsets and motion controllers. With these tools, players can now experience truly immersive and interactive gaming experiences, exploring new and exciting worlds in a way that was previously impossible.

But VR gaming is more than just technology – it's about storytelling, creativity, and imagination. Whether you're a seasoned VR gamer or just starting out, there's a whole new world of gaming experiences waiting for you in virtual reality.

"Virtual reality gaming is the future of gaming," says Sarah Lee, a VR game developer and entrepreneur. "From the immersive experiences to the innovative game design, it's a truly exciting time to be a VR gamer. The future of VR gaming is bright, and I can't wait to see what the next generation of VR gamers will create.''', source='Virtual Reality Insider', category_id= 5, user_id=4 )

art_game_3 = Article(title='The Growth of Mobile Gaming: An Overview of the Mobile Gaming Revolution', image_of_article='The Growth of Mobile Gaming_ An Overview of the Mobile Gaming Revolution.png', subtitle='From Casual Gaming to Competitive Tournaments, Mobile Gaming is Taking Over the World', content='''Mobile gaming has exploded in recent years, becoming one of the most popular and fast-growing segments of the gaming industry. From casual games like Candy Crush and Angry Birds to more complex and competitive titles like PUBG and Fortnite, mobile gaming has something to offer for everyone.

The growth of mobile gaming has been fueled by the rise of smartphones and other mobile devices, which have made gaming accessible to millions of people around the world. With the ability to play games anytime, anywhere, mobile gaming has become an integral part of daily life for many people.

But mobile gaming is more than just a way to pass the time – it's a way to connect with friends, compete against other players, and challenge yourself. Whether you're a hardcore gamer or just looking for a way to relax and unwind, mobile gaming has something to offer.

"Mobile gaming is the future of gaming," says John Smith, a mobile game designer and entrepreneur. "From the convenience and accessibility to the competitive and social aspects, it's a truly exciting time to be a mobile gamer.''', source='Mobile Gaming Today', category_id= 5, user_id=4 )

art_game_4 = Article(title='The Future of Console Gaming: An Overview of the Next Generation of Gaming Consoles', image_of_article='The Future of Console Gaming_ An Overview of the Next Generation of Gaming Consoles.png', subtitle='From Next-Generation Hardware to Cutting-Edge Games, Console Gaming is Evolving Rapidly', content='''Console gaming is undergoing a rapid evolution, with new hardware and cutting-edge games pushing the boundaries of what's possible in gaming. From the latest Xbox and PlayStation consoles to the new generation of gaming PCs, the future of console gaming is looking brighter than ever.

The next generation of consoles is set to offer a new level of performance, with faster processing power, higher graphics quality, and improved gaming experiences. Whether you're a seasoned gamer or just starting out, the next generation of consoles is set to offer something for everyone.

But console gaming is more than just technology – it's about the games, the stories, and the experiences. Whether you're exploring a vast open world, battling against other players, or taking on challenging puzzles, console gaming offers a unique and exciting way to connect with others and challenge yourself.

"The future of console gaming is bright," says Tom Green, a console game developer and analyst. "From the latest hardware to the cutting-edge games, the next generation of console gaming is set to take the gaming world by storm.''', source='Console Gaming Weekly', category_id= 5, user_id=3 )
# List of game article
# 
# 
game_all = [art_game_1, art_game_2, art_game_3, art_game_4]
