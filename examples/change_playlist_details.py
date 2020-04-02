import argparse
import logging
import os

import spotipy
import spotipy.util as util

logger = logging.getLogger('examples.change_playlist_details')
logging.basicConfig(level='DEBUG')

scope = 'playlist-modify-public playlist-modify-private'


def get_args():
    parser = argparse.ArgumentParser(description='Modify details of playlist')
    parser.add_argument('-u', '--username', required=False,
                        default=os.environ.get('SPOTIPY_CLIENT_USERNAME'),
                        help='Username id. Defaults to environment var')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Playlist id to alter details')
    parser.add_argument('-n', '--name', required=False,
                        help='Name of playlist')
    parser.add_argument('--public', action='store_true', required=False,
                        help='Include param if playlist is public')
    parser.add_argument('--private', action='store_false', required=False,
                        default=None,
                        help='Include param to make playlist is private')
    parser.add_argument('-c', '--collaborative', action='store_true',
                        required=False, default=None,
                        help='Include param if playlist is collaborative')
    parser.add_argument('-i', '--independent', action='store_false',
                        required=False, default=None,
                        help='Include param to make playlist non collaborative')
    parser.add_argument('-d', '--description', default=None, required=False,
                        help='Description of playlist')
    return parser.parse_args()


def main():
    args = get_args()
    token = util.prompt_for_user_token(args.username, scope)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_change_details(
            args.username, args.playlist, name=args.name,
            public=args.public or args.private,
            collaborative=args.collaborative or args.independent,
            description=args.description)
    else:
        logger.error("Can't get token for %s", args.username)


if __name__ == '__main__':
    main()
