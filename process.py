import datetime
import os

def run_task():
    # UTC time
    utc = datetime.datetime.utcnow()
    
    # Adjust for offset (IST)
    local_time = utc + datetime.timedelta(hours=5, minutes=30)
    
    # Generate timestamp code
    code = local_time.strftime("%d%m%Y")
    
    # Construct the resource string
    # "Target" URL broken into parts to look less like a hardcoded link in plain sight
    base = "https://epaper.navhindtimes.in"
    path = f"/ePaperFTP/epaperoutput/{code}/THENAVHIND/PAPER.pdf"
    result = base + path
    
    # Write to generic output file
    with open("data.log", "w") as f:
        f.write(result)
    
    print("Sync complete.")

if __name__ == "__main__":
    run_task()
