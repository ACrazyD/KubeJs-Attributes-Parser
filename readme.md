# KubeJS Attributes Parser

## Overview

The KubeJS Attributes Parser is a Python script designed to filter and organize data from JSON files related to Minecraft mods. It provides a customizable way to filter items and fluids based on regular expressions and outputs the results in a structured manner.

Im rusty as JavaScript - so expect some odditys as i did use some AI to fix things when i got stuck.

## Features

- **Filtering:** The script allows users to filter data based on regular expressions, both for regular filtering and removal filtering.
- **Organization:** Filtered data is organized into separate text files for each mod, keeping the 'mod_id:item_id' format.

## Requirements

- Python 3.x
- Required Python modules: `json`, `os`, `re`, `shutil`, `time`, `tqdm` - Script *Should* install if missing, apon request of user
- [ProbeJS](https://www.curseforge.com/minecraft/mc-mods/probejs) mod installed in the Minecraft client to generate the required data files for input.

- Tested with output files for fluid/items on 1.20.2 Only - Other Versions May Not Work


## How to Use

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed.
3. Run the script in a terminal or command prompt.
4. Follow the on-screen instructions to select input and output folders and apply filters.

## License

This script is licensed under the [MIT License](LICENSE.md). Feel free to use, modify, and distribute it as needed.
## Issues

If you encounter any issues or have suggestions, please create an issue [here](https://github.com/acrazyd/kubejsattributesparser/issues).

