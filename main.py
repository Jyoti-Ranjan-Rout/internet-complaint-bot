from internet import InternetSpeedTwitterBot 
import time 
import os 
from dotenv import load_dotenv
import smtplib
from google import genai

load_dotenv()

# Credidentals :- 

gemini_api = os.getenv("API")
my_email = os.getenv("EMAIL")
passwd = os.getenv("PASS")
receiver_email = os.getenv("EMAIL_R")

# Data_ Containers :- 

MIN_DOWN = 20    # Mbps
MIN_UP = 5  
service_reports = []

# Class Work :- 

service = InternetSpeedTwitterBot()
service.open_speedtest()
time.sleep(3)
service.internet_speed()

# The Work :- 

if  service.down <= MIN_DOWN  or  service.up <= MIN_UP  :
    service_reports.append([service.down,service.up])
    time.sleep(120)
    service.internet_speed()

    if service.down <= MIN_DOWN  or  service.up <= MIN_UP  :
        service_reports.append([service.down,service.up])
        time.sleep(120)
        service.internet_speed()

        if service.down <= MIN_DOWN  or  service.up <= MIN_UP  :
            service_reports.append([service.down,service.up])

            prompt = f"""You are a professional customer support email writer.

            Generate a concise, professional, and well-structured email to my Internet Service Provider's customer care.

            The variable `service_reports` contains the internet speed test results.

            {service_reports}

            Each inner list represents one speed test conducted 2 minutes apart.

            Analyze the values in `service_reports` and write a professional complaint email.

            Requirements:
            - Include a professional subject line.
            - Mention that the issue was verified through three consecutive speed tests.
            - Reference the measured speeds from `service_reports`.
            - State that the poor connection is affecting online meetings and work.
            - Politely request the support team to investigate and resolve the issue.
            - Keep the email under 150 words.
            - Do not invent or modify any values.
            - Return only the email body and subject.
            - Give the name as the {receiver_email} """

            client = genai.Client(api_key=gemini_api)
            response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

            email_msg = response.text
            

            with smtplib.SMTP("smtp.gmail.com",587) as connection : 
                connection.starttls()
                connection.login(user=my_email,password=passwd)
                connection.sendmail(from_addr=my_email , 
                    to_addrs="sahoopranil@gmail.com" ,
                    msg = f"Subject: Internet Speed Complaint\n\n{email_msg}"
                )
            

