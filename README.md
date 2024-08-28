# 📦 DreamWeaver.AI Streamlit App Starter Kit

An AI-powered sleep app designed to help you analyze and improve your sleep quality through advanced AI recommendations.

## Setup Instructions

### 1. Create and Activate a Virtual Environment

First, create a virtual environment:

```bash
python -m venv dw_venv
```

Activate the environment:

- **Windows:**

    ```bash
    .\dw_venv\Scripts\activate
    ```

- **macOS/Linux:**

    ```bash
    source dw_venv/bin/activate
    ```

### 2. Install Requirements

Install the necessary dependencies:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Application

To start the application, run the following command:

```bash
python -m streamlit run app.py
```

## Secrets Configuration

To keep your API keys and other sensitive information secure, add them to the `secrets.toml` file.

**Example `secrets.toml` Configuration:**

```toml
[general]
GOOGLE_API_KEY = "your_api_key"
```

## Deployment

### Deploying on Streamlit Cloud

1. Visit the Streamlit sharing platform:

   [Streamlit Cloud](https://share.streamlit.io/)

2. Click the **Create App** button on the top right.

3. Choose **Yup, I have an app**.
![Deployment Step 1](docs/images/1.png)
*Figure 1: Selecting the repository and branch.*

4. Select the appropriate repository, branch, and starting script (`app.py`).
![Deployment Step 2](docs/images/2.png)
*Figure 2: Reviewing deployment settings.*

5. Your app will be deployed and accessible via a public URL.

## GitHub Codespaces

You can also launch this project in GitHub Codespaces for a seamless development experience:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/app-starter-kit?quickstart=1)

## Further Reading

Explore more about this project:

- [Resource 1](#)
- [Resource 2](#)
- [Resource 3](#)