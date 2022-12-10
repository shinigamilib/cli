import argparse

from shinigami.shinigami import Shinigami

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', help="Docker image to generate", default=None, required=True)
parser.add_argument('-v', '--version', help="Version of the Docker image", default=None, required=True)
parser.add_argument('-b', '--build', help="Build the Dockerfile after generation", action='store_true', default=False, required=False)
args = parser.parse_args()

v = "0.1.0"

class CLI:
    def run() -> Shinigami:

        print(f"\nStience | v{v} (https://github.com/stience)\n")

        if args.build:
            return Shinigami(lang_os=str(args.image), version=str(args.version), build={args.build})
        else:
            return Shinigami(lang_os=str(args.image), version=str(args.version))

if __name__ == '__main__':
    CLI.run().generate_dockerfile()
    print("The Dockerfile should now be in the current working directory!\n")