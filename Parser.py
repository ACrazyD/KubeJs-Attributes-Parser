import json
import os
import re
import shutil
import time

# Function to apply regex filter to data
def apply_filter(data, regex_filter, is_removal_filter=False):
    try:
        compiled_filter = re.compile(regex_filter)
    except re.error as e:
        print(f'\033[91mError in regex filter: {e}\033[0m')
        return data

    if is_removal_filter:
        return [item for item in data if not compiled_filter.search(item['id'])]
    else:
        return [item for item in data if compiled_filter.search(item['id'])]

# Function to create an output folder with timestamp
def create_output_folder(output_directory, prefix):
    timestamp = time.strftime('%d%m%y_%H%M%S')
    folder_name = f'{prefix}_output_{timestamp}'
    output_subdirectory = os.path.join(output_directory, folder_name)
    os.makedirs(output_subdirectory, exist_ok=True)
    return output_subdirectory

# Function to copy a file
def copy_file(source_path, destination_directory, new_filename=None):
    if new_filename is None:
        base, extension = os.path.splitext(os.path.basename(source_path))
        new_filename = f'{base}_Copy{extension}'

    destination_path = os.path.join(destination_directory, new_filename)

    # Check if source and destination paths are the same
    if os.path.abspath(source_path) != os.path.abspath(destination_path):
        shutil.copyfile(source_path, destination_path)
        print(f'\033[95mCopied {os.path.basename(source_path)} to {destination_path}\033[0m')
    else:
        print(f'\033[93mSkipped copying {os.path.basename(source_path)} to {destination_path} (same file)\033[0m')

    time.sleep(1)  # Sleep for 1 second

# Function to clear the working folder
def clear_working_folder(working_directory):
    for file_name in os.listdir(working_directory):
        file_path = os.path.join(working_directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'\033[91mError while clearing the working directory: {e}\033[0m')

# Function to check and rescan the input folder for data files
def check_and_rescan_input_folder():
    available_data_files = [file for file in os.listdir(input_directory) if file.endswith('.json')]
    return available_data_files

# Function to run the script with user-selected or default folders
def run_script():
    global input_directory, output_directory, working_directory

    # Ask the user if they want to use default folders
    use_defaults = input('\033[94mDo you want to use default folders? (y/n): \033[0m').lower() == 'y'

    # Set default folders or let the user select folders
    if use_defaults:
        input_directory = 'input'
        output_directory = 'output'
        working_directory = 'working'
    else:
        input_directory = input('\033[94mEnter the path to the input folder: \033[0m').strip('"\'')
        output_directory = input('\033[94mEnter the path to the output folder: \033[0m').strip('"\'')
        working_directory = input('\033[94mEnter the path to the working folder: \033[0m').strip('"\'')

    # Create folders if they don't exist
    for directory in [input_directory, output_directory, working_directory]:
        os.makedirs(directory, exist_ok=True)

    while True:
        # Clear the working folder at the beginning of each run
        clear_working_folder(working_directory)

        # Check for available JSON data files in the input folder
        available_data_files = check_and_rescan_input_folder()

        # If no data files found, prompt the user to add at least one JSON file
        if not available_data_files:
            print('\033[91mNo JSON data files found in the selected input folder.')
            print('Please add at least one JSON file.\033[0m')
            input('Press Enter to rescan the input folder...')
            continue

        # If only one data file is found, automatically select it
        if len(available_data_files) == 1:
            json_file_path = os.path.join(input_directory, available_data_files[0])
            output_prefix = os.path.splitext(available_data_files[0])[0]
        else:
            # If multiple data files are found, prompt the user to select one
            print('\n\033[94mAvailable JSON data files:\033[0m')
            for idx, file in enumerate(available_data_files, start=1):
                print(f'{idx}. {file}')

            selection = input('\033[94mEnter the number corresponding to the JSON file to process: \033[0m')

            try:
                selection_idx = int(selection) - 1
                if 0 <= selection_idx < len(available_data_files):
                    json_file_path = os.path.join(input_directory, available_data_files[selection_idx])
                    output_prefix = os.path.splitext(available_data_files[selection_idx])[0]
                else:
                    print('\033[91mInvalid selection. Please enter a valid number.\033[0m')
                    continue
            except ValueError:
                print('\033[91mInvalid input. Please enter a number.\033[0m')
                continue

        # Load the data from the selected JSON file
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Apply filtering
        print('\n\033[94mFiltering Options:\033[0m')

        # Prompt the user to input regex filter for regular filtering
        regex_filter = input('\033[94mEnter the regex filter for regular filtering (default: .*): \033[0m')
        regex_filter = regex_filter or '.*'
        filtered_data = apply_filter(data, regex_filter)

        # Prompt the user to input regex filter for removal filtering
        removal_filter = input('\033[94mEnter the regex filter for removal filtering (default: ^$): \033[0m')
        removal_filter = removal_filter or '^$'
        filtered_data = apply_filter(filtered_data, removal_filter, is_removal_filter=True)

        # Create an output folder with timestamp
        output_subdirectory = create_output_folder(output_directory, output_prefix)

        # Save the filtered data to a new JSON file in the output folder
        output_json_path = os.path.join(output_subdirectory, f'{output_prefix}_filtered.json')
        with open(output_json_path, 'w') as f:
            json.dump(filtered_data, f, indent=4)
            print(f'\033[95mFiltered data saved to {output_json_path}\033[0m')

        # Copy the original JSON file to the working folder
        copy_file(json_file_path, working_directory)

        # Copy the filtered JSON file to the working folder
        copy_file(output_json_path, working_directory)

        # Group the filtered items by mod ID
        mod_groups = {}
        for item in filtered_data:
            mod_id, item_id = item['id'].split(':')
            if mod_id not in mod_groups:
                mod_groups[mod_id] = []
            mod_groups[mod_id].append(item['id'])

        # Save each mod group to a separate text file
        for mod_id, item_ids in mod_groups.items():
            output_txt_path = os.path.join(output_subdirectory, f'{mod_id}_output.txt')
            with open(output_txt_path, 'w') as f:
                f.write('\n'.join(item_ids))
                print(f'\033[95mFiltered data for mod {mod_id} saved to {output_txt_path}\033[0m')

        # Provide user feedback
        print('\033[94mFiltering completed successfully.\033[0m')

        # Prompt the user to rerun the script
        rerun_script = input('\033[94mDo you want to filter another JSON file? (y/n): \033[0m').lower() == 'y'
        if not rerun_script:
            break

# Run the script
if __name__ == "__main__":
    run_script()
