import os
from datetime import datetime

# Create folder to place all files in local

def create_tla_folder(tla, env):
    # Ensure start_time is defined, e.g., start_time = datetime.now()
    start_time = datetime.now()  # Example definition
    date_time = start_time.strftime("%Y-%m-%d_%H-%M-%S")

    FOLDER_NAME = tla + ' ' + env + "_" + date_time
    ROOT_DIR = os.path.join(MAIN_ROOT_DIR, FOLDER_NAME)

    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
        print(f'Created {ROOT_DIR} folder successfully')

    atmn_path = os.path.join(ROOT_DIR, 'Automation')
    os.makedirs(atmn_path)

    atr_folder_name = tla + env + ' ATR Reports'
    atr_report_path = os.path.join(atmn_path, atr_folder_name)
    os.makedirs(atr_report_path)

    sd_path = os.path.join(ROOT_DIR, 'Source Data')
    os.makedirs(sd_path)

    atr_reports_cl_path = os.path.join(atr_report_path, 'Cycle 1')
    atr_reports_c2_path = os.path.join(atr_report_path, 'Cycle 2')

    os.makedirs(atr_reports_cl_path)
    os.makedirs(atr_reports_c2_path)

    return ROOT_DIR, atmn_path
