Project Readme: Working with Load Balancer

Welcome to the Load Balancer project! This readme is designed to guide developers who are new to Python and the Flask framework through the process of working with a basic HTTP load balancer.


Introduction

This project aims to introduce you to the concept of load balancing in web development, specifically using Python and Flask. A load balancer is a crucial component in distributed systems architecture, distributing incoming web traffic across multiple servers to ensure optimal performance and reliability.
Technologies Used

    Python: A versatile and beginner-friendly programming language used for building the load balancer logic and handling server requests.
    Flask Framework: A lightweight web framework for Python used to create the HTTP server and manage routing.

Getting Started

   1.  Installation: Ensure you have Python installed on your system. You can download Python from the official website. Flask can be installed via pip, Python's package manager, using the command:

![image](https://github.com/DeBenign/load_balancer/assets/95944367/d88a43ca-f3bf-420b-8971-61edab703b49)

2. Clone the Repository: Clone or download the project repository from GitHub to your local machine.

3. Understanding the Code:

    load_balancer.py: This file contains the implementation of the load balancer logic. It includes methods for selecting servers, handling server failures, performing health checks, and sending requests to servers.
    app.py: This file initializes a Flask application and defines routes for incoming requests. It utilizes the load balancer logic to distribute requests across multiple servers.
    README.md: This readme file provides instructions and information about the project.

4. Configuration: Open app.py and modify the servers list to include the addresses of your backend servers. Replace "server1.com", "server2.com", etc., with the actual server addresses.

5. Running the Application: Execute app.py using Python to start the Flask server. You can do this by running the following command in your terminal:

![image](https://github.com/DeBenign/load_balancer/assets/95944367/5ecc7190-33af-4a19-a2ab-ece7ef7a35eb)

6. Testing: Open a web browser or use a tool like cURL to send HTTP requests to http://localhost:8080. The load balancer will distribute these requests to the backend servers based on the implemented logic.


Learning Resources

If you're new to Python and Flask, here are some resources to help you get started:

    Python Documentation: Official documentation for Python, including tutorials and guides for beginners.
    Flask Documentation: Official documentation for Flask, providing comprehensive guides and examples.
    Flask Mega-Tutorial: A popular tutorial series by Miguel Grinberg that covers Flask in-depth, suitable for beginners.




OUTPUTS:

FIRST TERMINAL

![image](https://github.com/DeBenign/load_balancer/assets/95944367/95fa9fca-8155-46c7-970d-286162f298e2)

SECOND TERMINAL
![image](https://github.com/DeBenign/load_balancer/assets/95944367/4e884458-a201-4ee6-be21-0c5673a183fd)

THIRD TERMINAL (WEB BROWSER)
![image](https://github.com/DeBenign/load_balancer/assets/95944367/41ddb62e-e38b-4c4a-9594-3337ce3cb7e4)


THE ONLY DRAWBACK IN THE PROGRAM IS THAT AFTER HITTING THE SERVERS SEVERALLY (COUPLE OF TIMES). ALL SERVERS FAIL WITHOUT WAKING UP UNTIL YOU RESTART THE WHOLE PROCESS AGAIN.
![image](https://github.com/DeBenign/load_balancer/assets/95944367/55ac80ad-7697-43be-9a5e-df87c9c506eb)
