# Accepted values for supported providers file
Example with accepted values for a single provider:
```json
{
    "ELEMENTO_SUPPORTED_PROVIDERS": {
        "provider_name": {
            "display_name": "string",
            "icon_classes": "<provider_name>_icon",
            "source": "fontawesome",
            "hex_color": "#4285f4",
            "svg_filename": "<provider_name>_icon.svg",
            "status": "soon|development|beta|production",
            "server_ips": [],  // List of IPs for the active provider's mesons
            "services": [
                {
                    "name": "string",
                    "display_name": "string",
                    "type": "compute|storage|network|service",
                    "sub_type": "vm|objectstorage|k8s|...",
                    "regions": {
                        "africa_south1": {
                            "country": "South Africa",
                            "location": "Johannesburg",
                            "plus_code": "",
                            "certifications": []
                        },
                        "asia_east1": {
                            "country": "Taiwan",
                            "location": "Changhua County",
                            "plus_code": "",
                            "certifications": []
                        },
                        "asia_east2": {
                            "country": "China",
                            "location": "Hong Kong",
                            "plus_code": "",
                            "certifications": []
                        },
                        {
                            "Other regions": "..."
                        }
                    },
                    "support_level": "planned|partial|full" 
                },
                {
                    "Other services": "..."
                }
            ]
        },
    }
}
```