"""
    Owner: azazelm3dj3d (https://github.com/azazelm3dj3d)
    Project: Shinigami CLI
    License: BSD 2-Clause
"""

import argparse

from shinigami.shinigami import Shinigami

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', help="Docker image to generate", default=None, required=True)
parser.add_argument('-v', '--version', help="Version of the Docker image", default=None, required=True)
parser.add_argument('-b', '--build', help="Build the Dockerfile after generation", action='store_true', default=False, required=False)
args = parser.parse_args()

v = "0.1.2"

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
Owner: https://github.com/azazelm3dj3d
"""

class CLI:
    def run() -> Shinigami:
        if args.build:
            return Shinigami(lang_os=str(args.image), version=str(args.version), build={args.build})
        else:
            return Shinigami(lang_os=str(args.image), version=str(args.version), verbose=True)

if __name__ == '__main__':
    print(banner)
    CLI.run().generate_dockerfile()