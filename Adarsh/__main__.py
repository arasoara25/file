# (c) adarsh-goel
import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from .bot import StreamBot
from .vars import Var
from aiohttp import web
from .server import web_server
from .utils.keepalive import ping_server
from Adarsh.bot.clients import initialize_clients

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

ppath = "Adarsh/bot/plugins/*.py"
files = glob.glob(ppath)
loop = asyncio.get_event_loop()


async def start_services():
    logging.info('------------------- Initalizing Telegram Bot -------------------')
    await StreamBot.start()
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    logging.info("------------------------------ DONE ------------------------------")
    logging.info(
        "---------------------- Initializing Clients ----------------------"
    )
    await initialize_clients()
    logging.info("------------------------------ DONE ------------------------------")
    logging.info('--------------------------- Importing ---------------------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"Adarsh/bot/plugins/{plugin_name}.py")
            import_path = ".plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["Adarsh.bot.plugins." + plugin_name] = load
            logging.info("Imported => " + plugin_name)
    if Var.ON_HEROKU:
        logging.info("------------------ Starting Keep Alive Service ------------------")
        asyncio.create_task(ping_server())
    logging.info('-------------------- Initalizing Web Server -------------------------')
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if Var.ON_HEROKU else Var.BIND_ADRESS
    await web.TCPSite(app, bind_address, Var.PORT).start()
    logging.info('----------------------------- DONE ---------------------------------------------------------------------')
    logging.info('----------------------- Service Started -----------------------------------------------------------------')
    logging.info('                        bot =>> {}'.format((await StreamBot.get_me()).first_name))
    logging.info('                        server ip =>> {}:{}'.format(bind_address, Var.PORT))
    logging.info('                        Owner =>> {}'.format((Var.OWNER_USERNAME)))
    if Var.ON_HEROKU:
        logging.info('                        app runnng on =>> {}'.format(Var.FQDN))
    logging.info('---------------------------------------------------------------------------------------------------------')
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except Exception as e:
        logging.error(f"An error occurred during bot startup: {e}", exc_info=True)
    finally:
        logging.info('----------------------- Service Stopped -----------------------')
