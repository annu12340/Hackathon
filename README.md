## Inspiration
We are on a quest to create a world where every woman feels safe, supported, and empowered to thrive. Together, we can make a difference and build a future where women's safety is non-negotiable.

## What it does
Sentinel has 2 core features:-

### A. Covert Communication for Victims of Abuse: 
Sentinel addresses a critical issue faced by women in abusive relationships who struggle to seek help directly due to their partner's constant monitoring of their social media and communication channels. Leveraging the power of steganography, our platform enables these women to encode distress signals within seemingly innocent messages, such as routine greetings or updates, thus circumventing detection by their abuser.

Sentinel operates through a clever integration of steganography and social media monitoring. Users can encode their distress messages within everyday posts, using a specific hashtag like #staywake to signal the need for assistance. Meanwhile, a background job constantly scans social media platforms for posts containing images and the designated hashtag. Upon detection, our system decodes the hidden messages embedded within the images, alerting designated support networks or authorities to intervene swiftly and discreetly.
![flowchart](https://i.ibb.co/t4x2c9H/steganpgraphy.png)

**How it helps**

Sentinel offers a lifeline to individuals trapped in abusive relationships, providing them with a covert means to reach out for help without fear of retaliation. By harnessing the innovative potential of steganography and social media monitoring, we empower vulnerable individuals to break free from isolation and access the support they desperately need.

### B. Culprit Identification System
 Sentinel also draws inspiration from the chilling tales of serial offenders like Ted Bundy. The platform designed to address the challenge of tracking repeated offenders who commit similar crimes across multiple locations by leveraging machine learning models, specifically sklearn and KNN (K-Nearest Neighbors), to analyze and link similar descriptions of suspects across different crime scenes.

For example:  Person A with dark brown eyes, tall, around 29ish age, curly long hair is similar to Person B with black eyes, medium, 30 years age, long black hair. 
Here we use ML to find the similarity in the text

Additionally, Sentinel provides intuitive visualization tools to map out the locations of these incidents, offering law enforcement agencies a comprehensive view of the offender's activities.
![Flowchart](https://i.ibb.co/g6dzcHZ/Untitled-2024-02-08-1720-1-1.png)

**How it helps**

Sentinel revolutionizes the way law enforcement agencies tackle crimes by providing them with powerful data-driven insights. By consolidating information from multiple crime scenes and identifying commonalities in suspect descriptions, our platform enables proactive measures to apprehend offenders more effectively. Moreover, Sentinel's visualization features offer a holistic understanding of the geographical distribution of criminal activities, facilitating strategic resource allocation and crime prevention efforts.

## How we built it
Convex db,  React js, tailwind, Flask, Swagger, OpenAI, KNN, SKlearn, Serve

## Where is Convex db used
- Clerk auth and convex is used to authenticate the user into the system

### A. Covert Communication for Victims of Abuse: 

- The convex table - messages get updated everytime there is a telegram post with an image and hastag #staywoke

### B. Culprit Identification System

- The users can report a new culprit into the table called culprit. We could get the individual values like eye color, hair, age, other details from the user and condense it into a single message & add it to the db
- Then they can see the detailed view and search for the report
- It also supports the deletion. 
**- Hence all the CRUD functionality is supported here**

## Screenshots of sample databases used
![culprit](https://i.ibb.co/rkqCWzN/Untitled.png)

![encoded](https://i.ibb.co/pK1hW0G/Untitled-1.png)

Flask server
![flask](https://i.ibb.co/vP50kNP/Screenshot-8.png)

## Challenges we ran into
- A lot of issues while connecting convex db in my windows system. Had to spend a lot of time troubleshooting
- We were using Python (flask) for certain steganography and ML models. But we were getting some issues like deploying the backend. Hence we were not able to deploy the entire code into production. **We tried to lot to deploy the entire stack, but were getting a lot of blockers. So please excuse us for not providing the deployed URL**
- Shortening the demo pitch to exactly 3mins also was a challenge

## How run the code on local
- Install the required packages in react and python

*For react*
```
npm install
```

*For python*
````
pip install -r requirements.txt
````

- Generate a new openAI key and export it (It is used to img generation)
```
export OPENAI_API_KEY=<Key>
```

- Update the .env file in apps/web with the following values
```
NEXT_PUBLIC_CONVEX_URL=
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
```

- To display the map we require serve package. For that do the following
```
npm install -g serve
```
In the parent directory, execute the following
```
serve
```

- Generate a new token forthe telegram bot and add it to a channel. The token needs to be exported
```
export TELEGRAM_TOKEN=<TOKEN>
```
Then open a new terminal and run the dvtelegram.py function

- Open another terminal and start the react convex server and specify which db we want to use (either new one or an existing one)
```
cd Convex
npx convex dev
```

Run the following command to start the server. This would open the app at http://localhost:5000
```
npm run dev
```

- Open a new terminal to start the flask server
```
python main.py
```
This would start a new flask swagger app. To see the URLs, go to http://127.0.0.1:5000/apidocs/

