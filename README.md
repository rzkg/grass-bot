# GetGrass

**For educational purposes only.**

Automated bot for creating accounts, farming points, and interacting with the GetGrass API. This documentation will guide you on how to install and run GetGrass using Docker.

## Installation

### 1. Install Docker
To run this project, you need to have Docker installed on your system. Here’s how to install Docker on **Ubuntu 22.04**:

1. **Update Your System Packages**
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Install Required Dependencies**
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **Add Docker’s Official GPG Key**
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. **Add Docker Repository**
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. **Install Docker**
   ```bash
   sudo apt update
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

6. **Start and Enable Docker**
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

7. **Verify Installation**
   ```bash
   docker --version
   ```
   You should see the Docker version displayed, confirming the installation.

### 2. Install Docker Compose
To install Docker Compose, run:
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Verify the installation:
```bash
docker-compose --version
```

## Clone the Repository
Clone the GetGrass project from GitHub and navigate to the project directory:
```bash
git clone https://github.com/staryone/grass-bot.git
cd grass-bot
```

### Module Installation
Make sure to have all required Python modules installed (if running locally, outside of Docker). However, the Docker setup will handle dependencies for you.

## Register on GetGrass
Sign up using the following referral link:
[Register on GetGrass](https://app.getgrass.io/register/?referralCode=M7a5kjyj1TdgU9I) (use this link to register!)

## How to Use

### Getting Your User ID
1. **Login to GetGrass**  
   Visit [https://app.getgrass.io](https://app.getgrass.io) and log in to your account.

2. **Retrieve Your User ID**
   - Open the browser's Developer Tools (usually by right-clicking the page and selecting "Inspect", then navigating to the "Console" tab).
   - Type the following command in the Console:
     ```javascript
     localStorage.getItem('userId')
     ```
   - If you receive a warning that says “Don’t paste code into the DevTools Console”, type `allow pasting` and press ENTER.
   - Run the command again:
     ```javascript
     localStorage.getItem('userId')
     ```
   - Copy the `userId` that is displayed.

## Usage Instructions

1. **Fill Your Proxy Information**
   - Open `proxies.txt` and fill in your proxy details, one proxy per line.

2. **Edit Your User ID**
   - Open `users_id.txt` and add your User ID. Each line should contain one account’s User ID.

## Usage Commands

### Build the Docker Image
```bash
docker-compose build
```

### Run the Script
```bash
docker-compose up
```

### View Logs
To monitor the logs and see the bot in action, use:
```bash
docker logs -f getgrass_app
```

This will keep the logs open and show you real-time activity from the container.

**Enjoy using GetGrass! Feel free to open an issue on GitHub if you encounter any problems.**
