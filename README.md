# DWT - AI Document Assistant

DWT is a simple AI tool that helps you process documents. It has two main features: 
1. Extracting information from ID cards. (EasyOCR 25M)
2. Chatting with text. (Qwen 2.5 3B)

local AI models to ensure your data stays private and secure.

# Features
- Chat with Data: Past any text into the `Context` box, and then ask the Ai questions about it.
- Identity Extraction: Upload the base64 of a picture of an ID card (Arabic or English). The system will return the text into JSON format.
- Local AI: Runs locally on your machine using Docker. So make sure docker is already installed.

# Prerequisites
- [Docker](https://docs.docker.com/engine/install/)
- A Read Hugging Face Token.
- Download the following
```bash
# Debian or any system based on it such as Ubuntu 
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Arch or any system based on it such as EndeavourOS
sudo pacman -S nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Any other system search it
```

# Installation
1. Clone the Repository
```bash
git clone https://github.com/Khaled-Saleh-KL1/DWT.git
cd DWT
```

2. Configure Environment
Create a file named `.env` inside the src folder. Add your Hugging Face token and the app details.

3. Run with Docker
```bash
cd docker
docker-compose up --build
```

# How to use
Once the terminal says that the application is running, open your web browser and go to:
`http://localhost:8000/GUI` and enjoy :)
