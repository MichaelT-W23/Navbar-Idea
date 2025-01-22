import boto3
import os

def download_images_from_s3(bucket_name, local_dir):
    """
    Downloads all images from an S3 bucket to a local directory.

    :param bucket_name: The name of the S3 bucket.
    :param local_dir: The local directory to save images.
    """
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Create local directory if it doesn't exist
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in objects:
            print("No objects found in the bucket.")
            return

        # Iterate through objects and download images
        for obj in objects['Contents']:
            key = obj['Key']
            if key.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                local_path = os.path.join(local_dir, key)
                os.makedirs(os.path.dirname(local_path), exist_ok=True)  # Ensure subdirectories exist
                s3.download_file(bucket_name, key, local_path)
                print(f"Downloaded: {key}")
            else:
                print(f"Skipped (not an image): {key}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Replace with the bucket name and desired local directory
    BUCKET_NAME = "crumb-pics"
    LOCAL_DIR = "downloaded_images"

    download_images_from_s3(BUCKET_NAME, LOCAL_DIR)
