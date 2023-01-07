"""
    Project: Shinigami CLI (https://github.com/shinigamilib/cli)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
    License: BSD 2-Clause
"""

import argparse

from shinigami.shinigami import Shinigami

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', help="Docker image to generate", default=None, required=False)
parser.add_argument('-v', '--version', help="Version of the Docker image", default=None, required=False)
parser.add_argument('-b', '--build', help="Build the Dockerfile after generation", action='store_true', default=False, required=False)
parser.add_argument('-rm', '--remove', help="Remove the Dockerfile in the current working directory", action='store_true', default=False, required=False)
args = parser.parse_args()

v = "0.1.4"

banner = \
f"""
 _____ _     _       _                       _   _____  _     _____ 
/  ___| |   (_)     (_)                     (_) /  __ \| |   |_   _|
\ `--.| |__  _ _ __  _  __ _  __ _ _ __ ___  _  | /  \/| |     | |  
 `--. \ '_ \| | '_ \| |/ _` |/ _` | '_ ` _ \| | | |    | |     | |  
/\__/ / | | | | | | | | (_| | (_| | | | | | | | | \__/\| |_____| |_ 
\____/|_| |_|_|_| |_|_|\__, |\__,_|_| |_| |_|_|  \____/\_____/\___/ 
                        __/ |                                       
                       |___/                                        

Shinigami CLI | v{v}
Author: https://github.com/azazelm3dj3d
Learn more: https://github.com/shinigamilib/cli
"""

class ShinigamiCli:
    def run():
        print(banner)

        if args.remove:
            return Shinigami().remove_dockerfile()

        if args.build:
            return Shinigami(lang_os=str(args.image), version=str(args.version), build={args.build}).generate_dockerfile()

        if args.image != None or args.version != None:
            return Shinigami(lang_os=str(args.image), version=str(args.version), verbose=True).generate_dockerfile()
        else:
            print("Missing one or more arguments: --image, --version (you can use -h if you need help)")

if __name__ == '__main__':
    ShinigamiCli.run()