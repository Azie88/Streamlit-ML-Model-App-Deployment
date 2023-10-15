# Streamlit-ML-Model-App-Deployment
Creating an app for a ML regression model to allow non-technical people to interact with it.

## Project Outline 📄
- Exploring streamlit framework
- Building basic UI with inputs and outputs
- Importing the model with other requirements (Scaler, encoder etc.)
- Retrieving and processing input values
- Passing processed data through ML model to predict
- Format prediction output and send to UI

## Summary

| Code      | Name        | Published Article |
|-----------|-------------|:-------------:|
| LP4 | Sales Prediction with Streamlit |  [Sales Prediction article]() |


## Installation

To setup and run this project you need to have [`Python3`](https://www.python.org/) installed on your system. Then you can clone this repo. At the repo's root, use the code from below which applies:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

    **NB:** For MacOs users, please install `Xcode` if you have an issue.

You can then run the app (still at the repository root) with:

      streamlit run src/app.py

Ideally, it should open your browser with the app in a new tab, if it doesn't, type this address in your browser:

      http://10.13.8.134:8501

## Screenshots 🖼️

<table>
    <tr>
        <th> Gradio App </th>
    </tr>
    <tr>
        <td><img src="screenshots\screenshot 1.png"/></td>
    </tr>
    <tr>
        <td><img src="screenshots\screenshot 2.png"/></td>
    </tr>
</table>

## Contact Information

- [Andrew Obando](https://www.linkedin.com/in/andrewobando/)
