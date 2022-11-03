import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13782543"))
    API_HASH = os.environ.get("API_HASH", "883e3fce7c3d9d8cfc28c9b9ff51a859")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5726864350:AAElXLDPLFUMs6Z7gISC0TuPXNtgwO41fyI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBu1sPPaQsroNemQux8S3eYAW0ur6o827HAktTSLqccimyBSjznBp-h7nJiooQqVwH6ON0JugvNyDQ_7IZ1lY_ewZWgE33oCmtDNd_R8J9j3ef4n9y9oBr7N2nxH-ke6K1Ldskzt3Qs7j_7f0W5UQYahnnJe-6UDTK9bkdmOE-gxRLnSkvmfDkNWdHEfqi5J9ia3eQE0gqHFlks4pSNkMk47VQgGsqx8CY8Qt9Ym22u3A09H-BQYlG8VDddKJRRU1SnDWGHE_smCaFP_YQ8hFm9KLGSmTy9HBpo-4hua6fuz4T3j5PThvgkN1hpwxIlD4G1JaKbbXYkDs0d5Vx70TLQcg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "ENABLE")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NatsuMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "natsumeown") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "evzesda") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/5d1c316818314de9af692.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1606068238")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
