import subprocess


def launch_labelme():
    # Replace 'labelme' with the appropriate command to launch labelme in your environment
    command = 'labelme'
    try:
        subprocess.Popen(command, shell=True)
        state = "success"
    except Exception as e:
        state = e
    return state
