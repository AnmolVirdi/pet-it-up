## Inspiration

Pets have a life too, they have emotions too. **We're really inspired by the Blue Cross Society**. We wanted to build an online stores to promote pet sales, but needed a "show-stopper" add-on to this project. So, we came up with this idea of petting an animal without being physically present there! In simple words, someone else(Volunteer) can pet that animal on its owner's behalf, and even get paid for it. This does sound like an employment opportunity too. 

## What it does

This is basically an e-commerce model with the sole aim to promote petting culture. This platform allows users to not only buy pets(common idea), but also pet an animal without being its real owner. This would encourage people to support animals as well as people willing to work. It's like baby-sitting a pet! Not only this, after applying to fund the pet, the owner will get access to the conditions (surrounding temperature) to be satisfied that they're taken care of really well.

## How we built it

We have used **HTML, CSS, PHP, JAVASCRIPT, JQUERY, BOOTSTRAP** for the frontend of the website. 

Database management was done using **Flask(python)  and MySQL.**

The Backend is made using **Python** and its libraries like **Flask, itsdangerous, pymysql, smtp, config_mail, email.mime, etc**

We've added a utility using **IOT and Node-MCU** that would be used to estimate whether the pet is living in favorable surroundings or not.

## Challenges we ran into

1. The first challenge was to design an **e-commerce model**. With a lot of research regarding the components and flowcharts of its working, we were finally able to make it possible.
2. Connecting **Node-MCU** with a **live server** was another rigid challenge. We couldn't connect firebase with the model for multiple reasons. Finally, we came out with an alternative to use Sheets as the medium to post and fetch readings.
3. The **systematic arrangement of the databases** of almost everything( Volunteers, pets in stock, user who want to buy a pet, etc) was tough. We had to theoretically lay down rules for classifications first. This was pretty time-consuming, but we made it!
4. We wanted to add a **chatbot** for the users, but had to drop this due to too many technical difficulties. We used the reddit comments dataset for it, and this was like 250-300 gb of files. Using **python(json, sqlite3),**  when we tried to store the filtered comments into the database, there was a really undetectable issue that stored all the comments without a parent_id. So, this feature had to pass. It could not be completed in 48 hours. 

## Accomplishments that we're proud of

We are really satisfied that we made something for a good cause. Implementing IOT and hardware was a bit tough, but achievable. It was fun, working with a team. We've explored firebase, sqlite3, flask, AI-based recommendation models and much more! It was not only a work-based project, but also a golden opportunity to learn new frameworks and skills.

## What we learned

We've learned a ton of new technologies like connecting **Node-MCU**(hardware) with **firebase and google sheets**, integrating **Flask** instance, Using **hashing to store passwords** to ensure security(**MySQL)**, Realtime measurement of pet's surrounding using **sensors(DHT11)**, An idea about how **chatbots work using datasets**, etc. It was a fun learning experience as well.

Apart from this, we've learned some decent life lessons like the importance of communication and team spirit. There were some situations where all of us were frustrated to the limit of dropping the project, but a common hope kept us working! Participating in an online hackathon was too much fun. We loved the chess session, drawasaurus and the idea of having coffee tables.

## What's next for Petito

Petito can prove to be a great boon  to humanity as well as animals. We have multiple features in our mind that can be added later **to enhance the experience** of petting.  The features that can be added in the future:-

1. Worried about whether your pet was taken out for a walk? We'll **add a GPS sensor** on its collar.
2. This project can open doors to **new earning methods** with petting an animal, like the cherry on a cake. Volunteers can even rescue stray animals and post their ads! Interested people can apply to fund them.
3. A **recommendation system** (AI based) can be integrated with the pet search option.
4. An **app variant** of Petito would be much more convenient for public use since this generation is extensively dependent on smart phones.

Petito would lay the foundation of another new step towards petting culture and also open doors to business opportunities. This would allow local pet shop owners to advertise their pets online. 



#### We wish the best for humanity.
