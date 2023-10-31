
import asyncio
from threading import Thread
from notebook.app import JupyterNotebookApp
from asgiref.sync import sync_to_async

NOTEBOOK_LOOP = None

# def launch_instance():
#     JupyterNotebookApp.launch_instance(argv=["notebook"])
JupyterNotebookApp.launch_instance(argv=["notebook"])
# print("In init")
# async def start():
#     print("Started func")
#     return sync_to_async(main)()

# def run_loop():
#     global NOTEBOOK_LOOP
#     NOTEBOOK_LOOP = asyncio.new_event_loop()
#     NOTEBOOK_LOOP.run_until_complete(start())

# Thread(target=run_loop).start()
# # NOTEBOOK_LOOP.call_soon_threadsafe(NOTEBOOK_LOOP.stop)