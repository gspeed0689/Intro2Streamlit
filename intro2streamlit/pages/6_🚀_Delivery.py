import streamlit as st

st.title("Delivery Options")

delivery_md = """
You have several delivery options for distributing your Streamlit app. 

1. Local Python program with `streamlit run app.py`
2. The Streamlit community cloud, where this app is currently running on presentation day.
3. Self hosting

## Streamlit community cloud

Free hosting, just point the website to a GitHub Repo, tell it which Python file is the home. 

This is probably not GDPR compliance. 

## Self-Hosting

I prefer self-hosting, my Vesuvius example is hosted on an AWS EC2 VM. 
The web server is nginx that reverse proxies to the Streamlit app running on localhost. 
The Streamlit app is running as a SystemD service with the following service definition template:

    [Unit]
    Description=Streamlit App
    After=network.target

    [Service]
    User={no logon user}
    WorkingDirectory=/home/{no logon user}/{app folder}
    ExecStart=/full/path/to/virtual/environment/bin/python main.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

The `main.py` in the config above is in the `WorkingDirectory`.
"""

st.markdown(delivery_md)

st.link_button("Go to the community hosting website", "https://share.streamlit.io/")