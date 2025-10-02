import os
import time

def capture_screenshot(page, name="screenshot"):
    # Set the folder path to the root directory's screenshots folder
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'screenshots')

    # Ensure the screenshots folder exists at the root level
    os.makedirs(folder, exist_ok=True)

    # Add a timestamp to the screenshot name
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(folder, f"{name}_{timestamp}.png")

    # Capture the screenshot and save it at the specified path
    page.screenshot(path=path)

    # Return the path where the screenshot was saved
    return path
