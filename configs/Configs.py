import os


class Config:
    def __init__(self):
        self.base_url = 'https://gpushare.com'
        # Get secret variables from environment
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('PASSWORD')


if __name__ == '__main__':
    config = Config()
    print(config.username, config.password)