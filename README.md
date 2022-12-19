<h1 align="center">
    <img src=".github/assets/shinigamicli_logo.jpg" />
    <br />
    Shinigami CLI
</h1>

Basic CLI showing off the [Shinigami](https://github.com/shinigamilib) library

Available commands:
```
-h, --help      |  Help menu
-i, --image     |  Docker image to generate
-v, --version   |  Version of the Docker image
-b, --build     |  Build the Dockerfile after generation
```

## Example(s)

This command will generate a Dockerfile for Ubuntu 22.04, but won't build the Docker image
```bash
python3 main.py -i "ubuntu" -v "22.04"
```

This command will build a Docker image running Python 3.8 and generate the Dockerfile
```bash
python3 main.py -i "python" -v "3.8" -b
```