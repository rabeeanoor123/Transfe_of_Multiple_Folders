import os
import shutil
from datetime import datetime

# KEY REPRESENTS THE COMPANY NAMES, VALUES REPRESENTS THE CAMERA NAMES
fix_data = {
    
}

def update_video_data_no_camera(main_folder, saving_folder):
    if not os.path.exists(main_folder):
        print(f"{main_folder} does not exist.")
        return

    if not os.path.exists(saving_folder):
        os.makedirs(saving_folder)

    for comp_fol in os.listdir(main_folder):
        if comp_fol in fix_data.keys():
            comp_fol_path = os.path.join(main_folder, comp_fol)

            for camera_angle in os.listdir(comp_fol_path):
                camera_angle_path = os.path.join(comp_fol_path, camera_angle)

                if camera_angle in fix_data.get(comp_fol):
                    # Debug print
                    print(f"Checking {camera_angle_path}...")

                    # Sort date folders in the main_folder in descending order
                    sorted_dates = sorted(os.listdir(camera_angle_path), reverse=True)

                    # Copy only the latest three date folders from the main_folder to the saving_folder
                    for date_fol in sorted_dates[:5]:
                        date_fol_path = os.path.join(camera_angle_path, date_fol)

                        for file in os.listdir(date_fol_path):
                            if file.endswith(('.jpg', '.mp4', '.jpeg')):
                                try:
                                    src_path = os.path.join(date_fol_path, file)
                                    dst_fol = os.path.join(saving_folder, comp_fol, camera_angle, date_fol)
                                    dst_path = os.path.join(saving_folder, comp_fol, camera_angle, date_fol, file)

                                    if not os.path.exists(dst_fol):
                                        os.makedirs(dst_fol)

                                    if not os.path.exists(dst_path):
                                        shutil.copy(src_path, dst_path)
                                        print(f"File {file} copied to {dst_path}")
                                    else:
                                        print(f"File {file} already exists in {dst_path}")
                                except Exception as e:
                                    print(f"Error while copying {file} from {src_path} to {dst_path}. Error: {e}")

                    # Delete folders other than the latest three from the saving_folder
                    saving_camera_angle_path = os.path.join(saving_folder, comp_fol, camera_angle)
                    if os.path.exists(saving_camera_angle_path):
                        saved_sorted_dates = sorted(os.listdir(saving_camera_angle_path), reverse=True)
                        for date_fol in saved_sorted_dates[5:]:
                            saved_date_fol_path = os.path.join(saving_camera_angle_path, date_fol)
                            try:
                                shutil.rmtree(saved_date_fol_path)
                                print(f"Folder {saved_date_fol_path} has been deleted.")
                            except Exception as e:
                                print(f"Error while deleting {saved_date_fol_path}. Error: {e}")

    return "Script executed."

if __name__ == '__main__':
    main_folder = r"E:\camera_monitoring"
    saving_folder = r"E:\Rabeea"
    update_video_data_no_camera(main_folder, saving_folder)
