from loguru import logger

host = "159.69.151.133"
port = 5056
user = "padawan_user_76"
password = "18011992Sev"
db_name = "qa_ddl_34_76"

if db_name != "qa_ddl_34_76":
    raise ValueError(logger.error("Check database name."))

