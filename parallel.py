import subprocess
import time

def run_script(script_name):
    try:
        subprocess.Popen(["python3", script_name])
    except Exception as e:
        print(f"FEhler beim Starten von {script_name}: {e}")

def main():
    script1 = "dht11_sensor.py"
    script2 = "openweathermap.py"

    print("Starte Skripte...")
    run_script(script1)
    run_script(script2)

if __name__ == "__main__":
    main()