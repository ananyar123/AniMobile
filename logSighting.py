def log_sighting():
    sighting = {}
    
    sighting["animal"] = input("Enter the type of animal: ")
    sighting["location"] = input("Enter the location: ")
    sighting["notes"] = input("Enter any additional notes: ")
    
    upload_picture = input("Do you want to upload an image? (yes/no): ").strip().lower()
    if upload_picture == "yes":
        sighting["picture"] = input("Enter the file path: ")
    else:
        sighting["picture"] = "No images uploaded"
    
    print("\nSighting Recorded:")
    for key, value in sighting.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    log_sighting()