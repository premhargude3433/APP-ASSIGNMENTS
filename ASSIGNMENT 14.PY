import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Display different logging levels
logging.debug("This is a debug message")
logging.info("This is an information message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("Logging completed successfully!")
