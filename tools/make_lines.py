#!/usr/bin/env python3
"""The script, line by line → audio/lines.json (for the AI33 narrator) and script.md (readable).
Each entry: id, chapter, text (spoken, numbers as words), subs (caption lines, digits, one line each ≤ ~58 characters).
Told backwards: ten frames from 2012 to 1888, then a fast-forward. Every fact is in FACTS.md."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = 'elevenlabs_0dPqNXnhg2bmxQv1WKDp'   # Storyteller Oxley (AI33 Pro / ElevenLabs)
C = []
def L(ch, i, spoken, *subs): C.append((ch, i, spoken, list(subs)))

# ── hook ──
L('hook', 'h01', "On the nineteenth of January, twenty twelve, the company that taught America how to save its memories filed for bankruptcy.",
  "On 19 January 2012, the company that taught America", "how to save its memories filed for bankruptcy.")
L('hook', 'h02', "Eastman Kodak. Rochester, New York.", "Eastman Kodak. Rochester, New York.")
L('hook', 'h03', "At its peak, more than sixty thousand people in this one city worked for Kodak.",
  "At its peak, more than 60,000 people in this one city", "worked for Kodak.")
L('hook', 'h04', "In nineteen fifty, Rochester was home to three hundred thirty-two thousand people. By twenty twenty, it was two hundred eleven thousand.",
  "In 1950, Rochester was home to 332,488 people.", "By 2020, it was 211,328.")
L('hook', 'h05', "Most stories start at the beginning. Not this one.", "Most stories start at the beginning. Not this one.")
L('hook', 'h06', "Tonight we're going to do what Rochester did with every roll of film it ever made. We're going to rewind it.",
  "Tonight we're going to do what Rochester did", "with every roll of film it ever made.", "We're going to rewind it.")
L('hook', 'h07', "Ten frames, each one further back, until we reach a young bank clerk who believed anyone should be able to take a picture.",
  "Ten frames, each one further back,", "until we reach a young bank clerk who believed", "anyone should be able to take a picture.")
L('hook', 'h08', "And somewhere in the middle, we'll find the moment Kodak held the future in its hands.",
  "And somewhere in the middle, we'll find the moment", "Kodak held the future in its hands.")
L('hook', 'h09', "This is Mill Town.", "This is Mill Town.")

# ── frame 10 · 2012 ──
L('f10', 'a01', "Frame ten. Twenty twelve.", "Frame ten. 2012.")
L('f10', 'a02', "On Thursday, the nineteenth of January, Eastman Kodak asked a federal court in New York for protection under Chapter Eleven.",
  "On Thursday, 19 January, Eastman Kodak asked", "a federal court in New York for protection", "under Chapter 11.")
L('f10', 'a03', "It had lined up nine hundred and fifty million dollars from Citigroup to keep running, and it promised to keep paying its people.",
  "It had lined up $950 million from Citigroup to keep running,", "and it promised to keep paying its people.")
L('f10', 'a04', "In the Rochester area, about seven thousand people still worked for Kodak. Thirty years earlier, it had been more than sixty thousand.",
  "In the Rochester area, about 7,000 people still worked for Kodak.", "Thirty years earlier, it had been more than 60,000.")
L('f10', 'a05', "And then there were the retirees. Kodak had about thirty-eight thousand of them, and around half still lived in and around Rochester.",
  "And then there were the retirees.", "Kodak had about 38,000 of them,", "and around half still lived in and around Rochester.")
L('f10', 'a06', "They had given their working lives to a company that promised to look after them. Now their health coverage was on the table, in a bankruptcy court.",
  "They had given their working lives to a company", "that promised to look after them.", "Now their health coverage was on the table, in a bankruptcy court.")
L('f10', 'a07', "The news kept coming. In February, Kodak said it would stop making digital cameras altogether.",
  "The news kept coming. In February, Kodak said", "it would stop making digital cameras altogether.")
L('f10', 'a08', "A judge let it walk away from its name on the Hollywood theatre where the Oscars are held. By spring, the Kodak Theatre was the Dolby Theatre.",
  "A judge let it walk away from its name on the Hollywood theatre", "where the Oscars are held.", "By spring, the Kodak Theatre was the Dolby Theatre.")
L('f10', 'a09', "Kodak's online photo service, holding more than five billion family pictures, was sold for twenty-three point eight million dollars.",
  "Kodak's online photo service, holding more than", "five billion family pictures, was sold for $23.8 million.")
L('f10', 'a10', "That same spring, Facebook paid about a billion dollars for Instagram. An app for sharing photographs, with thirteen employees.",
  "That same spring, Facebook paid about $1 billion for Instagram.", "An app for sharing photographs, with 13 employees.")
L('f10', 'a11', "Kodak would come out of bankruptcy in twenty thirteen, much smaller, making printing plates, chemicals and film for industry. It's still in Rochester today.",
  "Kodak came out of bankruptcy in 2013, much smaller,", "making printing plates, chemicals and film for industry.", "It's still in Rochester today.")
L('f10', 'a12', "But how does more than sixty thousand become a few thousand? To understand that, we have to rewind.",
  "But how does more than 60,000 become a few thousand?", "To understand that, we have to rewind.")

# ── frame 9 · 2010 ──
L('f9', 'b01', "Frame nine. Twenty ten.", "Frame nine. 2010.")
L('f9', 'b02', "Parsons, Kansas. A town of about ten thousand people, in the southeast corner of the state.",
  "Parsons, Kansas. A town of about 10,000 people,", "in the southeast corner of the state.")
L('f9', 'b03', "There's a photo lab here called Dwayne's. By twenty ten, it was the last place on Earth that could develop one particular film.",
  "There's a photo lab here called Dwayne's.", "By 2010, it was the last place on Earth", "that could develop one particular film.")
L('f9', 'b04', "Kodachrome.", "Kodachrome.")
L('f9', 'b05', "Kodak had made it for seventy-four years. It was the film of National Geographic, of family vacations, of slide shows on the living-room wall.",
  "Kodak had made it for 74 years.", "It was the film of National Geographic, of family vacations,", "of slide shows on the living-room wall.")
L('f9', 'b06', "Its colours were famous for lasting. Kept in the dark, a Kodachrome slide could hold its colour for decades longer than most other films.",
  "Its colours were famous for lasting.", "Kept in the dark, a Kodachrome slide could hold its colour", "for decades longer than most other films.")
L('f9', 'b07', "But it was hard to develop. It needed its own long, complicated process, with its own chemicals, and only a few labs in the world ever ran it.",
  "But it was hard to develop.", "It needed its own long, complicated process,", "with its own chemicals,", "and only a few labs in the world ever ran it.")
L('f9', 'b08', "As people stopped shooting it, those labs closed, one by one. In two thousand nine, Kodak stopped making it.",
  "As people stopped shooting it, those labs closed, one by one.", "In 2009, Kodak stopped making it.")
L('f9', 'b09', "Kodak gave one of the very last rolls to the photographer Steve McCurry, who had made some of his most famous pictures on it. He shot it, and sent it to Parsons.",
  "Kodak gave one of the very last rolls to the photographer", "Steve McCurry, who had made some of his most famous", "pictures on it. He shot it, and sent it to Parsons.")
L('f9', 'b10', "And then everyone else sent theirs. Rolls came in from all over the country, and from overseas. Some had sat in drawers for years.",
  "And then everyone else sent theirs.", "Rolls came in from all over the country, and from overseas.", "Some had sat in drawers for years.")
L('f9', 'b11', "On the thirtieth of December, twenty ten, Dwayne's took in its last rolls. The machine ran its final batch that January.",
  "On 30 December 2010, Dwayne's took in its last rolls.", "The machine ran its final batch that January.")
L('f9', 'b12', "And when it stopped, every roll of Kodachrome still sitting in a camera somewhere stayed there, undeveloped, for good.",
  "And when it stopped, every roll of Kodachrome", "still sitting in a camera somewhere stayed there,", "undeveloped, for good.")
L('f9', 'b13', "A film people loved, made in Rochester for three generations. So why did a film this loved stop selling?",
  "A film people loved, made in Rochester for three generations.", "So why did a film this loved stop selling?")

# ── frame 8 · 2007 ──
L('f8', 'c01', "Frame eight. Two thousand seven.", "Frame eight. 2007.")
L('f8', 'c02', "Saturday, the thirtieth of June. Lake Avenue, on the north side of Rochester. People have come out early to watch, and a local TV station is carrying it live.",
  "Saturday, 30 June. Lake Avenue, on the north side of Rochester.", "People have come out early to watch,", "and a local TV station is carrying it live.")
L('f8', 'c03', "This is Kodak Park. The company's great film factory. About thirteen hundred acres, with its own railroad, its own fire department, its own power plant.",
  "This is Kodak Park. The company's great film factory.", "About 1,300 acres, with its own railroad,", "its own fire department, its own power plant.")
L('f8', 'c04', "At eight o'clock in the morning, Building Nine comes down.", "At eight o'clock in the morning, Building 9 comes down.")
L('f8', 'c05', "The next morning it's Building Twenty-Three, the blue building north of Ridge Road. Almost half a million square feet.",
  "The next morning it's Building 23, the blue building", "north of Ridge Road. Almost half a million square feet.")
L('f8', 'c06', "More buildings came down that autumn, and in the years after. Kodak had been clearing out the parts of the park it no longer needed since two thousand three.",
  "More buildings came down that autumn, and in the years after.", "Kodak had been clearing out the parts of the park", "it no longer needed since 2003.")
L('f8', 'c07', "Some of the people watching had worked inside those buildings. One neighbour in Maplewood told W-X-X-I News that they'd rather see the buildings standing than the grass, because that was employment.",
  "Some of the people watching had worked inside those buildings.", "One neighbour in Maplewood told WXXI News they'd rather", "see the buildings standing than the grass,", "because that was employment.")
L('f8', 'q01', "I got to see one. I didn't want to see any more.", "")
L('f8', 'c08', "In November two thousand eight, Kodak Park got a new name. Eastman Business Park. Room for other companies.",
  "In November 2008, Kodak Park got a new name.", "Eastman Business Park. Room for other companies.")
L('f8', 'c09', "A company doesn't blow up its own factories unless it has stopped needing them. So what happened to all that film?",
  "A company doesn't blow up its own factories", "unless it has stopped needing them.", "So what happened to all that film?")

# ── frame 7 · 2004 ──
L('f7', 'd01', "Frame seven. Two thousand four.", "Frame seven. 2004.")
L('f7', 'd02', "Here's the part of the story most people get wrong.", "Here's the part of the story most people get wrong.")
L('f7', 'd03', "The usual version goes like this. Kodak invented the digital camera, got scared, and hid... it. And when digital came, Kodak was left behind.",
  "The usual version goes like this.", "Kodak invented the digital camera, got scared, and hid it.", "And when digital came, Kodak was left behind.")
L('f7', 'd04', "But look at two thousand four.", "But look at 2004.")
L('f7', 'd05', "Kodak had been selling simple digital cameras to ordinary families since two thousand one. They were called EasyShare. You set the camera in its dock, pressed one button, and your pictures went to the computer, or to a little printer.",
  "Kodak had been selling simple digital cameras", "to ordinary families since 2001. They were called EasyShare.", "You set the camera in its dock, pressed one button,", "and your pictures went to the computer, or to a little printer.")
L('f7', 'd06', "And in two thousand four, Kodak sold more digital cameras in the United States than anyone. More than Sony. More than Canon.",
  "And in 2004, Kodak sold more digital cameras", "in the United States than anyone.", "More than Sony. More than Canon.")
L('f7', 'd07', "In two thousand five, it did it again.", "In 2005, it did it again.")
L('f7', 'd08', "So if Kodak was number one, why did it still fall?", "So if Kodak was number one, why did it still fall?")
L('f7', 'd09', "The honest answer is about money. For a hundred years, Kodak didn't really make its money on cameras. It made it on film. On every roll you bought, and every print you made.",
  "The honest answer is about money.", "For a hundred years, Kodak didn't really", "make its money on cameras.", "It made it on film.", "On every roll you bought, and every print you made.")
L('f7', 'd10', "Film was a wonderful business. Kodak's margins on it ran to around seventy percent.",
  "Film was a wonderful business.", "Kodak's margins on it ran to around 70%.")
L('f7', 'd11', "A digital camera was different. You bought it once, and then the pictures were free. Dozens of companies in Asia made cameras too, so prices fell every year. Kodak earned very little on each one, and sold some at a loss.",
  "A digital camera was different.", "You bought it once, and then the pictures were free.", "Dozens of companies in Asia made cameras too,", "so prices fell every year.", "Kodak earned very little on each one, and sold some at a loss.")
L('f7', 'd12', "So the better Kodak did in digital, the faster it ate the business that actually paid the bills.",
  "So the better Kodak did in digital, the faster it ate", "the business that actually paid the bills.")
L('f7', 'd13', "That April, after seventy-four years, Kodak was dropped from the Dow Jones Industrial Average.",
  "That April, after 74 years,", "Kodak was dropped from the Dow Jones Industrial Average.")
L('f7', 'd14', "And in two thousand seven, the camera moved into the telephone. Within a few years, most people stopped buying a camera at all.",
  "And in 2007, the camera moved into the telephone.", "Within a few years, most people stopped buying a camera at all.")
L('f7', 'd15', "To see how big that film business had been, we have to go back to the very top.",
  "To see how big that film business had been,", "we have to go back to the very top.")

# ── frame 6 · 1982 ──
L('f6', 'e01', "Frame six. Nineteen eighty-two.", "Frame six. 1982.")
L('f6', 'e02', "This is Kodak at the top of the world.", "This is Kodak at the top of the world.")
L('f6', 'e03', "In Rochester alone, the company employs sixty thousand, four hundred people. More than it ever will again.",
  "In Rochester alone, the company employs 60,400 people.", "More than it ever will again.")
L('f6', 'e04', "For a lot of families here, Kodak isn't just a job. It's where your father works, and your aunt, and maybe, one day, you.",
  "For a lot of families here, Kodak isn't just a job.", "It's where your father works, and your aunt,", "and maybe, one day, you.")
L('f6', 'e05', "Every March, Kodak pays its workers a bonus on top of their wages, a share of the profits. They call it the wage dividend. Rochester plans its spring around it.",
  "Every March, Kodak pays its workers a bonus on top of their wages,", "a share of the profits. They call it the wage dividend.", "Rochester plans its spring around it.")
L('f6', 'e06', "Across America, Kodak sells about nine of every ten rolls of film, and more than eight of every ten cameras. Those were the numbers in nineteen seventy-six.",
  "Across America, Kodak sells about 9 of every 10 rolls of film,", "and more than 8 of every 10 cameras.", "Those were the numbers in 1976.")
L('f6', 'e07', "Rochester has Xerox, and Bausch and Lomb, too. It calls itself the World's Image Centre.",
  "Rochester has Xerox, and Bausch & Lomb, too.", "It calls itself the World's Image Centre.")
L('f6', 'e08', "The year before, in nineteen eighty-one, Sony showed off a camera that stored pictures as electronic signals, on a little disk. Kodak noticed.",
  "The year before, in 1981, Sony showed off a camera", "that stored pictures as electronic signals,", "on a little disk. Kodak noticed.")
L('f6', 'e09', "Because something like it already existed, inside Kodak. It had been built in Rochester, seven years earlier.",
  "Because something like it already existed, inside Kodak.", "It had been built in Rochester, seven years earlier.")

# ── frame 5 · 1975 ──
L('f5', 'g01', "Frame five. Nineteen seventy-five.", "Frame five. 1975.")
L('f5', 'g02', "Steve Sasson is a young electrical engineer. He joined Kodak two years ago, straight out of school.",
  "Steve Sasson is a young electrical engineer.", "He joined Kodak two years ago, straight out of school.")
L('f5', 'g03', "His supervisor, Gareth Lloyd, gives him what sounds like a small job. See whether a new kind of electronic chip, a charge-coupled device, can capture a picture.",
  "His supervisor, Gareth Lloyd,", "gives him what sounds like a small job.", "See whether a new kind of electronic chip,", "a charge-coupled device, can capture a picture.")
L('f5', 'g04', "Sasson builds a camera out of whatever he can find. The lens comes from a Kodak movie camera. The pictures go onto an ordinary cassette tape. It runs on sixteen double-A batteries.",
  "Sasson builds a camera out of whatever he can find.", "The lens comes from a Kodak movie camera.", "The pictures go onto an ordinary cassette tape.", "It runs on 16 AA batteries.")
L('f5', 'g05', "It weighs eight pounds. It's about the size of a toaster.", "It weighs 8 pounds. It's about the size of a toaster.")
L('f5', 'g06', "In December, nineteen seventy-five, it takes its first picture. Black and white. One hundred dots by one hundred dots. A hundredth of a megapixel.",
  "In December 1975, it takes its first picture.", "Black and white. 100 dots by 100 dots.", "A hundredth of a megapixel.")
L('f5', 'g07', "It takes twenty-three seconds to record that one picture onto the tape.", "It takes 23 seconds to record that one picture onto the tape.")
L('f5', 'g08', "To see it, you put the tape into a playback machine, and the picture comes up on a television set.",
  "To see it, you put the tape into a playback machine,", "and the picture comes up on a television set.")
L('f5', 'g09', "Sasson shows it to room after room of Kodak managers. He calls it filmless photography. In a company that lives on film.",
  "Sasson shows it to room after room of Kodak managers.", "He calls it filmless photography.", "In a company that lives on film.")
L('f5', 'q02', "That's cute, but don't tell anyone about it.", "")
L('f5', 'g10', "That's how he remembered it, years later. And to be fair to Kodak, this was not a product. Sasson himself guessed it would be fifteen or twenty years before pictures like this could compete with film.",
  "That's how he remembered it, years later.", "And to be fair to Kodak, this was not a product.", "Sasson himself guessed it would be 15 or 20 years", "before pictures like this could compete with film.")
L('f5', 'g11', "Kodak patented it. The patent was granted in nineteen seventy-eight. And Kodak's engineers kept working on digital pictures, quietly, for years.",
  "Kodak patented it. The patent was granted in 1978.", "And Kodak's engineers kept working on digital pictures,", "quietly, for years.")
L('f5', 'g12', "But in every meeting, the same question hung in the air. Why would a company that sells film build something that doesn't need any?",
  "But in every meeting, the same question hung in the air.", "Why would a company that sells film", "build something that doesn't need any?")
L('f5', 'g13', "How did film get so big that nobody wanted to replace it?", "How did film get so big that nobody wanted to replace it?")

# ── frame 4 · 1950 ──
L('f4', 'j01', "Frame four. Nineteen fifty.", "Frame four. 1950.")
L('f4', 'j02', "The census counts three hundred thirty-two thousand, four hundred and eighty-eight people in Rochester. The most it will ever have.",
  "The census counts 332,488 people in Rochester.", "The most it will ever have.")
L('f4', 'j03', "The war is over. America is having babies, buying cars, taking vacations. And Kodak sells the pictures of all of it.",
  "The war is over. America is having babies,", "buying cars, taking vacations.", "And Kodak sells the pictures of all of it.")
L('f4', 'j04', "A Brownie Hawkeye camera. A yellow box of film from the drugstore. Prints that come back in an envelope a few days later. Colour slides. Home movies.",
  "A Brownie Hawkeye camera. A yellow box of film from the drugstore.", "Prints that come back in an envelope a few days later.", "Colour slides. Home movies.")
L('f4', 'j05', "In Rochester, Kodak is the biggest employer by far. And the money it pays out keeps the whole city going.",
  "In Rochester, Kodak is the biggest employer by far.", "And the money it pays out keeps the whole city going.")
L('f4', 'j06', "A few years later, in nineteen sixty-three, the city made a film about itself. Look at it. This is the Rochester Kodak built.",
  "A few years later, in 1963, the city made a film about itself.", "Look at it. This is the Rochester Kodak built.")
L('f4', 'j07', "Department stores on Main Street. A brand-new indoor shopping centre downtown, Midtown Plaza, one of the first in any American city.",
  "Department stores on Main Street.", "A brand-new indoor shopping centre downtown, Midtown Plaza,", "one of the first in any American city.")
L('f4', 'j08', "The Philharmonic in the Eastman Theatre. The University of Rochester. The Eastman School of Music. Kodak's founder's name is everywhere.",
  "The Philharmonic in the Eastman Theatre.", "The University of Rochester. The Eastman School of Music.", "Kodak's founder's name is everywhere.")
L('f4', 'j09', "He paid for a lot of it. But he never saw this city at its height. So who was the man who built a city around a box camera?",
  "He paid for a lot of it. But he never saw this city at its height.", "So who was the man who built a city around a box camera?")

# ── frame 3 · 1932–1935 ──
L('f3', 'k01', "Frame three. Nineteen thirty-two.", "Frame three. 1932.")
L('f3', 'k02', "George Eastman is seventy-seven. He never married. He lives in a mansion on East Avenue, where an organist plays for him at breakfast.",
  "George Eastman is 77. He never married.", "He lives in a mansion on East Avenue,", "where an organist plays for him at breakfast.")
L('f3', 'k03', "And for years he has been giving his fortune away. To the University of Rochester. To MIT, under a made-up name, Mister Smith. To Tuskegee and Hampton, two of the great Black colleges of the South.",
  "And for years he has been giving his fortune away.", "To the University of Rochester.", "To MIT, under a made-up name, Mr. Smith.", "To Tuskegee and Hampton,", "two of the great Black colleges of the South.")
L('f3', 'k04', "To dental clinics for the children of Rochester. And to music. A school of music, and a theatre with more than three thousand seats.",
  "To dental clinics for the children of Rochester.", "And to music. A school of music,", "and a theatre with more than 3,000 seats.")
L('f3', 'k05', "His gifts came to more than seventy-five million dollars.", "His gifts came to more than $75 million.")
L('f3', 'k06', "In March nineteen thirty-two, after two years of a painful illness of the spine, George Eastman took his own life. He was seventy-seven.",
  "In March 1932, after two years of a painful illness of the spine,", "George Eastman took his own life. He was 77.")
L('f3', 'k07', "Three years later, his company brought out something he had wanted for a very long time. Colour.",
  "Three years later, his company brought out something", "he had wanted for a very long time. Colour.")
L('f3', 'k08', "Kodachrome. And it was invented, of all people, by two musicians.", "Kodachrome. And it was invented, of all people, by two musicians.")
L('f3', 'k09', "Leopold Mann-ess was a concert pianist. Leopold Godowsky Junior was a violinist. They had been chasing colour film since they were schoolboys in New York.",
  "Leopold Mannes was a concert pianist.", "Leopold Godowsky Jr. was a violinist.", "They had been chasing colour film", "since they were schoolboys in New York.")
L('f3', 'k10', "Kodak's research chief, Kenneth Mees, brought them to Rochester in nineteen thirty and gave them a laboratory.",
  "Kodak's research chief, Kenneth Mees, brought them to Rochester", "in 1930 and gave them a laboratory.")
L('f3', 'k11', "Working in the dark, the story goes, they timed their developing by whistling Brahms.",
  "Working in the dark, the story goes,", "they timed their developing by whistling Brahms.")
L('f3', 'k12', "In nineteen thirty-five, Kodachrome went on sale. The first colour film that ordinary people could really use. George Eastman never saw it.",
  "In 1935, Kodachrome went on sale.", "The first colour film that ordinary people could really use.", "George Eastman never saw it.")
L('f3', 'k13', "What he left behind was a company people stayed in for their whole lives. What kind of boss builds a company like that?",
  "What he left behind was a company", "people stayed in for their whole lives.", "What kind of boss builds a company like that?")

# ── frame 2 · 1900–1912 ──
L('f2', 'm01', "Frame two. Nineteen hundred.", "Frame two. 1900.")
L('f2', 'm02', "February, nineteen hundred. Kodak puts a new camera on sale. It's a cardboard box covered in imitation leather, with a simple lens. It costs one dollar.",
  "February 1900. Kodak puts a new camera on sale.", "It's a cardboard box covered in imitation leather,", "with a simple lens. It costs one dollar.")
L('f2', 'm03', "It's called the Brownie, and it's made for children. The name came from the Brownies, little cartoon characters every child in America knew.",
  "It's called the Brownie, and it's made for children.", "The name came from the Brownies,", "little cartoon characters every child in America knew.")
L('f2', 'm04', "In its first year, Kodak sold about a hundred and fifty thousand of them.", "In its first year, Kodak sold about 150,000 of them.")
L('f2', 'm05', "Now anyone could take a picture. And every picture needed film. And the film came from Rochester.",
  "Now anyone could take a picture. And every picture needed film.", "And the film came from Rochester.")
L('f2', 'm06', "So Kodak Park grew, and grew. These photographs come from a book Kodak printed for its shareholders in nineteen oh six. Look at the people.",
  "So Kodak Park grew, and grew.", "These photographs come from a book Kodak printed", "for its shareholders in 1906. Look at the people.")
L('f2', 'm07', "And in nineteen twelve, Eastman did something very few employers in America did. He shared the profits with the people who made them.",
  "And in 1912, Eastman did something", "very few employers in America did.", "He shared the profits with the people who made them.")
L('f2', 'm08', "The first wage dividend paid every eligible worker two percent of everything they had earned over the past five years.",
  "The first wage dividend paid every eligible worker 2%", "of everything they had earned over the past five years.")
L('f2', 'm09', "Later came a savings and loan to help workers buy houses, and then pensions, and life insurance.",
  "Later came a savings and loan to help workers buy houses,", "and then pensions, and life insurance.")
L('f2', 'm10', "Eastman saw it as good business. People who share in a company stay with it. And in Rochester, they did, for generations.",
  "Eastman saw it as good business.", "People who share in a company stay with it.", "And in Rochester, they did, for generations.")
L('f2', 'm11', "But where did a one-dollar camera come from?", "But where did a one-dollar camera come from?")

# ── frame 1 · 1888 ──
L('f1', 'p01', "Frame one. Eighteen eighty-eight.", "Frame one. 1888.")
L('f1', 'p02', "George Eastman grew up poor. His father died when he was a small boy. At fourteen he left school and went to work as an office boy, for three dollars a week.",
  "George Eastman grew up poor.", "His father died when he was a small boy.", "At 14 he left school and went to work as an office boy,", "for $3 a week.")
L('f1', 'p03', "Later he became a clerk at a savings bank in Rochester. And in eighteen seventy-seven he bought his first camera, for a trip he never took.",
  "Later he became a clerk at a savings bank in Rochester.", "And in 1877 he bought his first camera,", "for a trip he never took.")
L('f1', 'p04', "Taking a picture then was a chemistry lesson. Heavy glass plates, chemicals, a tent for a darkroom, a tripod. What Eastman called a pack-horse load.",
  "Taking a picture then was a chemistry lesson.", "Heavy glass plates, chemicals, a tent for a darkroom, a tripod.", "What Eastman called a pack-horse load.")
L('f1', 'p05', "He spent his nights experimenting in his mother's kitchen. In eighteen eighty-one he started a company making dry plates, ready to use.",
  "He spent his nights experimenting in his mother's kitchen.", "In 1881 he started a company making dry plates, ready to use.")
L('f1', 'p06', "Then he went further. He replaced the glass with a roll of film.", "Then he went further. He replaced the glass with a roll of film.")
L('f1', 'p07', "And in eighteen eighty-eight, he put that roll inside a small box camera, and gave it a name he made up himself. It started and ended with his favourite letter.",
  "And in 1888, he put that roll inside a small box camera,", "and gave it a name he made up himself.", "It started and ended with his favourite letter.")
L('f1', 'q03', "The letter K had been a favorite with me. It seems a strong, incisive sort of letter.", "")
L('f1', 'p08', "The Kodak cost twenty-five dollars. It came loaded with enough film for a hundred pictures. Little round ones.",
  "The Kodak cost $25.", "It came loaded with enough film for 100 pictures.", "Little round ones.")
L('f1', 'p09', "When the roll was finished, you didn't open the camera. You mailed the whole thing back to Rochester.",
  "When the roll was finished, you didn't open the camera.", "You mailed the whole thing back to Rochester.")
L('f1', 'p10', "There they developed your pictures, printed them, loaded fresh film, and sent the camera home to you. For ten dollars.",
  "There they developed your pictures, printed them,", "loaded fresh film, and sent the camera home to you.", "For $10.")
L('f1', 'p11', "He wanted a camera to be as easy to use as a pencil. For anybody. And he put the whole idea into eight words.",
  "He wanted a camera to be as easy to use as a pencil.", "For anybody. And he put the whole idea into eight words.")
L('f1', 'p12', "You press the button. We do the rest.", "You press the button. We do the rest.")

# ── epilogue · today ──
L('end', 'r01', "Now, let's fast-forward.", "Now, let's fast-forward.")
L('end', 'r02', "Rochester today is a city of about two hundred and eleven thousand people. Smaller. Still here.",
  "Rochester today is a city of about 211,000 people.", "Smaller. Still here.")
L('end', 'r03', "Kodak is still here too, in its tower on State Street. It still makes film, for movie directors, and for a new generation of photographers who have come back to it.",
  "Kodak is still here too, in its tower on State Street.", "It still makes film, for movie directors,", "and for a new generation of photographers", "who have come back to it.")
L('end', 'r04', "The old Kodak Park is Eastman Business Park now, home to more than a hundred companies. Some of them were started by people who used to work for Kodak.",
  "The old Kodak Park is Eastman Business Park now,", "home to more than a hundred companies.", "Some were started by people who used to work for Kodak.")
L('end', 'r05', "Steve Sasson, the young man with the toaster-sized camera, was given the National Medal of Technology and Innovation at the White House. Today there's a camera in almost every pocket on Earth.",
  "Steve Sasson, the young man with the toaster-sized camera,", "was given the National Medal of Technology and Innovation.", "Today there's a camera in almost every pocket on Earth.")
L('end', 'r06', "And somewhere in your house, in a closet or under a bed, there's probably a shoebox. Full of Kodak prints. People you love, holding still, exactly as they were.",
  "And somewhere in your house, in a closet or under a bed,", "there's probably a shoebox. Full of Kodak prints.", "People you love, holding still, exactly as they were.")
L('end', 'r07', "Kodak gave us that. And for a hundred years, it gave one city a way to live.",
  "Kodak gave us that.", "And for a hundred years, it gave one city a way to live.")
L('end', 'r08', "Did your family work for Kodak, or keep a shoebox of Kodak prints? Tell us in the comments.",
  "Did your family work for Kodak, or keep a shoebox of Kodak prints?", "Tell us in the comments.")

# quotes are voiced as quotes (no caption: the quote card shows the words) — who said them, for the card
QUOTE = {'q01': dict(who='A Maplewood neighbour', role='on the 2007 implosions', src='WXXI NEWS · "MAPLEWOOD RESIDENTS REMINISCE ABOUT KODAK\'S GLORY DAYS"'),
         'q02': dict(who='Steve Sasson', role='recalling management\'s reaction, 1975–76', src='THE NEW YORK TIMES · 2 MAY 2008'),
         'q03': dict(who='George Eastman', role='on the name "Kodak"', src='INTERVIEW WITH SAMUEL CROWTHER · SYSTEM MAGAZINE · 1920')}

os.makedirs(os.path.join(D, 'audio'), exist_ok=True)
json.dump([dict(id=i, chapter=ch, voice=V, text=sp, subs=su, **({'quote': QUOTE[i]} if i in QUOTE else {})) for ch, i, sp, su in C],
          open(os.path.join(D, 'audio', 'lines.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
names = {'hook': 'Hook', 'f10': 'Frame 10 · 2012 · The bankruptcy', 'f9': 'Frame 9 · 2010 · The last roll', 'f8': 'Frame 8 · 2007 · The implosions',
         'f7': 'Frame 7 · 2004 · Number one', 'f6': 'Frame 6 · 1982 · The peak', 'f5': 'Frame 5 · 1975 · The camera with no film',
         'f4': 'Frame 4 · 1950 · The city at its height', 'f3': 'Frame 3 · 1932–1935 · The founder, and the colour',
         'f2': 'Frame 2 · 1900–1912 · A dollar, and a dividend', 'f1': 'Frame 1 · 1888 · You press the button', 'end': 'Epilogue · Today · Fast-forward'}
out, last = ['# What Happened to Rochester? The City Kodak Built — script', ''], None
for ch, i, sp, su in C:
    if ch != last: out += ['', f'## {names[ch]}', '']; last = ch
    out.append(f'**{i}** {" ".join(su) if su else "“" + sp + "” (quote card)"}')
open(os.path.join(D, 'script.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
w = sum(len(sp.split()) for _, _, sp, _ in C); print(len(C), 'lines', w, 'words', f'~{w / 150:.1f} min of speech')
long = [(i, s) for _, i, _, su in C for s in su if len(s) > 66]; print('long caption lines:', long)
