import psutil  #CPU Usage
import smtplib #Send Emails
import time
import logging
import os



# Login Setup
logging.basicConfig(filename='cpu_usage.log', level=logging.INFO)



# Email Func
def send_alert(email_recipient):
    try:
        sender_email = "ofekbarel11@outlook.com"
        sender_password = os.getenv('EMAIL_PASSWORD')
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)  #Gmail Port
        server.starttls()
        server.login(sender_email, sender_password)
        message = "Subject: CPU Alert\n\nAlert: CPU usage exceeded 80%."
        server.sendmail(sender_email, email_recipient, message)
        server.quit()


        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Error sending email: {e}")


# Monitor Func
def monitor_cpu(threshold=80):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"Current CPU usage: {cpu_usage}%")
        
        if cpu_usage > threshold:
            send_alert("ofekbarel10@gmail.com") 
        
        time.sleep(10)  
        

monitor_cpu()

