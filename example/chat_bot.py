from common_utilities.pickle_database import PickleDatabase
from common_utilities.string_utilities import string_from_file
from credentials.secrets_reader import read_secret
from openai import OpenAI
import argparse
import os


class ChatBot:
    def __init__(self, config: dict, persistent_store_path: str):
        os.makedirs(persistent_store_path, exist_ok=True)

        self.model = config['model']
        self.client = OpenAI(
            api_key=config['api_key'],
            organization=config['organization'],
            project=config['project'])
        self.database = PickleDatabase(
            os.path.join(persistent_store_path, 'database.pkl'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.database.save()

    def purge(self):
        self.database.clear()

    def chat(self, chat_id: str, message: str):
        previous_response_id = self.database.get(chat_id)

        response = self.client.responses.create(
            model=self.model,
            input=message,
            previous_response_id=previous_response_id,
            store=True)

        self.database[chat_id] = response.id
        return response.status, response.output_text


def purge_database(persistent_store_path: str):
    os.makedirs(persistent_store_path, exist_ok=True)
    database = PickleDatabase(os.path.join(persistent_store_path, 'database.pkl'))
    database.clear()
    database.save()


def main():
    arg_parser = argparse.ArgumentParser(description="OpenAI chat bot.")

    arg_parser.add_argument(
        "--chat-id", type=str,
        help="The chat ID")

    arg_parser.add_argument(
        "--chat-input", type=str,
        help="Chat message or path to a file containing one")

    arg_parser.add_argument(
        "--purge-database", action="store_true", default=False)

    arg_parser.add_argument(
        "--organization", type=str,
        help="OpenAI organization ID")

    arg_parser.add_argument(
        "--project", type=str,
        help="OpenAI project ID")

    arg_parser.add_argument(
        "--model", type=str, default='gpt-4o',
        help="OpenAI model to use")

    arg_parser.add_argument(
        "--api-key-file", type=str, default='example_openai.key',
        help="Filename of the API key secret in the credentials directory")

    arg_parser.add_argument(
        "--persistent-store-path", type=str,
        default=os.path.join(os.path.expanduser('~'), '.mlSandbox'))

    args = arg_parser.parse_args()

    if args.purge_database:
        purge_database(args.persistent_store_path)
        return

    if not args.chat_id or not args.chat_input:
        arg_parser.error("--chat-id and --chat-input are required for chat mode")

    if not args.organization or not args.project:
        arg_parser.error("--organization and --project are required for chat mode")

    if os.path.isfile(args.chat_input):
        message = string_from_file(args.chat_input)
    else:
        message = args.chat_input

    config = dict(
        organization=args.organization,
        project=args.project,
        model=args.model,
        api_key=read_secret(args.api_key_file))

    with ChatBot(config=config,
                 persistent_store_path=args.persistent_store_path) as bot:

        status, result = bot.chat(args.chat_id, message)

        print(f'Status: {status}')
        print(f'Result:\n {result}')


if __name__ == "__main__":
    main()
