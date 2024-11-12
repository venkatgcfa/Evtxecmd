import subprocess
import os

def run_evtxecmd():
    # Take inputs from the user
    input_directory = input("Enter the input directory path: ")
    output_directory = input("Enter the output directory path: ")
    case_number = input("Enter the case number: ")

    # Ensure the input directory exists
    if not os.path.isdir(input_directory):
        print(f"Error: The input directory '{input_directory}' does not exist.")
        return

    # Check if the output directory exists, if not, create it
    if not os.path.isdir(output_directory):
        try:
            os.makedirs(output_directory)
            print(f"Output directory '{output_directory}' created successfully.")
        except OSError as e:
            print(f"Error: Unable to create output directory '{output_directory}'. {e}")
            return

    # Sync the maps from GitHub
    print("Syncing maps from GitHub...")
    sync_result = subprocess.run(["EvtxECmd.exe", "--sync"], capture_output=True, text=True)
    
    if sync_result.returncode != 0:
        print(f"Error during sync: {sync_result.stderr}")
        return
    else:
        print("Maps synced successfully.")

    # Prepare file paths for CSV and JSON outputs
    csv_output_file = os.path.join(output_directory, f"{case_number}.csv")
    json_output_file = os.path.join(output_directory, f"{case_number}-evtx_eventlogs.json")

    # Run EvtxECmd with specified arguments for both CSV and JSON outputs
    print(f"Processing EVTX files from '{input_directory}'...")
    evtx_result = subprocess.run(
        [
            "EvtxECmd.exe", 
            "-d", input_directory, 
            "--csv", output_directory, 
            "--csvf", csv_output_file,
            "--json", output_directory,
            "--jsonf", json_output_file
        ],
        capture_output=True,
        text=True
    )

    if evtx_result.returncode != 0:
        print(f"Error during processing: {evtx_result.stderr}")
    else:
        print(f"Processing complete! CSV Output saved to '{csv_output_file}' and JSON Output saved to '{json_output_file}'.")

if __name__ == "__main__":
    run_evtxecmd()