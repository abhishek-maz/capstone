# capstone
Repository created for hosting capstone project files.

Frontend Design 

  Tech stack: HTML, CSS, JavaScript 

    Main Menu for selecting either EC2 actions or S3 Actions. 

    In EC2 Menu: 

    Option to create an instance. 

    Options for Listing, Starting, stopping, resuming, and terminating instances. 

    Display area to list instances. 

    In S3 Menu: 

    Options to upload files to a bucket. 


Backend Design 

  Tech stack: Python, AWS API Gateway 

    Source code: 

    Python Code for manipulating resources as part of the Backend hosted in AWS Lambda 

    Front-end code hosted in EC2 instances. 

     EC2 instances (t2.micro instances, EBS volumes to host data) to host the servers for the front end. 

     API Gateway is used to connect the front end to Lambda. 
