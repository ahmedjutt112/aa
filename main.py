urls = "https://app.beefy.finance/"

from pywebcopy import save_website
save_website(
url=urls,
project_folder="E://savedpages//",
project_name="my_site",
bypass_robots=True,
debug=True,
open_in_browser=True,
delay=None,
threaded=False,
)