# AI Chatbot with OpenAI API and Django
This project is a web-based chatbot that uses OpenAI's GPT-3 language processing API to provide natural language responses to user queries. The chatbot is built using the Django web framework and is designed to be deployed to a production.

The project includes a README file with detailed instructions on how to install and use the chatbot, as well as troubleshoot common issues. It also includes information on potential future improvements and credits to resources used in the development of the project.

The chatbot's user interface is built using HTML, CSS, and JavaScript, and is designed to be responsive and user-friendly. Users can input their queries and view the chatbot's responses in real-time.

Overall, this project serves as an educational introduction to the world of chatbots and natural language processing, while also providing potential practical applications such as customer service and automated responses to frequently asked questions on websites or social media platforms.

## Getting Started
### Prerequisites:
  1. Python 3.6 or higher
  2. Django 3.2 or higher
  3. OpenAI API key
### Installing:
  1. Clone this repository to your local machine.
  2. Create a virtual environment for the project using virtualenv.
  3. Activate the virtual environment and install the required packages using pip install -r requirements.txt.
  Copy the example_config.py file to config.py and update the values for OPENAI_API_KEY and DEBUG as needed.
### Usage:
  * Run the development server using python manage.py runserver.
  * Visit http://127.0.0.1:8000/ in your web browser to access the chatbot.
  
### Contributing
  **Contributions to this project are welcome! If you would like to contribute, please follow these steps:**
  * Fork this repository.
  * Create a new branch with your changes: git checkout -b my-new-branch.
  * Make your changes and commit them: git commit -am 'Add some feature'.
  * Push to the branch: git push origin my-new-branch.
  * Submit a pull request.
  * Please ensure that your code follows the existing coding style and that your changes do not break the existing functionality.
  
### Acknowledgements
* OpenAI for providing the cutting-edge language processing capabilities through their API.
* Django for providing the web framework used in this project.

### Disclaimer
This project is for educational purposes only. The chatbot created in this project is not intended to be used for any commercial or production purposes. The chatbot may not always provide accurate or reliable responses, and the author of this project is not responsible for any consequences that may arise from the use of the chatbot. Use the chatbot at your own risk.

### Troubleshooting
If you run into any issues while setting up or using the chatbot, here are some common problems and their solutions:
* **OpenAI API key not working:** Make sure you have a valid OpenAI API key and that it is correctly configured in config.py. You can check the status of your API key by visiting the OpenAI website.
* **Chatbot not responding:** If the chatbot is not responding to user queries, check the server logs for any errors or exceptions. You can also try running the chatbot locally with python manage.py runserver to see if the problem is with the server or the OpenAI API.
* **Static files not loading:** If the chatbot interface is not loading properly, make sure that the STATIC_URL setting in settings.py matches the URL path where your static files are hosted. You can also try running python manage.py collectstatic to ensure that all static files are properly collected and stored in the STATIC_ROOT directory.

### Future Improvements
Here are some ideas for future improvements to this project:
* Improve the user interface of the chatbot, making it more intuitive and user-friendly.
* Implement more advanced natural language processing capabilities, such as sentiment analysis or language translation.
* Integrate the chatbot with other APIs or services, such as weather or news APIs.
* Allow users to customize the chatbot's responses based on their preferences or settings.


## Screenshot

A screenshot of the Django AI chatbot is shown below:![Screenshot 2023-05-05 011424](https://user-images.githubusercontent.com/117152309/236316986-5cc4b790-3349-4972-aa2f-98652a8684eb.png)
