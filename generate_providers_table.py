#!/usr/bin/env python3
"""
Generate a markdown table of supported providers and their services
from supported_providers.json and append it to README.md
"""

import json
import os

# Paths
PROVIDERS_FILE = "supported_providers.json"
README_FILE = "README.md"

# Marker in README.md where the table should be inserted
TABLE_MARKER = "<!-- PROVIDERS_TABLE_START -->"


def generate_table():
    """Generate markdown table from supported_providers.json"""
    with open(PROVIDERS_FILE, "r") as f:
        data = json.load(f)

    providers_data = data.get("ELEMENTO_SUPPORTED_PROVIDERS", {})
    
    # Table header
    table = []
    table.append("| Provider | Service | Type | Sub-Type | Support Level | Status |")
    table.append("|----------|---------|------|----------|----------------|--------|")

    # Sort providers by name
    for provider_name in sorted(providers_data.keys()):
        provider = providers_data[provider_name]
        display_name = provider.get("display_name", provider_name)
        status = provider.get("status", "unknown")
        
        services = provider.get("services", [])
        
        for service in sorted(services, key=lambda x: x.get("name", "")):
            service_name = service.get("name", "")
            service_display = service.get("display_name", service_name)
            service_type = service.get("type", "")
            service_subtype = service.get("sub_type", "")
            support_level = service.get("support_level", "")
            
            # Create table row
            row = f"| {display_name} | {service_display} | {service_type} | {service_subtype} | {support_level} | {status} |"
            table.append(row)

    return "\n".join(table)


def update_readme():
    """Update README.md with the generated table"""
    table = generate_table()
    
    # Table content with marker
    table_content = f"\n\n{TABLE_MARKER}\n\n{table}\n\n"
    
    # Check if README exists
    if os.path.exists(README_FILE):
        with open(README_FILE, "r") as f:
            readme_content = f.read()
        
        # Find existing table and replace it
        if TABLE_MARKER in readme_content:
            # Split by marker and replace everything after it
            parts = readme_content.split(TABLE_MARKER)
            new_content = parts[0] + table_content
        else:
            # Append to end of file
            new_content = readme_content + table_content
    else:
        # Create new README with basic content
        new_content = f"# Supported Providers\n\nThis document lists all supported cloud providers and their services.\n\n{TABLE_MARKER}\n\n{table}\n"
    
    with open(README_FILE, "w") as f:
        f.write(new_content)
    
    print(f"Updated {README_FILE} with providers table")


if __name__ == "__main__":
    update_readme()
