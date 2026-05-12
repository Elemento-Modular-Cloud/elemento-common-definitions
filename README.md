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
# Supported Providers

This document lists all supported cloud providers and their services.













<!-- PROVIDERS_TABLE_START -->

| Provider | Service | Type | Sub-Type | Support Level | Status |
|----------|---------|------|----------|----------------|--------|
| Azure | Block Storage | storage | blockstorage | full | production |
| Azure | Kubernetes | service | container | full | production |
| Azure | Object Storage | storage | objectstorage | full | production |
| Azure | VM Management | matcher | vm | full | production |
| Google | Block Storage | storage | blockstorage | full | production |
| Google | Database as a Service | service | dbaas | full | production |
| Google | Kubernetes | service | container | full | production |
| Google | VM Management | matcher | vm | full | production |
| Impossible Cloud | Object Storage | storage | objectstorage | full | production |
| OVH | Block Storage | storage | blockstorage | full | production |
| OVH | Kubernetes | service | container | full | production |
| OVH | Object Storage | storage | objectstorage | full | production |
| OVH | VM Management | matcher | vm | full | production |
| Scaleway | Object Storage | storage | objectstorage | planned | production |
| UpCloud | Block Storage | storage | blockstorage | full | production |
| UpCloud | Database as a Service | service | dbaas | full | production |
| UpCloud | Kubernetes | service | container | full | production |
| UpCloud | Object Storage | storage | objectstorage | full | production |
| UpCloud | VM Management | matcher | vm | full | production |
| Wasabi | Object Storage | storage | objectstorage | full | production |

