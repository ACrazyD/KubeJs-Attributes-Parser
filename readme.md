# KubeJS Attributes Parser

## Overview

The KubeJS Attributes Parser is a Python script designed to filter and organize data from JSON files created with ProbeJS Dumps. It provides a customizable way to filter items and fluids based on regular expressions and outputs the results in a structured manner.

Im rusty as JavaScript - so expect some odditys as i did use some AI to fix things when i got stuck.

## Features

- **Filtering:** The script allows users to filter data based on regular expressions, both for regular filtering and removal filtering.
- **Organization:** Filtered data is organized into separate text files for each mod, keeping the 'mod_id:item_id' format.

## Requirements

- Python 3.x
- Required Python modules: `json`, `os`, `re`, `shutil`, `time`, `tqdm` - Script *Should* install if missing, apon request of user
- [ProbeJS](https://www.curseforge.com/minecraft/mc-mods/probejs) mod installed in the Minecraft client to generate the required data files for input.
- [KubeJS](https://www.curseforge.com/minecraft/mc-mods/kubejs) Depentent for ProbeJS

- Tested with output files for fluid/items on 1.20.2 Only - Other Versions May Not Work


## How to Use

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed.
3. Run the script in a terminal or command prompt.
4. Follow the on-screen instructions to select input and output folders and apply filters.

## Regex Filtering:

The KubeJS Attributes Parser script supports powerful regex filtering options for refining the extracted data. When prompted for filtering options, you can provide regular expressions to customize the filtering process.

    Regular Filtering: Enter a regex filter to include items that match the specified pattern. For example, to filter items containing the word "sword" in their ID, you can use the regex filter: sword.

Enter the regex filter for regular filtering (default: .*):

Removal Filtering: To exclude specific items from the output based on a regex pattern, use the removal filter. By default, the removal filter is set to ^$, which essentially removes nothing. Adjust this filter to exclude items that match the specified pattern. For instance, to exclude items with IDs starting with "debug," you can use the removal filter: ^debug.

    Enter the regex filter for removal filtering (default: ^$):

Examples:

    Include all items with "sword" in their ID:
        Regular Filter: sword

    Exclude items with IDs starting with "debug":
        Removal Filter: ^debug

## License

This script is licensed under the [MIT License](LICENSE.md). Feel free to use, modify, and distribute it as needed.
## Issues

If you encounter any issues or have suggestions, please create an issue [here](https://github.com/ACrazyD/KubeJs-Attributes-Parser/issues).
Or Contact us on [Discord](https://discord.gg/UMhmuKMb9N)

