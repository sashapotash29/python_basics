# PIPELINES


### Basic Idea of a Pipeline

- a Data Pipeline is a unified system for capturing events for analysis and building products.
	- Events can be thought of as clicking, loading an application, buying something, etc.

- In its essence, you have a large chunk of data you have gathered. There is a process that will need this data to run analysis but not all of it. So, you have your data fed to a script which will transform the data into the form that is required by your analytical script. The "transform" script is  listening on a queue for incoming data and then sends to a following queue that the data is being processed. The "analysis" script is listening on its queue for data that is ready to be analyzed. This is a typical pipeline or at least the fundamental concept behind it.

- Example: LinkedIn people you may know or Amazon Recommended Products for you
	- The server takes in click and view events and produces recommendations.
- Example: a website with advertising availability
	- Server takes in user click events as well as available cookie information to determine a user profile.

### AWS Data Pipelines

- An web service to allow for automating the movement and transformation of data.
- Basic Set Up:
	- Copy files that analysis will be conducted on. (Usually files into Amazon S3)
	- Establish task that dictates the analysis that needs to be completed. (Done on Amazon EMR)

- Benefits:
	- Amazon Web Services has provided the infrastructure to allow your server not to be overloaded.
		- Imagine a CSV file being written into your production database. If it is too large, it can overload your SQL server and disallow others to read/write as they are waiting for your process.
	- AWS SQS creates a queue that allows for your processes to speak with eachother and has mechanisms built to accomplish load balancing and over usage.
		- Simply put, it acts as a buffer to ensure you do not overload your server.
	- The process is automated. In an essence, it is "load it into the patch queue and forget about it". Essentially, you want to capture as much data as you can and send it to a patch queue which is design to deliver the information into a "Processing" Script. The actual analytical portion as well as storing into the DB is done over a few hours, not right away. Now if the information collected was analyzed right away and stored, your server would be limited in how much data it can process and thus many users using said feature would overload your system.