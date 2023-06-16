EP 1: THE PHREAKY WORLD OF PBX HACKING

[BIRDS CHIRPING]

JACK: It’s just before dawn in a February morning in a quiet residential neighborhood in Karachi, a city in Pakistan. Pakistani’s Chief Intelligence Office, Mir Mazhar Jabbar, is walking towards the home of a hacker who he’s been tracking for over two years. Behind Jabbar is a team of Pakistani police officers. Jabbar arrives at the front door and knocks. [KNOCKING] You’re probably already aware the FBI has a Top 10 Most Wanted Criminals list, but what you may not know is the FBI also puts out a Cyber’s Most Wanted list which is a list of FBI’s most-wanted hackers. Jabbar and his team are about to raid the house of one of FBI’s Cyber’s Most Wanted. Just then the door opens. Jabbar and his team forcefully push the door open and raid the house. [SHOUTING AND BANGING]

JACK: This is Darknet Diaries, true stories from the dark side of the internet. I’m Jack Rhysider.

ADAM: They did the whole thing in a single weekend when nobody was in the office.

JACK: That’s Adam Finch, a victim to one of these types of attacks.

ADAM: We didn’t even know about it until a month later when we got the bill.

JACK: He’s talking about his phone bill.

ADAM: The bill was $24,000 more than normal.

JACK: Why was it so high?

ADAM: The bill said we had called multiple pay-per-minute numbers.

JACK: Like 1-900-SEX and psychic chat lines?

ADAM: Exactly. We tried to refute the charges with the telephone company, telling them we didn’t make these calls.

JACK: What did they say?

ADAM: They basically said tough luck, pay up. We did go to the police but they didn’t seem to care and ultimately gave us no help.

JACK: Adam didn’t want me to reveal what company he worked for because it’s embarrassing for the company. Adam’s company did pay the charges though, because there was no other option. You may be wondering why somebody would break into an office and rack up an enormous phone bill for someone else. But here’s the crux of the hack; the hackers were dialing pay-per-minute numbers that they owned. With this attack they literally are turning other people’s phones into ATMs. There are two main methods hackers use to do this. Method one - the hacker will call a desk phone in a random office. [PHONE RINGING] But it’s 7:00p.m.and it’s Friday so nobody picks up. The call goes to voicemail but some phones have the ability to check voicemail remotely.

VOICEMAIL: To access your voicemail, please enter your pin followed by the pound key.

JACK: The hacker will first try the last four digits of the phone number. [DIALING] This is usually the default pin for a voicemail box. Once they get into voicemail they’re looking for a specific configuration option.

VOICEMAIL: To activate do not disturb, press 1. To change your permanent forwarding number, press 2.

JACK: Bingo. Call forwarding. The hacker sets the call forwarding number to be the number of their pay-per-minute line. Now the next time anyone dials a phone it will place a new call to the pay-per-minute line. [RINGING, HANGS UP] Method two - this method is a little bit more involved. Many companies are adopting voice-over IP or VOIP phones in their office. This is where the phone plugs into the regular office network and not the plain old telephone system. Most of the VOIP phones are dumb. They don’t know what to do without the help of another system. That other system is called a Private Branch Exchange, or PBX. When someone picks up the handset of a phone, the phone freaks out and says to the PBX, help! Someone just picked up the handset. What do I do? The PBX is very friendly and says calm down. Just play a dial tone. [DIAL TONE] When the user pushes a number, the phone panics again and asks for help again. The PBX says don’t worry, just play a digit tone. [DIGIT TONE] This continues until the user pushes enough numbers and the PBX connects the call. [RING TONE] But the problem is the PBX is sometimes too helpful. Nobody taught it who can and can’t make calls. It wasn’t properly secured. Anyone who knows the IP address of an insecure PBX can make phone calls that originate from that office. With this method hackers find the IP address of PBXs and try to make a call using that PBX. They configure their phone [TYPING], pick up the handset [HANDSET NOISE], and check for a dial tone. [HANDSET NOISE] This takes patience by the hacker because they have to hunt and poke into the darkness of the internet, but eventually they pick up the phone and hear a dial tone. [DIAL TONE] To a PBX hacker that is the sound of money. [DIALING] Now the hacker begins making calls to the pay-per-minute numbers. [DIALING] They use robo-dialers, dialing hundreds of times a day or thousands of times in a weekend. Calls are made to Guinea, East Timor, Lithuania. For every minute connected results in more money for the hacker. More and more calls are made. More and more minutes are racked up and this continues until someone somewhere notices the calls and stops them. [PHONE HANGS UP] I guess my question is why can’t the victim go to the phone company to refund the charges?

PAUL: Because the phone company doesn’t cover consequence and losses. My name is Paul Byrne, I work for a company called UC Defence which I founded to mitigate the threat of the crime of toll fraud or otherwise commonly known as PBX hacking.

JACK: Paul has been protecting companies from PBX hackers since 2012. He says the phone companies have a legal right to collect any fees their customers accrue. This is usually spelled out in the contract.

PAUL: Yeah, the victim tends to be found liable.

JACK: But most importantly, the PBX is not property of the telecom. It’s owned by the victim. It was the victim’s own negligence of security that resulted in this attack. Just like when an ISP gives a company an internet connection they aren’t liable if that company gets hacked. How much is PBX hacking costing people yearly?

PAUL: The best evidence is from the Communications Fraud Control Association. They estimate that PBX hacking is costing the business community in excess of ten billion dollars per annum.

JACK: That number, ten billion, has doubled in the last four years.

PAUL: There’s absolutely no doubt that fraud is on the rise and it’s primarily due to the vulnerabilities around VOIPs.

JACK: These VOIP vulnerabilities are simply that companies aren’t taking the steps to secure their PBX correctly. Often a business doesn’t have anyone capable of configuring a PBX so they outsource the job to a contractor. But they often go with the cheapest contractor to save money which results in an insecure or hastily-configured PBX. It’s not an easy task to properly secure a PBX. Since the PBX must be on the internet to receive incoming calls, you can’t simply block all incoming access to it. To further complicate things, some offices have mobile workers who have their office desk phone at home. Now a PBX needs to be configured to allow calls initiated from the internet. It’s a delicate balance between what’s allowed and what’s not allowed. What’s the average bill for a victim?

PAUL: What we’re seeing is a company with an average of a hundred users on the phone system; they get compromised on a Friday night. On Monday morning their phone bill will be in the region of 60,000 Euros.

JACK: Are the police able to help victims of this crime?

PAUL: No, because the police aren’t aware of this. They’re used to other types of crimes that they know how to investigate but when this incident occurs, they don’t have the resources to even understand what the crime means and how they would go about investigating it.

JACK: As Paul said, the police just aren’t equipped to handle international crimes. Calls are almost always going to foreign countries such as East Timor, Cuba, Latvia, even Zimbabwe. Many of these crimes don’t get reported. Companies fear bad publicity if they say they’ve been hacked. Sometimes victims contact the FBI but the FBI is usually only interested in threats against the government or the country or crimes that were over one million dollars in damages. Most of this PBX hacking is in the tens of thousands. The FBI does appreciate when people report the crime, since it helps them collect data to build a case. In 2012 the FBI did receive enough reports about PBX hacking that they began looking at the data. Somehow they were able to track down who was making these phone calls. While looking at the data, patterns began emerging which eventually led them to two men. [ELECTRONIC MUSIC] Farhan Arshad and Noor Aziz Uddin. Somehow the FBI found out that the two men were on a flight to Kuala Lumpur in Malaysia. The FBI contacted Interpol to arrest the two men. Within hours of the two hackers arriving in Kuala Lumpur, Interpol raided their hotel and arrested both of them. The FBI was thrilled and began sending extradition requests to Malaysia. But after being held for sixty days, the Malaysian Attorney General let them both go free. [MUSIC ENDS] According to the official report the Malaysian Attorney General said, “The arrest warrant obtained by Malaysian Home Ministry violated the technicalities involved in the requirements of the Extradition Act of 1992.” Malaysia believed they had arrested these two men illegally. Farhan and Uddin both immediately fled the country, got out of Malaysia, and went back to Pakistan. The very next month the FBI indicted both men and they added them to the Cyber’s Most Wanted list and offered a $50,000 bounty for any information leading to the arrest of either one of them. I’m looking at the indictment form now and it shows a list of victims that were targeted by these hackers. I want to share with you the top three highest charges that I see on this list. A company in Carlstadt, New Jersey is claiming that they lost $78,000. A company in Englewood, New Jersey is claiming they lost $83,000. But the highest one on the list is the township of Parsippany-Troy Hills in New Jersey. They’re claiming these hackers racked up a phone bill of $395,000. According to the indictment report the FBI claims these men dialed for thirteen million minutes from 4,800 different hacked phone numbers. Once the FBI had a warrant for their arrest they notified Pakistan, which is where they thought these two men were living. In Pakistan the FIA began researching it. The FIA is the Federal Investigation Agency, similar to the CIA in the US. The Chief Security Officer of the FIA is Mir Mazhar Jabbar and for years the FIA had no leads towards catching these two individuals. Then the FIA got a tip. Somebody had claimed they knew the cellphone number of Uddin. The FIA then worked with the telephone company to track down the GPS coordinates of that cell phone. That’s when Jabbar raided the home of Uddin. Not only did he catch Uddin but Arshad was there in the house too, and both men were arrested on February 14, 2015. It’s ironic, don’t you think? These two phone hackers were brought down because their phone number became known? In total the FBI claims they cost fifty million dollars in damages. What did Uddin do with the money? He purchased about fifty plots of land around Karachi, his home town in Pakistan, and was even investing about $400,000 in various local business ventures. Now, two years later, both men continue to sit in a prison in Pakistan, still awaiting their trial and sentencing. These two men were arrested for PBX hacking but there are thousands of other PBX hackers that haven’t been caught. Even though we don’t know who they are or where they are, we do know one thing is for certain; PBX hacking will continue until security improves. [DIALING] [BUSY TONE]

[OUTRO MUSIC]

JACK: You’ve been listening to Darknet Diaries. For show notes and links, check out darknetdiaries.com. Music is provided by Ian Alex Mac, Sro, Hicham Chahidi, and Podington Bear.

[OUTRO MUSIC ENDS]

[END OF RECORDING]
