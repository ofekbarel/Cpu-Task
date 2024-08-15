# Cpu-HA

In this application, which is written in Python, we have built a monitor application that accesses the CPU usage and performs actions accordingly.
First of all we will use the libraries:
 psutil
 smtplib
 time
 logging
 os

If the percentage of processor usage is higher than 80 percent, an alert will be sent to the email we will define in the code.




## steps for Mac


1.  ## install email-to with pip
        pip3 install email-to, smtplib, psutil




2.  ## add environment variable for the email password

    echo "export EMAIL_PASSWORD=..." >> ~/.zshrc   #add env variable




3.  ## Run the Code

    python3 Cpu.py




4. ## Check cpu_usage.log
