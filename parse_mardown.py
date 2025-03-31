import os
import re
import requests
import hashlib
from urllib.parse import urlparse

# --- Configuration ---
MARKDOWN_DIR = '.'  # Directory to scan for markdown files ('.' for current)
IMAGE_DIR = 'images' # Subdirectory to save downloaded images
USER_AGENT = 'MyMarkdownImageDownloader/1.0' # Be polite to servers
# --- End Configuration ---

# Regex to find Markdown images: ![alt](src)
# and HTML images: <img ... src="..." ...>
# It captures the full image tag/markdown and the src part
# Group 1: Full match for ![alt](src)
# Group 2: src part for ![alt](src)
# Group 3: Full match for <img ...>
# Group 4: src part for <img ...>
IMAGE_REGEX = re.compile(r'(!\[(?:[^\]]*)\]\(([^)]+)\))|(<img[^>]*src=["\']([^"\']+)["\'][^>]*>)')

def is_url(path):
    """Checks if a given path is an external URL."""
    return path.startswith('http://') or path.startswith('https://')

def sanitize_filename(url):
    """Creates a reasonably safe filename from a URL."""
    parsed_url = urlparse(url)
    # Get path part, remove leading slash if exists
    path_part = parsed_url.path.lstrip('/')
    if not path_part: # Handle cases like http://example.com
        # Use a hash of the URL for uniqueness if path is empty
        return hashlib.md5(url.encode()).hexdigest() + ".img"

    # Get the filename from the path
    base = os.path.basename(path_part)
    # Basic sanitization (replace common problematic chars)
    # A more robust solution might involve a dedicated library or stricter rules
    safe_base = re.sub(r'[\\/*?:"<>|]', '_', base)
    # Prevent excessively long names
    return safe_base[:100] # Limit length

def download_image(url, local_filepath):
    """Downloads an image from a URL and saves it locally."""
    print(f"  Downloading: {url}")
    headers = {'User-Agent': USER_AGENT}
    try:
        response = requests.get(url, stream=True, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(local_filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  Saved to: {local_filepath}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"  Error downloading {url}: {e}")
        # Clean up potentially incomplete file
        if os.path.exists(local_filepath):
            try:
                os.remove(local_filepath)
            except OSError:
                pass # Ignore cleanup errors
        return False
    except Exception as e:
        print(f"  An unexpected error occurred for {url}: {e}")
        # Clean up potentially incomplete file
        if os.path.exists(local_filepath):
            try:
                os.remove(local_filepath)
            except OSError:
                 pass # Ignore cleanup errors
        return False


def process_markdown_file(filepath):
    """Processes a single markdown file."""
    print(f"\nProcessing file: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading file: {e}")
        return

    original_content = content
    modified = False

    # Create image directory relative to the script's CWD or specified MARKDOWN_DIR
    # For simplicity, placing images in IMAGE_DIR subdir relative to script execution
    # If MD files are deep, adjust path calculation as needed
    local_image_dir_abs = os.path.abspath(os.path.join(MARKDOWN_DIR, IMAGE_DIR))
    os.makedirs(local_image_dir_abs, exist_ok=True)

    # Use finditer to handle replacements correctly even if URLs repeat
    matches = list(IMAGE_REGEX.finditer(content))
    replacements = {} # Store changes: original_string -> new_string

    for match in matches:
        full_match_md, src_md, full_match_html, src_html = match.groups()

        if src_md: # Matched ![alt](src)
            original_src = src_md
            full_original_tag = full_match_md
        elif src_html: # Matched <img src="...">
            original_src = src_html
            full_original_tag = full_match_html
        else:
            continue # Should not happen with the regex structure

        if is_url(original_src):
            print(f"- Found external image: {original_src}")
            local_filename = sanitize_filename(original_src)
            local_filepath_abs = os.path.join(local_image_dir_abs, local_filename)
            # Path to use in Markdown (relative to the MD file location)
            # Assumes IMAGE_DIR is a direct subdirectory where MD files are.
            # For nested MD files, calculate relative path properly.
            relative_img_path = os.path.join(IMAGE_DIR, local_filename).replace('\\', '/') # Use forward slashes

            # Check if already downloaded (simple check)
            if not os.path.exists(local_filepath_abs):
                 if not download_image(original_src, local_filepath_abs):
                     print(f"  Skipping update for: {original_src}")
                     continue # Skip replacement if download failed
            else:
                 print(f"  Image already exists locally: {local_filepath_abs}")

            # Prepare the replacement tag string
            if src_md: # Update Markdown link
                new_tag = f"![{match.group(1).split('](')[0][2:]}]({relative_img_path})" # Reconstruct ![alt](new_path)
            else: # Update HTML link
                 # Replace only the src attribute value within the original tag
                 # This is safer than rebuilding the whole tag
                 # Note: Uses simple replace; edge cases with src appearing elsewhere in tag exist
                 new_tag = full_original_tag.replace(original_src, relative_img_path, 1)


            # Check if replacement is needed (maybe URL already points relatively?)
            if full_original_tag != new_tag:
                 # Store replacement to apply later
                 # Use full tag to avoid accidental partial replacements
                 replacements[full_original_tag] = new_tag
                 modified = True
                 print(f"  Marked for update: {original_src} -> {relative_img_path}")
        else:
            print(f"- Found local image (skipping): {original_src}")

    # Apply all replacements after finding them
    if modified:
        new_content = content
        for original_tag, new_tag in replacements.items():
             # Replace specific instances identified earlier
             # Using count=1 ensures only the first occurrence is replaced per loop,
             # but since we iterate unique tags, this works. A safer method
             # might involve replacing based on match positions if tags could be identical.
             # However, this approach is generally sufficient.
             new_content = new_content.replace(original_tag, new_tag, 1)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  File updated: {filepath}")
        except Exception as e:
            print(f"  Error writing updated file {filepath}: {e}")
    else:
        print("  No changes needed.")


if __name__ == "__main__":
    print("Starting Markdown image processing...")
    print(f"Scanning directory: {os.path.abspath(MARKDOWN_DIR)}")
    print(f"Saving images to subdirectory: {IMAGE_DIR}")

    found_files = False
    for filename in os.listdir(MARKDOWN_DIR):
        if filename.lower().endswith('.md'):
            found_files = True
            filepath = os.path.join(MARKDOWN_DIR, filename)
            if os.path.isfile(filepath):
                process_markdown_file(filepath)

    if not found_files:
         print(f"No Markdown (.md) files found in {os.path.abspath(MARKDOWN_DIR)}")

    print("\nProcessing finished.")