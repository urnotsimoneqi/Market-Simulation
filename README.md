# Market-Simulation
The final project for Intelligent System Deployment. 

## Project Overview and Goals
### Logic
Write the CEO function for the program. 
Consider ideas like: using past purchase behavior to guide the automated CEO. Improve the logic of Selling Agent, 
Buyer Agent, CEO Agent and reporting Agent. At a minimum provide the following changes as a checklist: 
### Selling Agent
- [x] Enable more than one seller and ability to sell more than one product per seller.
- [x] Provide ability to increase or reduce price based on past history 
- [x] Establish relationships between products, such as if a phone has an accessory like a case, the Seller should offer together. 
### Buyer Agent
- [x] Enable ability to own more than one product
- [x] Add a buyer “type” or demographics, for example
    - [x] Certain buyers prefer items of higher quality or are more sensitive to price 
    - Buyers are interested in buying related products like a phone and its case in separate transaction. I.e. if a buyer bought the phone, they are more likely to purchase the case.
### CEO Agent
- [x] Choose between ad types
- Choose how much to spend on ads
- [x] Avoid going bankrupt (But do not simply inject money into the system, you’ll need some controls on spending)
- Analyze the buying data and make better either: ad spending, product decisions
    - Identify patterns in the buyers
    - React to patterns in the buyers 
### Reporting Output
Use basic data visualization to insure humans understand whats happening. Visualization should occur either in a basic visual system in code or in a visualization tool like Google Data Studio or Microsoft PowerBI
- Provide information on total sales and buyers 
- Present promotion effectiveness 
- Write these details to a file 
- Bonus
    - [x] Write to a database (mysql, bigquery, etc) to store information
    - Present in PowerBI or Google Data Studio
    
### Environment: (refer to auction MAS provided in class)
- Add inventory to the system, meaning there is a limit to how many products are available each period
- Interaction with the external environment: Send emails or Update Google drive collaboration documents describe what is happening
- Bonus: add the ability to auction either by buyers or sellers or both
    - Buyer: if product in the market isn’t enough, then buyers start to bid
    - Seller: if the product is too much and there’s less interest, enable ability to reduce the price
- Bonus: consider limiting the number of ads available which would also setup a requirement for an auction by the sellers