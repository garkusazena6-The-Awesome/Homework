import logging
logging.basicConfig(level=logging.DEBUG,filename="logs.log",filemode="w",format="We have next login messange: %(name)s - %(levelname)s - %(message)s : %(asctime)s")
try:
    print(10/0)
except Exception:
    logging.exception("No.")
logging.info("Todays date")