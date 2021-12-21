# We want to import all the modules here so they are accessible after a 
# simple `import wmfdata`. 
# 
# First, we import `utils`, which should not depend on any other wmfdata modules.
from wmfdata import utils

# After importing `utils`, we import the low-level modules, which should not
# depend on wmfdata modules other than `utils`.
from wmfdata import (
    conda,
    hdfs
)

# After importing the low-level modules, we import the high-level modules,
# which should not depend on other high-level modules.
from wmfdata import (
    charting,
    hive,
    mariadb,
    metadata,
    presto,
    spark
)

try:
    remote = utils.check_remote_version(metadata.source, metadata.version)
    if remote['is_newer']:
        update_message = (
            "You are using wmfdata v{0}, but v{1} is available.\n\n" +
            "To update, run `pip install --upgrade git+{2}.git@release`.\n\n" +
            "To see the changes, refer to {2}/blob/release/CHANGELOG.md"
        ).format(metadata.version, remote['version'], metadata.source)
        utils.print_err(update_message)

# If the file with the version info is ever moved, or the code hosting changes, and so
# on, it will make all previous versions of the version check fail, so we should turn
# any errors into an understandable warning.
except:
    utils.print_err((
        "The check for a newer release of wmfdata failed to complete. Consider "
        "checking manually."
    ))
