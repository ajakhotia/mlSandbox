from credentials.secrets_reader import read_secret

openai_credentials = dict(
    organization='<FILL-ME>',

    example_assistant=dict(
        project='<FILL-ME>',
        assistant='<FILL-ME>',
        api_key=read_secret('example_openai.key'),
    )
)
