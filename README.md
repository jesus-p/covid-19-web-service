# COVID-19 Web Application
Our group created this Google App Engine to display live COVID-19 stats for several countries, and graphing those statistics live as requested.
<br /> <br />
The group created a COVID-19 Death Rate Model which is displayed for each country in our case study and demo.
<br /> <br />
Johns Hopkins maintains a dataset of COVID-19 confirmed cases and have made it free in the form of a CSV file for academic and research use. In an effort to make the data easier to query and analyze, Google Cloud is making it publicly available in BigQuery. BigQuery is used on our application to fetch the latest data.
<br /> <br />
Google Firebase is also implemented in our project as a database back-end used to store meta-data such as the number of times the website is visited.

## Installation
#### Before you begin
* In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
* Go to project selector
* Make sure that billing is enabled for your Cloud project. Learn how to check if billing is enabled on a project.
* Enable the Cloud Build API.
* Enable the API
* Install and initialize the Google Cloud CLI.

#### Initialize your App Engine app with your project and choose its region:

```bash
gcloud app create --project=covid-19-web-service
```

When prompted, select the region where you want to locate your App Engine application.
Caution: You cannot change an app's region once it has been set.

#### Install the following prerequisites:
* Download and install Git.
* Run the following command to install the gcloud component that includes the App Engine extension for Python:
```bash
gcloud components install app-engine-python
```
Prepare your environment for Python development. It is recommended that you have the latest version of Python, pip, and other related tools installed on your system. For instructions, refer to the Python Development Environment Setup Guide.

#### Download the COVID-19 Web Service Project
1. Clone the COVID-19 app repository to your local machine.

```bash
git clone https://github.com/jesus-p/covid-19-web-service
````
2. Change to the directory that contains the sample code.


## Deploying Application
Deploy the COVID-19 app by running the following command from the covid directory:

```bash
gcloud app deploy
```
## Launching Web App
Launch your browser to view the app at (can be different since I'm currently hosting this name)
<https://covid-19-web-service.r.appspot.com>
or you can use the following command:
```bash
gcloud app browse
````

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
