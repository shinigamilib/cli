<h1 align="center">
    <img src="https://raw.githubusercontent.com/shinigamilib/cli/main/assets/shinigamicli_logo.jpg" />
</h1>

Basic CLI showing off the [Shinigami](https://github.com/shinigamilib) library

## Usage

You can install the cli via pip:
```bash
pip install shinigami-cli
```

Available commands:
```
-h,  --help      |  Help menu
-i,  --image     |  Docker image to generate
-v,  --version   |  Version of the Docker image
-b,  --build     |  Build the Dockerfile after generation
-rm, --remove    |  Remove the Dockerfile in your current working directory
```

## Example(s)

This command will generate a Dockerfile for Ubuntu 22.04, but won't build the Docker image
```bash
shinigami-cli -i "ubuntu" -v "22.04"
```

This command will build a Docker image running Python 3.8 and generate the Dockerfile
```bash
shinigami-cli -i "python" -v "3.8" -b
```

Removes the Dockerfile in your current working directory
```bash
shinigami-cli -rm
```