import json
import sys

def generate_devcontainer(herramientas):
    extensions = []
    puertos = []
    install_commands = []

    if "redis" in herramientas:
        extensions.append("ms-azuretools.vscode-docker")
        puertos.append(6379)
        install_commands.append("redis-server")
    if "localstack" in herramientas:
        extensions.append("ms-azuretools.vscode-docker")
        puertos.append(4566)
        install_commands.append("localstack")
    if "mysql" in herramientas:
        extensions.append("ms-python.python")
        puertos.append(3306)
        install_commands.append("mysql-server")
    if "python" in herramientas:
        extensions.append("ms-python.python")
        install_commands.append("python3")

    devcontainer_json = {
        "name": "Devcontainer Personalizado",
        "dockerFile": "Dockerfile",
        "extensions": extensions,
        "forwardPorts": puertos,
        "postCreateCommand": " && ".join(install_commands)
    }

    with open(".devcontainer/devcontainer.json", "w") as f:
        json.dump(devcontainer_json, f, indent=4)

    with open(".devcontainer/Dockerfile", "w") as dockerfile:
      dockerfile.write("FROM mcr.microsoft.com/devcontainers/base:ubuntu\n")
      dockerfile.write("RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install " + " ".join(install_commands))

if __name__ == "__main__":
    herramientas = sys.argv[1].split(",")
    generate_devcontainer(herramientas)